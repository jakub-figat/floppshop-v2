from src.settings.database import DatabaseSettings
from src.settings.general import GeneralSettings
from src.settings.api_urls import APIUrls


class Settings(GeneralSettings, DatabaseSettings):
    pass


settings = Settings()
