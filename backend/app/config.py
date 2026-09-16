from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND_ROOT = Path(__file__).resolve().parents[1]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BACKEND_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    MODEL_PATH: str = "models/house_price.pkl"
    LOCATIONS_PATH: str = "models/locations.json"
    CORS_ORIGINS: list[str] = Field(
        default_factory=lambda: [
            "http://localhost:5173",
            "http://localhost:3000",
        ]
    )

    @property
    def model_file(self) -> Path:
        path = Path(self.MODEL_PATH)
        return path if path.is_absolute() else BACKEND_ROOT / path

    @property
    def locations_file(self) -> Path:
        path = Path(self.LOCATIONS_PATH)
        return path if path.is_absolute() else BACKEND_ROOT / path


settings = Settings()
