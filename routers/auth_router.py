from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.user import User
from services.user_service import create_user, find_user
from auth.auth_handler import (
    create_token,
    hash_password,
    verify_password
)
from database.connection import get_db
from fastapi import HTTPException

router = APIRouter()

@router.post("/register", status_code=201)
def register(user: User, db: Session = Depends(get_db)):

    existing_user = find_user(db, user.username)

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="User already exists"
        )

    user.password = hash_password(user.password)

    create_user(db, user)

    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: User, db: Session = Depends(get_db)):

    existing_user = find_user(db, user.username)

    if not existing_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(user.password, existing_user.password):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_token(existing_user.username)

    return {"access_token": token}