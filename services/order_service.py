from sqlalchemy.orm import Session
from models.order import OrderModel
from schemas.order import OrderItem
from services.product_service import find_product
from fastapi import HTTPException

def create_new_order(db: Session, order_items: list[OrderItem]):

    total_price = 0
    order_summary = []

    # Validation
    for item in order_items:

        product = find_product(db, item.product_id)

        if not product:
            raise HTTPException(
                status_code=404,
                detail=f"Product with id {item.product_id} not found"
            )

        if product.quantity == 0:
            raise HTTPException(
                status_code=400,
                detail=f"{product.name} is out of stock"
            )

        if item.quantity > product.quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Only {product.quantity} of {product.name} available"
            )

    # Process order
    for item in order_items:

        product = find_product(db, item.product_id)

        product.quantity -= item.quantity

        total_price += product.price * item.quantity

        order_summary.append(
            f"{product.name} x{item.quantity}"
        )

    new_order = OrderModel(
        items=", ".join(order_summary),
        total_price=total_price
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return {
        "message": "Order created successfully",
        "order": {
            "id": new_order.id,
            "items": new_order.items,
            "total_price": new_order.total_price
        }
    }

def get_all_orders(db: Session):

    orders = db.query(OrderModel).all()

    return orders