def upsert_membership(db, workspace_id, user_id, role):
    return db.execute(
        "INSERT INTO workspace_memberships (workspace_id, user_id, role) VALUES (?, ?, ?) "
        "ON CONFLICT(workspace_id, user_id) DO UPDATE SET role = excluded.role",
        (workspace_id, user_id, role),
    )
