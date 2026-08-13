from fastapi.testclient import TestClient

from app.main import app


def test_home():

    with TestClient(app) as client:

        response = client.get("/")

        assert response.status_code == 200

def test_health():

    with TestClient(app) as client:

        response = client.get("/health")

        assert response.status_code == 200

        data = response.json()

        assert data["status"] == "healthy"

def test_recommendation():

    with TestClient(app) as client:

        response = client.get(
            "/api/v1/recommend",
            params={"movie": "Avatar"}
        )

        assert response.status_code == 200

        data = response.json()

        assert data["movie"] == "Avatar"

        assert "recommendations" in data

def test_movie_not_found():

    with TestClient(app) as client:

        response = client.get(
            "/api/v1/recommend",
            params={"movie": "ThisMovieDoesNotExist"}
        )

        assert response.status_code == 404

from app.schemas import Recommendation


def test_recommendation_schema():

    recommendation = Recommendation(
        title="Avatar",
        similarity_score=0.91
    )

    assert recommendation.title == "Avatar"

    assert recommendation.similarity_score == 0.91

import pytest

from pydantic import ValidationError
from app.schemas import Recommendation


def test_invalid_similarity_score():

    with pytest.raises(ValidationError):

        Recommendation(
            title="Avatar",
            similarity_score=2.0
        )