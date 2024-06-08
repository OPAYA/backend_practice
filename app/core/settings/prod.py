import logging
from app.core.settings.app import AppSettings


class ProdAppSettings(AppSettings):
    title: str = "Backend API PROD"
    base_url: str = "https://api.dns"
    openapi_url: str = ""
    docs_url: str = ""
    redoc_url: str = ""

    logging_level: int = logging.INFO

    redis_use_tls: bool = True
