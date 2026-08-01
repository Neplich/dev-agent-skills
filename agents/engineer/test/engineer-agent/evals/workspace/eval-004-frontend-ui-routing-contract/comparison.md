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
- Fresh validation date: 2026-07-31.
- With-skill source: current `agents/engineer/README.md`, current `agents/engineer/skills/engineer-agent/SKILL.md`, eval definition, README, metadata, and same-path PRD/TRD.
- Without-skill source: the same original prompt and fixture only; it was regenerated without reading or applying the skill, Agent README, with-skill output, old comparison, or a previous baseline.

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
- Overall result: PASS

All 7 current assertions were exercised and passed in the with-skill run.

## Assertions

- PASS `routes_frontend_update_to_engineer`: treats frontend code and UI implementation as Engineering work.
- PASS `does_not_route_to_external_ui_skill`: does not use external `ui-ux-pro-max`.
- PASS `runs_feature_alignment`: preserves `customer-portal/profile-settings` and reads same-path PRD/TRD.
- PASS `checks_design_deliverables`: checks the same-path UI/UX and visual-system files.
- PASS `hands_design_gap_to_designer`: hands missing design inputs to `designer-agent` with the resolved gap.
- PASS `routes_implementation_after_design`: returns to `feature-implementor` only after design completion and plan confirmation.
- PASS `does_not_execute_directly`: remains route-only.

## With Skill Behavior

The route explicitly keeps frontend/UI implementation in Engineer, resolves and aligns the same feature path, checks the two repository-native design deliverables, hands the fixture's design gap to `designer-agent`, and returns to `feature-implementor` with the confirmed plan gate. It does not call an external UI skill or execute work.

## Without Skill Baseline

The fresh baseline recognizes a frontend implementation request, reads the exact PRD/TRD paths, suggests generic design confirmation, and stays route-only. It does not establish the repository-specific Engineer route, exact design-file checks, named Designer handoff, or `feature-implementor` plan gate. Baseline assertion result: 3/7.

## L2-4 Coverage Observation

This scenario directly exercises and passes the corrected `feature-implementor` frontend/UI signal. No current engineer-agent eval triggers the project-bootstrap alternatives (confirmed TRD, approved PM docs, explicit skip-PM override) or debugger runtime-regression/hotfix signals. Those two change groups are therefore NOT EXERCISED in the aggregate L2-4 change-surface review; they were not fabricated. The current eval's seven assertion scenarios are fully covered.

## Failures

- None.

## Next Steps

- Keep this eval as direct regression coverage for frontend/UI implementation routing.
- Add direct project-bootstrap and debugger signal cases only in a separately approved eval-scope change.

## Runtime Artifacts Policy

- Fresh runtime evidence is under `tmp/eval-runs/issue-196-l2-3-l2-4/engineer-agent/eval-004-frontend-ui-routing-contract/`.
- `with_skill.md`, `without_skill.md`, and `verdict.md` are scratch evidence and must not be committed.
- This `comparison.md` is the only durable result.
