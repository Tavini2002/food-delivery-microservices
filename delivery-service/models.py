from sqlalchemy import Column, Integer, String
from data_service import Base

class Delivery(Base):
    __tablename__ = "deliveries"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, nullable=False)
    driver_name = Column(String, nullable=False)
    status = Column(String, default="Pending") # Statuses: Picked Up, Out for Delivery, Delivered