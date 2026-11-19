import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session
from app.models.tenant.tenant import Tenant
from app.models.tenant_user.tenant_user import TenantUser
from app.schemas.tenants.tenant_schemas import TenantResponseSchema, UpdateTenantSchema
from app.services.user_service import CurrentUser

tenant_router = APIRouter()


@tenant_router.get(
    "", status_code=status.HTTP_200_OK, response_model=TenantResponseSchema
)
async def get_current_tenant(
    current_user: CurrentUser, session: Annotated[AsyncSession, Depends(app_session)]
):
    """This will get the current tenant base on the logged in user"""
    statement = await session.execute(
        select(Tenant)
        .join(TenantUser, TenantUser.tenant_id == Tenant.id)
        .where(TenantUser.application_user_id == current_user.id)
    )

    tenant = statement.scalars().first()

    return tenant


@tenant_router.patch(
    "", response_model=TenantResponseSchema, status_code=status.HTTP_200_OK
)
async def update_tenant_details(
    current_user: CurrentUser,
    tenant_data: UpdateTenantSchema,
    session: Annotated[AsyncSession, Depends(app_session)],
):
    """This will use this to update the tenant details"""
    tenant_to_update = await get_current_tenant(
        current_user=current_user, session=session
    )

    tenant_data_dict = tenant_data.model_dump(exclude_unset=True)

    for keys, values in tenant_data_dict.items():
        setattr(tenant_to_update, keys, values)

    await session.commit()
    return tenant_to_update
