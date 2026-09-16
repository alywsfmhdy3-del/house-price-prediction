# House Price Predictor (Frontend)

React + Vite form that calls the FastAPI house-price API and shows the predicted price.

## Prerequisites

- Node.js 18 or higher
- Backend running at the URL in `.env` (default `http://localhost:8000`)

## Setup

```bash
cd frontend
npm install
copy .env.example .env   # Windows
# cp .env.example .env    # macOS / Linux
```

`VITE_API_URL` must point at the API. Components never hardcode the backend URL.

## Run

```bash
npm run dev
```

Opens on http://localhost:5173

## Build

```bash
npm run build
```

If `npm install` fails with `UNABLE_TO_VERIFY_LEAF_SIGNATURE` on Windows, run:

```bash
node --use-system-ca "C:\Program Files\nodejs\node_modules\npm\bin\npm-cli.js" install
```
