from pydantic import BaseModel
from typing import List, Optional

class OrderItem(BaseModel):
    menu_id: int
    quantity: int

class Order(BaseModel):
    id: int
    user_id: int
    restaurant_id: int
    items: List[OrderItem]
    status: str

class OrderCreate(BaseModel):
    user_id: int
    restaurant_id: int
    items: List[OrderItem]

class OrderUpdate(BaseModel):
    status: Optional[str] = None