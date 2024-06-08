import logging
from app.core.settings.app import AppSettings


class LocalAppSettings(AppSettings):
    title: str = "Backend API LOCAL"
    base_url: str = "http://localhost:8000"
    debug: bool = True

    logging_level: int = logging.DEBUG
    sqlalchemy_logging_level: int = logging.DEBUG
