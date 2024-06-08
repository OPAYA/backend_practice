import logging
from app.core.settings.app import AppSettings


class TestAppSettings(AppSettings):
    title: str = "FastAPI - TEST"
    base_url: str = "http://localhost:8000"
    debug: bool = True

    logging_level: int = logging.DEBUG

    # Database
    database_url: str = "postgresql+asyncpg://tsdbadmin:password@localhost:34552/tsdb"
    