from typing import Any

from pydantic import BaseSettings


class DatabaseSettings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_DATABASE: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: int
    TEST_MODE: bool = False
    APP_MODELS: dict[str, Any] = {"products": ["src.apps.product.models"]}

    @property
    def postgres_url(self) -> str:
        database_name = self.POSTGRES_DATABASE if not self.TEST_MODE else "test"

        return (
            f"postgres://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{database_name}"
        )
