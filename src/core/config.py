import os
from typing import Optional

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

DOTENV = os.path.join(os.path.dirname(__file__), '../../infra/.env')


class Settings(BaseSettings):
    """Базовые настройки для БД."""

    app_title: str = 'GeoService'
    app_title_remote: str
    api_url: str
    postgres_db: str
    postgres_user: str
    postgres_password: str
    db_host: str
    db_port: str
    debug_mode: bool = True

    model_config = SettingsConfigDict(
        env_file=DOTENV,
        extra='ignore',
    )

    @property
    def db_url(self) -> Optional[PostgresDsn]:
        """Метод получает ссылку к БД."""
        return (
            f'postgresql+asyncpg://'
            f'{self.postgres_user}:{self.postgres_password}@'
            f'{self.db_host}:{self.db_port}/{self.postgres_db}'
        )


settings = Settings()
