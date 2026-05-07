from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI 
from routers import predictions, auth
from database.database import engine
from database import models


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(predictions.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Welcome to my first api endpoint"}


@app.get("/health")
async def health_status():
    return {"status": "okay"}

    