from datetime import UTC, datetime, timedelta

import jwt
from fastapi import HTTPException, status
from jwt.exceptions import InvalidTokenError

from app.config.settings.app_settings import AppSettings


def create_jwt_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(
            days=AppSettings.access_token_expiry_days
        )
    to_encode.update({"exp": expire})
    jwt_encoded = jwt.encode(
        to_encode, AppSettings.access_token_key, AppSettings.algorithm
    )
    return jwt_encoded


# verifying the access_token
def verify_access_token(token: str) -> bool:
    credentials_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        return jwt.decode(
            token, AppSettings.access_token_key, algorithms=[AppSettings.algorithm]
        )
    except InvalidTokenError:
        raise credentials_error
