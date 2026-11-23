import uuid
from datetime import UTC, datetime
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import selectinload

from app.config.database.app_database import app_session
from app.models.branches.branch import Branch
from app.models.tenant.tenant import Tenant
from app.models.tenant_user.tenant_user import TenantUser
from app.schemas.branches.branch_schema import (
    BranchResponseSchema,
    CreateBranchSchema,
    UpdateBranchSchema,
)
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

    # we will check if the email already exists
    statement = await session.execute(
        select(Branch).where(
            func.lower(Branch.branch_email) == branch_data.branch_email
        )
    )

    branch = statement.scalars().first()

    if branch:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Branch email already registered",
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
    await session.commit()
    await session.refresh(new_branch)
    return new_branch


# for all the branches
@branch_router.get("/{user_id}", response_model=list[BranchResponseSchema])
async def get_all_branches(
    user_id: uuid.UUID,
    current_user: CurrentUser,
    session: Annotated[AsyncSession, Depends(app_session)],
):
    """This will fetch all the branches"""
    if user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authorized to perform the action",
            headers={"WWW-Authenticate": "Bearer"},
        )

    statement = await session.execute(select(Branch))

    all_branches = statement.scalars().all()

    return all_branches


@branch_router.get(
    "/{user_id}/branch/${branch_id}",
    response_model=BranchResponseSchema,
    status_code=status.HTTP_200_OK,
)
async def get_branch(
    user_id: uuid.UUID,
    branch_id: uuid.UUID,
    current_user: CurrentUser,
    session: Annotated[AsyncSession, Depends(app_session)],
):
    """This will fetch all the branches"""
    if user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authorized to perform the action",
            headers={"WWW-Authenticate": "Bearer"},
        )

    statement = await session.execute(select(Branch).where(Branch.id == branch_id))

    branch = statement.scalars().first()

    if not branch:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Branch with that id not found",
        )

    return branch


# fetching branches based on the tenant
@branch_router.get(
    "/{user_id}/tenant-braches/{tenant_id}", status_code=status.HTTP_200_OK
)
async def get_branches_by_tenant(
    user_id: uuid.UUID,
    tenant_id: uuid.UUID,
    current_user: CurrentUser,
    session: Annotated[AsyncSession, Depends(app_session)],
):
    """This will fetch all the branches belonging to a tenant"""
    if user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authorized to perform the action",
            headers={"WWW-Authenticate": "Bearer"},
        )

    statement = await session.execute(
        select(Tenant).options(selectinload(Tenant.branches))
    )

    all_tenant_branches = statement.scalars().all()

    return all_tenant_branches


@branch_router.patch(
    "/{user_id}/branch/${branch_id}", response_model=BranchResponseSchema
)
async def update_branch(
    user_id: uuid.UUID,
    branch_id: uuid.UUID,
    current_user: CurrentUser,
    branch_data: UpdateBranchSchema,
    session: Annotated[AsyncSession, Depends(app_session)],
):
    """This will be used to update the branch"""

    if user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authorized to perform the action",
            headers={"WWW-Authenticate": "Bearer"},
        )

    statement = await session.execute(select(Branch).where(Branch.id == branch_id))

    branch = statement.scalars().first()

    if not branch:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Branch with that id not found",
        )

    branch_data_dict = branch_data.model_dump(exclude_unset=True)
    branch_data_dict["updated_date"] = datetime.now(UTC)

    for keys, values in branch_data_dict.items():
        setattr(branch, keys, values)

    session.add(branch)
    await session.commit()
    await session.refresh(branch)
    return branch
