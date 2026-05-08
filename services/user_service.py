from sqlalchemy.orm import Session
from models.user import UserModel
from schemas.user import User

def create_user(db: Session, user: User):
    new_user = UserModel(
        username=user.username,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def find_user(db: Session, username: str):
    return db.query(UserModel).filter(UserModel.username == username).first()