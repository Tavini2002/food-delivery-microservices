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

@app.get("/gateway/menu")
async def get_all():
    return await forward_request("menu", "/api/menu", "GET")

@app.post("/gateway/menu")
async def create(req: Request):
    body = await req.json()
    return await forward_request("menu", "/api/menu", "POST", body)

@app.get("/gateway/menu/{id}")
async def get_one(id: int):
    return await forward_request("menu", f"/api/menu/{id}", "GET")

@app.put("/gateway/menu/{id}")
async def update(id: int, req: Request):
    body = await req.json()
    return await forward_request("menu", f"/api/menu/{id}", "PUT", body)

@app.delete("/gateway/menu/{id}")
async def delete(id: int):
    return await forward_request("menu", f"/api/menu/{id}", "DELETE")

#--------------------------------------------------------------------------------------