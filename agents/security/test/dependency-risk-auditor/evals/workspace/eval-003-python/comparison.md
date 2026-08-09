# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-003-python`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-003-python`.
- Fixture SHA-256: `8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3`
- Prompt SHA-256: `109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0f253c18407bc188d3558e673dc587116dcb519a01d7ef15849f9e98e350e1c1`
- Skill overlay SHA-256: `0cc706a818794631f426534d787ec1444a803ce7555683ff49eb3015d8e3ce7c`
- Judge schema SHA-256: `07345508cc5d326f024163cc8715111c4efeeb1bd80f16886d65b16eb2ef9292`
- Eval definition SHA-256: `b851960b1dd4c6ab11f9c42f685034d6bd0e27ae3c26e4256af19942329ed614`
- Metadata SHA-256: `86d72efa91ee3890167dbac2135eac8aaff379e02491ea01e89a3595936d759c`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `dependency_inventory` | PASS | 报告直接识别 Python 生态及三个关键直接依赖：requests、urllib3、Jinja2，并覆盖 HTTP、TLS/连接和模板风险来源。 |
| `risk_classification` | PASS | 报告区分了高/中风险、条件性风险、ReDoS/XSS/凭据泄露/模板代码执行、维护线过期及供应链风险，并说明了严重度与触发条件。 |
| `evidence` | PASS | 报告引用了 requirements.txt 中三个精确固定版本，并提供多个 CVE/GHSA、NVD、PyPI 和上游公告链接作为证据。 |
| `upgrade_plan` | PASS | 报告给出统一升级目标、兼容性注意事项、回归验证重点及无法立即升级时的重定向、凭据清理、TLS、模板隔离和资源限制等临时缓解措施。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210; fixture_sha256=8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3; output_sha256=2d3d0ee3e2bd5c742592b13f697832a4f76881ad70ef2a2bae0a8e5c98065f1b; snapshot_sha256=f21f06af028ad00f4481d85d8a72c14c1b500b7684da2207903d1c89e2f868d9
- Behavior: 完成了结构化依赖安全审计，识别固定版本、分类风险、提供证据，并给出升级与临时缓解建议；交付了审计文件且未修改 requirements.txt。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210; fixture_sha256=8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3; output_sha256=67ba5bcabf707d1795df6c5ab7891fdd41d6ec5f288f9d249ac50e0681695874; snapshot_sha256=cf23b7945262be95ce66636b1d6a0425ab31d16c13c69bd5d5e7075d1cb766bc
- Behavior: 同样交付了审计文件并覆盖主要依赖、风险、证据和升级建议，但内容较精简，风险分类和证据范围较窄。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
