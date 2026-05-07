import pytest
import os
os.environ["API_KEY"] = "testsecretkey"
os.environ["DATABASE_URL"] = "sqlite:///./test.db"
os.environ["REDIS_URL"] = "redis://localhost:6379"

from unittest.mock import MagicMock, patch 
from fastapi.testclient import TestClient 
from main import app 
from database.database import engine
from database import models 

models.Base.metadata.create_all(bind=engine)

@pytest.fixture
def client():
    mock_redis = MagicMock()
    mock_redis.get.return_value = None
    mock_redis.setex.return_value = True
    mock_redis.delete.return_value = True
    mock_redis.pipeline.return_value = MagicMock(
        incr=MagicMock(),
        expire=MagicMock(),
        execute=MagicMock(return_value=[1, True])
    )

    with patch("routers.predictions.redis_client", mock_redis), \
    patch("auth.rate_limit.redis_client", mock_redis):
        yield TestClient(app)
    