# Profile Form E2E Test Suite

Feature path: `docs/qa/e2e/account/profile-settings/profile-form/`
Scenario: `feature-update`
Platform version: missing, so execution is blocked until the user provides it.

## Active Cases

No active TC exists yet. The QA route should explore the changed profile
settings files, then create durable `cases/TC-NNN-<short-slug>.md` and matching
`scripts/TC-NNN-<short-slug>.spec.md` files before execution.

## Execution Protocol

- Prefer repo harness when it covers the TC.
- Use Chrome plugin / browser connector when no repo harness covers the flow.
- Use Playwright only as fallback.
- Run E2E TC through subagents; the main agent summarizes results.
