from fastapi import FastAPI, Request
import httpx

app = FastAPI(title="API Gateway")

# 🔗 connect your services here
SERVICES = {
    "restaurant": "http://localhost:8002"
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

# 🌐 Gateway routes
@app.get("/gateway/restaurants")
async def get_restaurants():
    return await forward_request("restaurant", "/api/restaurants", "GET")

@app.post("/gateway/restaurants")
async def create_restaurant(req: Request):
    body = await req.json()
    return await forward_request("restaurant", "/api/restaurants", "POST", body)