def upsert_membership(db, workspace_id, user_id, role):
    return db.execute(
        "INSERT INTO workspace_memberships (workspace_id, user_id, role) VALUES (?, ?, ?) "
        "ON CONFLICT(workspace_id, user_id) DO UPDATE SET role = excluded.role",
        (workspace_id, user_id, role),
    )


def create_invitation(db, invitation_id, workspace_id, email, token_hash, expires_at):
    return db.execute(
        "INSERT INTO workspace_invitations "
        "(id, workspace_id, invited_email, token_hash, expires_at) VALUES (?, ?, ?, ?, ?)",
        (invitation_id, workspace_id, email, token_hash, expires_at),
    )
