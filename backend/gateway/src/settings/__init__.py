from src.settings.database import DatabaseSettings
from src.settings.general import GeneralSettings


class Settings(GeneralSettings, DatabaseSettings):
    pass


settings = Settings()
