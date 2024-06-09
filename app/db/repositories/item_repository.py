from typing import Optional, List
from sqlalchemy import select, insert, and_, func, update, or_

from app.db.session import session

from app.models.db import ItemModel
from app.models.domain.item import ItemDTO

class ItemRepository:
    async def read_item_by_id(self, item_id: int):
        stmt = select(ItemModel).where(
            ItemModel.id == int(item_id)
        )
        
        result: ItemModel = (await session.execute(stmt)).scalar_one_or_none()

        if result:
            return ItemDTO(
                name=result.name,
                description=result.description,
                price=result.price,
                quantity=result.quantity
            )
        else:
            return None
    
    async def create_item(self, item: ItemDTO) -> None:
        stmt = insert(ItemModel).values(
            name=item.name,
            description=item.description,
            price=item.price,
            quantity=item.quantity
        )
        await session.execute(stmt)
        await session.commit()