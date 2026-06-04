# Login Session E2E Test Suite

Feature path: `docs/qa/e2e/auth/login/session-start/`
Scenario: `feature-update`
Platform version: `v1.2.0-fix.1`

## Active Cases

| TC | Status | Scope |
| --- | --- | --- |
| `TC-001-login-session` | active | Successful login creates a session and redirects to dashboard. |

## Regression Scope

For this fix, run the original failure recheck and adjacent invalid-credential
and locked-account paths. Do not expand to release full E2E unless the scenario
is explicitly `release`.
