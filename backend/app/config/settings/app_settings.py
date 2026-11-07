from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    public_database_url: str

    model_config = SettingsConfigDict(
        env_file=".env", validate_default=False, env_ignore_empty=True
    )


AppSettings = AppSettings()
