from fastapi import APIRouter, Depends, HTTPException

from app.dependencies.models import ModelStore, get_models
from app.recommender import recommend
from app.schemas import RecommendationResponse

router = APIRouter(
    prefix="/api/v1",
    tags=["Recommendation"]
)


@router.get(
    "/recommend",
    response_model=RecommendationResponse
)
def recommend_movie(
    movie: str,
    models: ModelStore = Depends(get_models)
):

    result = recommend(
        movie_name=movie,
        movies=models.movies,
        similarity=models.similarity
    )

    if len(result["recommendations"]) == 0:
        raise HTTPException(
            status_code=404,
            detail={
                "message": "Movie not found",
                "suggestions": result["suggestions"]
            }
        )

    return result