from fastapi import APIRouter
from sqlalchemy import text

from backend.database import engine

router = APIRouter()


@router.get("/health/database")
def database_health():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {"database": "ok"}