from fastapi import FastAPI

from app.core.config import get_app_settings
from app.core import logger


def get_application() -> FastAPI:
    settings = get_app_settings()
    logger.init(settings)
    application = FastAPI(**settings.fastapi_kwargs)
    
    return application


app = get_application()


@app.get("/healthcheck")
async def healthcheck():
    return "OK"
