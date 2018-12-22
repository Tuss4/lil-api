from starlette.testclient import TestClient
from api import app
import json


def test_ping():
    client = TestClient(app)
    response = client.get('/')
    data = json.loads(response.content)
    assert response.status_code == 200
    assert data['ping'] == "Pong yo."
