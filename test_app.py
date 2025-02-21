import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_hello(client):
    response = client.get("/")
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["message"] == "Hello, World!"
