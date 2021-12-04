from fastapi_jwt_auth import AuthJWT

from src.settings.database import DatabaseSettings
from src.settings.general import GeneralSettings
from src.settings.jwt import AuthJWTSettings
from src.settings.rabbitmq import RabbitMQSettings
from src.settings.api_urls import APIUrls


class Settings(GeneralSettings, DatabaseSettings, RabbitMQSettings, AuthJWTSettings):
    pass


settings = Settings()


app_models_dict = {
    app: {"models": models, "default_connection": "default"} for app, models in settings.APP_MODELS.items()
}

app_models_dict["models"] = {
    "models": ["aerich.models"],
    "default_connection": "default",
}

TORTOISE_CONFIG = {
    "connections": {"default": settings.postgres_url},
    "apps": app_models_dict,
}


@AuthJWT.load_config
def get_config() -> Settings:
    return settings
