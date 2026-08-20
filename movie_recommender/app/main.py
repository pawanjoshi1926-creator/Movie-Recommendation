from fastapi import FastAPI

from app.lifespan import lifespan

from app.routers.health import router as health_router
from app.routers.recommendation import router as recommendation_router

from app.config import settings
from app.exception_handlers import (
    generic_exception_handler
)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    lifespan=lifespan
)
app.add_exception_handler(
    Exception,
    generic_exception_handler
)

app.include_router(health_router)
app.include_router(recommendation_router)
