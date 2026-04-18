from fastapi import APIRouter, HTTPException, Depends
from schemas import IrisInput, PredictionResponse
from database.database import get_db
from database.models import PredictionModel
from sqlalchemy.orm import Session
from datetime import datetime
import uuid
from ml.model import model
from auth.auth import get_api_key


router = APIRouter(
    prefix="/predictions", 
    tags=["predictions"]
)

CLASS_NAMES = ["setosa", "versicolor", "virginica"]


@router.post("/predict", response_model=PredictionResponse)
async def predict(input: IrisInput, db: Session = Depends(get_db), api_key: str = Depends(get_api_key)):
    try:
        features = [[
            input.sepal_length,
            input.sepal_width,
            input.petal_length,
            input.petal_width
        ]]


        prediction = model.predict(features)[0]
        predicted_class = CLASS_NAMES[prediction]

        db_prediction = PredictionModel(
            id=str(uuid.uuid4()),
            sepal_length=input.sepal_length,
            sepal_width=input.sepal_width,
            petal_length=input.petal_length,
            petal_width=input.petal_width,
            prediction=int(prediction),
            predicted_class=predicted_class,
            timestamp=datetime.now()
        )

        db.add(db_prediction)
        db.commit()
        db.refresh(db_prediction)



        return PredictionResponse(
            id=db_prediction.id,
            input=input,
            prediction=db_prediction.prediction,
            predicted_class=db_prediction.predicted_class,
            timestamp=db_prediction.timestamp
        )


    except ValueError as e:
        raise HTTPException(status_code=422, detail=f"invalid input {str(e)}")


    except IndexError as e:
        raise HTTPException(status_code=500, detail=f"Prediction out of range {str(e)}")
    

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed {str(e)}")



@router.get("/", response_model=list[PredictionResponse])
async def get_predictions(db: Session = Depends(get_db)):
    predictions = db.query(PredictionModel).all()
    return[
        PredictionResponse(
            id=p.id,
            input=IrisInput(
                sepal_length=p.sepal_length,
                sepal_width=p.sepal_width,
                petal_length=p.petal_length,
                petal_width=p.petal_width
            ),
            prediction=p.prediction,
            predicted_class=p.predicted_class,
            timestamp=p.timestamp
        )
        for p in predictions

    ]


@router.get("/{prediction_id}", response_model=PredictionResponse)
async def get_prediction(prediction_id: str, db : Session = Depends(get_db)):
    p = db.query(PredictionModel).filter(
        PredictionModel.id == prediction_id 
    ).first()

    if not p:
        raise HTTPException(status_code=404, detail=f"prediction with id {prediction_id} not found")

    return PredictionResponse(
        id=p.id,
        input=IrisInput(
            sepal_length=p.sepal_length,
            sepal_width=p.sepal_width,
            petal_length=p.petal_length,
            petal_width=p.petal_width
            ),
        prediction=p.prediction,
        predicted_class=p.predicted_class,
        timestamp=p.timestamp
    )