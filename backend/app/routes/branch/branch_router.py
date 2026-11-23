import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session
from app.models.branches.branch import Branch
from app.models.tenant.tenant import Tenant
from app.models.tenant_user.tenant_user import TenantUser
from app.schemas.branches.branch_schema import BranchResponseSchema, CreateBranchSchema
from app.services.user_service import CurrentUser

branch_router = APIRouter()


@branch_router.post(
    "/{user_id}",
    status_code=status.HTTP_201_CREATED,
    response_model=BranchResponseSchema,
)
async def create_branch(
    current_user: CurrentUser,
    user_id: uuid.UUID,
    branch_data: CreateBranchSchema,
    session: Annotated[AsyncSession, Depends(app_session)],
):
    """This will create a new branch for the tenant"""
    if user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authorized to create branch",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # we will fetch the tenant based on the user
    statement = await session.execute(
        select(Tenant)
        .join(TenantUser, Tenant.id == TenantUser.tenant_id)
        .where(TenantUser.application_user_id == user_id)
    )

    tenant = statement.scalars().first()

    branch_data_dict = branch_data.model_dump()

    new_branch = Branch(**branch_data_dict)
    new_branch.tenant_id = tenant.id

    session.add(new_branch)
    await session.refresh(new_branch)
    await session.commit()
    return new_branch
