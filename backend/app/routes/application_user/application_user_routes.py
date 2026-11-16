import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session
from app.schemas.application_users.application_user_schemas import (
    ApplicationUserResponse,
    UpdateApplicationUserSchema,
)
from app.services.user_service import CurrentUser

appliication_user_router = APIRouter()


@appliication_user_router.patch(
    "/update-account/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=ApplicationUserResponse,
)
async def update_user_account(
    user_id: uuid.UUID,
    current_user: CurrentUser,
    user_data: UpdateApplicationUserSchema,
    session: Annotated[AsyncSession, Depends(app_session)],
):
    """This will attempt to update the user account"""
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You cannot update this profile",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_data_dict = user_data.model_dump(exclude_unset=True)
    for keys, values in user_data_dict.items():
        setattr(current_user, keys, values)

    session.add(current_user)
    await session.commit()
    return current_user
