"""Create a tiny compatible pipeline when house_price.pkl is not present yet."""

from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

BACKEND_ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = BACKEND_ROOT / "models" / "house_price.pkl"

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


def main() -> None:
    rng = np.random.default_rng(42)
    n = 80
    locations = ["mumbai", "bangalore", "new-delhi", "Other"]
    furnishings = ["Furnished", "Semi-Furnished", "Unfurnished"]
    transactions = ["New Property", "Resale"]
    ownerships = ["Freehold", "Leasehold", "Co-operative Society", "Power of Attorney"]
    facings = [
        "North",
        "South",
        "East",
        "West",
        "North-East",
        "North-West",
        "South-East",
        "South-West",
    ]

    X = pd.DataFrame(
        {
            "carpet_area_sqft": rng.uniform(400, 2500, n),
            "floor_num": rng.integers(0, 20, n),
            "Bathroom": rng.integers(1, 4, n),
            "Balcony": rng.integers(0, 3, n),
            "location_grouped": rng.choice(locations, n),
            "Furnishing": rng.choice(furnishings, n),
            "Transaction": rng.choice(transactions, n),
            "Ownership": rng.choice(ownerships, n),
            "facing": rng.choice(facings, n),
        }
    )[FEATURE_COLUMNS]
    y = 2_000_000 + X["carpet_area_sqft"] * 8_000 + X["Bathroom"] * 400_000

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "num",
                Pipeline(
                    steps=[
                        ("imputer", SimpleImputer(strategy="median")),
                        ("scaler", StandardScaler()),
                    ]
                ),
                ["carpet_area_sqft", "floor_num", "Bathroom", "Balcony"],
            ),
            (
                "cat",
                Pipeline(
                    steps=[
                        ("imputer", SimpleImputer(strategy="most_frequent")),
                        ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=True)),
                    ]
                ),
                ["location_grouped", "Furnishing", "Transaction", "Ownership", "facing"],
            ),
        ]
    )

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", RandomForestRegressor(n_estimators=10, random_state=42)),
        ]
    )
    pipeline.fit(X, y)

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, MODEL_PATH, compress=3)
    print(f"Wrote placeholder model to {MODEL_PATH}")


if __name__ == "__main__":
    main()
