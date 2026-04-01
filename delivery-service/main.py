from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models
from data_service import engine, get_db

# This line creates the 'deliveries' table in delivery.db if it doesn't exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Delivery Service")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Delivery Service API. Use /docs to view the API documentation."}

@app.post("/deliveries/")
def create_delivery(order_id: int, driver: str, db: Session = Depends(get_db)):
    new_delivery = models.Delivery(order_id=order_id, driver_name=driver)
    db.add(new_delivery)
    db.commit()
    db.refresh(new_delivery)
    return new_delivery

@app.get("/deliveries/")
def get_all_deliveries(db: Session = Depends(get_db)):
    return db.query(models.Delivery).all()

@app.get("/deliveries/{delivery_id}")
def get_delivery_status(delivery_id: int, db: Session = Depends(get_db)):
    return db.query(models.Delivery).filter(models.Delivery.id == delivery_id).first()

@app.put("/deliveries/{delivery_id}/status")
def update_delivery_status(delivery_id: int, status: str, db: Session = Depends(get_db)):
    delivery = db.query(models.Delivery).filter(models.Delivery.id == delivery_id).first()
    if not delivery:
        return {"error": "Delivery not found"}
    delivery.status = status
    db.commit()
    db.refresh(delivery)
    return delivery