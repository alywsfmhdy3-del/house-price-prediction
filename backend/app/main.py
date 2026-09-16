from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.schemas import HealthResponse, PredictionRequest, PredictionResponse
from app.services.model_loader import model_service
from app.services.preprocessing import request_to_dataframe


@asynccontextmanager
async def lifespan(_app: FastAPI):
    model_service.load(settings.model_file, settings.locations_file)
    yield


app = FastAPI(
    title="House Price Prediction API",
    description="Predict Indian house prices from property features using a trained Random Forest pipeline.",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", model_loaded=model_service.is_loaded())


@app.get("/locations")
def locations() -> dict[str, list[str]]:
    return {"locations": model_service.locations}


@app.post("/predict", response_model=PredictionResponse)
def predict(payload: PredictionRequest) -> PredictionResponse:
    if not model_service.is_loaded():
        raise HTTPException(status_code=503, detail="Model is not loaded. Start the API after placing house_price.pkl in models/.")

    dataframe = request_to_dataframe(payload, model_service.locations)
    prediction = float(model_service.model.predict(dataframe)[0])

    return PredictionResponse(
        predicted_price=prediction,
        predicted_price_lac=prediction / 100_000,
        predicted_price_cr=prediction / 10_000_000,
        currency="INR",
    )
