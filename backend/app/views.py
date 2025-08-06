from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/items/")
def create_item(name: str, description: str, db: Session = Depends(get_db)):
    db_item = models.Item(name=name, description=description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/test_connection")
def test_connection():
    return {"message": "Connection to backend successful!"}