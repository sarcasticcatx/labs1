from fastapi import FastAPI

from database.database import engine
from models.models import Base
from routes import accomodation_routes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(accomodation_routes.router)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
