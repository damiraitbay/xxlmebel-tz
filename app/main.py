import time
from fastapi import FastAPI
from sqlalchemy.exc import OperationalError
from app.database import Base, engine
from app.routers import furniture, orders
from app.init_data import init_furniture_data


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    """Инициализация базы данных и данных при запуске приложения"""
    # Ждем готовности базы данных с повторными попытками
    max_retries = 10
    retry_delay = 2  # секунды
    
    for attempt in range(max_retries):
        try:
            # Создаем таблицы
            Base.metadata.create_all(bind=engine)
            print("Таблицы успешно созданы")
            
            # Инициализируем начальные данные
            init_furniture_data()
            print("Приложение готово к работе")
            break
        except OperationalError as e:
            if attempt < max_retries - 1:
                print(f"Попытка подключения к БД {attempt + 1}/{max_retries} не удалась, повтор через {retry_delay} сек...")
                time.sleep(retry_delay)
            else:
                print(f"Не удалось подключиться к БД после {max_retries} попыток: {e}")
                raise


app.include_router(furniture.router)
app.include_router(orders.router)