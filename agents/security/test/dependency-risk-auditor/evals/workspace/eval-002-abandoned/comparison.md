# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-002-abandoned`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4ef6c6ec20f409ae50ba76d9496bdabb654cdb81289a7a2eacee1dc6b802832f` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-002-abandoned`.
- Fixture SHA-256: `4ef6c6ec20f409ae50ba76d9496bdabb654cdb81289a7a2eacee1dc6b802832f`
- Prompt SHA-256: `89079b812ce4ce066ef86759ed6c1d41f09649e1cedce1ebb540e93d141b1137`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0f253c18407bc188d3558e673dc587116dcb519a01d7ef15849f9e98e350e1c1`
- Skill overlay SHA-256: `0cc706a818794631f426534d787ec1444a803ce7555683ff49eb3015d8e3ce7c`
- Judge schema SHA-256: `07345508cc5d326f024163cc8715111c4efeeb1bd80f16886d65b16eb2ef9292`
- Eval definition SHA-256: `88dd9b929d53963534f872d5c6b43117be6b35cb41fa6b99bd7d05175018ade8`
- Metadata SHA-256: `6e01d4daa6b468e7c7a0ddfd1d17ad1116a727bf8d6709ea8ad0e5baec7fce48`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `dependency_inventory` | PASS | 报告识别了 Node.js 依赖生态中的 `request@2.88.2` 与 `node-uuid@1.4.8`，并关联网络请求链路、UUID 生成逻辑及维护风险。 |
| `risk_classification` | PASS | 报告区分了 deprecated/停止维护与未确认漏洞，分别给出 HIGH 风险及 P0/P1 优先级，并明确说明缺少 lockfile 导致无法确认 CVE。 |
| `evidence` | PASS | 报告引用了 `package.json` 中的具体版本、npm/上游维护声明、Node.js 文档，并记录 `npm audit` 因缺少 lockfile 返回 `ENOLOCK`。 |
| `upgrade_plan` | PASS | 报告建议迁移至内建 `fetch`、评估 `undici`、使用 `uuid` 或 `crypto.randomUUID()`，并包含 lockfile、兼容性测试、SSRF 防护和隔离措施。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=89079b812ce4ce066ef86759ed6c1d41f09649e1cedce1ebb540e93d141b1137; fixture_sha256=4ef6c6ec20f409ae50ba76d9496bdabb654cdb81289a7a2eacee1dc6b802832f; output_sha256=51c13ec0542575360ef2f2c3d5a82d1d4ee74d6d59f95d248e2d7257e1ec7461; snapshot_sha256=ae0e4bd273f272a48841a1522401e03db1281eb61cd5b786abc38a83a5935c7e
- Behavior: 完成结构化依赖风险审计，覆盖两个直接生产依赖、风险分类、证据与替换计划，且未修改依赖文件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=89079b812ce4ce066ef86759ed6c1d41f09649e1cedce1ebb540e93d141b1137; fixture_sha256=4ef6c6ec20f409ae50ba76d9496bdabb654cdb81289a7a2eacee1dc6b802832f; output_sha256=a2be26c21178bcdf0324aaaed280644f8c1c81688f2b37fd1930ac51ac14a229; snapshot_sha256=457308e8c050065affcbfbb1eccbc7b9aaed7659c39e5aaaeb7889d580a3e8f7
- Behavior: 同样完成了依赖审计并提供替换建议；作为比较基线，其结论更直接提出具体 CVE，但未影响 with_skill 断言判定。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
