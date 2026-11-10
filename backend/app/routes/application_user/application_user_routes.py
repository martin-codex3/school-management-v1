from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session
from app.schemas.application_users.application_user_schemas import (
    UpdateApplicationUserSchema,
)
from app.services.user_service import CurrentUser

appliication_user_router = APIRouter()


@appliication_user_router.post("/update-account")
async def update_user_accoun(
    current_user: CurrentUser,
    user_data: UpdateApplicationUserSchema,
    session: Annotated[AsyncSession, Depends(app_session)],
):
    """This will attempt to update the user account"""
    user_data_dict = user_data.model_dump(exclude_unset=True)
