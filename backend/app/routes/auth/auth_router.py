from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio.session import AsyncSession

from app.config.database.app_database import app_session
from app.models.application_user.application_user import ApplicationUser
from app.models.tenant.tenant import Tenant
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

    new_user = ApplicationUser(
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
        phone_number=data.phone_number,
        password_hash=data.password_hash,
    )

    session.add(new_user)

    # we then have to create the tenant here
    statement = await session.execute(
        select(Tenant).where(func.lower(Tenant.school_name) == data.school_name.lower())
    )

    existing_school = statement.scalars().first()

    if existing_school:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="School with that name already exists",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # we will also check if the school email exists
    statement = await session.execute(
        select(Tenant).where(func.lower(Tenant.school_email) == data.school_email)
    )

    email_exists = statement.scalars().first()

    if email_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="That email is already registered",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # we will create the tenant here
    new_tenant = Tenant(
        school_name=data.school_name,
        school_type=data.school_type,
        school_email=data.school_email,
        school_phone=data.school_phone,
        address=data.address,
        city=data.city,
        country=data.country,
    )

    # we will add the tenant to the session here
    session.add(new_tenant)
    session.flush()
