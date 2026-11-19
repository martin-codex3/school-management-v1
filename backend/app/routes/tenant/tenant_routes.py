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
    "/{tenant_id}", response_model=TenantResponseSchema, status_code=status.HTTP_200_OK
)
async def update_tenant_details(
    tenant_id: uuid.UUID,
    current_user: CurrentUser,
    tenant_data: UpdateTenantSchema,
    session: Annotated[AsyncSession, Depends(app_session)],
):
    """This will used path the tenant details"""
    if tenant_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"Not authorized to update this record"},
            headers={"WWW-Authenticate"},
        )

    tenant_data_dict = tenant_data.model_dump(exclude_unset=True)
    tenant_to_update = await get_current_tenant(
        current_user=current_user, session=session
    )

    for keys, values in tenant_data_dict.items():
        setattr(tenant_to_update, keys, values)

    session.add(tenant_to_update)
    await session.refresh(tenant_to_update)
    await session.commit()
    return tenant_to_update
