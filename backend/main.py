from fastapi import FastAPI
from backend.routes.health import router as health_router

app = FastAPI(title="WhyBack API")

app.include_router(health_router)


@app.get("/")
def root():
    return {"message": "WhyBack backend is running"}