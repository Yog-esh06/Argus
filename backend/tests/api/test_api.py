from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_route():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json()['status'] == 'healthy'


def test_cameras_route():
    response = client.get('/api/v1/cameras/')
    assert response.status_code == 200
    assert len(response.json()['items']) >= 1


def test_incidents_route():
    response = client.get('/api/v1/incidents/')
    assert response.status_code == 200
    assert len(response.json()['items']) >= 1
