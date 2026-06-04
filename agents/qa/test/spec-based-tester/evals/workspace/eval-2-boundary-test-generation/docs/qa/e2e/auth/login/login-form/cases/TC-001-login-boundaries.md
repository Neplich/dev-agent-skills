# TC-001 Login Boundaries

## Basic Info

- Feature directory: `docs/qa/e2e/auth/login/login-form/`
- Scenario: `feature-update`
- Platform version: `v1.2.0-rc.1`
- Credential ref: `platform.login.qa_user`
- Script: `scripts/TC-001-login-boundaries.spec.md`

## Assertions

- Empty email and password are rejected with validation errors.
- Overlong input does not crash validation.
- Special characters are handled without leaking raw input.
- Invalid email format stays on the login form.
- Locked account state returns the locked-account message.

## Result Archive

Append execution evidence to
`results/TC-001-login-boundaries/{platform-version}/result.md` and snapshot the
case as `testcase.snapshot.md`.
