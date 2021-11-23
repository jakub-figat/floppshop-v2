from src.settings.api_urls import APIUrls
from src.settings.database import DatabaseSettings
from src.settings.email import EmailSettings
from src.settings.general import GeneralSettings


class Settings(GeneralSettings, DatabaseSettings, EmailSettings):
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
