from pathlib import Path

import pytest

from src.workspace_access.service import assign_role, invite_user


def test_workspace_domain_schema_constraints():
    schema = Path("src/workspace_access/schema.sql").read_text(encoding="utf-8")

    def table_definition(table_name):
        definition = schema.split(f"CREATE TABLE {table_name} (", 1)[1]
        return definition.split(");", 1)[0]

    workspaces = table_definition("workspaces")
    memberships = table_definition("workspace_memberships")
    invitations = table_definition("workspace_invitations")

    assert "status TEXT NOT NULL CHECK (status IN ('active', 'archived'))" in workspaces
    assert "created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP" in workspaces

    assert "workspace_id TEXT NOT NULL REFERENCES workspaces(id) ON DELETE CASCADE" in memberships
    assert "user_id TEXT NOT NULL" in memberships
    assert "role TEXT NOT NULL CHECK (role IN ('owner', 'editor', 'viewer'))" in memberships
    assert "created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP" in memberships
    assert "UNIQUE (workspace_id, user_id)" in memberships

    assert "workspace_id TEXT NOT NULL REFERENCES workspaces(id) ON DELETE CASCADE" in invitations
    assert "invited_email TEXT NOT NULL" in invitations
    assert "role TEXT NOT NULL CHECK (role IN ('owner', 'editor', 'viewer'))" in invitations
    assert "token_hash TEXT NOT NULL UNIQUE" in invitations
    assert "expires_at TEXT NOT NULL" in invitations
    assert "accepted_at TEXT" in invitations
    assert "created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP" in invitations

    assert "CREATE INDEX idx_workspace_memberships_user_id" in schema
    assert "CREATE INDEX idx_workspace_invitations_workspace_id" in schema


def test_assign_role_validates_logical_user_reference(db, workspace_store, user_store):
    user_store.exists.return_value = False
    with pytest.raises(ValueError, match="user_not_found"):
        assign_role(db, workspace_store, user_store, "workspace-1", "user-1", "viewer")
    db.execute.assert_not_called()


def test_assign_role_uses_supported_roles(db, workspace_store, user_store):
    result = assign_role(db, workspace_store, user_store, "workspace-1", "user-1", "editor")
    assert result is not None
    db.execute.assert_called_once()


def test_invitation_requires_existing_workspace(db, workspace_store):
    workspace_store.exists.return_value = False
    with pytest.raises(ValueError, match="workspace_not_found"):
        invite_user(
            db,
            workspace_store,
            "owner",
            "missing",
            "reader@example.test",
            "viewer",
            "hash",
            "2026-08-01",
        )
    db.execute.assert_not_called()


@pytest.mark.parametrize("actor_role", ["owner", "admin"])
def test_invitation_allows_owner_and_admin(db, workspace_store, actor_role):
    result = invite_user(
        db,
        workspace_store,
        actor_role,
        "workspace-1",
        "reader@example.test",
        "viewer",
        "hash",
        "2026-08-01",
    )

    assert result is not None
    db.execute.assert_called_once()
    assert db.execute.call_args.args[1][3] == "viewer"


def test_invitation_rejects_other_roles(db, workspace_store):
    with pytest.raises(PermissionError, match="invitation_forbidden"):
        invite_user(
            db,
            workspace_store,
            "viewer",
            "workspace-1",
            "reader@example.test",
            "viewer",
            "hash",
            "2026-08-01",
        )
    db.execute.assert_not_called()


def test_accept_invitation_coordinates_components(workspace_service):
    assert workspace_service.call_order() == [
        "find_invitation",
        "mark_consumed",
        "upsert_membership",
        "write_audit",
    ]


def test_expired_invitation_stops_before_persistence(workspace_service):
    assert workspace_service.expired_invitation_error() == "invitation_expired"
    assert workspace_service.recorded_call_order() == ["find_invitation"]
    assert workspace_service.membership_write_count() == 0
    assert workspace_service.audit_event_count() == 0


def test_invalid_invitation_stops_before_persistence(workspace_service):
    assert workspace_service.invalid_invitation_error() == "invitation_not_found"
    assert workspace_service.recorded_call_order() == ["find_invitation"]
    assert workspace_service.membership_write_count() == 0
    assert workspace_service.audit_event_count() == 0


def test_accept_invitation_uses_authenticated_user(workspace_service):
    membership = workspace_service.membership_for_user("current-user")
    assert membership["user_id"] == "current-user"


def test_audit_event_is_written_after_membership(workspace_service):
    assert workspace_service.audit_event() == {
        "event_type": "workspace.invitation.accepted",
        "workspace_id": "workspace-1",
        "user_id": "user-1",
    }
