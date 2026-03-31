from pydantic import BaseModel
from typing import Optional

class MenuItem(BaseModel):
    id: int
    name: str
    price: float
    description: str
    category: str        # NEW (e.g., Main Course, Beverage)
    size: str            # NEW (Small, Medium, Large)

class MenuCreate(BaseModel):
    name: str
    price: float
    description: str
    category: str
    size: str

class MenuUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    category: Optional[str] = None
    size: Optional[str] = None