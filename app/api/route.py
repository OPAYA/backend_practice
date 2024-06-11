from fastapi import APIRouter
from app.api.v1 import (
    item, user, payment
)

router = APIRouter()

router.include_router(item.router, tags=["Item"], prefix="/v1/item")
router.include_router(user.router, tags=["User"], prefix="/v1/user")
router.include_router(user.router, tags=["Payment"], prefix="/v1/payment")
