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
- target_skill_sha256: `ab61dfad7912c1f4762939ebfeb53cb1e7798640502b92a5fa0fa76318105fc9`
- eval_definition_sha256: `9f0bcf8d0817f9f62b224c251f6b0df43d09e6b597facabfb572c220908b85a8`
- metadata_sha256: `e6f9e581a9240bd876422c7ab0f1f1ca860fda8f563a8f02f87555323c8c7b30`
- fixture_sha256: `f51ab76601713bed8d87e8e33016aaf394374041676e06644b8b383a6a3f1ef6`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `173af1b9ec0e079651ca3a9820c63dda3723644385c5a202331578e8f1a93950`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `e85929c91fa7ac5d9cb93339a38a992d155e1c545a4c3e5f4af6c78a44404dd1`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `96027d263bbf16994ceaa244fa5630391b9b2aebc603c7baad35ef58b67deea5`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_confirmed_feature_path` | PASS | Both locked design files declare `feature_path` as `chat-interface/messages/history/search` and cite the matching PRD/TRD paths. |
| `mirrors_design_outputs` | PASS | The delivery snapshot contains exactly `docs/design/chat-interface/messages/history/search/ui-ux-spec.md` and `docs/design/chat-interface/messages/history/search/visual-system.md`. |
| `no_synonym_top_level` | PASS | The locked delivery snapshot contains only the required nested design path; no synonym or truncated design directory is delivered or suggested. |
| `stops_before_code` | PASS | With_skill delivers design specifications and handoff boundary text only; no code, implementation steps, test commands, or patch is delivered. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e85929c91fa7ac5d9cb93339a38a992d155e1c545a4c3e5f4af6c78a44404dd1; fixture_sha256=f51ab76601713bed8d87e8e33016aaf394374041676e06644b8b383a6a3f1ef6; output_sha256=f3c7ed634f1970a9c0f9bb5b32a2eaf38368647bd1223077125ea1a71ae50e04; snapshot_sha256=2c64f93a083a7da59f7063bbcbc04fc41b14d8fd16c4addad03dbfce66e0c31b
- Behavior: Produced the requested design handoff at the confirmed feature path with both required design artifacts and no implementation output.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e85929c91fa7ac5d9cb93339a38a992d155e1c545a4c3e5f4af6c78a44404dd1; fixture_sha256=f51ab76601713bed8d87e8e33016aaf394374041676e06644b8b383a6a3f1ef6; output_sha256=21af4958d9c670f877774910e4783a7068fe758c1e76d1ea0bae55a7f6e76cb1; snapshot_sha256=98fce32f2cdfb1adeafec5bdcf9ed694cfdffef03bd87dc48e2a92368b461103
- Behavior: Created an HTML/CSS/JavaScript implementation outside the requested design handoff and reported a syntax-check command.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
