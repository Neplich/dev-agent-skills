# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-006-nested-feature-path`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7` from `agents/product_manager/test/idea-to-spec/workspace/iteration-3/eval-6-nested-feature-path`.
- Fixture SHA-256: `7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7`
- Prompt SHA-256: `c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9c3b136c6958582b2c5c3d552759bbe4fd3ef24876075804e91c5b21980a34af`
- Skill overlay SHA-256: `e4cc003a0e06320ef354c6c9cdbebb2b75980ec8b23ae530ac78b0667fab31da`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `0d6c5b2207f916945e44c4152d1df1a5456bcf63eecb7a912ef1fe1811598afa`
- Metadata SHA-256: `4835f86af8c88f61556ab924715c5dc8125d2c5616e22976f405e64c105bc13a`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `scan_existing_prds` | PASS | With-skill output references the existing Chat Interface, Messages, and Message History PRDs and their docs/pm paths. |
| `nested_feature_path` | PASS | It explicitly specifies feature_path as chat-interface/messages/history/search and the nested search PRD path. |
| `no_parallel_top_level` | PASS | It explicitly says the feature belongs under existing history as a fourth-level child and should not create a top-level feature. |
| `handoff_fields` | FAIL | The output includes feature_path, parent_feature, and feature_level, but does not provide a handoff packet containing feature, feature_path_evidence, or all required fields. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818; fixture_sha256=7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7; output_sha256=caed880328598e205b0d2e4b3051260c661fcb49afa10632277624586fd3e112; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identified the nested fourth-level feature path and avoided parallel top-level paths, but omitted a complete handoff packet.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818; fixture_sha256=7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7; output_sha256=c80e5fddf6840b01578baff257215744d810730e2506d5be208866c6cbfaee4a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Identified the correct nested search PRD path and parent PRD updates, but did not provide the required handoff fields.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output does not contain a complete handoff packet with feature, feature_path, parent_feature, feature_level, and feature_path_evidence.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

# Eval Result: eval-006-nested-feature-path

## Latest Fresh Evaluation — 2026-08-07

- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; fresh paired manifests matched exactly.
- Behavior result: FAIL — 3/4 assertions passed.
- Coverage result: FULL — all 4 assertion scenarios were exercised.
Overall result: FAIL

### Assertion Results

- `scan_existing_prds`: PASS — the trace shows the existing PM PRDs were scanned and read before choosing a path.
- `nested_feature_path`: PASS — resolved `chat-interface/messages/history/search`.
- `no_parallel_top_level`: PASS — did not choose a truncated or top-level sibling path.
- `handoff_fields`: FAIL — no complete handoff packet was produced, and `feature_path_evidence` was missing.

### With-Skill / Baseline Comparison

The with-skill candidate correctly resolved the four-level path and stayed read-only. The baseline also found the nested path; it is comparison evidence only.

### Failures / Next Steps

- Include `feature_path`, `feature`, `parent_feature`, `feature_level`, and evidence-backed `feature_path_evidence` in an explicit handoff packet.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-006-nested-feature-path/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-006-nested-feature-path`
- Workspace: `workspace/iteration-3/eval-6-nested-feature-path`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`; approved three-level PRD chain with all candidate stale child paths excluded by `execution_cleanup`.
- Fresh run: `2026-08-03 11:58:20 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/pm/eval-006-nested-feature-path/`

## Latest Result

- Behavior result: PASS — all 4 assertions passed.
- Coverage result: FULL — 4/4 assertion scenarios were exercised; no `NOT EXERCISED` items.
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- `scan_existing_prds`: PASS — reads the complete `chat-interface/messages/history` PRD ancestry.
- `nested_feature_path`: PASS — resolves `chat-interface/messages/history/search` with parent and level metadata.
- `no_parallel_top_level`: PASS — rejects all parallel and truncated candidate directories.
- `handoff_fields`: PASS — includes `feature_path`, `feature`, `parent_feature`, `feature_level`, and structured `feature_path_evidence`.

## With-Skill Behavior

The response uses the existing PRD chain as the authoritative ownership evidence, proposes a child PRD and DECISIONS directory only under the confirmed parent, and keeps the handoff not ready until search scope is confirmed. No BRD context is required or emitted.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and cleaned fixture, without reading or applying the target skill, Product Manager README, internal instructions, or historical comparison. It found the correct four-level path but used weaker path-only evidence and did not consistently preserve the not-ready PM gate.

## Failures

- No assertion failures or baseline blockers.
- BRD removal caused no feature-path or handoff regression; ownership is fully established by PRDs.

## Next Steps

- Keep this eval as coverage for PRD-based nested feature ownership after BRD removal.

## Runtime Artifact Policy

- Fresh responses and judge notes remain under `tmp/eval-runs/issue-198-brd/pm/eval-006-nested-feature-path/` and are not committed.
