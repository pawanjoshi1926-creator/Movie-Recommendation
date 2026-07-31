from fastapi import FastAPI

from app.lifespan import lifespan

from app.routers.health import router as health_router
from app.routers.recommendation import router as recommendation_router

from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    lifespan=lifespan
)

app.include_router(health_router)
app.include_router(recommendation_router)