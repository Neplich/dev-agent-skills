# Eval Result: eval-004-frontend-ui-routing-contract

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-004-frontend-ui-routing-contract`
- Test case: frontend-ui-routing-contract
- Workspace: `workspace/eval-004-frontend-ui-routing-contract`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-06-24 after the issue #35 frontend UI routing contract update

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Nested `customer-portal/profile-settings` PRD/TRD with missing design docs.
- Expected output: route local frontend UI implementation through Engineer, check design deliverables, hand design gaps to Designer, then return to implementation planning.
- Validation context: fresh Codex subagent semantic validation plus CLI transcript diagnostics under `tmp/eval-runs/manual-issue35/engineer-agent/`.

## Assertions

- PASS `routes_frontend_update_to_engineer`: frontend code updates, UI implementation, "改 UI", and design-to-code requests remain Engineer-entry requests.
- PASS `does_not_route_to_external_ui_skill`: the skill explicitly avoids routing local frontend implementation to external UI reference skills such as `ui-ux-pro-max`.
- PASS `runs_feature_alignment`: the fixture PRD/TRD share `feature_path: customer-portal/profile-settings`, and the skill requires same-feature PRD/TRD alignment first.
- PASS `checks_design_deliverables`: the skill checks `docs/design/{feature_path}/ui-ux-spec.md` and/or `visual-system.md` before UI implementation planning.
- PASS `hands_design_gap_to_designer`: missing, stale, or conflicting design docs are handed to `designer-agent` with feature path, source docs, and design gap.
- PASS `routes_implementation_after_design`: implementation returns to `feature-implementor` only after design handoff, with the `IMPLEMENTATION_PLAN` confirmation gate preserved.
- PASS `does_not_execute_directly`: route-only requests do not write code, implementation plans, or run tests.

## With Skill

- PASS. The with-skill CLI transcript treated the request as an Engineer routing task, checked the PRD/TRD, detected missing design deliverables, handed the gap to `designer-agent`, and did not recommend `ui-ux-pro-max` or implementation.

## Without Skill / Baseline

- Baseline CLI output treated the prompt as a direct UI design/change request and offered layout/style directions, without preserving the Engineer PRD/TRD and design-handoff routing contract.

## Failures

- None found in fresh Codex subagent validation.

## Next Steps

- Keep this eval as regression coverage for frontend UI routing. Re-run fresh subagent validation if `engineer-agent` routing, Designer handoff, or eval fixture docs change.

## Runtime Artifacts Policy

- CLI transcript diagnostics were generated under `tmp/eval-runs/manual-issue35/engineer-agent/` and are runtime artifacts only.
- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
