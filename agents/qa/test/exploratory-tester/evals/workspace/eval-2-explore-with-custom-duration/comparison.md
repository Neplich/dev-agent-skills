# Eval Result: eval-002-explore-with-custom-duration

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-002-explore-with-custom-duration`
- Test case: explore-with-custom-duration
- Workspace: `workspace/eval-2-explore-with-custom-duration`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05
- Validation method: fresh Codex subagent review; baseline was derived before reading `exploratory-tester` or QA README, then with-skill behavior was checked against `SKILL.md`, `agents/qa/README.md`, direct shared references, eval assertions, and fixture evidence.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Expected output: 5 分钟探索测试报告
- Fixture context: settings-panel PRD, `SettingsPanel`, `EmailPreferenceForm`, shared toast notifications, QA environment note, `TEST_SUITE.md`, and `FLOW_INDEX.md`.
- Target and timebox: `https://qa.example.test/settings`, 5 minutes.
- Scenario and version: `feature-update`, platform version missing.

## Without Skill Baseline

- A generic exploratory answer might honor the 5-minute phrase but skip the function-tree QA memory and platform-version gate.
- It could start browser automation against the URL before confirming reachability, execution entry, platform version, or subagent delegation.
- It might create a new save/cancel TC without first updating `FLOW_INDEX.md` or checking for existing equivalent cases.
- It would be less likely to keep console/network anomalies as unconfirmed signals unless reproduction evidence is strong enough.

## With Skill Behavior

- PASS: `exploratory-tester` uses the user-provided 5-minute timebox exactly and builds the charter from URL, changed surface, environment note, and toast-risk context.
- PASS: The skill requires reading `TEST_SUITE.md`, `FLOW_INDEX.md`, `cases/*.md`, `scripts/*.spec.md`, prior `results/`, and `_reports/`; absent cases/scripts/results/reports are recorded as gaps.
- PASS: The fixture explicitly lacks a platform version. The correct with-skill result is blocked before E2E execution, never an `unknown` archive path.
- PASS: Execution-entry precedence is repo harness > Chrome plugin / browser connector > Playwright fallback, and executable E2E TC are delegated to subagents by default while the main agent owns scope and summary.
- PASS: Because this is an existing-feature exploration, reusable TC creation/update/execution also remains blocked until same-path PRD/TRD expectation alignment and a confirmed implementation plan are available.
- PASS: The report must separate observed issues, suspicious but unconfirmed signals, gaps not explored, evidence references, risk notes, and recommended next actions.

## Failures

- None identified. The current skill contract satisfies all eval assertions for context-driven scope, E2E memory confirmation, platform-version blocking, execution-entry precedence, subagent default, anomaly layering, evidence output, and risk handoff.

## Next Steps

- No fixture or skill change is required from this eval.
- A real execution should ask for platform version before any E2E run and keep URL reachability, TRD, implementation-plan, and missing TC/script gaps visible.

## Runtime Artifact Policy

- No runtime artifacts were created for this validation.
- Do not commit transcripts, verdicts, timing files, diagnostics, `with_skill/`, `without_skill/`, `outputs/`, or `comparison.auto.md`.
