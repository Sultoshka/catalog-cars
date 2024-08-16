from fastapi.testclient import TestClient
from src.main import app
from cars.models import Car

client = TestClient(app)

def test_create_car():
    # Тестируем создание нового автомобиля
    response = client.post("/cars/", json={
        "id": 1,
        "model": "BYD Tang",
        "price": 40000,
        "year": 2024,
        "mileage": 0,
        "description": "New BYD Tang 2024",
        "in_stock": True
    })
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "model": "BYD Tang",
        "price": 40000,
        "year": 2024,
        "mileage": 0,
        "description": "New BYD Tang 2024",
        "in_stock": True
    }

def test_get_all_cars():
    # Тестируем получение списка всех автомобилей
    response = client.get("/cars/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_get_car():
    # Тестируем получение конкретного автомобиля по ID
    response = client.get("/cars/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "model": "BYD Tang",
        "price": 40000,
        "year": 2024,
        "mileage": 0,
        "description": "New BYD Tang 2024",
        "in_stock": True
    }

def test_update_car():
    # Тестируем обновление информации об автомобиле
    response = client.put("/cars/1", json={
        "id": 1,
        "model": "BYD Tang Updated",
        "price": 42000,
        "year": 2024,
        "mileage": 100,
        "description": "Updated BYD Tang 2024",
        "in_stock": True
    })
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "model": "BYD Tang Updated",
        "price": 42000,
        "year": 2024,
        "mileage": 100,
        "description": "Updated BYD Tang 2024",
        "in_stock": True
    }

def test_delete_car():
    # Тестируем удаление автомобиля
    response = client.delete("/cars/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "model": "BYD Tang Updated",
        "price": 42000,
        "year": 2024,
        "mileage": 100,
        "description": "Updated BYD Tang 2024",
        "in_stock": True
    }

    # Проверяем, что автомобиль был удален
    response = client.get("/cars/1")
    assert response.status_code == 404
