from fastapi.testclient import TestClient
from main import app
from src.model.inputData import InputData

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome!"}

def test_classifyNumbers():    
    payload = {"numbers": [10,3,4], "algorithm": ""}
    response = client.post("classifier/classify", json=payload)
    assert response.status_code == 200
    