from fastapi import FastAPI, Request
from pydantic import BaseModel
import httpx
from typing import Optional

# ---------------------------------------------------------------------------
# Models for request bodies
# ---------------------------------------------------------------------------
class Restaurant(BaseModel):
    name: str
    location: str
    cuisine: str

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

class User(BaseModel):
    id: int
    name: str
    email: str

# 💳 YOUR NEW PAYMENT MODEL
# Adjust these fields to match exactly what your Payment microservice expects
class PaymentCreate(BaseModel):
    order_id: int
    amount: float
    payment_method: str 
# ---------------------------------------------------------------------------

from typing import Optional
class Restaurant(BaseModel):
    name: str
    location: str
    cuisine: str

app = FastAPI(title="API Gateway")

# Models for request bodies
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

# 🔗 connect your services here
SERVICES = {
    "user": "http://localhost:8001",
    "restaurant": "http://localhost:8002",
    "menu": "http://localhost:8003",
    "order": "http://localhost:8004",
    "delivery": "http://localhost:8005",
    "payment": "http://localhost:8006"
}

# 🔁 forward request function
async def forward_request(service, path, method, body=None):
    url = SERVICES[service] + path
    async with httpx.AsyncClient() as client:
        if method == "GET":
            response = await client.get(url)
        elif method == "POST":
            response = await client.post(url, json=body)
        elif method == "PUT":
            response = await client.put(url, json=body)
        elif method == "DELETE":
            response = await client.delete(url)
        return response.json()

# 🌐 Gateway routes - add your routes here

# Restaurant --------------------------------------------------------------------------
@app.get("/gateway/restaurants")
async def get_restaurants():
    return await forward_request("restaurant", "/api/restaurants", "GET")

@app.post("/gateway/restaurants")
async def create_restaurant(data: Restaurant):
    return await forward_request(
        "restaurant",
        "/api/restaurants",
        "POST",
        data.dict()
    )

#--------------------------------------------------------------------------------------

# Delivery ---------------------------------------------------------------------------
@app.get("/gateway/deliveries")
async def get_deliveries():
    # Delivery service list endpoints live under "/deliveries/"
    return await forward_request("delivery", "/deliveries/", "GET")

@app.post("/gateway/deliveries")
async def create_delivery(order_id: int, driver: str):
    # Delivery service expects `order_id` and `driver` as query params on POST.
    path = f"/deliveries/?order_id={order_id}&driver={driver}"
    return await forward_request("delivery", path, "POST", {})

@app.get("/gateway/deliveries/{delivery_id}")
async def get_delivery(delivery_id: int):
    return await forward_request("delivery", f"/deliveries/{delivery_id}", "GET")

# Menu --------------------------------------------------------------------------
@app.put("/gateway/deliveries/{delivery_id}/status")
async def update_delivery_status(delivery_id: int, status: str):
    # Delivery service expects `status` as a query param on PUT.
    path = f"/deliveries/{delivery_id}/status?status={status}"
    return await forward_request("delivery", path, "PUT", {})
@app.get("/gateway/menu")
async def get_all():
    return await forward_request("menu", "/api/menu", "GET")

@app.post("/gateway/menu")
async def create(item: MenuCreate):
    return await forward_request("menu", "/api/menu", "POST", item.dict())

@app.get("/gateway/menu/{id}")
async def get_one(id: int):
    return await forward_request("menu", f"/api/menu/{id}", "GET")

@app.put("/gateway/menu/{id}")
async def update(id: int, item: MenuUpdate):
    return await forward_request("menu", f"/api/menu/{id}", "PUT", item.dict())

@app.delete("/gateway/menu/{id}")
async def delete(id: int):
    return await forward_request("menu", f"/api/menu/{id}", "DELETE")

#-----User---------------------------------------------------------------------------------
class User(BaseModel):
    id: int
    name: str
    email: str

@app.get("/gateway/users")
async def get_users():
    return await forward_request("user", "/api/users", "GET")

@app.post("/gateway/users")
async def create_user(data: User):
    return await forward_request("user", "/api/users", "POST", data.dict())

# 💳 Payment ---------------------------------------------------------------------------
# YOUR ROUTES, updated to use the original code structure (Pydantic validation)
@app.get("/gateway/payments")
async def get_payments():
    return await forward_request("payment", "/api/payments", "GET")

@app.post("/gateway/payments")
async def create_payment(data: PaymentCreate):
    return await forward_request("payment", "/api/payments", "POST", data.dict())

# --------------------------------------------------------------------------------------
# SERVER RUNNER (From your code)
# --------------------------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
