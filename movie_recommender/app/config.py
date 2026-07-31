from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):

    APP_NAME: str = "Movie Recommendation API"

    VERSION: str = "1.0.0"

    ARTIFACT_DIR: Path = BASE_DIR / "artifacts"

    DEFAULT_RECOMMENDATIONS: int = 5

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()