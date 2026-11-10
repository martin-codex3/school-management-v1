from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio.session import AsyncSession
from typing import Annotated
from app.config.database.app_database import app_session
from app.services.user_service import CurrentUser

appliication_user_router = APIRouter()

@appliication_user_router.post("/update-account")
async def update_user_accoun(current_user: CurrentUser, session: Annotated[AsyncSession, Depends(app_session)]):
    