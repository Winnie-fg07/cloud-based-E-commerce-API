from sqlalchemy.orm import Session
from models.product import ProductModel
from schemas.product import Product
from fastapi import HTTPException

def get_all_products(db: Session):
    return db.query(ProductModel).all()

def add_product(db: Session, product: Product):

    existing_product = find_product(db, product.id)

    if existing_product:
        raise HTTPException(
            status_code=409,
            detail="Product already exists"
        )

    new_product = ProductModel(
        id=product.id,
        name=product.name,
        price=product.price,
        quantity=product.quantity
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

def find_product(db: Session, product_id: int):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    return product