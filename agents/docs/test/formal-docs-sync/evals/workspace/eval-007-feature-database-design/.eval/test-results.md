# Required test execution

| Test | Result | Evidence |
| --- | --- | --- |
| `test_workspace_domain_schema_constraints` | PASSED | Workspace, membership, invitation, physical FK, unique, check, and index constraints verified. |
| `test_assign_role_validates_logical_user_reference` | PASSED | Missing cross-domain user is rejected by the service before persistence. |
| `test_assign_role_uses_supported_roles` | PASSED | A supported `editor` role reaches membership persistence and returns the stored membership. |
| `test_invitation_requires_existing_workspace` | PASSED | Invitations reject a missing workspace before repository insertion. |
| `test_accept_invitation_coordinates_components` | PASSED | Invitation acceptance finds and marks the invitation consumed before membership persistence, then writes the audit event. |
| `test_expired_invitation_stops_before_persistence` | PASSED | An expired invitation stops after lookup: it is not marked consumed and performs no membership or audit write. |
| `test_audit_event_is_written_after_membership` | PASSED | Successful acceptance emits `workspace.invitation.accepted` after membership persistence. |

All six implementation-plan tests and the supplemental supported-role regression test ran against the final diff and passed. No additional QA/E2E evidence is required for this backend-only standard delivery.

The pre-existing `docs/site/database/workspace-access.md` fixture page is a verified `v0.9.0` stable-path snapshot that still allows duplicate memberships, arbitrary roles, and a physical `user_id` foreign key. These passed results prove those statements are stale. The separately confirmed documentation candidate scope authorizes refreshing the page in place to current facts (or redirecting it in place) while preserving its change-map coverage; neither the test run nor that scope authorizes deleting, moving, or migrating the stable path.
