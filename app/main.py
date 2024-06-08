from fastapi import FastAPI

from app.core.config import get_app_settings
from app.api.route import router as api_router
from app.core.containers import Container
from app.core import logger

def get_application() -> FastAPI:
    settings = get_app_settings()
    logger.init(settings)
    application = FastAPI(**settings.fastapi_kwargs)
    
    container = Container()
    container.config.from_dict(settings.model_dump())
    
    application.include_router(api_router)
    
    return application


app = get_application()


@app.get("/healthcheck")
async def healthcheck():
    return "OK"
