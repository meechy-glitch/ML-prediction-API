from sqlalchemy import Column, String, Float, Integer, DateTime 
from datetime import datetime
from database.database import Base

class PredictionModel(Base):
    __tablename__ = "predictions"

    id = Column(String, primary_key=True)
    sepal_length = Column(Float, nullable=False)
    sepal_width = Column(Float, nullable=False)
    petal_length = Column(Float, nullable=False)
    petal_width = Column(Float, nullable=False)
    prediction = Column(Integer, nullable=False)
    predicted_class = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.now)
