from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session
from app.models.branches.branch import Branch
from app.models.tenant.tenant import Tenant
from app.schemas.branches.branch_schema import CreateBranchSchema
from app.services.user_service import CurrentUser
import uuid
branch_router = APIRouter()


@branch_router.post("/{user_id}", status_code=status)
async def create_branch(
    current_user: CurrentUser,
    user_id: uuid.UUID,
    branch_data: CreateBranchSchema,
    session: Annotated[AsyncSession, Depends(app_session)],
):
    """This will create a new branch for the tenant"""
    if 
