# Eval Result: eval-001-route-mixed-qa-request

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-001-route-mixed-qa-request`
- Test case: route-mixed-qa-request
- Workspace: `workspace/eval-1-route-mixed-qa-request`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-06

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: login refresh implementation with PM acceptance question and intermittent CI failure evidence.
- Context read before applying the skill: `evals.json`, workspace `eval_metadata.json`, `docs/pm/login-refresh/PRD.md`, `docs/engineer/login-refresh/TRD.md`, `docs/qa/e2e/auth/login/login-refresh/TEST_SUITE.md`, `FLOW_INDEX.md`, `implementation/changes.md`, and `ci/login-intermittent-failure.log`.
- #81 context read: `Safety-Net Closeout and Auto-Continue` from `agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md`.

## Assertions

- PASS `assertion_1`: the primary QA route is `spec-based-tester` because PM asks whether an implementation can enter documented acceptance; the intermittent CI failure remains a risk note or possible `bug-analyzer` follow-up.
- PASS `assertion_2`: downstream context includes PM/spec, TRD, implementation changes, CI failure log, environment constraints, and test commands.
- PASS `qa`: E2E work reads the function-tree memory set under `docs/qa/e2e/{feature_path}/`, including suite, flow index, cases, scripts, prior results, and reports.
- PASS `e2e_execution_protocol`: E2E routing requires scenario and platform version, blocks missing versions instead of writing `unknown`, selects repo harness > Chrome plugin / browser connector > Playwright fallback, and delegates TC execution to subagents.
- PASS `credential_and_report_refs`: credential storage uses `references/e2e-credential-store.md` and `.qa/e2e/accounts.local.json`; summary reporting uses `references/e2e-test-report.md`.
- PASS `alignment_and_plan_gate`: existing-feature and code-complete E2E updates require same-path PRD, TRD, product decisions when present, and confirmed `IMPLEMENTATION_PLAN.md`; gaps return to PM, `trd-gen`, or `feature-implementor`.
- PASS `assertion_4`: expected artifacts include route decision, execution path, evidence references, risk notes, blockers, and handoff notes.
- PASS `assertion_5`: only one primary QA route is selected; the intermittent failure is not promoted to a confirmed bug without stronger evidence.

## With Skill Behavior

`qa-agent` satisfies the mixed QA routing contract. It chooses the narrowest current evidence route, preserves the intermittent CI failure as risk or follow-up rather than a parallel execution path, and carries the required QA memory, environment, credential, report, and PRD/TRD/plan gates into the selected specialist. Because the fixture does not include a confirmed implementation plan, the route can still be selected, but E2E acceptance creation or execution would be blocked until `engineer-agent:feature-implementor` supplies the confirmed plan.

#81 closeout behavior is safe for this case: after routing, `qa-agent` may propose the next collaboration-chain owner, but `auto-continue` cannot make QA perform engineering fixes, bypass E2E gates, or execute another role's workflow.

## Without Skill Baseline

Fresh baseline generated on 2026-07-06 without reading or applying `qa-agent` skill instructions or the QA Agent README: a generic response would likely either start running tests immediately or split the work into both acceptance testing and bug analysis. It might assume a localhost port or browser path, miss the durable E2E memory read set, omit credential/report references, or classify the intermittent CI log as a confirmed bug too early.

## Failures

- None found. The missing implementation plan is an expected gate condition for acceptance execution, not a router failure.
- No #81 regression found: original single-route selection and gate behavior remain intact, and `auto-continue` does not cross the QA role boundary.

## Next Steps

- Keep this eval as regression coverage for mixed QA requests, single-route selection, E2E gate preservation, and #81 closeout boundary behavior.

## Runtime Artifacts Policy

- No runtime artifacts were created for this validation.
- Runtime transcripts, verdicts, timing, output directories, diagnostics, and generated with_skill / without_skill files must not be committed.
