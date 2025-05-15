from fastapi import APIRouter

from app.api.routes import predictor

router = APIRouter()
router.include_router(
    predictor.router,
    prefix="/predictor",
    tags=["Predictor"]
)
