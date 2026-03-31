from fastapi import FastAPI
import httpx

app = FastAPI(title="API Gateway", description="Main entry point for all microservices")

SERVICES = {
    "payment": "http://localhost:8006"
}

from fastapi import HTTPException

from typing import Optional

async def forward_request(service: str, path: str, method: str, body: Optional[dict] = None):
    url = SERVICES[service] + path
    try:
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
    except httpx.RequestError as exc:
        raise HTTPException(status_code=503, detail=f"Microservice '{service}' at {url} is unavailable.")

# Gateway routes - payment service
@app.get("/gateway/payments", tags=["Payment Service"])
async def gateway_list_payments():
    """Forward GET request to Payment microservice"""
    return await forward_request("payment", "/api/payments", "GET")

@app.post("/gateway/payments", tags=["Payment Service"])
async def gateway_create_payment(body: dict):
    """Forward POST request to Payment microservice"""
    return await forward_request("payment", "/api/payments", "POST", body)

if __name__ == "__main__":
    import uvicorn
    # Run the Gateway on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
