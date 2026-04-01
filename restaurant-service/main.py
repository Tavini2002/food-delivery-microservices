from fastapi import FastAPI, HTTPException
from service import RestaurantService
from models import Restaurant, RestaurantCreate, RestaurantUpdate
from typing import List

app = FastAPI(title="Restaurant Service")

service = RestaurantService()

@app.get("/api/restaurants", response_model=List[Restaurant])
def get_all():
    return service.get_all()

@app.get("/api/restaurants/{id}", response_model=Restaurant)
def get_one(id: int):
    r = service.get_by_id(id)
    if not r:
        raise HTTPException(status_code=404)
    return r

@app.post("/api/restaurants")
def create(data: RestaurantCreate):
    return service.create(data)

@app.put("/api/restaurants/{id}")
def update(id: int, data: RestaurantUpdate):
    r = service.update(id, data)
    if not r:
        raise HTTPException(status_code=404)
    return r

@app.delete("/api/restaurants/{id}")
def delete(id: int):
    if not service.delete(id):
        raise HTTPException(status_code=404)
    return {"message": "Deleted"}