from models import User
from schemas import UserClient

def get_all_users(db):
    return db.query(User).all()

def get_user_by_id(db, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db, user_data: UserClient):
    new_user = User(username=user_data.username, email=user_data.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
