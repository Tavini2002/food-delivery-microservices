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

# Order --------------------------------------------------------------------------------------


@app.get("/gateway/orders")
async def get_orders():
    return await forward_request("order", "/api/orders", "GET")

@app.post("/gateway/orders")
async def create_order(req: Request):
    body = await req.json()
    return await forward_request("order", "/api/orders", "POST", body)