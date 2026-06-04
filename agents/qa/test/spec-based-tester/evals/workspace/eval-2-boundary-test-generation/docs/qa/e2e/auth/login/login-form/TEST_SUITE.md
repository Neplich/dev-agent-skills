# Login Form E2E Test Suite

Feature path: `docs/qa/e2e/auth/login/login-form/`
Scenario: `feature-update`
Platform version: `v1.2.0-rc.1`

## Active Cases

| TC | Status | Scope |
| --- | --- | --- |
| `TC-001-login-boundaries` | active | Empty values, long strings, special characters, invalid email format, locked account state |

## Execution Protocol

The repo package exposes `npm test -- login-boundaries`, so the repo harness is
the preferred execution path for this TC. Browser checks use Chrome only when
the harness cannot cover a user-visible assertion.
