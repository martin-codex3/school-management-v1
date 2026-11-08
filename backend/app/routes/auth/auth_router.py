from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session
from app.models.application_user.application_user import ApplicationUser
from app.schemas.authentication.create_account_schema import CreateAccountSchema

auth_router = APIRouter()


@auth_router.post("/create-account")
async def create_tenant_account(
    data: CreateAccountSchema, session: Annotated[AsyncSession, Depends(app_session)]
):
    statement = await session.execute(
        select(ApplicationUser).where(
            func.lower(ApplicationUser.email) == data.email.lower()
        )
    )
    user = statement.scalars().first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    print("user does not exists create one")
