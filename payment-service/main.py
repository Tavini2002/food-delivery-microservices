from fastapi import FastAPI, HTTPException, status
from typing import List
from models import Payment, PaymentCreate, PaymentUpdate
from service import PaymentService

app = FastAPI(title="Payment Service")

payment_service = PaymentService()

@app.get("/")
def root():
    return {"message": "Payment Service Running"}

@app.get("/api/payments", response_model=List[Payment])
def get_all():
    return payment_service.get_all()

@app.get("/api/payments/{id}", response_model=Payment)
def get_one(id: int):
    payment = payment_service.get_by_id(id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@app.post("/api/payments", response_model=Payment, status_code=status.HTTP_201_CREATED)
def create(payment: PaymentCreate):
    return payment_service.create(payment)

@app.put("/api/payments/{id}", response_model=Payment)
def update(id: int, payment: PaymentUpdate):
    updated = payment_service.update(id, payment)
    if not updated:
        raise HTTPException(status_code=404, detail="Payment not found")
    return updated

@app.delete("/api/payments/{id}")
def delete(id: int):
    if not payment_service.delete(id):
        raise HTTPException(status_code=404, detail="Payment not found")
    return {"message": "Deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8006)
