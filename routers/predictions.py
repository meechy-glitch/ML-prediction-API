from fastapi import APIRouter
from schemas import PredictionInput, PredictionResponse
from datetime import datetime
import uuid
import random


router = APIRouter(
    prefix="/predictions", 
    tags=["predictions"]
)

prediction_log = []

@router.post("/predict", response_model=PredictionResponse)
async def predict(input: PredictionInput):
    fake_prediction = round(random.uniform(0,1),4)

    result = PredictionResponse(
        id = str(uuid.uuid4()),
        input =  input,
        prediction = fake_prediction,
        timestamp = datetime.now()
    )

    prediction_log.append(result)
    return result


@router.get("/", response_model=list[PredictionResponse])
async def get_predictions():
    return prediction_log
