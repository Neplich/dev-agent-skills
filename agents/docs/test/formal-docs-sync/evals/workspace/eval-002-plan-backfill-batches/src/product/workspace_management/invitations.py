MAX_PENDING_INVITATIONS = 3


def invite_member(actor_role: str, email: str, pending_count: int, existing_email: str | None = None):
    if actor_role not in {"owner", "admin"}:
        return {"ok": False, "message": "Only owners and admins can invite members.", "recovery": "Ask a workspace owner for access."}
    if pending_count >= MAX_PENDING_INVITATIONS:
        return {"ok": False, "message": "Pending invitation limit reached.", "recovery": "Revoke an unused invitation, then retry."}
    if existing_email == email:
        return {"ok": False, "message": "An invitation is already pending.", "recovery": "Resend or revoke the existing invitation."}
    return {"ok": True, "status": "pending", "email": email}


def accept_invitation(token_state: str):
    if token_state == "valid":
        return {"ok": True, "membership": "active"}
    if token_state == "expired":
        return {"ok": False, "message": "Invitation expired.", "recovery": "Request a new invitation."}
    return {"ok": False, "message": "Invitation is invalid.", "recovery": "Open the latest invitation email or contact an owner."}
