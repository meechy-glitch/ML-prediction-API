from fastapi import APIRouter, HTTPException
from schemas import IrisInput, PredictionResponse
from datetime import datetime
import uuid
from ml.model import model


router = APIRouter(
    prefix="/predictions", 
    tags=["predictions"]
)

CLASS_NAMES = ["setosa", "versicolor", "virginica"]

prediction_log = []

@router.post("/predict", response_model=PredictionResponse)
async def predict(input: IrisInput):
    try:
        features = [[
            input.sepal_length,
            input.sepal_width,
            input.petal_length,
            input.petal_width
        ]]


        prediction = model.predict(features)[0]
        predicted_class = CLASS_NAMES[prediction]



        result = PredictionResponse(
            id = str(uuid.uuid4()),
            input =  input,
            prediction = int(prediction),
            predicted_class = predicted_class,
            timestamp = datetime.now()
        )

        prediction_log.append(result)
        return result

    except ValueError as e:
        raise HTTPException(status_code=422, detail=f"invalid input {str(e)}")


    except IndexError as e:
        raise HTTPException(status_code=500, detail=f"Prediction out of range {str(e)}")
    

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed {str(e)}")



@router.get("/", response_model=list[PredictionResponse])
async def get_predictions():
    return prediction_log


@router.get("/{prediction_id}", response_model=PredictionResponse)
async def get_prediction(prediction_id: str):
    for prediction in prediction_log:
        if prediction.id == prediction_id:
            return prediction

    raise HTTPException(status_code=404, detail=f"prediction with id {prediction_id} not found")