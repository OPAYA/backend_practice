from datetime import date
from typing import Optional, Dict

from fastapi import APIRouter, Depends, Path
from dependency_injector.wiring import inject, Provide

import app.services as services
from app.core.containers import Container
from app.models.schemas.item import ItemResp, ItemReq
from app.models.schemas.common import V1HttpResponse, BaseHttpResponse


router = APIRouter()


@router.get(
    "/{itemId}",
    response_model=BaseHttpResponse[ItemResp],
)
@inject
async def get_item_by_id(
    itemId: str = Path(..., alias="itemId"),
    item_service: services.ItemService = Depends(Provide[Container.item_service]),
) -> BaseHttpResponse[ItemResp]:
    result = await item_service.retrieve_item_info(item_id=itemId)

    return V1HttpResponse(content=ItemResp.from_dto(result))

@router.post(
    ""
)
@inject
async def create_item(
    body: ItemReq,
    item_service: services.ItemService = Depends(Provide[Container.item_service]),
):
    await item_service.create_item(body.to_dto())
    
    return V1HttpResponse(content="success")
    
    
    