def test_get_account_contract(client):
    response = client.get("/api/accounts/acct-1")
    assert response.status_code == 200
    assert response.json()["id"] == "acct-1"


def test_missing_account_contract(client):
    response = client.get("/api/accounts/missing")
    assert response.status_code == 404
    assert response.json()["detail"]["code"] == "account_not_found"
