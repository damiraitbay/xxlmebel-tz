from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, shemas


router = APIRouter(prefix="/furniture")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[shemas.FurnitureOut])
def list_furniture(
    category: str | None = Query(None),
    db: Session = Depends(get_db),
):
    return crud.get_furniture(db, category)


@router.get("/{item_id}", response_model=shemas.FurnitureOut)
def get_item(item_id: int, db: Session = Depends(get_db)):
    return crud.get_furniture_by_id(db, item_id)
