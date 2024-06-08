from datetime import date
from typing import Optional, Dict

from fastapi import APIRouter, Depends, Path
from dependency_injector.wiring import inject, Provide

import app.services as services
from app.core.containers import Container


router = APIRouter()


@router.get(
    "/{itemId}",
)
@inject
async def get_user_credit_balance(
    itemId: str = Path(..., alias="itemId"),
    item_service: services.ItemService = Depends(Provide[Container.item_service]),
):
    result = await item_service.retrieve_item_info(itemId)

    return result