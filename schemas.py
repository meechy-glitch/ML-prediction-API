from pydantic import BaseModel, Field, field_validator
from datetime import datetime

class ItemCreate(BaseModel):
    name: str
    price: float = Field(gt=0, description = "Price must be positive")
    description: str | None = None
    in_stock: bool = True

    @field_validator("name")
    @classmethod
    def name_must_not_be_empty(cls, name_value):
        if not name_value.strip():
            raise ValueError("name cannot be empty")
        return name_value.strip()


class ItemResponse(BaseModel):
    id: str
    name: str
    price: float
    description: str | None = None
    in_stock: bool


class Address(BaseModel):
    street: str
    city: str
    country: str


class UserCreate(BaseModel):
    name: str
    email: str
    address: Address

    @field_validator("name")
    @classmethod
    def name_must_not_be_empty(cls, name_value):
        if not name_value.strip():
            raise ValueError("name cannot be empty")
        return name_value.strip()


    @field_validator("email")
    @classmethod
    def email_validator(cls, email_value):
        if "@" not in email_value:
            raise ValueError("email must contain @")
        if not email_value.endswith(".com"):
            raise ValueError("email must end in .com")
        return email_value





class UserResponse(BaseModel):
    id: str
    name: str




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