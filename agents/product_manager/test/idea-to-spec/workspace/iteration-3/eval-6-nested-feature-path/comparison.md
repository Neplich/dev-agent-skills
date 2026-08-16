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
- Identity schema: `2`
- target_skill_sha256: `62f7a88900be8a0aae1af9e34b28dc32abd76006ca95f89107567b68f5780813`
- eval_definition_sha256: `0d6c5b2207f916945e44c4152d1df1a5456bcf63eecb7a912ef1fe1811598afa`
- metadata_sha256: `4835f86af8c88f61556ab924715c5dc8125d2c5616e22976f405e64c105bc13a`
- fixture_sha256: `7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `4fbce5299edbfab7f3f9e314d3ad852d562878858c404b524820ab2f7613136e`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `7b19869a4835a1feeb491815cac7af7bde071247819525989c10dbfbc0acd2f7`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `scan_existing_prds` | PASS | With_skill output lists the three existing PRDs, including Chat Interface, Message History, and the nested history PRD. |
| `nested_feature_path` | PASS | With_skill output explicitly specifies feature_path `chat-interface/messages/history/search` and the corresponding nested PRD path. |
| `no_parallel_top_level` | PASS | With_skill recommends the nested history/search path and explicitly advises against updating the top-level Chat Interface or Messages PRDs. |
| `handoff_fields` | FAIL | The output includes feature_path, feature, parent_feature, and feature_level, but does not provide a handoff packet or feature_path_evidence field. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818; fixture_sha256=7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7; output_sha256=7aabb4b1c64807c9a17656bd454118364fe31641704ef43f8a91be327de2c6be; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly scans existing PRDs and identifies the nested history/search child path while preserving the parent-child structure; handoff metadata is incomplete.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818; fixture_sha256=7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7; output_sha256=6e0d891dc5df7dd87015aa4b9e86643824f6b1387e9828ae28b9b723975432f7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also identifies the existing PRDs and correct nested search path, but provides no handoff packet fields.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane omits the required handoff packet field `feature_path_evidence` and does not present the required fields as a handoff packet.
- Next: Add a handoff packet containing feature_path, feature, parent_feature, feature_level, and feature_path_evidence.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
