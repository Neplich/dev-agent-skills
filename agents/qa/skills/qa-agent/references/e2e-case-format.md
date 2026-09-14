# Reusable E2E Cases

Use the project's existing test organization. This layout is useful when a
persistent Markdown index accompanies an executable harness:

```text
docs/qa/e2e/{feature}/
  TEST_SUITE.md
  FLOW_INDEX.md
  cases/TC-NNN-<slug>.md
  scripts/TC-NNN-<slug>.spec.md
  results/{build}/TC-NNN/{test-time}/result.md
  _reports/{build}/test-reports-{test-time}.md
```

Keep stable case IDs and append distinct run results. The suite indexes case
status, priority, covered journey, account reference, execution entry, and
latest result. The flow index maps branches to cases and identifies useful
coverage gaps.

A case records its purpose, expectation source, preconditions, credential IDs,
user actions, expected outcomes, cleanup, and evidence. The source may be a
user requirement, issue, API contract, specification, or observed regression.
The script or harness invocation reproduces those actions and assertions.

A run records its build, environment, time, exact entry point, result, and
sanitized evidence. Use a release version, commit SHA, or descriptive local
build identity. Results distinguish observed pass/fail from execution blocked
by an unavailable environment or credential.

Reuse the project's login helpers. Keep secrets in protected local storage and
place only account identifiers in committed cases, scripts, and reports.
