from server.utils.test import test_client


def test_ping():
    response = test_client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"message": "pong!"}
