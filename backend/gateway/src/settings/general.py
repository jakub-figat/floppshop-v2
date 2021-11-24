from pathlib import Path

from pydantic import BaseSettings


class GeneralSettings(BaseSettings):
    ENV: str = "development"
    BASE_DIR: Path = Path(__file__).parents[2]
    DOMAIN: str
    TEMPLATE_FOLDER: Path = BASE_DIR / "templates"
