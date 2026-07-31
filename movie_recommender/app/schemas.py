from pydantic import BaseModel, Field
from typing import List


class Recommendation(BaseModel):
    title: str = Field(
        ...,
        description="Recommended movie title",
        example="John Carter"
    )

    similarity_score: float = Field(
        ...,
        ge=0,
        le=1,
        description="Cosine similarity score",
        example=0.914
    )


class RecommendationResponse(BaseModel):
    movie: str = Field(
        ...,
        description="Movie selected by the user",
        example="Avatar"
    )

    recommendations: List[Recommendation]