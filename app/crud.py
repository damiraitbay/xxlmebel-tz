from sqlalchemy.orm import Session
from app import models


def get_furniture(db: Session, category: str | None = None):
    query = db.query(models.Furniture)
    if category:
        query = query.filter(models.Furniture.category == category)
    return query.all()


def get_furniture_by_id(db: Session, item_id: int):
    return db.query(models.Furniture).filter(models.Furniture.id == item_id).first()


def create_order(db: Session, email: str, item_ids: list[int]):
    items = db.query(models.Furniture).filter(models.Furniture.id.in_(item_ids)).all()
    total = sum(i.price for i in items)

    order = models.Order(email=email, total_price=total)
    db.add(order)
    db.flush()  # get order.id

    for item in items:
        db.add(models.OrderItem(order_id=order.id, furniture_id=item.id))

    db.commit()
    db.refresh(order)
    return order


def get_orders_by_email(db: Session, email: str):
    return db.query(models.Order).filter(models.Order.email == email).all()