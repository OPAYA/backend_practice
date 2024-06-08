import logging
from app.core.settings.app import AppSettings


class DevAppSettings(AppSettings):
    title: str = "Backend API DEV"
    base_url: str = "https://dev.dns"

    logging_level: int = logging.DEBUG
    sqlalchemy_logging_level: int = logging.DEBUG
