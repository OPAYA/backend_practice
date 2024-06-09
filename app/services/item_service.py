from typing import Dict

from app.db.repositories import ItemRepository

from app.models.domain.item import ItemDTO

class ItemService:
    def __init__(self, item_repository: ItemRepository):
        self.item_repository = item_repository
    
    async def retrieve_item_info(self, item_id: int) -> ItemDTO:
        return await self.item_repository.read_item_by_id(item_id)
    
    async def create_item(self, item_dto: ItemDTO) -> None:
        await self.item_repository.create_item(item_dto)
        
        