# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-001-sql-injection`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6` from `agents/security/test/appsec-checklist/evals/workspace/eval-001-sql-injection`.
- Identity schema: `2`
- target_skill_sha256: `9ac7059a9a39550256d4de1ed82086d7f6b3c81bd069d831f0bf87ce02417c58`
- eval_definition_sha256: `8fc30622b3de679ebf38da0b0fc7b8032d774fb8a425496383ba9ed0da1fdbb0`
- metadata_sha256: `c35665f3cf1a3d670f1f84679f59821ede559ff2507cf10a314ee5a06060b2f7`
- fixture_sha256: `ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `01ca86a4951823e3b6c703072ce5be09764c747ae9938b66975b80e4d41e39dd`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `d316d6849a82751d5c66c424af9993a42c304fe892fdb2411469b461bec624ee`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `security_findings` | PASS | 报告明确识别 SQL 注入：`req.query.name` 被直接插入 SQL 模板字符串并执行，且讨论了通配符和资源消耗风险。 |
| `evidence_and_impact` | PASS | 报告引用 `src/api/user-search.js:2-4`，说明了请求参数到数据库查询的路径，并描述了已认证用户目录越权读取、错误和潜在资源影响。 |
| `severity_rationale` | PASS | 报告将 SQL 注入分为 Critical，并以攻击前置条件低、可扩大数据读取及潜在完整性/可用性影响作为依据，同时区分了未经驱动证据确认的多语句风险。 |
| `remediation` | PASS | 报告提供参数化查询示例、输入校验、LIKE 转义、最小权限、错误处理以及恶意输入回归验证步骤。 |
| `writes_protocol_shaped_security_report` | PASS | 锁定交付文件包含要求的 frontmatter 字段、Executive Summary（问题总数、风险等级分布、总体态势）及逐问题的位置、风险解释和修复建议；git 证据显示仅新增安全报告文件。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28; fixture_sha256=ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6; output_sha256=ef5563cc9c9fdd4890a9b0b69f0082616c3f58d58027433658a3eaca6f4fe186; snapshot_sha256=4208dfaec394bdc4dc3b40e73a2473a205c767ff24aeae4349ccb5fb9182d500
- Behavior: 完成安全审查并落盘协议化报告，涵盖 SQL 注入证据、影响、Critical 分级、修复与验证建议。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28; fixture_sha256=ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6; output_sha256=65b48903c59bcd939f7f96523092476721d7dc411ab237753ab5b117dace673e; snapshot_sha256=e9387ebf4ab0b5b9ea3ef3e41ea24486ca5f5d60872023ac09da3484a7f7ca22
- Behavior: 识别了 SQL 注入及通配符/资源风险并声称生成报告，但其锁定报告缺少协议要求的 frontmatter 和 Executive Summary 结构。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
