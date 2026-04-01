from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import httpx

# 🚀 Initialize app
app = FastAPI(title="API Gateway")

# ---------------------------------------------------------------------------
# 🔗 SERVICES CONFIGURATION
# ---------------------------------------------------------------------------
SERVICES = {
    "user": "http://localhost:8001",
    "restaurant": "http://localhost:8002",
    "menu": "http://localhost:8003",
    "order": "http://localhost:8004",
    "delivery": "http://localhost:8005",
    "payment": "http://localhost:8006"
}

# ---------------------------------------------------------------------------
# 🔁 FORWARD REQUEST FUNCTION
# ---------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------
# 📦 MODELS
# ---------------------------------------------------------------------------

# 👤 User
class User(BaseModel):
    id: int
    name: str
    email: str

# 🍽️ Restaurant
class Restaurant(BaseModel):
    name: str
    location: str
    cuisine: str

# 🍔 Menu
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

# 📦 Order
class Order(BaseModel):
    id: int
    item: str
    quantity: int

# 💳 Payment
class PaymentCreate(BaseModel):
    order_id: int
    amount: float
    payment_method: str

# ---------------------------------------------------------------------------
# 🌐 USER ROUTES
# ---------------------------------------------------------------------------
@app.get("/gateway/users")
async def get_users():
    return await forward_request("user", "/api/users", "GET")

@app.post("/gateway/users")
async def create_user(data: User):
    return await forward_request("user", "/api/users", "POST", data.dict())

# ---------------------------------------------------------------------------
# 🍽️ RESTAURANT ROUTES
# ---------------------------------------------------------------------------
@app.get("/gateway/restaurants")
async def get_restaurants():
    return await forward_request("restaurant", "/api/restaurants", "GET")

@app.post("/gateway/restaurants")
async def create_restaurant(data: Restaurant):
    return await forward_request("restaurant", "/api/restaurants", "POST", data.dict())

# ---------------------------------------------------------------------------
# 🍔 MENU ROUTES
# ---------------------------------------------------------------------------
@app.get("/gateway/menu")
async def get_menu():
    return await forward_request("menu", "/api/menu", "GET")

@app.post("/gateway/menu")
async def create_menu(item: MenuCreate):
    return await forward_request("menu", "/api/menu", "POST", item.dict())

@app.get("/gateway/menu/{id}")
async def get_menu_item(id: int):
    return await forward_request("menu", f"/api/menu/{id}", "GET")

@app.put("/gateway/menu/{id}")
async def update_menu(id: int, item: MenuUpdate):
    return await forward_request("menu", f"/api/menu/{id}", "PUT", item.dict())

@app.delete("/gateway/menu/{id}")
async def delete_menu(id: int):
    return await forward_request("menu", f"/api/menu/{id}", "DELETE")

# ---------------------------------------------------------------------------
# 📦 ORDER ROUTES
# ---------------------------------------------------------------------------
@app.get("/gateway/orders")
async def get_orders():
    return await forward_request("order", "/api/orders", "GET")

@app.post("/gateway/orders")
async def create_order(data: Order):
    return await forward_request("order", "/api/orders", "POST", data.dict())

# ---------------------------------------------------------------------------
# 🚚 DELIVERY ROUTES
# ---------------------------------------------------------------------------
@app.get("/gateway/deliveries")
async def get_deliveries():
    return await forward_request("delivery", "/deliveries/", "GET")

@app.post("/gateway/deliveries")
async def create_delivery(order_id: int, driver: str):
    path = f"/deliveries/?order_id={order_id}&driver={driver}"
    return await forward_request("delivery", path, "POST", {})

@app.get("/gateway/deliveries/{delivery_id}")
async def get_delivery(delivery_id: int):
    return await forward_request("delivery", f"/deliveries/{delivery_id}", "GET")

@app.put("/gateway/deliveries/{delivery_id}/status")
async def update_delivery_status(delivery_id: int, status: str):
    path = f"/deliveries/{delivery_id}/status?status={status}"
    return await forward_request("delivery", path, "PUT", {})

# ---------------------------------------------------------------------------
# 💳 PAYMENT ROUTES
# ---------------------------------------------------------------------------
@app.get("/gateway/payments")
async def get_payments():
    return await forward_request("payment", "/api/payments", "GET")

@app.post("/gateway/payments")
async def create_payment(data: PaymentCreate):
    return await forward_request("payment", "/api/payments", "POST", data.dict())

# ---------------------------------------------------------------------------
# 🚀 RUN SERVER
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)