from fastapi import FastAPI

from lab1.database.database import engine
from lab1.models.models import Base
from lab1.routes import accomodation_routes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(accomodation_routes.router)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/api")
async def get_accommodation():
    return {"message": "List of accommodations"}
