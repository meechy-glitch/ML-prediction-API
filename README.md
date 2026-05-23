# ML Prediction API

A production-ready FastAPI app serving a trained scikit-learn RandomForest model for Iris flower classification. Features persistent storage, API key and JWT authentication, Redis caching, rate limiting, and structured request logging.

## Live API
https://ml-prediction-api-ugex.onrender.com/docs

## Stack
- FastAPI
- scikit-learn
- Pydantic
- SQLAlchemy + PostgreSQL
- Redis
- Docker
- Python 3.10

## Authentication

**API Key** — for machine to machine access. Pass the `X-API-Key` header on protected endpoints. Rate limited to 10 requests per 60 seconds.

```
X-API-Key: your-api-key
```

**JWT** — for user access. Login via `POST /auth/login` to receive a token. Pass it as a Bearer token on protected endpoints. Tokens expire after 30 minutes.

```
Authorization: Bearer your-token
```

## Endpoints

**Predictions**
- `POST /predictions/predict` — submit Iris features, get a predicted class (requires API key)
- `GET /predictions/` — retrieve all past predictions (cached)
- `GET /predictions/{prediction_id}` — retrieve a specific prediction by ID

**Auth**
- `POST /auth/login` — login with username and password, returns a JWT
- `GET /auth/me` — returns current user info (requires JWT)

## Middleware
- **Logging** — every request logs method, path, status code, duration and client IP
- **CORS** — restricted to specific allowed origins and methods

## Run locally

Requires Docker Desktop running for Redis.

```bash
pip install -r requirements.txt
python ml/train.py
docker start redis-cache
uvicorn main:app --reload
```

## Run with Docker
```bash
docker build -t ml-prediction-api .
docker run -p 8000:8000 ml-prediction-api
```

## Testing

Tests use mocked Redis and SQLite — no external services required.

```bash
pytest tests/ -v
```

## Environment variables

| Variable | Description |
|---|---|
| `API_KEY` | Secret key for API key authentication |
| `DATABASE_URL` | PostgreSQL connection string |
| `REDIS_URL` | Redis connection string |
| `JWT_SECRET` | Secret key for signing JWTs |

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
  "timestamp": "2026-05-01T12:00:00"
}
```