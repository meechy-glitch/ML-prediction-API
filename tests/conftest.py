import pytest
import os
os.environ["API_KEY"] = "testsecretkey"
from fastapi.testclient import TestClient 
from main import app 

@pytest.fixture
def client():
    return TestClient(app) 