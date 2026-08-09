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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c0da2e0366232678672d0c64ce9fa764d3b78f3caaaa8493348af1a7e1cd00fe`
- Skill overlay SHA-256: `8f09b52303d9393824dd3e732e656dd74f7ac606a082939547181274986dfb2d`
- Judge schema SHA-256: `4fbce5299edbfab7f3f9e314d3ad852d562878858c404b524820ab2f7613136e`
- Eval definition SHA-256: `0d6c5b2207f916945e44c4152d1df1a5456bcf63eecb7a912ef1fe1811598afa`
- Metadata SHA-256: `4835f86af8c88f61556ab924715c5dc8125d2c5616e22976f405e64c105bc13a`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `scan_existing_prds` | PASS | with_skill 输出提到读取现有 history PRD，并引用 docs/pm/chat-interface/messages/history/PRD.md。 |
| `nested_feature_path` | PASS | with_skill 的 current_feature_identity 明确给出 feature_path: chat-interface/messages/history/search。 |
| `no_parallel_top_level` | PASS | with_skill 明确建议不创建新的顶层 chat-interface 或 message-history PRD，并将搜索归入 history 子功能路径。 |
| `handoff_fields` | FAIL | handoff 中包含 feature_path、feature、parent_feature、feature_level，但使用 evidence 字段而非要求的 feature_path_evidence 字段。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818; fixture_sha256=7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7; output_sha256=2c3864e0cae091619f20c98421e7a902c2876d902eb5eea15bb81f3f731a889d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别并规划了嵌套的消息历史搜索功能，但 handoff 字段不完整。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818; fixture_sha256=7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7; output_sha256=2084d074434cad53a3ba3be399863b1ea46a3604f2ec16955a261eab8ddc5dea; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确建议使用嵌套 PRD 路径并避免顶层搜索文档，但未提供结构化 handoff 字段。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill handoff packet 缺少明确的 feature_path_evidence 字段。
- Next: 补充 feature_path_evidence 字段，并保留现有嵌套 feature_path。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
