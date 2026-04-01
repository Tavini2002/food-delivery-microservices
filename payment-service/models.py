from pydantic import BaseModel
from typing import Optional

class Payment(BaseModel):
    id: int
    amount: float
    status: str

class PaymentCreate(BaseModel):
    amount: float
    status: str = "pending"

class PaymentUpdate(BaseModel):
    amount: Optional[float] = None
    status: Optional[str] = None
