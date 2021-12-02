from src.settings.api_urls import APIUrls, api_urls
from src.settings.general import GeneralSettings
from src.settings.hosts import ServiceSettings


class Settings(GeneralSettings, ServiceSettings):
    pass


settings = Settings()
