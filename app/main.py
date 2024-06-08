from fastapi import FastAPI


from app.core.app_events import create_start_app_handler, create_stop_app_handler
from app.core.config import get_app_settings
from app.api.route import router as api_router
from app.core.containers import Container
from app.core import logger
from app.core.middlewares import SQLAlchemyMiddleware

def get_application() -> FastAPI:
    settings = get_app_settings()
    logger.init(settings)
    application = FastAPI(**settings.fastapi_kwargs)
    
    #docker run -p 5432:5432 --name postgres -e POSTGRES_PASSWORD=1111 -d postgres
    #docker run --name postgres-container -e POSTGRES_PASSWORD=1111 -d -p 5432:5432 postgres

    
    application.add_event_handler(
        "startup",
        create_start_app_handler(application, settings),
    )
    application.add_event_handler(
        "shutdown",
        create_stop_app_handler(application),
    )
    
    container = Container()
    container.config.from_dict(settings.model_dump())
    
    application.include_router(api_router)
    application.add_middleware(SQLAlchemyMiddleware)
    
    return application


app = get_application()


@app.get("/healthcheck")
async def healthcheck():
    return "OK"
