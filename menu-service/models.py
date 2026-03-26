from pydantic import BaseModel
from typing import Optional

class MenuItem(BaseModel):
    id: int
    name: str
    price: float
    description: str

class MenuCreate(BaseModel):
    name: str
    price: float
    description: str

class MenuUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None