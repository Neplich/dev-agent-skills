from pathlib import Path

import pytest

from src.workspace_access.service import assign_role, invite_user


def test_workspace_domain_schema_constraints():
    schema = Path("src/workspace_access/schema.sql").read_text(encoding="utf-8")
    assert "REFERENCES workspaces(id) ON DELETE CASCADE" in schema
    assert "UNIQUE (workspace_id, user_id)" in schema
    assert "token_hash TEXT NOT NULL UNIQUE" in schema
    assert "expires_at TEXT NOT NULL" in schema


def test_assign_role_validates_logical_user_reference(db, workspace_store, user_store):
    user_store.exists.return_value = False
    with pytest.raises(ValueError, match="user_not_found"):
        assign_role(db, workspace_store, user_store, "workspace-1", "user-1", "viewer")


def test_assign_role_uses_supported_roles(db, workspace_store, user_store):
    result = assign_role(db, workspace_store, user_store, "workspace-1", "user-1", "editor")
    assert result is not None


def test_invitation_requires_existing_workspace(db, workspace_store):
    workspace_store.exists.return_value = False
    with pytest.raises(ValueError, match="workspace_not_found"):
        invite_user(db, workspace_store, "missing", "reader@example.test", "hash", "2026-08-01")
