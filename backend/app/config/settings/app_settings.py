from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine import URL


class AppSettings(BaseSettings):
    drivername: str
    password: str
    host: str
    port: int
    database: str
    username: str
    algorithm: str
    access_token_expiry_days: int = 2
    access_token_key: SecretStr
    audience: str
    issuer: str

    # for the database connection
    database_url = URL.create()

    model_config = SettingsConfigDict(
        env_file=".env", validate_default=False, env_ignore_empty=True
    )


AppSettings = AppSettings()
