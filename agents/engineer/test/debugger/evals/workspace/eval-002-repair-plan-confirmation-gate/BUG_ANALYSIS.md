# Bug Analysis

- Classification: `implementation_deviation`
- Feature path: `notifications`
- Expected behavior: notification status accepts `active`, `read`, and `archived`; archived items remain queryable in the archive view.
- Reproduction command: `npm test -- test/api/notifications.test.ts`
- Observed failure: `Unsupported notification status: archived`
- Root cause: `src/api/notifications.ts` handles `active` and `read` but omits the approved `archived` branch.
- Impact: archive API requests fail; active-list behavior is unaffected.
- Repair-planning state: reproduction and root cause are confirmed, and the user explicitly requested a repair implementation plan. No repair has been authorized.

The plan must identify the minimal source/test scope, verification commands, whether a sub-agent split is needed, and the later QA E2E handoff basis under `docs/qa/e2e/notifications/`. It must wait for exact plan confirmation before changing source, tests, or E2E assets.
