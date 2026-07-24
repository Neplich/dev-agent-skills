MAX_PENDING_INVITATIONS = 3


def invite_member(
    actor_role: str,
    email: str,
    pending_count: int,
    existing_email: str | None = None,
):
    if actor_role not in {"owner", "admin"}:
        return {
            "ok": False,
            "message": "Only owners and admins can invite members.",
            "recovery": "Ask a workspace owner for access.",
        }
    if pending_count >= MAX_PENDING_INVITATIONS:
        return {
            "ok": False,
            "message": "Pending invitation limit reached.",
            "recovery": "Revoke an unused invitation, then retry.",
        }
    if existing_email == email:
        return {
            "ok": False,
            "message": "An invitation is already pending.",
            "recovery": "Resend or revoke the existing invitation.",
        }
    return {"ok": True, "status": "pending", "email": email}


def manage_pending_invitation(
    actor_role: str,
    email: str,
    action: str,
    invitation_exists: bool = True,
):
    if actor_role not in {"owner", "admin"}:
        return {
            "ok": False,
            "message": "Only owners and admins can manage invitations.",
            "recovery": "Ask a workspace owner for access.",
        }
    if not invitation_exists:
        return {
            "ok": False,
            "message": "Pending invitation not found.",
            "recovery": "Refresh the invitation list.",
        }
    if action == "resend":
        return {"ok": True, "status": "pending", "email": email, "action": "resent"}
    if action == "revoke":
        return {"ok": True, "status": "revoked", "email": email, "action": "revoked"}
    return {
        "ok": False,
        "message": "Unsupported invitation action.",
        "recovery": "Choose resend or revoke.",
    }
