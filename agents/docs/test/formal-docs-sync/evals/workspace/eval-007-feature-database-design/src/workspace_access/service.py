from .invitations import consume_invitation, create_invitation
from .repository import upsert_membership


def assign_role(db, workspace_store, user_store, workspace_id, user_id, role):
    if not workspace_store.exists(workspace_id):
        raise ValueError("workspace_not_found")
    # identity.accounts is owned by another data domain and has no physical FK
    # from workspace_memberships; the service validates the logical reference.
    if not user_store.exists(user_id):
        raise ValueError("user_not_found")
    return upsert_membership(db, workspace_id, user_id, role)


def invite_user(
    db,
    workspace_store,
    actor_role,
    workspace_id,
    email,
    role,
    token_hash,
    expires_at,
):
    if not workspace_store.exists(workspace_id):
        raise ValueError("workspace_not_found")
    return create_invitation(
        actor_role,
        db,
        "invitation-1",
        workspace_id,
        email,
        role,
        token_hash,
        expires_at,
    )


def accept_invitation(db, invitation_store, audit_writer, token, user_id):
    invitation = consume_invitation(invitation_store, token)
    membership = upsert_membership(
        db, invitation.workspace_id, user_id, invitation.role
    )
    audit_writer.write("workspace.invitation.accepted", invitation.workspace_id, user_id)
    return membership
