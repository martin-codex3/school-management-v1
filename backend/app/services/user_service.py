import uuid
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.database.app_database import app_session
from app.config.settings.app_settings import AppSettings
from app.models.application_user.application_user import ApplicationUser

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/authentication/token")


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    session: Annotated[AsyncSession, Depends(app_session)],
) -> ApplicationUser:

    try:
        payload = jwt.decode(
            token,
            key=AppSettings.access_token_key.get_secret_value(),
            algorithms=[AppSettings.algorithm],
            issuer="",
            audience="",
        )

        print("payload", payload)

        user_id = payload.get("sub")

        if not user_id:
            raise InvalidTokenError("Missing user subject")

        user_uuid = uuid.UUID(str(user_id))

    except InvalidTokenError, TypeError, ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    statement = await session.execute(
        select(ApplicationUser).where(ApplicationUser.id == user_uuid)
    )

    application_user = statement.scalars().first()

    if not application_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User could not be found",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return application_user


CurrentUser = Annotated[
    ApplicationUser,
    Depends(get_current_user),
]
