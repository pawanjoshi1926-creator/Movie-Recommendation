from fastapi import APIRouter, Depends

from app.dependencies.model import (
    get_movies,
    get_similarity
)
from app.config import settings

router = APIRouter(
    tags=["Health"]
)

@router.get("/")
def home():
    return {
        "message": "Movie Recommendation API"
    }

@router.get("/health")
def health_check():

    return {
        "status": "healthy",
        "model_version": settings.MODEL_VERSION,
        "app_version": settings.VERSION
    }

import mlflow


def get_model_version():

    return "1"
