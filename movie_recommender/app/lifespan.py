from contextlib import asynccontextmanager

from app.services.model_loader import load_artifacts

from app.logging_config import logger
from app.config import settings


@asynccontextmanager
async def lifespan(app):

    logger.info(
        f"Loading model version: {settings.MODEL_VERSION}"
    )

    try:
        load_artifacts()

        logger.info(
            "Artifacts loaded successfully."
        )

        yield

    finally:
        logger.info(
            "Application shutting down."
        )
