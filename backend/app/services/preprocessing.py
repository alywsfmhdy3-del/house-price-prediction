from __future__ import annotations

import pandas as pd

from app.schemas import PredictionRequest

FEATURE_COLUMNS = [
    "carpet_area_sqft",
    "floor_num",
    "Bathroom",
    "Balcony",
    "location_grouped",
    "Furnishing",
    "Transaction",
    "Ownership",
    "facing",
]


def request_to_dataframe(
    request: PredictionRequest,
    valid_locations: list[str],
) -> pd.DataFrame:
    location = request.location_grouped
    if location not in valid_locations:
        location = "Other"

    row = {
        "carpet_area_sqft": request.carpet_area_sqft,
        "floor_num": request.floor_num,
        "Bathroom": request.Bathroom,
        "Balcony": request.Balcony,
        "location_grouped": location,
        "Furnishing": request.Furnishing,
        "Transaction": request.Transaction,
        "Ownership": request.Ownership,
        "facing": request.facing,
    }
    return pd.DataFrame([row], columns=FEATURE_COLUMNS)
