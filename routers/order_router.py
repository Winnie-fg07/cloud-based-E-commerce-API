from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas.order import OrderItem
from services.order_service import create_new_order, get_all_orders
from auth.auth_handler import get_current_user
from database.connection import get_db

router = APIRouter()

@router.post("/orders", status_code=201)
def create_order(
    order_items: List[OrderItem],
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return create_new_order(db, order_items)

@router.get("/orders")
def get_orders(db: Session = Depends(get_db)):
    return get_all_orders(db)