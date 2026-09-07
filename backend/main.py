from fastapi import FastAPI
from backend.routes.health import router as health_router
from backend.routes.database_health import router as database_health_router
app = FastAPI(title="WhyBack API")

app.include_router(health_router)
app.include_router(database_health_router)


@app.get("/")
def root():
    return {"message": "WhyBack backend is running"}