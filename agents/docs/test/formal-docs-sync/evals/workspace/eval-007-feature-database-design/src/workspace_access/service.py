from .invitations import consume_invitation
from .repository import create_invitation, upsert_membership


def assign_role(db, workspace_store, user_store, workspace_id, user_id, role):
    if not workspace_store.exists(workspace_id):
        raise ValueError("workspace_not_found")
    # identity.accounts is owned by another data domain and has no physical FK
    # from workspace_memberships; the service validates the logical reference.
    if not user_store.exists(user_id):
        raise ValueError("user_not_found")
    return upsert_membership(db, workspace_id, user_id, role)


def invite_user(db, workspace_store, workspace_id, email, token_hash, expires_at):
    if not workspace_store.exists(workspace_id):
        raise ValueError("workspace_not_found")
    return create_invitation(
        db,
        "invitation-1",
        workspace_id,
        email,
        token_hash,
        expires_at,
    )


def accept_invitation(db, invitation_store, audit_writer, token):
    invitation = consume_invitation(invitation_store, token)
    membership = upsert_membership(
        db, invitation.workspace_id, invitation.user_id, invitation.role
    )
    audit_writer.write("workspace.invitation.accepted", invitation.workspace_id, invitation.user_id)
    return membership
