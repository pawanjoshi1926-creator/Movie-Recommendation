from fastapi import APIRouter

router = APIRouter(
    tags=["Health"]
)

@router.get("/")
def home():
    return {
        "message": "Movie Recommendation API"
    }

@router.get("/health")
def health():
    return {
        "status": "healthy"
    }