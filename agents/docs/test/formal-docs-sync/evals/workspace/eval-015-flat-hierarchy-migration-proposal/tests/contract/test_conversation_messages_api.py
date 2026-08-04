def test_create_conversation_message_contract(client):
    response = client.post(
        "/api/knowledge-discovery/conversations/conversation-1/messages",
        json={"content": "Summarize the evidence."},
    )
    assert response.status_code == 201
    assert response.json() == {
        "id": "message-1",
        "conversation_id": "conversation-1",
        "content": "Summarize the evidence.",
    }


def test_conversation_message_validates_content(client):
    response = client.post(
        "/api/knowledge-discovery/conversations/conversation-1/messages",
        json={"content": ""},
    )
    assert response.status_code == 422


def test_conversation_message_requires_conversation_access(client):
    response = client.get(
        "/api/knowledge-discovery/conversations/forbidden/messages"
    )
    assert response.status_code == 403
    assert response.json()["detail"]["code"] == "conversation_forbidden"
