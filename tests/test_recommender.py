import numpy as np
import pandas as pd

from app.recommender import recommend


def test_recommend_returns_correct_number():

    movies = pd.DataFrame({
        "title": [
            "Avatar",
            "Titanic",
            "Inception",
            "Interstellar",
            "The Matrix",
            "Gladiator"
        ]
    })

    similarity = np.array([
        [1.0, 0.9, 0.8, 0.7, 0.6, 0.5],
        [0.9, 1.0, 0.7, 0.6, 0.5, 0.4],
        [0.8, 0.7, 1.0, 0.9, 0.8, 0.6],
        [0.7, 0.6, 0.9, 1.0, 0.8, 0.7],
        [0.6, 0.5, 0.8, 0.8, 1.0, 0.7],
        [0.5, 0.4, 0.6, 0.7, 0.7, 1.0]
    ])

    result = recommend(
        movie_name="Avatar",
        movies=movies,
        similarity=similarity,
        top_n=5
    )

    assert len(result["recommendations"]) == 5

def test_movie_not_found():

    movies = pd.DataFrame({
        "title": [
            "Avatar",
            "Titanic",
            "Inception"
        ]
    })

    similarity = np.eye(3)

    result = recommend(
        movie_name="Unknown Movie",
        movies=movies,
        similarity=similarity,
        top_n=5
    )

    assert result["recommendations"] == []