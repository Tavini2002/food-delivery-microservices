from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(title="Payment Microservice", description="Handles payment processing")

# Temporary in-memory database
payments_db = [
    {"id": 1, "amount": 100.0, "status": "completed"},
    {"id": 2, "amount": 250.50, "status": "pending"}
]

class Payment(BaseModel):
    amount: float
    status: str = "pending"

@app.get("/api/payments", tags=["Payments"])
async def get_payments():
    """Get all payments directly from the microservice"""
    return {"message": "Success", "data": payments_db}

@app.post("/api/payments", tags=["Payments"])
async def create_payment(payment: Payment):
    """Create a new payment directly in the microservice"""
    new_payment = {"id": len(payments_db) + 1, "amount": payment.amount, "status": payment.status}
    payments_db.append(new_payment)
    return {"message": "Payment created successfully", "data": new_payment}

if __name__ == "__main__":
    import uvicorn
    # Run the Payment Microservice on port 8006
    uvicorn.run(app, host="0.0.0.0", port=8006)
