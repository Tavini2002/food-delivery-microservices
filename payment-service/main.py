from fastapi import FastAPI
import httpx

app = FastAPI(title="API Gateway")

SERVICES = {
   
    "payment": "http://localhost:8006"
}


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
        else:
            raise ValueError(f"Unsupported method: {method}")
    return response.json()


# Gateway routes - payment service only
@app.get("/gateway/payments")
async def gateway_list_payments():
    return await forward_request("payment", "/api/payments", "GET")


@app.post("/gateway/payments")
async def gateway_create_payment(body: dict):
    return await forward_request("payment", "/api/payments", "POST", body)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
