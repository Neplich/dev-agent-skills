# Eval Result: eval-001-route-design-handoff

## Evaluation Target

- Agent: `designer`
- Skill: `designer-agent`
- Eval: `eval-001-route-design-handoff`
- Test case: route-design-handoff
- Workspace: `workspace/eval-1-route-design-handoff`
- Review context: PR #98 trigger description routing review
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-08

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: billing notifications design route with a user request to also write React components.
- Fixture context: `docs/pm/billing-notifications/PRD.md`, which establishes billing notification settings for channels, thresholds, and escalation preferences.
- Context read before applying the skill: `AGENTS.md`, `agents/designer/README.md`, `agents/designer/skills/designer-agent/SKILL.md`, `agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md`, `evals.json`, workspace `eval_metadata.json`, and `docs/pm/billing-notifications/PRD.md`.

## Assertions

- PASS `routes_ux_first`: the route starts with `ui-ux-design` for flow, page structure, IA, wireframes, and interaction states.
- PASS `routes_visual_followup`: visual styling, component rules, colors, typography, and tone route to `visual-design` as the follow-up.
- PASS `uses_real_output_filenames`: design outputs are `docs/design/billing-notifications/ui-ux-spec.md` and `docs/design/billing-notifications/visual-system.md`.
- PASS `stops_before_code`: Designer does not write React components, tests, scripts, deployment files, shell commands, code patches, or implementation task lists.
- PASS `hands_off_to_engineer`: implementation is explicitly handed to `engineer-agent` after design completion.

## With Skill Behavior

`designer-agent` satisfies the design-only route. It treats `docs/pm/billing-notifications/PRD.md` as an equivalent confirmed PM document chain with stable feature path `billing-notifications`, then selects the narrow design sequence `ui-ux-design` -> `visual-design` because the request asks for both settings page flow and visual style.

The with-skill route writes or updates only durable design deliverables under `docs/design/billing-notifications/`: `ui-ux-spec.md` for UX flow, page structure, information architecture, wireframes, and interaction states; `visual-system.md` for visual style, component rules, colors, typography, and copy tone. It refuses the requested React component implementation in the Designer stage and stops at a handoff to `engineer-agent`.

## Without Skill Baseline

Source: fresh without-skill baseline generated on 2026-07-08 in `tmp/eval-runs/2026-07-08-router-trigger-batch4-final/eval-001-route-design-handoff/without_skill.md`.

The baseline used only the eval prompt and fixture's general billing notification settings context. It did not read or apply `agents/designer/README.md`, `agents/designer/skills/designer-agent/SKILL.md`, historical `comparison.md`, or any previous baseline output.

Without the router skill, a generic response can likely honor the explicit "不要进入实现" instruction and describe settings-page flow plus visual style. It does not reliably name `ui-ux-design` first, name `visual-design` second, use the durable filenames `docs/design/billing-notifications/ui-ux-spec.md` and `docs/design/billing-notifications/visual-system.md`, or identify `engineer-agent` as the handoff owner.

## Failures

- None found. All eval assertions pass in the with-skill run.
- The without-skill baseline remains weaker on router-specific guarantees, especially specialist sequence, durable file names, and named Engineer handoff.

## Next Steps

- Keep this eval as regression coverage for Designer trigger-description routing, design-only boundaries, durable design artifact naming, and implementation handoff behavior.
- No follow-up action is required for this eval result.

## Runtime Artifacts Policy

- Runtime evidence for this run is stored only under `tmp/eval-runs/2026-07-08-router-trigger-batch4-final/eval-001-route-design-handoff/`.
- The runtime files are `with_skill.md`, `without_skill.md`, and `verdict.md`.
- These runtime artifacts, transcripts, verdicts, timing files, output directories, diagnostics, and generated with_skill / without_skill files must not be committed.
