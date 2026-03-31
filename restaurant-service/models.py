from pydantic import BaseModel
from typing import Optional

class Restaurant(BaseModel):
    id: int
    name: str
    location: str
    cuisine: str

class RestaurantCreate(BaseModel):
    name: str
    location: str
    cuisine: str

class RestaurantUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    cuisine: Optional[str] = None