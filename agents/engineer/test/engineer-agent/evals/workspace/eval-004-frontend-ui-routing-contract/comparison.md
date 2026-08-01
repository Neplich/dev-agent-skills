# Eval Result: eval-004-frontend-ui-routing-contract

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-004-frontend-ui-routing-contract`
- Test case: frontend-ui-routing-contract
- Workspace: `workspace/eval-004-frontend-ui-routing-contract`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: frontend UI request for `customer-portal/profile-settings` with same-path PRD/TRD and intentionally absent design deliverables.
- Fresh validation date: 2026-08-01.
- With-skill source: current Engineer README, current `engineer-agent` SKILL, eval definition, metadata, README, and same-path PRD/TRD.
- Without-skill source: the same prompt and fixture, freshly regenerated without reading or applying the target README/SKILL, with-skill output, historical comparison, or prior baseline.

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
- Overall result: PASS

All 7 assertions were exercised and passed in the with-skill run.

## Assertions

- PASS `routes_frontend_update_to_engineer`: treats local frontend/UI implementation as Engineering work.
- PASS `does_not_route_to_external_ui_skill`: does not use external `ui-ux-pro-max`.
- PASS `runs_feature_alignment`: preserves `customer-portal/profile-settings` and reads its PRD/TRD.
- PASS `checks_design_deliverables`: checks the same-path UI/UX and visual-system files.
- PASS `hands_design_gap_to_designer`: hands the missing information hierarchy and button-style design scope to `designer-agent`.
- PASS `routes_implementation_after_design`: returns to `feature-implementor` only after design completion and plan confirmation.
- PASS `does_not_execute_directly`: remains route-only.

## With Skill Behavior

The fresh route keeps frontend implementation in Engineer, aligns the same feature path, checks both repository-native design deliverables, hands the fixture's design gap to `designer-agent`, and returns to `feature-implementor` behind the confirmed-plan gate.

## Without Skill Baseline

The fresh baseline identifies frontend engineering, avoids the external skill, generically recommends a designer for missing specifications, and remains route-only. It omits the exact same-path alignment, repository design-file checks, named agent handoff, and `feature-implementor` implementation-plan gate. Baseline assertion result: 4/7.

## Failures

- None.

## Next Steps

- Keep this eval as regression coverage for frontend/UI implementation routing and repository-native design handoff.

## Runtime Artifacts Policy

- Fresh runtime evidence is under `tmp/eval-runs/issue-196-project-bootstrap-removal-20260801-131022/engineer-agent/eval-004-frontend-ui-routing-contract/`.
- `with_skill.md`, `without_skill.md`, and `verdict.md` are scratch evidence and must not be committed.
- This `comparison.md` is the only durable result.
