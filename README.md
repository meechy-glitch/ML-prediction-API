# ML Prediction Logger API

A FastAPI app that logs ML model predictions with timestamps.

## Stack
- FastAPI
- Pydantic
- Python 3.10

## Endpoints
- `POST /predictions/predict` — submit features and get a prediction
- `GET /predictions/` — retrieve all past predictions
- `GET /items/` — list items
- `POST /items/` — create an item
- `GET /users/` — list users
- `POST /users/` — create a user

## Run locally
pip install fastapi uvicorn httpx
uvicorn main:app --reload