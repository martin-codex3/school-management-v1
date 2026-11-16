from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session
from app.models.tenant.tenant import Tenant
from app.models.tenant_user.tenant_user import TenantUser
from app.services.user_service import CurrentUser

tenant_routes = APIRouter()


@tenant_routes.get("/tenant", status_code=status)
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
