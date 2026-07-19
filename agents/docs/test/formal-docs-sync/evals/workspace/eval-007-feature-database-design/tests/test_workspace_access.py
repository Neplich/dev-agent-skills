def test_membership_schema_constraints(schema_text):
    assert "UNIQUE (workspace_id, user_id)" in schema_text
    assert "owner', 'editor', 'viewer" in schema_text


def test_assign_role_validates_references(workspace_service):
    assert workspace_service.rejects_missing_workspace_and_user()


def test_assign_role_upserts_membership(workspace_service):
    assert workspace_service.assign_twice_keeps_one_current_membership()
