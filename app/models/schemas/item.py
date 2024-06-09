from typing import Optional, List
from pydantic.dataclasses import dataclass

from app.models.domain.item import ItemDTO


@dataclass
class ItemResp:
    name: str
    description: str
    price: float
    quantity: int

    @classmethod
    def from_dto(cls, dto: ItemDTO) -> "ItemResp":
        return cls(
            name=dto.name,
            description=dto.description,
            price=dto.price,
            quantity=dto.quantity
        )

@dataclass
class ItemReq:
    name: str
    description: str
    price: float
    quantity: int
    
    def to_dto(self) -> ItemDTO:
        return ItemDTO(
            name=self.name,
            description=self.description,
            price=self.price,
            quantity=self.quantity
        )
    