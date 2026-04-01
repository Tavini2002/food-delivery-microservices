from fastapi import FastAPI, HTTPException
from typing import List
from service import OrderService
from models import Order, OrderCreate, OrderUpdate

app = FastAPI(title="Order Service")

service = OrderService()

@app.get("/api/orders", response_model=List[Order])
def get_all():
    return service.get_all()

@app.get("/api/orders/{id}", response_model=Order)
def get_one(id: int):
    o = service.get_by_id(id)
    if not o:
        raise HTTPException(status_code=404, detail="Order not found")
    return o

@app.post("/api/orders")
def create(data: OrderCreate):
    return service.create(data)

@app.put("/api/orders/{id}")
def update(id: int, data: OrderUpdate):
    o = service.update(id, data)
    if not o:
        raise HTTPException(status_code=404, detail="Order not found")
    return o

@app.delete("/api/orders/{id}")
def delete(id: int):
    if not service.delete(id):
        raise HTTPException(status_code=404, detail="Order not found")
    return {"message": "Deleted"}