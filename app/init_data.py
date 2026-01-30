from app.database import SessionLocal
from app.models import Furniture


def init_furniture_data():
    """Инициализация начальных данных для таблицы furniture"""
    db = SessionLocal()
    try:
        # Проверяем, есть ли уже данные
        if db.query(Furniture).count() > 0:
            print("Данные в таблице furniture уже существуют, пропускаем инициализацию")
            return

        # Начальные данные мебели
        initial_furniture = [
            Furniture(name="Диван угловой", price=45000.0, category="Диваны"),
            Furniture(name="Диван прямой", price=35000.0, category="Диваны"),
            Furniture(name="Кровать двуспальная", price=55000.0, category="Кровати"),
            Furniture(name="Кровать односпальная", price=30000.0, category="Кровати"),
            Furniture(name="Шкаф-купе 3-дверный", price=65000.0, category="Шкафы"),
            Furniture(name="Шкаф-купе 2-дверный", price=45000.0, category="Шкафы"),
            Furniture(name="Стол обеденный", price=25000.0, category="Столы"),
            Furniture(name="Стол письменный", price=20000.0, category="Столы"),
            Furniture(name="Стул офисный", price=5000.0, category="Стулья"),
            Furniture(name="Стул кухонный", price=3500.0, category="Стулья"),
            Furniture(name="Комод 4-ящичный", price=18000.0, category="Комоды"),
            Furniture(name="Тумба прикроватная", price=8000.0, category="Тумбы"),
        ]

        db.add_all(initial_furniture)
        db.commit()
        print(f"Инициализировано {len(initial_furniture)} записей в таблице furniture")
    except Exception as e:
        print(f"Ошибка при инициализации данных: {e}")
        db.rollback()
    finally:
        db.close()
