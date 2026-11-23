import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session
from app.models.branches.branch import Branch
from app.models.tenant.tenant import Tenant
from app.schemas.branches.branch_schema import CreateBranchSchema
from app.services.user_service import CurrentUser

branch_router = APIRouter()


@branch_router.post("/{user_id}", status_code=status.HTTP_201_CREATED)
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

    branch_data_dict = branch_data.model_dump()

    new_branch = Branch(**branch_data_dict)

    print(new_branch)
