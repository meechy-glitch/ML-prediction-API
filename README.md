# ML Prediction API

A FastAPI app that serves a trained scikit-learn RandomForest model for Iris flower classification, with database logging, API key authentication, and a live deployment.

## Live API
https://ml-prediction-api-4gxo.onrender.com/docs

## Stack
- FastAPI
- scikit-learn
- Pydantic
- SQLAlchemy + SQLite
- Docker
- Python 3.10

## Authentication
Protected endpoints require an `X-API-Key` header.

```
X-API-Key: your-api-key
```

## Endpoints

**Predictions**
- `POST /predictions/predict` — submit Iris features, get a predicted class (protected)
- `GET /predictions/` — retrieve all past predictions
- `GET /predictions/{prediction_id}` — retrieve a specific prediction

**Items**
- `POST /items/` — create an item
- `GET /items/` — list all items
- `GET /items/{item_id}` — get a specific item
- `DELETE /items/{item_id}` — delete an item

**Users**
- `POST /users/` — create a user
- `GET /users/` — list all users

## Run locally
```bash
pip install -r requirements.txt
python ml/train.py
uvicorn main:app --reload
```

## Run with Docker
```bash
docker build -t ml-prediction-api .
docker run -p 8000:8000 ml-prediction-api
```

## Testing
```bash
pytest tests/ -v
```

## Example prediction request
```json
POST /predictions/predict
Headers: X-API-Key: your-api-key

{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

## Example response
```json
{
  "id": "uuid",
  "input": {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
  },
  "prediction": 0,
  "predicted_class": "setosa",
  "timestamp": "2024-01-01T00:00:00"
}
```