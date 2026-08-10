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
- Fixture SHA-256: `318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89`
- Prompt SHA-256: `6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e8c75de1d6f9996313bad1fce4ede6ed7cde9c08fd07355edd02169db57e8e68`
- Skill overlay SHA-256: `a999946ff7bd8c02d585ab2a5420fd1a5c4016373f3e682b7b9832c315b881b3`
- Judge schema SHA-256: `463caa76fbf321564869d8651cfcd73afe8721c939c5039c5cfd81c4ab25d935`
- Eval definition SHA-256: `22532d649002dfa1851fec27c554d610e1ed3e70ab860965c5b4914f96d4ccce`
- Metadata SHA-256: `b228adbda9579c0023d949fdd52d3bd090b6ff85b7c6c2610e5202c6900dbe10`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_ux_first` | PASS | Raw trace records the design specialist chain as `ui-ux-design` → `visual-design`, with UI/UX skill inspection before visual skill inspection. |
| `routes_visual_followup` | PASS | Raw trace explicitly records `ui-ux-design` → `visual-design`; visual-system delivery snapshot contains visual-system content. |
| `uses_real_output_filenames` | PASS | Locked delivery snapshot contains `docs/design/billing-notifications/ui-ux-spec.md` and `docs/design/billing-notifications/visual-system.md`. |
| `stops_before_code` | PASS | Git status and locked delivery snapshot show only the two design documents; no React, test, script, or deployment files were delivered. |
| `hands_off_to_engineer` | PASS | Final output and locked design documents state that React implementation and tests should be handed to `engineer-agent`. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c; fixture_sha256=318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89; output_sha256=6e8f78c380b0f1741a592a3e8bdf21a807cad4046113e5ee5300d78359fe2eb5; snapshot_sha256=633edb41b2870772daec4de620c7cf056975ca1533938ca57938eb1a97f70531
- Behavior: Followed the UX-first then visual-design route, delivered the required design documents, stopped before implementation, and handed off to engineer-agent.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c; fixture_sha256=318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89; output_sha256=4f38869817214bf915cea73c378c08ef7a552167599657c8adc3bcd88bcbf4fb; snapshot_sha256=b4c8dcdf073a861e788eb9c386dd6573c61408b68d58e2c0c906969669738668
- Behavior: Implemented React UI and supporting project files directly, using DESIGN.md under the PM directory instead of the required design-only handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
