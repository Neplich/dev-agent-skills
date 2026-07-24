def test_create_session_contract(client):
    response = client.post("/api/identity/sessions", json={"device_name": "MacBook"})
    assert response.status_code == 201
    assert response.json() == {
        "id": "session-1",
        "account_id": "account-1",
        "device_name": "MacBook",
    }


def test_create_session_validates_device_name(client):
    response = client.post("/api/identity/sessions", json={"device_name": ""})
    assert response.status_code == 422


def test_revoke_session_errors(client):
    assert client.delete("/api/identity/sessions/missing").status_code == 404
    forbidden = client.delete("/api/identity/sessions/other-account")
    assert forbidden.status_code == 403
    assert forbidden.json()["detail"]["code"] == "session_forbidden"
