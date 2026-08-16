from fastapi import APIRouter, Depends, HTTPException

from app.dependencies.model import  get_model
from app.recommender import recommend
from app.schemas import RecommendationResponse

router = APIRouter(
    prefix="/api/v1",
    tags=["Recommendation"]
)


@router.get("/recommend")
def recommend_movie(
    movie: str,
    model=Depends(get_model)
):

    result = model.predict(
        {
            "movie": [movie]
        }
    )

    return result
