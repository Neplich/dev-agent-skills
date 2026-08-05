# Eval Result: eval-002-existing-feature-alignment-gate

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-002-existing-feature-alignment-gate`
- Test case: existing-feature-alignment-gate
- Workspace: `workspace/eval-002-existing-feature-alignment-gate`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: small existing-feature behavior change request for Notification Center archived items.
- Fresh validation date: 2026-08-01.
- With-skill source: current Engineer README, current `engineer-agent` SKILL, eval definition, and workspace metadata.
- Without-skill source: the same prompt and fixture, freshly regenerated without reading or applying the target README/SKILL, with-skill output, historical comparison, or prior baseline.

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


All 6 assertions were exercised and passed in the with-skill run.

## Assertions

- PASS `reads_product_and_engineer_docs`: requires the same-feature PRD, TRD, and present decision records.
- PASS `classifies_expectation_change`: treats archived entries in active as a possible approved-expectation change.
- PASS `routes_to_existing_project_update`: sends conflicts to `pm-agent:idea-to-spec` through `existing-project-update`.
- PASS `routes_trd_gap_to_trd_gen`: constructs a gap packet for missing, stale, or incomplete TRD coverage and sends it to `trd-gen`.
- PASS `requires_plan_after_alignment`: preserves the confirmed implementation-plan gate after alignment.
- PASS `does_not_route_directly_to_implementation`: does not accept “small change” as permission to bypass alignment.

## With Skill Behavior

The fresh route blocks direct implementation until PRD, TRD, and decision records establish expected behavior. It distinguishes a PM expectation conflict from a TRD gap and keeps `feature-implementor` behind the confirmed implementation-plan gate.

## Without Skill Baseline

The fresh baseline routes directly to implementation and only suggests optional product confirmation. It omits the required document reads, named PM update lane, TRD gap packet/specialist, and confirmed implementation-plan gate. Baseline assertion result: 0/6.

## Failures

- None.

## Next Steps

- Keep this eval as regression coverage for existing-feature alignment and attempts to bypass PM/TRD gates.

## Runtime Artifacts Policy

- Fresh runtime evidence is under `tmp/eval-runs/issue-196-project-bootstrap-removal-20260801-131022/engineer-agent/eval-002-existing-feature-alignment-gate/`.
- `with_skill.md`, `without_skill.md`, and `verdict.md` are scratch evidence and must not be committed.
- This `comparison.md` is the only durable result.
