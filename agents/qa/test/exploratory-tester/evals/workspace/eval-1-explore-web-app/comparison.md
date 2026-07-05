# Eval Result: eval-001-explore-web-app

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-001-explore-web-app`
- Test case: explore-web-app
- Workspace: `workspace/eval-1-explore-web-app`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05
- Validation method: fresh Codex subagent review; baseline was derived before reading `exploratory-tester` or QA README, then with-skill behavior was checked against `SKILL.md`, `agents/qa/README.md`, direct shared references, eval assertions, and fixture evidence.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Expected output: 探索测试报告，包含发现的问题列表和复现路径
- Fixture context: search-refresh PRD, `SearchPanel`, `FilterPills`, `ResultsList`, QA environment note, `TEST_SUITE.md`, `FLOW_INDEX.md`, and `cases/TC-001-filter-results.md`.
- Scenario and version: `feature-update`, platform version `v0.9.0-dev`.

## Without Skill Baseline

- A generic exploratory answer would likely begin browser probing or list ad hoc checks without first building a charter from PM context, changed surface, known risks, and environment constraints.
- It could skip the existing `docs/qa/e2e/search/results/filtering/` memory and create a duplicate filter-results TC instead of updating `TC-001-filter-results`.
- It might not separate observed defects, suspicious unconfirmed signals, and gaps not explored.
- It could ignore that browser execution depends on `QA_BASE_URL`, and it would be less likely to state repo harness > Chrome plugin / browser connector > Playwright fallback as the execution-entry order.

## With Skill Behavior

- PASS: `exploratory-tester` requires a charter before interaction, including surface, timebox source, heuristics, and escalation signals. The fixture supplies the changed search surfaces and keyboard-focus risk needed for that charter.
- PASS: Existing QA memory is primary. The skill requires reading `TEST_SUITE.md`, `FLOW_INDEX.md`, `cases/*.md`, `scripts/*.spec.md`, prior `results/`, and `_reports/`; absent scripts/results/reports must be recorded instead of silently skipped.
- PASS: The fixture's existing `TC-001-filter-results` covers the filter-results flow. The skill requires updating the existing TC, script, or `FLOW_INDEX.md` when the same flow is found, and keeps one-off observations in the exploratory report.
- PASS: For existing-feature exploration, reusable TC creation/update/execution remains gated by same-path PRD/TRD expectation alignment and a confirmed `IMPLEMENTATION_PLAN.md`; fixture-level browser execution is also blocked unless `QA_BASE_URL` is present.
- PASS: The report contract separates observed issues, suspicious but unconfirmed signals, gaps not explored, exploration path covered, evidence used, and recommended next actions.

## Failures

- None identified. The current skill contract satisfies all eval assertions for chartering, QA memory reuse, scope/timebox discipline, evidence layering, chartered exploration, handoff-ready output, and duplicate TC avoidance.

## Next Steps

- No fixture or skill change is required from this eval.
- A real execution should record any missing `scripts/`, prior `results/`, `_reports/`, `QA_BASE_URL`, TRD, or implementation-plan gates as blocked before browser or E2E execution.

## Runtime Artifact Policy

- No runtime artifacts were created for this validation.
- Do not commit transcripts, verdicts, timing files, diagnostics, `with_skill/`, `without_skill/`, `outputs/`, or `comparison.auto.md`.
