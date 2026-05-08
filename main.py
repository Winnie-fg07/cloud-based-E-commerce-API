from fastapi import FastAPI
from routers import product_router, order_router, auth_router
from database.connection import engine, Base
from models.product import ProductModel
from models.user import UserModel
from models.order import OrderModel
app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(product_router.router)
app.include_router(order_router.router)
app.include_router(auth_router.router)
@app.get("/")
def root():
    return {"MESSAGE": "E-COMMERCE💸💸 IS RUNNING"}

@app.get("/introducing-me")
def introduce_me():
    return {"MESSAGE": "HELLO️!! I'M WINNIE THE CREATOR OF THIS API, JUST LETTING YOU KNOW YOUR FASTAPI IS WORKING"}