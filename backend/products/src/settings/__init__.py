from src.settings.database import DatabaseSettings
from src.settings.general import GeneralSettings
from src.settings.rabbitmq import RabbitMQSettings


class Settings(GeneralSettings, DatabaseSettings, RabbitMQSettings):
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
