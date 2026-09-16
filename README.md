\# 🏠 House Price Prediction — End-to-End ML Web App



An end-to-end Machine Learning web application that predicts house prices in India based on property features. The project covers the complete ML product lifecycle: from raw data cleaning and model training, to a FastAPI backend serving the model, and a React frontend where users can get instant price predictions.



\---



\## 📌 Overview



Given property details such as \*\*carpet area, floor number, bathrooms, balconies, location, furnishing status, transaction type, ownership, and facing direction\*\*, the model predicts the estimated price in \*\*Indian Rupees\*\*, and displays it in \*\*Lakh\*\* and \*\*Crore\*\* as well.



The app was built as a student project to demonstrate a full ML deployment pipeline, from Jupyter notebook to a deployed web application.



\---



\## 🏗️ Architecture

┌──────────────────┐

│ Kaggle Dataset │ (187,531 rows, 21 columns)

└────────┬─────────┘

│

▼

┌──────────────────┐

│ Jupyter Notebook│ Data cleaning → EDA → Feature Engineering

│ │ → Pipeline training → Model evaluation

└────────┬─────────┘

│

▼

┌──────────────────┐

│ house\_price.pkl │ Full scikit-learn Pipeline

│ locations.json │ List of 51 valid locations

└────────┬─────────┘

│

▼

┌──────────────────┐

│ FastAPI Backend │ POST /predict GET /health GET /locations

│ (port 8000) │ Loads model once at startup

└────────┬─────────┘

│

▼

┌──────────────────┐

│ React Frontend │ User enters property details

│ (port 5173) │ Sees predicted price instantly

└──────────────────┘



text



\---



\## 🛠️ Tech Stack



| Layer | Technology |

|-------|------------|

| \*\*Data \& ML\*\* | Python 3.12, pandas, NumPy, scikit-learn, Jupyter |

| \*\*Model\*\* | RandomForestRegressor (100 trees) inside a full Pipeline |

| \*\*Backend\*\* | FastAPI, Uvicorn, Pydantic, joblib |

| \*\*Frontend\*\* | React 18, Vite, Axios, plain CSS |

| \*\*Version Control\*\* | Git + GitHub |



\---



\## 📂 Project Structure

house-price-prediction/

│

├── notebooks/

│ └── house\_price\_model.ipynb # Full ML pipeline: cleaning → EDA → training → export

│

├── models/

│ ├── house\_price.pkl # Trained sklearn Pipeline (preprocessing + model)

│ └── locations.json # List of 51 valid locations for the dropdown

│

├── backend/

│ ├── app/

│ │ ├── main.py # FastAPI app + lifespan + endpoints

│ │ ├── schemas.py # Pydantic request/response models

│ │ ├── config.py # Settings loaded from .env

│ │ └── services/

│ │ ├── model\_loader.py # Singleton that loads the .pkl once

│ │ └── preprocessing.py # Builds DataFrame from request

│ ├── tests/ # pytest test suite (health + predict)

│ ├── .env.example

│ ├── requirements.txt

│ └── README.md

│

├── frontend/

│ ├── src/

│ │ ├── components/ # PredictionForm, ResultCard, Spinner, ErrorBanner

│ │ ├── services/api.js # Axios instance using VITE\_API\_URL

│ │ ├── constants.js # Dropdown option arrays

│ │ └── App.jsx

│ ├── .env.example

│ ├── package.json

│ └── README.md

│

├── docs/

│ └── screenshot.png # App screenshot used in this README

│

├── .gitignore

└── README.md # ← you are here



text



\---



\## 📊 Dataset



\- \*\*Source:\*\* \[House Price by Juhi Bhojani](https://www.kaggle.com/datasets/juhibhojani/house-price)

\- \*\*Size:\*\* 187,531 rows × 21 columns

\- \*\*Content:\*\* Real property listings from India, including `Amount(in rupees)`, `Carpet Area`, `location`, `Floor`, `Furnishing`, `Bathroom`, `Balcony`, `Ownership`, `facing`, and more.



\*\*To download the dataset:\*\*



```bash

pip install kaggle



\# Get your API token from: Kaggle → Settings → API → "Create New Token"

\# Place kaggle.json in C:\\Users\\<you>\\.kaggle\\ (Windows)

\# or \~/.kaggle/ (macOS/Linux)



kaggle datasets download -d juhibhojani/house-price -p notebooks/data --unzip

⚠️ The raw CSV is intentionally not committed to this repo (too large). Follow the steps above to download it.



📈 Model Performance

Evaluated on a 20% test set (19,053 rows). Trained on 76,210 rows.



Model	MAE (₹)	RMSE (₹)	R²

Linear Regression (baseline)	4,166,205	6,621,137	0.7523

Random Forest ⭐	968,035	3,229,036	0.9411

Winner: Random Forest Regressor — it captures non-linear relationships between property features far better than the linear baseline, raising R² from 0.75 to 0.94 and cutting the average error to under 1 million rupees.



Key Cleaning Steps

Parsed "42 Lac" / "1.2 Cr" → numeric rupees.



Parsed "1200 sqft" / "140 sqm" → normalized to sqft.



Extracted floor number from "3 out of 10" and handled "Ground" / "Basement".



Kept the top-50 locations, grouped the rest into "Other".



Removed outliers outside the 1st–99th percentile of price-per-sqft.



🚀 Getting Started

Prerequisites

Python 3.11 or higher



Node.js 18 or higher + npm



Git



1️⃣ Clone the repository

bash

git clone https://github.com/alywsfmhdy3-del/house-price-prediction.git

cd house-price-prediction

2️⃣ Backend Setup (FastAPI)

bash

cd backend



\# Create \& activate a virtual environment

python -m venv .venv

.venv\\Scripts\\activate            # Windows

\# source .venv/bin/activate        # macOS / Linux



\# Install dependencies

pip install -r requirements.txt



\# Create your .env file from the example

copy .env.example .env            # Windows

\# cp .env.example .env             # macOS / Linux



\# Run the test suite

pytest -v



\# Start the server

uvicorn app.main:app --reload --port 8000

API docs: http://localhost:8000/docs



Health check: http://localhost:8000/health



3️⃣ Frontend Setup (React + Vite)

Open a new terminal:



bash

cd frontend



\# Install dependencies

npm install



\# Create your .env file from the example

copy .env.example .env            # Windows

\# cp .env.example .env             # macOS / Linux



\# Start the dev server

npm run dev

Open http://localhost:5173 in your browser.



🌍 Environment Variables

Backend (backend/.env)

Variable	Description	Default

MODEL\_PATH	Path to the trained .pkl file	models/house\_price.pkl

LOCATIONS\_PATH	Path to the locations JSON	models/locations.json

CORS\_ORIGINS	Allowed frontend origins	\["http://localhost:5173","http://localhost:3000"]

Frontend (frontend/.env)

Variable	Description	Default

VITE\_API\_URL	Base URL of the FastAPI backend	http://localhost:8000

⚠️ Never hardcode http://localhost:8000 in frontend components. Always read from import.meta.env.VITE\_API\_URL.



🔌 API Reference

GET /health

Returns the current status of the API and whether the model is loaded.



Response:



json

{

&#x20; "status": "ok",

&#x20; "model\_loaded": true

}

GET /locations

Returns the list of valid locations for the frontend dropdown.



Response:



json

{

&#x20; "locations": \["Other", "ahmedabad", "bangalore", "chandigarh", "chennai", "..."]

}

POST /predict

Predicts the price of a property based on the given features.



Request body:



json

{

&#x20; "carpet\_area\_sqft": 1200,

&#x20; "floor\_num": 5,

&#x20; "Bathroom": 2,

&#x20; "Balcony": 1,

&#x20; "location\_grouped": "mumbai",

&#x20; "Furnishing": "Semi-Furnished",

&#x20; "Transaction": "Resale",

&#x20; "Ownership": "Freehold",

&#x20; "facing": "East"

}

Response:



json

{

&#x20; "predicted\_price": 36974000.0,

&#x20; "predicted\_price\_lac": 369.74,

&#x20; "predicted\_price\_cr": 3.70,

&#x20; "currency": "INR"

}

Curl example:



bash

curl -X POST http://localhost:8000/predict \\

&#x20; -H "Content-Type: application/json" \\

&#x20; -d '{

&#x20;   "carpet\_area\_sqft": 1200,

&#x20;   "floor\_num": 5,

&#x20;   "Bathroom": 2,

&#x20;   "Balcony": 1,

&#x20;   "location\_grouped": "mumbai",

&#x20;   "Furnishing": "Semi-Furnished",

&#x20;   "Transaction": "Resale",

&#x20;   "Ownership": "Freehold",

&#x20;   "facing": "East"

&#x20; }'

📸 Screenshots

Prediction Form \& Result

https://docs/screenshot.png



API Documentation (Swagger)

Run the backend and visit http://localhost:8000/docs for the interactive Swagger UI.



🧪 Testing

Backend

bash

cd backend

pytest -v

Tests cover:



✅ GET /health returns 200 with model\_loaded: true



✅ POST /predict happy path returns a positive price



✅ POST /predict with invalid input (negative area) returns 422



✅ POST /predict with unknown location falls back to "Other" and returns 200



🔒 Important Notes

scikit-learn version pinning: The pickle file was exported with scikit-learn 1.6.1. Loading it with a different version may fail. This version is pinned in backend/requirements.txt.



Model loading: The model is loaded once at FastAPI startup (via lifespan), not on every request.



Unknown locations: If a location isn't in the trained list, the backend replaces it with "Other" before prediction.



File size: house\_price.pkl is \~44 MB, which is under GitHub's 50 MB limit and is committed to this repo.



👤 Author

Youssef Mahdy Saleh



GitHub: @alywsfmhdy3-del



Email: alywsfmhdy3@gmail.com

