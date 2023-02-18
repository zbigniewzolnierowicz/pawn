from http_constants.status import HttpStatus

from server.utils.test import test_client, wipe_db


def test_create_user() -> None:
    wipe_db()
    body = {"email": "foo@bar.com", "password": "test"}
    response = test_client.post(
        "/auth/create",
        json=body,
    )
    assert response.status_code == HttpStatus.OK
    assert response.json()["email"] == "foo@bar.com"

def test_creating_an_exiting_user_returns_message() -> None:
    wipe_db()
    body = {"email": "foo@bar.com", "password": "test"}
    response = test_client.post(
        "/auth/create",
        json=body,
    )
    assert response.status_code == HttpStatus.OK
    response = test_client.post(
        "/auth/create",
        json=body,
    )
    assert response.status_code == HttpStatus.CONFLICT
