from fastapi import FastAPI

from app.database.database import Base, engine
from app.database import base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="IntelliWealth API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "IntelliWealth API is Running"
    }