from fastapi import FastAPI, HTTPException, status
from typing import List
from models import MenuItem, MenuCreate, MenuUpdate
from service import MenuService

app = FastAPI(title="Menu Service")

menu_service = MenuService()

@app.get("/")
def root():
    return {"message": "Menu Service Running"}

@app.get("/api/menu", response_model=List[MenuItem])
def get_all():
    return menu_service.get_all()

@app.get("/api/menu/{id}", response_model=MenuItem)
def get_one(id: int):
    item = menu_service.get_by_id(id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/api/menu", response_model=MenuItem, status_code=status.HTTP_201_CREATED)
def create(item: MenuCreate):
    return menu_service.create(item)

@app.put("/api/menu/{id}", response_model=MenuItem)
def update(id: int, item: MenuUpdate):
    updated = menu_service.update(id, item)
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated

@app.delete("/api/menu/{id}")
def delete(id: int):
    if not menu_service.delete(id):
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Deleted"}