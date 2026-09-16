from typing import Literal

from pydantic import BaseModel, Field

FurnishingType = Literal["Furnished", "Semi-Furnished", "Unfurnished"]
TransactionType = Literal["New Property", "Resale"]


class PredictionRequest(BaseModel):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "carpet_area_sqft": 1200,
                    "floor_num": 5,
                    "Bathroom": 2,
                    "Balcony": 1,
                    "location_grouped": "mumbai",
                    "Furnishing": "Semi-Furnished",
                    "Transaction": "Resale",
                    "Ownership": "Freehold",
                    "facing": "East",
                }
            ]
        }
    }

    carpet_area_sqft: float = Field(..., gt=0, le=100000)
    floor_num: int = Field(..., ge=0, le=200)
    Bathroom: int = Field(..., ge=0, le=20)
    Balcony: int = Field(..., ge=0, le=20)
    location_grouped: str = Field(..., min_length=1)
    Furnishing: FurnishingType
    Transaction: TransactionType
    Ownership: str = Field(..., min_length=1)
    facing: str = Field(..., min_length=1)


class PredictionResponse(BaseModel):
    predicted_price: float
    predicted_price_lac: float
    predicted_price_cr: float
    currency: str = "INR"


class HealthResponse(BaseModel):
    status: str = "ok"
    model_loaded: bool
