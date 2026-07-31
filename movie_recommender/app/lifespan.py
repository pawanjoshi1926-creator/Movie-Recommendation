from contextlib import asynccontextmanager
from pathlib import Path
import pickle

BASE_DIR = Path(__file__).resolve().parent.parent
from app.config import settings
from app.logging_config import logger


@asynccontextmanager
async def lifespan(app):
    
    logger.info("Loading artifacts...")

    app.state.movies = pickle.load(
        open(settings.ARTIFACT_DIR / "movies.pkl", "rb")
    )

    app.state.similarity = pickle.load(
        open(settings.ARTIFACT_DIR / "similarity.pkl", "rb")
    )

    print("Artifacts loaded successfully.")

    yield

    print("Application shutting down...")