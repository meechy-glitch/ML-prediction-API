from pydantic import BaseModel, Field, field_validator
from datetime import datetime


class IrisInput(BaseModel):
    sepal_length: float = Field(gt=0)
    sepal_width: float = Field(gt=0)
    petal_length: float = Field(gt=0)
    petal_width: float = Field(gt=0)

class PredictionResponse(BaseModel):
    id: str
    input: IrisInput
    prediction: int
    predicted_class: str
    timestamp: datetime