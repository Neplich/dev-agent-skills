# Eval Result: eval-003-bug-report-conflicts-with-prd

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-003-bug-report-conflicts-with-prd`
- Test case: bug-report-conflicts-with-prd
- Workspace: `workspace/eval-003-bug-report-conflicts-with-prd`
- Latest result: PASS (5/5 assertions) - fresh Codex paired validation completed on 2026-07-26

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: same-path confirmed PRD and TRD that both exclude archived notifications from active
- Fresh run: isolated paired copies under `tmp/eval-runs/issue-158-round1/engineer-a/`; no historical baseline was reused
- Source branch: `test/issue-158-round1-thin-fixtures`

## Assertions

- PASS `detects_prd_conflict`: classifies the report as `requirement_change`.
- PASS `hands_off_to_pm_update`: names `pm-agent:idea-to-spec` and the `existing-project-update` lane, then requires TRD synchronization.
- PASS `blocks_e2e_when_expectation_changes`: blocks new E2E expectations until PRD/decision, TRD and confirmed implementation plan align.
- PASS `does_not_produce_repair_plan`: produces no repair plan, code or test change.
- PASS `blocks_explicit_skip_override`: states that a skip request remains a blocker/risk, not authorization.

## With Skill Behavior

The candidate used the durable expectation chain, stopped before reproduction or repair, and gave the exact PM update route and downstream gates.

## Without Skill Baseline

The fresh baseline noticed the PRD conflict and declined to fix, but did not name the exact PM lane, the E2E blocker chain, or the skip-override rule. Baseline result: 2/5 assertions.

## Failures

- With-skill: none.
- Baseline: `hands_off_to_pm_update`, `blocks_e2e_when_expectation_changes`, and `blocks_explicit_skip_override` failed.

## Next Steps

Keep this as the requirement-change negative path.

## Runtime Artifacts Policy

Only this durable comparison is committed; paired responses stay in ignored scratch space.
