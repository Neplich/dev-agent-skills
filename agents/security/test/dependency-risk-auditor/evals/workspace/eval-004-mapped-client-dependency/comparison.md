# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-004-mapped-client-dependency`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-004-mapped-client-dependency`.
- Fixture SHA-256: `9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5`
- Prompt SHA-256: `7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0f253c18407bc188d3558e673dc587116dcb519a01d7ef15849f9e98e350e1c1`
- Skill overlay SHA-256: `0cc706a818794631f426534d787ec1444a803ce7555683ff49eb3015d8e3ce7c`
- Judge schema SHA-256: `fe1f59786edfa4e3b7ee12601522d693ef12a42cdfce9b4a390ad6d7b95d03d2`
- Eval definition SHA-256: `8b3afd523591d93b0ae2bfbea1c5709666ee81c09a14160679da5b53064efb14`
- Metadata SHA-256: `72846a754080f41b7de9981348b71040115d4704d0a16f2aad7aa4b526a44443`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 候选输出明确列出命中 change-map、required_docs 和相关文档；但锁定证据无法证明实际读取顺序。 |
| `verifies_against_code` | PASS | 明确核对清单实际为 network-client@1.4.0、文档声称为 2.1.0，并以清单事实为依据。 |
| `treats_unverified_as_low_trust` | PASS | 明确识别两份文档的 last_verified_version 为 unverified，并将其作为低信任导航而非直接采信。 |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | 候选输出将请求退回 pm-agent 分类并补齐交接；由于缺少 PM/Security handoff packet，后续创建 issue 和产出升级证据尚不能执行。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994; fixture_sha256=9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5; output_sha256=ba14685392e63edc4da87fd7132e0029dd0b7daceed6b2f674d7f82e74c39d62; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别映射文档、实际依赖版本及 unverified 状态，并在缺少交接上下文时暂停审计、回交 pm-agent。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994; fixture_sha256=9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5; output_sha256=ff3c9ef3ca9f21f3365267821b5fd18c13dd1ed8c4f9ee4c79b2c0b481617df6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成了版本漂移分析并给出风险及缓解建议，作为 fresh baseline 对照。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 由 pm-agent 提供确认的安全审计 handoff packet 后，再执行后续风险结论升级及 issue 创建。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
