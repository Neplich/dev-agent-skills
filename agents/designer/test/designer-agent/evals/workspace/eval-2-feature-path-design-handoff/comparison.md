# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `designer`
- Skill: `designer-agent`
- Eval: `eval-002-feature-path-design-handoff`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `f51ab76601713bed8d87e8e33016aaf394374041676e06644b8b383a6a3f1ef6` from `agents/designer/test/designer-agent/evals/workspace/eval-2-feature-path-design-handoff`.
- Fixture SHA-256: `f51ab76601713bed8d87e8e33016aaf394374041676e06644b8b383a6a3f1ef6`
- Prompt SHA-256: `e85929c91fa7ac5d9cb93339a38a992d155e1c545a4c3e5f4af6c78a44404dd1`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e8c75de1d6f9996313bad1fce4ede6ed7cde9c08fd07355edd02169db57e8e68`
- Skill overlay SHA-256: `bb133a8c85c48881a2031584ba17c553a39faea708969d0cf9c8fc7668592bf7`
- Judge schema SHA-256: `173af1b9ec0e079651ca3a9820c63dda3723644385c5a202331578e8f1a93950`
- Eval definition SHA-256: `53f91ea5792318b5883984b62004cc098b15b6389da8f0c2233bdab77fbf2aa6`
- Metadata SHA-256: `e6f9e581a9240bd876422c7ab0f1f1ca860fda8f563a8f02f87555323c8c7b30`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_confirmed_feature_path` | PASS | The UI/UX snapshot declares `chat-interface/messages/history/search` and cites the matching PRD and TRD paths. |
| `mirrors_design_outputs` | PASS | Locked delivery snapshots contain both required files at the exact `docs/design/chat-interface/messages/history/search/` paths. |
| `no_synonym_top_level` | PASS | Locked git status and delivery snapshots show only the required nested design files; no synonym or truncated design directory is present or proposed. |
| `stops_before_code` | PASS | Both locked design files explicitly state that the handoff stops before code, implementation, and tests; no code, commands, or patches are delivered. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e85929c91fa7ac5d9cb93339a38a992d155e1c545a4c3e5f4af6c78a44404dd1; fixture_sha256=f51ab76601713bed8d87e8e33016aaf394374041676e06644b8b383a6a3f1ef6; output_sha256=02f6ced0d0f9a08fa7f3f464a7d5afb454d4f8e870b7c0beb8b7327e6e488fd3; snapshot_sha256=5b9f8941d802be4ba5120a2606b8392cab37303ff776b332a190d1ce03609a1d
- Behavior: Delivered the required nested UI/UX and visual-system design artifacts, aligned to the confirmed feature path and stopped at design handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e85929c91fa7ac5d9cb93339a38a992d155e1c545a4c3e5f4af6c78a44404dd1; fixture_sha256=f51ab76601713bed8d87e8e33016aaf394374041676e06644b8b383a6a3f1ef6; output_sha256=d4dedc2cd6b725e824876e0c9cb47ef90ed718e76fe2dc2fb905b048ac79f7b7; snapshot_sha256=e7ed3217952cfde6b9e60004cb4d243e1ffc2f60345bebb1ead06dd8432ebed3
- Behavior: Delivered a single PM-scoped DESIGN.md under the wrong output location, so it did not satisfy the required design artifact paths.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
