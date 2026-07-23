from .repository import create_invitation as persist_invitation


def create_invitation(
    actor_role,
    db,
    invitation_id,
    workspace_id,
    email,
    role,
    token_hash,
    expires_at,
):
    if actor_role not in {"owner", "admin"}:
        raise PermissionError("invitation_forbidden")
    return persist_invitation(
        db,
        invitation_id,
        workspace_id,
        email,
        role,
        token_hash,
        expires_at,
    )


def consume_invitation(invitation_store, token):
    invitation = invitation_store.find(token)
    if invitation is None:
        raise ValueError("invitation_not_found")
    if invitation.expired:
        raise ValueError("invitation_expired")
    invitation_store.mark_consumed(token)
    return invitation
