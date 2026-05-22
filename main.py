from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from routers import predictions, auth
from database.database import engine
from database import models
from middleware.logging_middleware import log_and_time_requests



models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://ml-prediction-api-ugex.onrender.com"
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["X-API-Key", "Authorization", "Content-Type"]
)

app.middleware("http")(log_and_time_requests)


app.include_router(predictions.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Welcome to my first api endpoint"}


@app.get("/health")
async def health_status():
    return {"status": "okay"}

    