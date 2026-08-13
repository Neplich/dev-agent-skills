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
- target_skill_sha256: `0ea73feefb23eaaa1087f7930615deb60bd48042a3221450dac25110527e9a02`
- eval_definition_sha256: `81da08302867bb0360b62db9057e07b009cd93243321e4fb904ab779192971e2`
- metadata_sha256: `b228adbda9579c0023d949fdd52d3bd090b6ff85b7c6c2610e5202c6900dbe10`
- fixture_sha256: `318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `463caa76fbf321564869d8651cfcd73afe8721c939c5039c5cfd81c4ab25d935`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c`
- Repository HEAD: `2f950c46c67111058957774f796ccf97ae616d36`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `08aafb5ab4f6346282a3571edc0bcbd3cde0a44d4f90ceae2c697a568d95ad53`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_ux_first` | PASS | Trace records the route as `ui-ux-design → visual-design`, with UX handling flows, structure, IA, wireframes, and interaction states first. |
| `routes_visual_followup` | PASS | Trace explicitly selects `ui-ux-design → visual-design`; the visual-system snapshot contains visual direction, components, colors, typography, and copy tone. |
| `uses_real_output_filenames` | PASS | Locked delivery snapshots contain exactly `docs/design/billing-notifications/ui-ux-spec.md` and `docs/design/billing-notifications/visual-system.md`. |
| `stops_before_code` | PASS | Locked git evidence shows only the two design Markdown files were added; the final message states React implementation was not performed in the design stage. |
| `hands_off_to_engineer` | PASS | Both locked design documents and the final message explicitly hand implementation to `engineer-agent`. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c; fixture_sha256=318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89; output_sha256=85a702ea051ebd9173bfbe1e7eed290dfcc8d5cab1f65c3db058e9c08e9940d6; snapshot_sha256=b38bacb6fa723effc9b27f97c0b8a3e799567f6d3f770a9017b34ccb94445fe4
- Behavior: Completed the UX-first then visual-design workflow, delivered both required design documents, stopped before implementation, and handed off to engineer-agent.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c; fixture_sha256=318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89; output_sha256=110788c730e80691d82689fff9666550eb0e485bf08728ea36e2fb259d207a21; snapshot_sha256=fdde5ac550abb0aea166b4fa44322913028de46ba2823a4527996dd088909fe9
- Behavior: Produced a React implementation and source files directly, without the required design workflow or design deliverables.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
