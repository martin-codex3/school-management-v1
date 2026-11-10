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

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Cannot verify the credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            key=AppSettings.access_token_key.get_secret_value(),
            algorithms=[AppSettings.algorithm],
            issuer=AppSettings.issuer,
            audience=AppSettings.audience,
        )

        user_uuid = uuid.UUID(payload.get("sub"))

        if user_uuid is None:
            raise credentials_exception

    except InvalidTokenError, ValueError:
        raise credentials_exception

    # we will get the user here
    statement = await session.execute(
        select(ApplicationUser).where(ApplicationUser.id == user_uuid)
    )

    user = statement.scalars().first()

    if not user:
        raise credentials_exception

    return user


CurrentUser = Annotated[
    ApplicationUser,
    Depends(get_current_user),
]
