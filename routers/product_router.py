from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.product import Product
from services.product_service import get_all_products, add_product
from database.connection import get_db

router = APIRouter()

@router.get("/products")
def get_products(db: Session = Depends(get_db)):
    return get_all_products(db)

@router.post("/products", status_code=201)
def create_product(product: Product, db: Session = Depends(get_db)):
    return add_product(db, product)