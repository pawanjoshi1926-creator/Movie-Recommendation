# app/services/model_loader.py

from pathlib import Path
from app.config import settings
import pickle

movies = None
similarity = None
artifact_dir = Path("artifacts") / settings.MODEL_VERSION


def load_artifacts():

    global movies, similarity

    movies_path = artifact_dir / "movies.pkl"
    similarity_path = artifact_dir / "similarity.pkl"

    # Validation
    if not movies_path.exists():
        raise FileNotFoundError(
            f"{movies_path} not found"
        )

    if not similarity_path.exists():
        raise FileNotFoundError(
            f"{similarity_path} not found"
        )

    # Load files
    with open(movies_path, "rb") as f:
        movies = pickle.load(f)

    with open(similarity_path, "rb") as f:
        similarity = pickle.load(f)

    return movies, similarity