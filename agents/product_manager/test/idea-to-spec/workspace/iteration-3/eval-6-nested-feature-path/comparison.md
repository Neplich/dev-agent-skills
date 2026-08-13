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
- target_skill_sha256: `34042e851466ff927567e09fc5777d952f1546cabc96fbe4de98617d27f5b1fb`
- eval_definition_sha256: `0d6c5b2207f916945e44c4152d1df1a5456bcf63eecb7a912ef1fe1811598afa`
- metadata_sha256: `4835f86af8c88f61556ab924715c5dc8125d2c5616e22976f405e64c105bc13a`
- fixture_sha256: `7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `4fbce5299edbfab7f3f9e314d3ad852d562878858c404b524820ab2f7613136e`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818`
- Repository HEAD: `c13c53a9b6e4cf18215450050bc9e7d0a810b73c`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `55d032569bbd4014a60103aafb1c0773a93ff9dbe0ea681c46297ebeef4a35b3`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `scan_existing_prds` | PASS | with_skill 输出列出并读取 Chat Interface、Messages、Message History PRD。 |
| `nested_feature_path` | PASS | with_skill 输出明确 `feature_path: chat-interface/messages/history/search`，并列出对应搜索 PRD 路径。 |
| `no_parallel_top_level` | PASS | with_skill 输出采用 `chat-interface/messages/history/search` 嵌套路径，并明确不重生成 Chat Interface 或 Messages PRD。 |
| `handoff_fields` | PASS | with_skill 的 `current_feature_identity` 明确包含 feature_path、feature、parent_feature、feature_level 和 feature_path_evidence。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818; fixture_sha256=7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7; output_sha256=ec260e65672e58db5d8bc32fb6e7dcf43b4006793542907672fcb474f6c1e31d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成只读文档扫描，识别历史搜索为 history 下的四级子功能，并提供完整 handoff 字段。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818; fixture_sha256=7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7; output_sha256=d2f3811f808eda33c00f6b168e516c5b9ccb961272d017fc32625569215b6e39; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别出正确的嵌套 PRD 路径并建议更新父级 PRD，但未提供结构化 handoff 字段。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
