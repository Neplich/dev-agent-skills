from .repository import upsert_membership


def assign_role(db, workspace_store, user_store, workspace_id, user_id, role):
    if not workspace_store.exists(workspace_id):
        raise ValueError("workspace_not_found")
    if not user_store.exists(user_id):
        raise ValueError("user_not_found")
    return upsert_membership(db, workspace_id, user_id, role)
