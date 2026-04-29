import pytest
import os
os.environ["API_KEY"] = "testsecretkey"
os.environ["DATABASE_URL"] = "sqlite:///./test.db"

from fastapi.testclient import TestClient 
from main import app 
from database.database import engine
from database import models 

models.Base.metadata.create_all(bind=engine)

@pytest.fixture
def client():
    return TestClient(app) 