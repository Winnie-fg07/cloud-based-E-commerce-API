from sqlalchemy import Column, Integer, Float, String
from database.connection import Base

class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    items = Column(String, nullable=False)
    total_price = Column(Float, nullable=False)