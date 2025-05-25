from fastapi import FastAPI

from lab1.database.database import engine
from lab1.models.models import Base
from lab1.routes import accomodation_routes, temp_reservations
from fastapi.middleware.cors import CORSMiddleware
Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:5173",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/")
# def read_root():
#     return {"message": "Hello, FastAPI!"}
#
#
# @app.get("/api")
# async def get_accommodation():
#     return {"message": "List of accommodations"}

app.include_router(accomodation_routes.router)
app.include_router(temp_reservations.router)