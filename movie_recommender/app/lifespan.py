from contextlib import asynccontextmanager

from app.config import settings
from app.services.model_loader import load_model


@asynccontextmanager
async def lifespan(app):

    print("Loading MLflow model...")

    load_model(
        settings.MLFLOW_MODEL_URI
    )

    print("Model loaded.")

    yield

    print("Shutting down...")
