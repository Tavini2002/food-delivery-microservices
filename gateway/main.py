from fastapi import FastAPI, Request
import httpx

app = FastAPI(title="API Gateway")

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
async def create_restaurant(req: Request):
    body = await req.json()
    return await forward_request("restaurant", "/api/restaurants", "POST", body)

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

@app.put("/gateway/deliveries/{delivery_id}/status")
async def update_delivery_status(delivery_id: int, status: str):
    # Delivery service expects `status` as a query param on PUT.
    path = f"/deliveries/{delivery_id}/status?status={status}"
    return await forward_request("delivery", path, "PUT", {})