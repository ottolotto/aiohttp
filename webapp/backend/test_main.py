from fastapi.testclient import TestClient

from .main import app, DATA_FILE

client = TestClient(app)


def setup_function(function):
    if DATA_FILE.exists():
        DATA_FILE.unlink()


def test_add_and_get_data():
    response = client.post('/data', json={'name': 'foo', 'value': 1})
    assert response.status_code == 200
    response = client.get('/data')
    assert response.status_code == 200
    assert response.json() == [{'name': 'foo', 'value': 1.0}]

    # ensure data persisted
    assert DATA_FILE.exists()
