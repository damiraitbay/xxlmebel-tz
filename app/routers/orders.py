from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, shemas
from app.email_service import send_order_confirmation

router = APIRouter(prefix="/orders")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=shemas.OrderOut)
def create_order(order: shemas.OrderCreate, db: Session = Depends(get_db)):
    created = crud.create_order(db, order.email, order.items)
    # Имитация отправки письма на email через SMTP (MailHog)
    send_order_confirmation(
        to_email=created.email,
        order_id=created.id,
        total_price=created.total_price,
    )
    return created


@router.get("/", response_model=list[shemas.OrderOut])
def get_orders(email: str = Query(...), db: Session = Depends(get_db)):
    return crud.get_orders_by_email(db, email)