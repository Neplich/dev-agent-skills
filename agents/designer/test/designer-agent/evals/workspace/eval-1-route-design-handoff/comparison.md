# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `designer`
- Skill: `designer-agent`
- Eval: `eval-001-route-design-handoff`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89` from `agents/designer/test/designer-agent/evals/workspace/eval-1-route-design-handoff`.
- Identity schema: `2`
- target_skill_sha256: `ab61dfad7912c1f4762939ebfeb53cb1e7798640502b92a5fa0fa76318105fc9`
- eval_definition_sha256: `81da08302867bb0360b62db9057e07b009cd93243321e4fb904ab779192971e2`
- metadata_sha256: `b228adbda9579c0023d949fdd52d3bd090b6ff85b7c6c2610e5202c6900dbe10`
- fixture_sha256: `318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `463caa76fbf321564869d8651cfcd73afe8721c939c5039c5cfd81c4ab25d935`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `96027d263bbf16994ceaa244fa5630391b9b2aebc603c7baad35ef58b67deea5`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_ux_first` | PASS | Trace states the route as `ui-ux-design → visual-design`; UX skill was read before visual-design, and the delivered UX document contains flow, structure, interaction states, and responsive guidance. |
| `routes_visual_followup` | PASS | Trace explicitly routes visual work to `visual-design` after UX; the delivered visual-system.md contains visual direction, colors, typography, components, and copy guidance. |
| `uses_real_output_filenames` | PASS | Locked delivery_snapshot contains exactly `docs/design/billing-notifications/ui-ux-spec.md` and `docs/design/billing-notifications/visual-system.md`. |
| `stops_before_code` | PASS | Locked delivery_snapshot contains only the two design documents; trace file-change evidence shows no React components, tests, scripts, or deployment configuration were added. |
| `hands_off_to_engineer` | PASS | Both locked design documents state that design stops and the next responsibility is `engineer-agent`; final output repeats the handoff boundary and defers React implementation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c; fixture_sha256=318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89; output_sha256=c5aeedb23d1dd991db19fc4ee9137e97c6519777adc33fe953c3ccb1593f8529; snapshot_sha256=8dd101cae63b884566982d1f5e0a4df0b533f1cd327bc81a09887b3bc0704e13
- Behavior: Produced the two required design deliverables, routed UX before visual design, stayed within design scope, and handed implementation to engineer-agent.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c; fixture_sha256=318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89; output_sha256=fbc5d1f104db474fa272f43b984cbc19e3c56e2ae53c2e0329dd329b6108dca0; snapshot_sha256=414c84c3628d68e97fb4858c92d830d1ebb5190180a4381bfa3e8677e6485e35
- Behavior: Implemented a React settings page directly, with no design deliverables, design routing, or engineer-agent handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
