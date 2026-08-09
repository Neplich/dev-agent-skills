# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-001-npm-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-001-npm-audit`.
- Fixture SHA-256: `5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa`
- Prompt SHA-256: `77f74479311f236d7bdd232169db921b777009b1ba418244e6f3905f8b530b3e`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0f253c18407bc188d3558e673dc587116dcb519a01d7ef15849f9e98e350e1c1`
- Skill overlay SHA-256: `0cc706a818794631f426534d787ec1444a803ce7555683ff49eb3015d8e3ce7c`
- Judge schema SHA-256: `07345508cc5d326f024163cc8715111c4efeeb1bd80f16886d65b16eb2ef9292`
- Eval definition SHA-256: `971feaa0f85d14f75fe45df2640551915965f181de289e0a977efb57d2391e3e`
- Metadata SHA-256: `aee94fbc4f1b4c53f14bd2d88b010307b382e89dd9cc2398f8a45f7d41146704`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `dependency_inventory` | PASS | 报告直接列出 Node.js 生产依赖 lodash@4.17.15 与 minimist@0.0.8，并说明对象路径、模板和命令行参数风险来源。 |
| `risk_classification` | PASS | 报告区分了 Critical/High/Moderate 漏洞、维护活跃度观察项及无 lockfile 导致的供应链可复现性缺口，并为风险标注严重度和优先级。 |
| `evidence` | PASS | 报告引用 PM_HANDOFF.md、PRD.md、package.json、具体版本、CVE/GHSA 编号、CVSS 分数及 NVD/GitHub/npm 链接作为证据。 |
| `upgrade_plan` | PASS | 报告给出了 minimist 与 lodash 的明确升级目标、lockfile 与扫描计划、回归测试、CI 门禁及对象路径/模板/参数解析缓解措施。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=77f74479311f236d7bdd232169db921b777009b1ba418244e6f3905f8b530b3e; fixture_sha256=5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa; output_sha256=b6992fa77a640dd9ca0b5ff58378c73f96aab32033a060f65566d75bd0ebcb43; snapshot_sha256=e9e565b952dc9fef8d97275e2acb8935f544e0af73efdef5b7dbfec3b5773e3e
- Behavior: 完成并交付结构化依赖风险审计，覆盖清单、风险分类、证据和升级/缓解计划。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=77f74479311f236d7bdd232169db921b777009b1ba418244e6f3905f8b530b3e; fixture_sha256=5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa; output_sha256=15a06609c852b4645c7e6f36cb9409cef3f5f1377eb715f1188b5878d9cdc87c; snapshot_sha256=d1bcc6a5bb5f50ca397b2eaa5242a0941ec9b54a944ecfac66d6d6ff5b58cd19
- Behavior: 同样交付了依赖风险审计并识别主要包与漏洞；作为 fresh baseline，报告内容较简略且升级与风险覆盖不如 with_skill 完整。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
