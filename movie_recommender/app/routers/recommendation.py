from fastapi import APIRouter, HTTPException

from app.services.recommender import recommend
from app.exceptions import MovieNotFoundException

from app.dependencies.model import (
    get_movies,
    get_similarity
)

router = APIRouter(
    prefix="/api/v1",
    tags=["Recommendation"]
)

@router.get("/recommend")
def get_recommendations(movie: str):

    movies = get_movies()
    similarity = get_similarity()

    try:

        result = recommend(
            movie,
            movies,
            similarity
        )

        return {
            "success": True,
            **result
        }

    except MovieNotFoundException as e:

        raise HTTPException(
            status_code=404,
            detail={
                "success": False,
                "message": f"Movie '{e.movie_name}' not found",
                "suggestions": e.suggestions
            }
        )
