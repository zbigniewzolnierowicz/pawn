from server.utils.test import test_client

def test_create_user():
    response = test_client.post(
        "/auth/create",
        json={"email": "foo@bar.com", "password": "test"}
    )
    assert response.status_code == 200
    assert response.json()["email"] == "foo@bar.com"
