from http_constants.status import HttpStatus

from server.utils.test import test_client


def test_ping() -> None:
    response = test_client.get("/ping")
    assert response.status_code == HttpStatus.OK
    assert response.json() == {"message": "pong!"}
