from asyncio import gather as asyncio_gather
from typing import Callable
from fastapi import FastAPI
from dependency_injector.wiring import inject, Provide
from sqlalchemy import text

from app.core.containers import Container
from app.db.session import session
from app.core.settings.app import AppSettings


def create_start_app_handler(
    app: FastAPI,
    settings: AppSettings,
) -> Callable:
    async def start_app() -> None:
        await session.execute(text("SELECT 1")),
        
    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        session.close_all()

    return stop_app


