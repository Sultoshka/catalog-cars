from fastapi import APIRouter, HTTPException
from cars.models import Car
from cars.crud import get_all_cars, get_car, add_car, update_car, delete_car
from typing import List

router = APIRouter()

@router.get("/cars/", response_model=List[Car])
def read_cars():
    return get_all_cars()

@router.get("/cars/{car_id}", response_model=Car)
def read_car(car_id: int):
    car = get_car(car_id)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@router.post("/cars/", response_model=Car)
def create_car(car: Car):
    add_car(car)
    return car

@router.put("/cars/{car_id}", response_model=Car)
def update_existing_car(car_id: int, car: Car):
    updated_car = update_car(car_id, car)
    if updated_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return updated_car

@router.delete("/cars/{car_id}", response_model=Car)
def delete_existing_car(car_id: int):
    car = delete_car(car_id)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car