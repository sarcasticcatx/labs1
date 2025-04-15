from fastapi import FastAPI
from routes import accomodation_routes


app = FastAPI()

app.include_router(accomodation_routes.router)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
