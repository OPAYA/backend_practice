class UserService:
    async def get_user_info_by_id(self, user_id: int):
        return {"user_id": user_id}
    
    async def get_user_info_by_name(self, user_name: str):
        return {"user_name": user_name}