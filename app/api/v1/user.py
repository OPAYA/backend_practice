from datetime import date
from typing import Optional, Dict

from fastapi import APIRouter, Depends, Path
from dependency_injector.wiring import inject, Provide

import app.services as services
from app.core.containers import Container


router = APIRouter()

# localhost:8000/v1/user/user_id/3
@router.get(
    "/user_id/{userId}",
)
@inject
async def get_item_info(
    userId: str = Path(..., alias="userId"),
    user_service: services.UserService = Depends(Provide[Container.user_service]),
):
    result = await user_service.get_user_info_by_id(user_id=userId)

    return result

@router.get(
    "/user_name/{userName}"
)
@inject
async def get_item_info_by_name(
    userName: str = Path(..., alias="userName"),
    user_service: services.UserService = Depends(Provide[Container.user_service]),
):
    result = await user_service.get_user_info_by_name(user_name=userName)
    return result