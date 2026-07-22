# Required test execution

| Test | Result | Evidence |
| --- | --- | --- |
| `test_workspace_domain_schema_constraints` | PASSED | Workspace, membership, invitation, physical FK, unique, check, and index constraints verified. |
| `test_assign_role_validates_logical_user_reference` | PASSED | Missing cross-domain user is rejected by the service before persistence. |
| `test_invitation_requires_existing_workspace` | PASSED | Invitations reject a missing workspace before repository insertion. |

All implementation-plan tests ran against the final diff and passed. No additional QA/E2E evidence is required for this backend-only standard delivery.

The pre-existing `docs/site/database/workspace-access.md` fixture page is a verified `v0.9.0` stable-path snapshot that still allows duplicate memberships, arbitrary roles, and a physical `user_id` foreign key. These passed results prove those statements are stale. The separately confirmed documentation candidate scope authorizes refreshing the page in place to current facts (or redirecting it in place) while preserving its change-map coverage; neither the test run nor that scope authorizes deleting, moving, or migrating the stable path.
