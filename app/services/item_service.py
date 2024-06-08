from typing import Dict

class ItemService:
    def __init__(self):
        print('hi')
    
    async def retrieve_item_info(self, item_id: int) -> Dict:
        return {
            "id": "12345",
            "name": "Wireless Mouse",
            "description": "A high-precision wireless mouse with ergonomic design.",
            "price": 29.99,
            "currency": "USD",
            "stock": 150,
            "category": "Electronics",
            "tags": ["wireless", "mouse", "electronics"],
            "rating": 4.5,
            "reviews": [
                {
                    "user": "user123",
                    "rating": 5,
                    "comment": "Great mouse, very responsive!",
                    "date": "2024-06-08"
                },
                {
                    "user": "user456",
                    "rating": 4,
                    "comment": "Good value for the price.",
                    "date": "2024-06-07"
                }
            ],
            "images": [
                "https://example.com/images/wireless_mouse_1.jpg",
                "https://example.com/images/wireless_mouse_2.jpg"
            ],
            "specifications": {
                "dimensions": "4.5 x 2.8 x 1.6 inches",
                "weight": "3.2 ounces",
                "battery_life": "12 months",
                "connectivity": "Bluetooth, USB receiver"
            }
        }


