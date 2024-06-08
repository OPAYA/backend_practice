from fastapi import APIRouter
from app.api.v1 import (
    item
)

router = APIRouter()

router.include_router(item.router, tags=["Item"], prefix="/v1/item")