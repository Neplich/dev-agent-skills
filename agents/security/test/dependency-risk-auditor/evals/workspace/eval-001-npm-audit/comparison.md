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
- Identity schema: `2`
- target_skill_sha256: `0f253c18407bc188d3558e673dc587116dcb519a01d7ef15849f9e98e350e1c1`
- eval_definition_sha256: `971feaa0f85d14f75fe45df2640551915965f181de289e0a977efb57d2391e3e`
- metadata_sha256: `aee94fbc4f1b4c53f14bd2d88b010307b382e89dd9cc2398f8a45f7d41146704`
- fixture_sha256: `5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `07345508cc5d326f024163cc8715111c4efeeb1bd80f16886d65b16eb2ef9292`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `dependency_inventory` | PASS | 交付报告列出 Node.js 生态、lodash@4.17.15 与 minimist@0.0.8，并说明对象路径、模板、命令行参数、传递依赖和供应链可复现性风险。 |
| `risk_classification` | PASS | 报告区分了原型污染、代码注入、ReDoS、过期/维护滞后及 lockfile 缺失导致的供应链与可复现性风险，并标注 High/Medium、P0/P1 严重度与优先级。 |
| `evidence` | PASS | 报告直接引用 package.json 中的固定版本、漏洞编号、受影响范围、修复版本及 NVD/GitHub Advisory/Snyk/OSV/npm 证据链接。 |
| `upgrade_plan` | PASS | 报告给出升级目标、lockfile/npm ci、审计门禁、回归测试，以及输入校验、危险路径禁用、超时、资源隔离和低权限运行等缓解措施。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=77f74479311f236d7bdd232169db921b777009b1ba418244e6f3905f8b530b3e; fixture_sha256=5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa; output_sha256=8f1b533d1958a9a9730bb946efc10a0e332c6a3b35a745608106283cb06079ea; snapshot_sha256=1fd2b7942df7a8af5866a63c102ad341c158f6dfb5ce2fd315af8e7a76f1e8d1
- Behavior: 生成并交付了完整的依赖风险审计文件，覆盖清单、风险分类、证据、严重度和升级/缓解计划。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=77f74479311f236d7bdd232169db921b777009b1ba418244e6f3905f8b530b3e; fixture_sha256=5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa; output_sha256=93ed7632440f2265937cee8a52aa9c414f7e50e259176a4772a9cc80e89ef793; snapshot_sha256=cf1781c8162c815f517b8c505c3fcdaf0b1813c67f314d42746f2179b1ed1c62
- Behavior: 生成了基本合格的依赖风险审计报告，可作为 fresh baseline；with_skill 报告在风险覆盖和证据边界方面更完整。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
