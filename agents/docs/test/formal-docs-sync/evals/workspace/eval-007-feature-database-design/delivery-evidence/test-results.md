# Required test execution

| Test | Result | Evidence |
| --- | --- | --- |
| `test_workspace_domain_schema_constraints` | PASSED | Per-table blocks verify workspace status/defaults, membership and invitation fields, each table's own role/FK/created-at constraints, uniqueness/expiry, and both secondary indexes. |
| `test_assign_role_validates_logical_user_reference` | PASSED | Missing cross-domain user is rejected by the service before persistence. |
| `test_assign_role_uses_supported_roles` | PASSED | A supported `editor` role reaches membership persistence and returns the stored membership. |
| `test_invitation_requires_existing_workspace` | PASSED | Invitations reject a missing workspace before repository insertion. |
| `test_invitation_allows_owner_and_admin` | PASSED | Both owner and admin roles pass the fail-closed guard and reach invitation persistence. |
| `test_invitation_rejects_other_roles` | PASSED | A viewer receives `PermissionError('invitation_forbidden')` before repository insertion. |
| `test_accept_invitation_coordinates_components` | PASSED | Invitation acceptance finds and marks the invitation consumed before membership persistence, then writes the audit event. |
| `test_expired_invitation_stops_before_persistence` | PASSED | An expired invitation stops after lookup: it is not marked consumed and performs no membership or audit write. |
| `test_invalid_invitation_stops_before_persistence` | PASSED | A missing token stops after lookup with no consume, membership, or audit write. |
| `test_accept_invitation_uses_authenticated_user` | PASSED | Invitation acceptance persists the role for the authenticated accepting user rather than reading a nonexistent invitation user ID. |
| `test_audit_event_is_written_after_membership` | PASSED | The real `AuditWriter` appends the complete accepted-invitation payload after membership persistence. |
