from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import UserClient
from database import SessionLocal, engine
import models
from crud import create_user, get_all_users, get_user_by_id

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
def read_users(db: Session= Depends(get_db)):
    users = get_all_users(db)
    return users

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/create_user", response_model=UserClient)
def create_new_user(user_data: UserClient, db: Session = Depends(get_db)):
    user = create_user(db, user_data)
    return user
