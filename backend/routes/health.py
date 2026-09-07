from fastapi import APIRouter
from backend.models.health import HealthResponse
from backend.services.health_service import get_health_status

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
def health():
    return get_health_status()