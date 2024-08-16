from fastapi import FastAPI
from cars.routers import router as car_router

app = FastAPI()

app.include_router(car_router)