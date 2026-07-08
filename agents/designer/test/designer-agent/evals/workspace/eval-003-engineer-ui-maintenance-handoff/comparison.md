# Eval Result: eval-003-engineer-ui-maintenance-handoff

## Evaluation Target

- Agent: `designer`
- Skill: `designer-agent`
- Eval: `eval-003-engineer-ui-maintenance-handoff`
- Test case: engineer-ui-maintenance-handoff
- Workspace: `workspace/eval-003-engineer-ui-maintenance-handoff`
- Review context: PR #98 trigger description routing review
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-08

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Engineer-sourced UI maintenance design gap for `customer-portal/profile-settings`.
- Prompt source: `agents/designer/test/designer-agent/evals/evals.json` and workspace `eval_metadata.json`.
- Fixture documents:
  - `docs/pm/customer-portal/profile-settings/PRD.md`
  - `docs/engineer/customer-portal/profile-settings/TRD.md`
- Fixture document status: both approved, both dated 2026-06-24, both confirming `feature_path: customer-portal/profile-settings`

## Assertions

| Assertion | Result | Notes |
| --- | --- | --- |
| `accepts_engineer_design_handoff` | PASS | The with-skill route treats the request as an Engineer UI maintenance design gap, not an engineering implementation request. |
| `uses_confirmed_feature_path` | PASS | The route preserves `customer-portal/profile-settings` and uses the approved PRD/TRD fixture documents as the design basis. |
| `routes_design_skills` | PASS | The route selects `ui-ux-design` for information hierarchy and page structure, and selects `visual-design` for the primary button visual rule. |
| `writes_design_outputs_only` | PASS | The route limits outputs to `docs/design/customer-portal/profile-settings/ui-ux-spec.md` and `docs/design/customer-portal/profile-settings/visual-system.md`; it does not produce code, tests, shell commands, deployment config, or engineering implementation lists. |
| `hands_back_to_engineer` | PASS | The route stops after design handoff and names `engineer-agent` as the next owner for TRD / IMPLEMENTATION_PLAN / code / test continuation. |

## With Skill Behavior

The with-skill run read and applied `AGENTS.md`, `agents/designer/README.md`, `agents/designer/skills/designer-agent/SKILL.md`, the eval definition, `eval_metadata.json`, the PRD/TRD fixture documents, and the directly referenced PM shared handoff / closeout contract in `agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md`.

Observed behavior:

- Entry gate is satisfied by equivalent confirmed PM/Engineer documents: the PRD and TRD are approved, share the same stable `feature_path`, and identify the missing UI/UX and visual guidance as the current blocker.
- The request is accepted as Designer scope because `designer-agent` explicitly supports Engineer UI maintenance and frontend-update design handoffs.
- The route selects `ui-ux-design` for settings page information hierarchy and structure.
- The route selects `visual-design` because the primary button visual emphasis affects component visual rules.
- The only valid design outputs are `docs/design/customer-portal/profile-settings/ui-ux-spec.md` and `docs/design/customer-portal/profile-settings/visual-system.md`.
- The router stops at design handoff and returns implementation to `engineer-agent`; it does not invoke Engineer skills or produce implementation work.

## Without Skill Baseline

Source: fresh baseline generated on 2026-07-08 using only the eval prompt and general PRD/TRD fixture facts. It did not read or apply `agents/designer/README.md`, `agents/designer/skills/designer-agent/SKILL.md`, historical `comparison.md`, or any old baseline.

Baseline behavior summary:

- It would likely recognize a design documentation gap because the prompt explicitly says Engineer completed alignment and asks for settings page information hierarchy plus primary button guidance.
- It would likely preserve `customer-portal/profile-settings` because the prompt states the feature path directly.
- It would likely avoid code because the prompt explicitly forbids code and implementation checklists.
- It is less reliable on the repository-specific router contract: exact design artifact filenames, split routing between interaction structure and visual-system work, and the role-gated Designer stopping point are not guaranteed without the skill.

## Failures

None.

## Next Steps

- Keep the eval result as PASS for this PR #98 routing review.
- Do not commit runtime artifacts from `tmp/eval-runs/`.
- If the Designer router trigger wording changes again, rerun this eval with a new fresh without-skill baseline and update this comparison file in the same change set.

## Runtime Artifacts Policy

Runtime evidence for this validation was written only under:

`tmp/eval-runs/2026-07-08-router-trigger-batch4-final/eval-003-engineer-ui-maintenance-handoff/`

Files:

- `with_skill.md`
- `without_skill.md`
- `verdict.md`

These files are scratch runtime artifacts for short-term review only. They must not be committed, and they must not be copied into the fixture workspace. The durable result for the eval is this `comparison.md` file.
