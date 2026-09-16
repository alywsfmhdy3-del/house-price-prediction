import json
from pathlib import Path

import joblib


class ModelService:
    def __init__(self) -> None:
        self.model = None
        self.locations: list[str] = []

    def load(self, model_path: str | Path, locations_path: str | Path) -> None:
        model_file = Path(model_path)
        locations_file = Path(locations_path)

        if not model_file.exists():
            raise FileNotFoundError(f"Model file not found: {model_file}")
        if not locations_file.exists():
            raise FileNotFoundError(f"Locations file not found: {locations_file}")

        self.model = joblib.load(model_file)
        with locations_file.open(encoding="utf-8") as handle:
            self.locations = json.load(handle)

        if not isinstance(self.locations, list):
            raise ValueError("locations.json must contain a JSON array of strings")

    def is_loaded(self) -> bool:
        return self.model is not None and isinstance(self.locations, list) and len(self.locations) > 0


model_service = ModelService()
