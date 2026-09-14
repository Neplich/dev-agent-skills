---
name: test-writer
description: "Add unit, integration, or end-to-end tests for requested behavior and regressions using the repository test harness."
---

# Test Writing

Identify the behavior under test from the user request, issue, API contract,
existing tests, or implementation evidence. Inspect the project's harness,
fixtures, assertion style, and CI commands before choosing test locations.

## Select meaningful coverage

- Unit tests for calculations, state transitions, boundaries, and pure logic.
- Integration tests for storage, transactions, API contracts, permissions, and
  external-service adapters.
- End-to-end tests for the user journeys whose integration is material to the
  change. Reuse existing cases and authentication helpers.

Test observable behavior. Include representative success, failure, and boundary
cases, with deterministic data and explicit cleanup. Mock at external boundaries
where appropriate and preserve the contract of the real dependency.

For a defect, show that the regression test exposes the original failure, then
verify the corrected behavior. For a feature, map the relevant expectations to
assertions. Run the focused tests followed by the relevant existing suite.

Use temporary directories, isolated databases, or the project's test fixtures.
Keep credentials in the approved secret mechanism and refer to them by stable
identifiers. Report executed commands, pass/fail results, uncovered behavior,
and any environment dependency that prevented a test from running.
