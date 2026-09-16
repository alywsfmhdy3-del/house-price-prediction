# House Price Prediction API

FastAPI service that loads a scikit-learn `Pipeline` + `RandomForest` model and returns predicted house prices in Indian Rupees (plus Lakh and Crore).

## Prerequisites

- Python 3.11 or higher
- A trained `house_price.pkl` (scikit-learn **1.6.1**) and `locations.json`

Place both files in `models/`:

```
backend/models/house_price.pkl
backend/models/locations.json
```

If `house_price.pkl` is missing, generate a **placeholder** model (not the notebook model) so the API and tests can run:

```bash
python scripts/create_placeholder_model.py
```

Replace that file with the notebook export before any real predictions.

The pickle only loads reliably with **scikit-learn 1.6.1** (same as training).

## Install and run

From the `backend/` folder:

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
copy .env.example .env   # Windows
# cp .env.example .env    # macOS / Linux

uvicorn app.main:app --reload --port 8000
```

API: http://localhost:8000  
Swagger: http://localhost:8000/docs

## Tests

```bash
pytest -v
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | `{ "status": "ok", "model_loaded": true }` |
| GET | `/locations` | `{ "locations": [...] }` for the frontend dropdown |
| POST | `/predict` | Predict price from property features |

Example `POST /predict` body:

```json
{
  "carpet_area_sqft": 1200,
  "floor_num": 5,
  "Bathroom": 2,
  "Balcony": 1,
  "location_grouped": "mumbai",
  "Furnishing": "Semi-Furnished",
  "Transaction": "Resale",
  "Ownership": "Freehold",
  "facing": "East"
}
```

Unknown `location_grouped` values are mapped to `"Other"` before inference.

## Environment

See `.env.example`:

- `MODEL_PATH` — default `models/house_price.pkl`
- `LOCATIONS_PATH` — default `models/locations.json`
- `CORS_ORIGINS` — includes `http://localhost:5173` and `http://localhost:3000`
