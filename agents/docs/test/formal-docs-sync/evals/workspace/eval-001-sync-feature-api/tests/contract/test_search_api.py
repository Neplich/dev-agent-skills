def test_search_contract(client):
    response = client.get("/api/search", params={"q": "codex", "limit": 5})
    assert response.status_code == 200
    assert response.json() == {
        "items": [{"id": "doc-1", "title": "Result for codex"}],
        "total": 1,
    }


def test_search_rejects_blank_query(client):
    response = client.get("/api/search", params={"q": "   "})
    assert response.status_code == 400
    assert response.json()["detail"]["code"] == "invalid_query"
