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
- target_skill_sha256: `4936716a99cef8bc1e927ef64eaa0d20fa85f573a00b76c6ef0e6212ccbb3af0`
- eval_definition_sha256: `971feaa0f85d14f75fe45df2640551915965f181de289e0a977efb57d2391e3e`
- metadata_sha256: `b384f8f560614179a0a93d18259ac2f4d1d78a8283a28bd2f5b6097f32a74e67`
- fixture_sha256: `5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `07345508cc5d326f024163cc8715111c4efeeb1bd80f16886d65b16eb2ef9292`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `77f74479311f236d7bdd232169db921b777009b1ba418244e6f3905f8b530b3e`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `41b45499ae9ca5616b92679964200469b31cddbc1797bbf9c8e3a1dc71be48a5`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `dependency_inventory` | PASS | 交付快照列出 Node.js 生产依赖 lodash@4.17.15 与 minimist@0.0.8，并说明对象路径、命令行参数、传递依赖和供应链风险来源。 |
| `risk_classification` | PASS | 报告区分原型污染、模板代码注入、ReDoS、过期版本及 lockfile/完整性缺失导致的供应链风险，并标注 Critical/High/Moderate、P0/P1 和影响条件。 |
| `evidence` | PASS | 报告引用 package.json、具体固定版本、CVE/GHSA 编号、受影响版本范围、修复版本和公开公告链接；同时明确缺少 lockfile 与源码调用点的证据边界。 |
| `upgrade_plan` | PASS | 报告提出将 lodash 升级至 4.18.0+、minimist 升级至 1.2.8 或移除，生成并提交 lockfile/SBOM，重新扫描和测试，并给出危险键拒绝、静态模板、输入限制、隔离和监控等短期缓解措施。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=77f74479311f236d7bdd232169db921b777009b1ba418244e6f3905f8b530b3e; fixture_sha256=5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa; output_sha256=dd7bb5a83769e1e3e2f07af06aa87df11d61ed4de2155e8d8d73bc80097a0339; snapshot_sha256=2b0a24d8ec50a6734839fc7c3b093b23972623c7f0ffe89c04fcc7c9a559eb9b
- Behavior: 完成了结构化依赖安全审计交付，识别两个直接生产依赖的多项风险，提供证据、严重度、影响、升级和缓解建议，并保留了证据边界。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=77f74479311f236d7bdd232169db921b777009b1ba418244e6f3905f8b530b3e; fixture_sha256=5d978f8d24e5dad96aba91cd89101e33e9f1a0bda647abfca6c8a768de860caa; output_sha256=dc9fe1be794fd62e50ae9f1df83cacae866356137554fef7ca2531c4f6d5a6bc; snapshot_sha256=55b108e9918c2c7a37a72620437c75eefd345c67f734b15a7e68a0b45e2db863
- Behavior: 提供了较简短的审计摘要和交付文件，覆盖主要依赖风险与升级方向，但细节和风险分类不如 with_skill 完整。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
