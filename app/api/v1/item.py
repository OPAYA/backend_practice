from datetime import date
from typing import Optional, Dict

from fastapi import APIRouter, Depends, Path
from dependency_injector.wiring import inject, Provide

import app.services as services
from app.core.containers import Container


router = APIRouter()


@router.get(
    "item_id/{itemId}",
)
@inject
async def get_item_info(
    itemId: str = Path(..., alias="itemId"),
    item_service: services.ItemService = Depends(Provide[Container.item_service]),
):
    result = await item_service.retrieve_item_info(itemId)

    return result

@router.get(
    "item_name/{itemName}"
)
@inject
async def get_item_info_by_name(
    itemName: str = Path(..., alias="itemName"),
    item_service: services.ItemService = Depends(Provide[Container.item_service]),
):
    result = await item_service.retrive_item_info_by_name(itemName)
    return result