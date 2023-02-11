from server.utils.test import test_client, wipe_db


def test_create_user():
    wipe_db()
    body = {"email": "foo@bar.com", "password": "test"}
    response = test_client.post(
        "/auth/create",
        json=body,
    )
    assert response.status_code == 200
    assert response.json()["email"] == "foo@bar.com"

def test_creating_an_exiting_user_returns_message():
    wipe_db()
    body = {"email": "foo@bar.com", "password": "test"}
    response = test_client.post(
        "/auth/create",
        json=body,
    )
    assert response.status_code == 200
