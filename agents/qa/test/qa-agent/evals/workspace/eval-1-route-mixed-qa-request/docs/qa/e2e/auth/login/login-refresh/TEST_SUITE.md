# Login Refresh E2E Test Suite

Feature path: `docs/qa/e2e/auth/login/login-refresh/`
Scenario options: `feature-update`, `release`

## Active Cases

| TC | Status | Scope |
| --- | --- | --- |
| `TC-001-refresh-session` | active | Login refresh keeps the session valid after token rotation. |

Feature-update runs should cover this TC and direct affected login paths only.
Release runs should select all active E2E TC after platform version and release
environment are confirmed.
