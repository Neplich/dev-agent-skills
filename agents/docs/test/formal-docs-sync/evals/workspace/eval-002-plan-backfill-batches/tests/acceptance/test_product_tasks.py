from src.product.analytics.dashboard import view_dashboard
from src.product.workspace_management.invitations import accept_invitation, invite_member


def test_invitation_tasks_expose_limits_feedback_and_recovery():
    invited = invite_member("admin", "new@example.com", 0)
    forbidden = invite_member("viewer", "new@example.com", 0)
    limited = invite_member("owner", "new@example.com", 3)
    duplicate = invite_member(
        "owner", "pending@example.com", 1, "pending@example.com"
    )
    expired = accept_invitation("expired")
    invalid = accept_invitation("invalid")

    assert invited == {
        "ok": True,
        "status": "pending",
        "email": "new@example.com",
    }
    assert invite_member("owner", "new@example.com", 0)["status"] == "pending"
    assert forbidden["message"] == "Only owners and admins can invite members."
    assert forbidden["recovery"] == "Ask a workspace owner for access."
    assert limited["message"] == "Pending invitation limit reached."
    assert limited["recovery"] == "Revoke an unused invitation, then retry."
    assert duplicate["message"] == "An invitation is already pending."
    assert duplicate["recovery"] == "Resend or revoke the existing invitation."
    assert accept_invitation("valid")["membership"] == "active"
    assert expired["message"] == "Invitation expired."
    assert expired["recovery"] == "Request a new invitation."
    assert invalid["message"] == "Invitation is invalid."
    assert invalid["recovery"] == "Open the latest invitation email or contact an owner."


def test_dashboard_roles_empty_state_and_retry():
    empty = view_dashboard("analyst", 0)
    ready = view_dashboard("owner", 2)
    forbidden = view_dashboard("viewer", 1)
    failed = view_dashboard("admin", 1, load_failed=True)

    assert empty["state"] == "empty"
    assert empty["message"] == "No activity yet."
    assert ready["state"] == "ready"
    assert ready["event_count"] == 2
    assert forbidden["message"] == "Dashboard access is unavailable."
    assert forbidden["recovery"] == "Ask an admin for the analyst role."
    assert failed["message"] == "Activity could not be loaded."
    assert failed["recovery"] == "Retry from the dashboard."
