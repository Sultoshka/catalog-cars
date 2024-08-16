from typing import List
from cars.models import Car

car_db: List[Car] = []

def get_all_cars() -> List[Car]:
    return car_db

def get_car(car_id: int) -> Car:
    return next((car for car in car_db if car.id == car_id), None)

def add_car(car: Car):
    car_db.append(car)

def update_car(car_id: int, updated_car: Car) -> Car:
    car = get_car(car_id)
    if car:
        car.model = updated_car.model
        car.price = updated_car.price
        car.year = updated_car.year
        car.mileage = updated_car.mileage
        car.description = updated_car.description
        car.in_stock = updated_car.in_stock
    return car

def delete_car(car_id: int) -> Car:
    car = get_car(car_id)
    if car:
        car_db.remove(car)
    return car