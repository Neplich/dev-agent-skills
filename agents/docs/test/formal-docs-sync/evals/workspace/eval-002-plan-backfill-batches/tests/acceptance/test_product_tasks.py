from src.product.analytics.dashboard import view_dashboard
from src.product.workspace_management.invitations import accept_invitation, invite_member


def test_invitation_tasks_expose_limits_feedback_and_recovery():
    assert invite_member("admin", "new@example.com", 0)["status"] == "pending"
    assert invite_member("viewer", "new@example.com", 0)["recovery"] == "Ask a workspace owner for access."
    assert invite_member("owner", "new@example.com", 3)["recovery"] == "Revoke an unused invitation, then retry."
    assert accept_invitation("expired")["recovery"] == "Request a new invitation."


def test_dashboard_roles_empty_state_and_retry():
    assert view_dashboard("analyst", 0)["state"] == "empty"
    assert view_dashboard("viewer", 1)["message"] == "Dashboard access is unavailable."
    assert view_dashboard("admin", 1, load_failed=True)["recovery"] == "Retry from the dashboard."
