import pytest_
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixature
def client():
    return TestClient(app)