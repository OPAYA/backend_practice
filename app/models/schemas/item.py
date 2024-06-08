from typing import Optional, List
from pydantic.dataclasses import dataclass

from app.models.domain import ItemDTO


@dataclass
class ItemResp:
    itemId: int
    name: str
    description: str
    price: float
    quantity: int

    @classmethod
    def from_dto(cls, dto: ItemDTO) -> "ItemResp":
        return cls(
            itemId=dto.item_id,
            name=dto.name,
            description=dto.description,
            price=dto.price,
            quantity=dto.quantity
        )
