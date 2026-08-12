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
- Identity schema: `2`
- target_skill_sha256: `0f253c18407bc188d3558e673dc587116dcb519a01d7ef15849f9e98e350e1c1`
- eval_definition_sha256: `b851960b1dd4c6ab11f9c42f685034d6bd0e27ae3c26e4256af19942329ed614`
- metadata_sha256: `86d72efa91ee3890167dbac2135eac8aaff379e02491ea01e89a3595936d759c`
- fixture_sha256: `8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3`
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
| `dependency_inventory` | PASS | 报告及交付文件均识别 Python 依赖生态，并明确列出 requests==2.19.1、urllib3==1.23、Jinja2==2.10.1 及其 HTTP/TLS/模板风险来源。 |
| `risk_classification` | PASS | 交付文件区分了公开漏洞、TLS/凭据泄露、XSS、ReDoS、供应链/锁文件不足及过期固定版本，并标注 High/Medium/P0/P1 等严重度或优先级。 |
| `evidence` | PASS | 交付文件直接引用 requirements.txt、PM_HANDOFF.md、PRD.md 中的精确版本，并提供多个 CVE/GHSA 及官方公告链接作为风险证据。 |
| `upgrade_plan` | PASS | 交付文件给出了三项依赖的升级基线、兼容性验证要求、临时缓解措施、发布阻断条件和下游交接建议。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210; fixture_sha256=8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3; output_sha256=8ad148535c5802b36e4b960d98a79411492646c034e7c1df83b830ad9bcd5d98; snapshot_sha256=5df7e4d4da0ac9956fe0d2687a213d5ea7774b145256dec67d6ce34cadfefaeb
- Behavior: 完成结构化安全审计交付，覆盖依赖盘点、风险分级、证据和升级/缓解方案，并保持 requirements.txt 未修改。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210; fixture_sha256=8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3; output_sha256=b468a4dc25686ccecf0fee6f98df44572f2e2ae1b8d9ec317fbadd89e09bd1ec; snapshot_sha256=bc4219789ad6e6aba8b567ecf6f73650b92f01176d9b59495e200f2636dd7382
- Behavior: 提供了基本完整的依赖风险审计、版本证据、升级目标和临时缓解建议，作为 fresh baseline；其表现不影响 with_skill assertion verdicts。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
