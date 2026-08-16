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
- Identity schema: `2`
- target_skill_sha256: `1d67d4772843dc0275749d693d7415791b7459f5d948588a69fb240bcfd7f02b`
- eval_definition_sha256: `9f0bcf8d0817f9f62b224c251f6b0df43d09e6b597facabfb572c220908b85a8`
- metadata_sha256: `e6f9e581a9240bd876422c7ab0f1f1ca860fda8f563a8f02f87555323c8c7b30`
- fixture_sha256: `f51ab76601713bed8d87e8e33016aaf394374041676e06644b8b383a6a3f1ef6`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `173af1b9ec0e079651ca3a9820c63dda3723644385c5a202331578e8f1a93950`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `e85929c91fa7ac5d9cb93339a38a992d155e1c545a4c3e5f4af6c78a44404dd1`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `902f97074f6d958600dd8079608539a38bff227cb03726b9ab277705b1b8ded7`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_confirmed_feature_path` | PASS | Both locked design files use `chat-interface/messages/history/search` as `feature_path` and explicitly reference the matching PRD and TRD. |
| `mirrors_design_outputs` | PASS | The delivery snapshot contains exactly `docs/design/chat-interface/messages/history/search/ui-ux-spec.md` and `docs/design/chat-interface/messages/history/search/visual-system.md`. |
| `no_synonym_top_level` | PASS | The with_skill delivery snapshot and git status show only the confirmed design path; no synonym or truncated directory is present. |
| `stops_before_code` | PASS | The locked outputs contain design handoff documents only, with no code, patch, test command, or engineering implementation procedure; they stop at handoff to engineer-agent. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e85929c91fa7ac5d9cb93339a38a992d155e1c545a4c3e5f4af6c78a44404dd1; fixture_sha256=f51ab76601713bed8d87e8e33016aaf394374041676e06644b8b383a6a3f1ef6; output_sha256=8c9f192c8e013efe8c2801e700be44029f8751778e4afd2a1636046a9ed3c819; snapshot_sha256=aa76691f1ee9fc792f1f0a016dae0421530e78e6ab7b4ea282b321aa5ac53f43
- Behavior: Delivered both required design artifacts at the confirmed feature path and stopped at the design handoff boundary.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e85929c91fa7ac5d9cb93339a38a992d155e1c545a4c3e5f4af6c78a44404dd1; fixture_sha256=f51ab76601713bed8d87e8e33016aaf394374041676e06644b8b383a6a3f1ef6; output_sha256=ca4d239b100d45e43a4116a6ae06be6f911403ff7bc8393db6d30f182a14f62a; snapshot_sha256=875666abfa4fc5b43fbefbe4b797e05c390bf266a7f6fff16beccdfdca9ee074
- Behavior: Created an implementation prototype (`index.html`, `styles.css`, `app.js`) and ran a syntax check, without the required design deliverables or confirmed design-path handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
