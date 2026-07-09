from fastapi import FastAPI
from sqlalchemy import text

from app.database.database import engine

app = FastAPI()


@app.get("/")
def home():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        version = result.scalar()

    return {
        "message": "Database Connected Successfully!",
        "postgres_version": version
    }