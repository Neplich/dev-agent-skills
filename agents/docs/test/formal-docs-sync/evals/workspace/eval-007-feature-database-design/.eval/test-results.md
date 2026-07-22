# Required test execution

| Test | Result | Evidence |
| --- | --- | --- |
| `test_workspace_domain_schema_constraints` | PASSED | Workspace, membership, invitation, physical FK, unique, check, and index constraints verified. |
| `test_assign_role_validates_logical_user_reference` | PASSED | Missing cross-domain user is rejected by the service before persistence. |
| `test_invitation_requires_existing_workspace` | PASSED | Invitations reject a missing workspace before repository insertion. |

All implementation-plan tests ran against the final diff and passed. No additional QA/E2E evidence is required for this backend-only standard delivery.
