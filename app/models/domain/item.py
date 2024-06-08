from dataclasses import dataclass, field
from typing import Optional, List
from datetime import datetime

@dataclass
class ItemDTO:
    item_id: int = field(default=None)
    name: str = field(default=None)
    description: str = field(default=None)
    price: float = field(default=None)
    quantity: int = field(default=None)