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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e8c75de1d6f9996313bad1fce4ede6ed7cde9c08fd07355edd02169db57e8e68`
- Skill overlay SHA-256: `bb133a8c85c48881a2031584ba17c553a39faea708969d0cf9c8fc7668592bf7`
- Judge schema SHA-256: `463caa76fbf321564869d8651cfcd73afe8721c939c5039c5cfd81c4ab25d935`
- Eval definition SHA-256: `22532d649002dfa1851fec27c554d610e1ed3e70ab860965c5b4914f96d4ccce`
- Metadata SHA-256: `b228adbda9579c0023d949fdd52d3bd090b6ff85b7c6c2610e5202c6900dbe10`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_ux_first` | NOT_EXERCISED | Locked evidence does not prove the required route selection or ordering. |
| `routes_visual_followup` | NOT_EXERCISED | Locked evidence does not prove delegation to visual-design as a later or second route. |
| `uses_real_output_filenames` | PASS | Delivered files are exactly docs/design/billing-notifications/ui-ux-spec.md and docs/design/billing-notifications/visual-system.md. |
| `stops_before_code` | PASS | Both delivered files explicitly define the work as design-only and exclude React implementation and tests; the snapshot contains no code deliverables. |
| `hands_off_to_engineer` | PASS | Both delivered files explicitly hand remaining implementation to engineer-agent. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c; fixture_sha256=318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89; output_sha256=2868393852ea5a4f1f9911fb881fde3111022e9d38faff25a09ff16e45f90348; snapshot_sha256=58bdc5d739570e882eec31f89ee4fbc136ce3b395ebf602bd44f8c4fe95b7d13
- Behavior: Produced the requested UX and visual design deliverables, stopped at design, and handed implementation to engineer-agent.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c; fixture_sha256=318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89; output_sha256=982c1920fa1f7664c12c097b7c21d9323ff1b2e8ba4c46d5c48f200c187a2adb; snapshot_sha256=ab31f19621725ba90c2297b9a96398a29ab2b970ff8d37cdbe0c498a5dff6763
- Behavior: Implemented React/Vite files directly, providing a fresh code-first baseline.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Exercise or capture route-selection and route-order evidence for the two routing assertions.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
