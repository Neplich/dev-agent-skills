# Eval Result: eval-001-route-mixed-qa-request

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-001-route-mixed-qa-request`
- Test case: route-mixed-qa-request
- Workspace: `workspace/eval-1-route-mixed-qa-request`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-08 for PR #98 trigger description routing review.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: login refresh implementation with PM acceptance question and intermittent CI failure evidence.
- Context read before applying the skill: `AGENTS.md`, `agents/qa/README.md`, `agents/qa/skills/qa-agent/SKILL.md`, `evals.json`, workspace `eval_metadata.json`, `docs/pm/login-refresh/PRD.md`, `docs/engineer/login-refresh/TRD.md`, `docs/qa/e2e/auth/login/login-refresh/TEST_SUITE.md`, `FLOW_INDEX.md`, `implementation/changes.md`, and `ci/login-intermittent-failure.log`.
- Runtime evidence: fresh subagent artifacts were generated under `tmp/eval-runs/2026-07-08-router-trigger-batch3/eval-001-route-mixed-qa-request/`.

## Assertions

- PASS `assertion_1`: the primary QA route is `spec-based-tester` because PM asks whether an implementation can enter documented acceptance; the intermittent CI failure remains a risk note or possible `bug-analyzer` follow-up.
- PASS `assertion_2`: downstream context includes PM/spec, TRD, implementation changes, CI failure log, QA E2E memory, environment constraints, and test command constraints.
- PASS `qa`: E2E work reads the function-tree memory set under `docs/qa/e2e/{feature_path}/`, including suite, flow index, cases, scripts, prior results, and reports.
- PASS `e2e_execution_protocol`: E2E routing requires scenario and platform version, blocks missing versions instead of writing `unknown`, selects repo harness > Chrome plugin / browser connector > Playwright fallback, and delegates TC execution to subagents.
- PASS `credential_and_report_refs`: credential storage uses `references/e2e-credential-store.md` and `.qa/e2e/accounts.local.json`; summary reporting uses `references/e2e-test-report.md`.
- PASS `alignment_and_plan_gate`: existing-feature and code-complete E2E updates require same-path PRD, TRD, product decisions when present, and confirmed `IMPLEMENTATION_PLAN.md`; gaps return to PM, `trd-gen`, or `feature-implementor`.
- PASS `assertion_4`: expected artifacts include route decision, requirement matrix, execution path, evidence references, risk notes, blockers, and defect handoff notes.
- PASS `assertion_5`: only one primary QA route is selected; the intermittent failure is not promoted to a confirmed bug without stronger evidence.

## With Skill Behavior

`qa-agent` satisfies the mixed QA routing contract after the PR #98 trigger description edits. The with-skill run selected the single primary route `qa-agent:spec-based-tester` because the current evidence outcome is documented acceptance readiness. It preserved the intermittent CI failure as a risk note or possible `bug-analyzer` follow-up, not a confirmed bug, and carried the required PM/spec, TRD, implementation changes, CI evidence, QA E2E memory, platform-version gate, execution-entry priority, credential/report references, and PRD/TRD/implementation-plan gate into the selected specialist. It did not execute tests or invoke multiple QA skills.

## Without Skill Baseline

Fresh baseline generated on 2026-07-08 from the eval prompt and fixture files only, without applying `qa-agent`, the QA Agent README, historical `comparison.md`, or any previous baseline. The baseline gave a plausible generic acceptance-validation recommendation, but omitted several repo-specific protocol details: the complete E2E memory read set, platform-version blocking rule, credential/report references, and missing implementation-plan owner.

## Failures

- None found. PR #98 did not regress mixed QA single-route selection, E2E gate preservation, risk handling for intermittent CI evidence, or the no-direct-execution boundary.

## Next Steps

- Keep this eval as regression coverage for mixed QA requests, single-route selection, and E2E gate preservation.

## Runtime Artifacts Policy

- Runtime artifacts were created only under `tmp/eval-runs/2026-07-08-router-trigger-batch3/eval-001-route-mixed-qa-request/`.
- Generated `with_skill.md`, `without_skill.md`, and `verdict.md` are scratch evidence only and must not be committed.
- Durable committed evidence for this run is this `comparison.md`.
