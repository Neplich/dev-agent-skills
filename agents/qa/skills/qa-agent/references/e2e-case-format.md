# E2E Case and Script Format Reference

This file is the only manually maintained authority for persistent E2E suite,
flow, case, script, and per-run result formats.

## Directory Layout

```text
docs/qa/e2e/{feature_path}/
├── TEST_SUITE.md
├── FLOW_INDEX.md
├── cases/TC-NNN-<short-slug>.md
├── scripts/TC-NNN-<short-slug>.spec.md
├── results/{platform-version}/TC-NNN/{test-time}/result.md
└── _reports/{platform-version}/test-reports-{test-time}.md
```

Use lower kebab-case slugs and a stable three-digit TC number. Existing history
is append-only.

## TEST_SUITE

List each active or retired case with its ID, title, priority, status, covered
flow, required account ID, script path, and latest result pointer. Do not embed
the full case or script body.

## FLOW_INDEX

Map each product flow and branch to the TC IDs that cover it. Record uncovered
branches explicitly. A feature update changes this map incrementally; a release
run executes every active mapped TC.

## Case File

Each `cases/TC-NNN-<short-slug>.md` contains:

- title and stable TC ID;
- status and priority;
- source PRD/TRD/confirmed implementation plan;
- preconditions and platform version requirement;
- credential IDs only, never secrets;
- numbered user actions;
- expected result after each meaningful action;
- cleanup and evidence requirements;
- history pointers to appended results.

## Script File

`scripts/TC-NNN-<short-slug>.spec.md` stores the smallest repeatable executable
flow or repository-harness invocation. It must match the case actions and
assertions. It may reference a credential ID but must never contain passwords,
tokens, cookies, sessions, TOTP secrets, SSH passwords, key contents, or
passphrases.

Execution priority is repository harness, then Chrome/browser connector, then
Playwright fallback. Reuse a shared login flow under
`docs/qa/e2e/_shared/login-flows/` when multiple cases authenticate the same
way.

## Per-Run Result

Each `result.md` records:

- TC ID, scenario, platform version, environment, and local test time;
- execution entry and exact command or interactive flow;
- `pass`, `fail`, or `blocked`;
- evidence paths;
- failure or blocked reason;
- residual risk and follow-up owner.

Never use `unknown` as the platform-version directory. A missing platform
version, credential reference, environment, aligned expectation, or confirmed
implementation plan blocks the affected run.
