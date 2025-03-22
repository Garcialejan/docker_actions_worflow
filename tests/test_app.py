from ..app import app
from fastapi.testclient import TestClient

# Instance of the client
client = TestClient(app)

def test_home(): #Rememeber to start files and functions with test for pytest interpretation
    response = client.get("/")
    # Verify the response (200 = Ok)
    assert response.status_code == 200
    # Verify the content of the response
    assert response.text == "Welcome to the GitHUB Actions workflow"