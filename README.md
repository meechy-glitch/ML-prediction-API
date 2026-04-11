# ML Prediction API

A FastAPI app that serves a trained scikit-learn RandomForest model for Iris flower classification.

## Stack
- FastAPI
- scikit-learn
- Pydantic
- Docker
- Python 3.10

## Endpoints
- `POST /predictions/predict` — submit Iris features, get a predicted class
- `GET /predictions/` — retrieve all past predictions
- `GET /predictions/{prediction_id}` — retrieve a specific prediction
- `POST /items/` — create an item
- `GET /items/` — list all items
- `GET /items/{item_id}` — get a specific item
- `DELETE /items/{item_id}` — delete an item
- `POST /users/` — create a user
- `GET /users/` — list all users

## Run locally
pip install fastapi uvicorn scikit-learn joblib httpx pydantic
python ml/train.py
uvicorn main:app --reload

## Run with Docker
docker build -t ml-prediction-api .
docker run -p 8000:8000 ml-prediction-api

## Example prediction request
POST /predictions/predict
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}

## Example response
{
  "predicted_class": "setosa",
  "prediction": 0
}