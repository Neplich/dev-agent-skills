def test_list_invoices_contract(client):
    response = client.get(
        "/api/billing/invoices",
        params={"limit": 5},
        headers={"X-Billing-Role": "reader"},
    )
    assert response.status_code == 200
    assert response.json() == {"items": ["invoice-1"], "total": 1}


def test_list_invoices_rejects_wrong_role(client):
    response = client.get(
        "/api/billing/invoices",
        headers={"X-Billing-Role": "writer"},
    )
    assert response.status_code == 403
    assert response.json()["detail"]["code"] == "billing_forbidden"
