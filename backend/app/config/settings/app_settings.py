from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    public_database_url: str
    algorithm: str
    access_token_key: int = 2
    access_token_expiry_days: SecretStr

    model_config = SettingsConfigDict(
        env_file=".env", validate_default=False, env_ignore_empty=True
    )


AppSettings = AppSettings()
