from fastapi import APIRouter, Depends

from app.dependencies.model import  get_model

router = APIRouter(
    tags=["Health"]
)

@router.get("/")
def home():
    return {
        "message": "Movie Recommendation API"
    }

@router.get("/health")
def health(model=Depends(get_model)):

    return {
        "status": "healthy",
        "model_loaded": model is not None
    }

import mlflow


def get_model_version():

    return "1"
