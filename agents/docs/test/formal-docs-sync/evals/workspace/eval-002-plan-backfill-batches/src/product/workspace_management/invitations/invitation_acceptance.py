def accept_invitation(token_state: str):
    if token_state == "valid":
        return {"ok": True, "membership": "active"}
    if token_state == "expired":
        return {
            "ok": False,
            "message": "Invitation expired.",
            "recovery": "Request a new invitation.",
        }
    return {
        "ok": False,
        "message": "Invitation is invalid.",
        "recovery": "Open the latest invitation email or contact an owner.",
    }
