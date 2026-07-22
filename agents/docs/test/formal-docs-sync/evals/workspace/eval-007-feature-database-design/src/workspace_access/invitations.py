def create_invitation(actor_role, invitation_store, workspace_id, email, role):
    if actor_role not in {"owner", "admin"}:
        raise PermissionError("invitation_forbidden")
    return invitation_store.create(workspace_id, email, role)


def consume_invitation(invitation_store, token):
    invitation = invitation_store.find(token)
    if invitation is None:
        raise ValueError("invitation_not_found")
    if invitation.expired:
        raise ValueError("invitation_expired")
    invitation_store.mark_consumed(token)
    return invitation
