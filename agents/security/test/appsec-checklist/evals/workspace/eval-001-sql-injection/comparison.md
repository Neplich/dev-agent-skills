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
- target_skill_sha256: `412a68c0dfdb2d720e3447fdc4faf74b408d3de29706093a3a69fb0ca69d983c`
- eval_definition_sha256: `8fc30622b3de679ebf38da0b0fc7b8032d774fb8a425496383ba9ed0da1fdbb0`
- metadata_sha256: `c35665f3cf1a3d670f1f84679f59821ede559ff2507cf10a314ee5a06060b2f7`
- fixture_sha256: `ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `01ca86a4951823e3b6c703072ce5be09764c747ae9938b66975b80e4d41e39dd`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `035cdf3596c1888564523ed3d4e73116a3d2b231b30d91c462fb62cf6da52e05`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `security_findings` | PASS | with_skill 报告识别了 `src/api/user-search.js:2-4` 中将 `req.query.name` 拼接进 SQL 的 SQL 注入风险，并指出通配符和输入规模导致的资源消耗风险。 |
| `evidence_and_impact` | PASS | 报告直接引用了参数读取、SQL 拼接和 `db.query` 调用位置，说明了认证用户可造成越权读取、查询语义改变、数据库完整性风险及可用性影响。 |
| `severity_rationale` | PASS | 报告按 Critical/Medium 分级，并分别依据可控 SQL 语法、数据机密性/完整性影响和资源消耗风险说明判断依据。 |
| `remediation` | PASS | 报告提供了参数化查询、类型与长度校验、LIKE 转义、结果限制、超时、限流、最小权限和恶意输入回归测试等可执行建议。 |
| `writes_protocol_shaped_security_report` | PASS | delivery_snapshot 中的 `docs/security/user-search/appsec-checklist.md` 含完整 frontmatter（feature、feature_path、version、date 等）、Executive Summary、风险分布和逐问题的 file:line、风险影响与修复建议；git_status 显示仅新增安全报告。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28; fixture_sha256=ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6; output_sha256=72070e380ec2c9cf67a8eee589ec38cd18872b139d806d311e2bb0ff99adaac7; snapshot_sha256=3e779f8a22bf3a50d2445ef464cba41925570894873b7d6ca6991b5221bf22fc
- Behavior: 完成安全审查并落盘协议化安全报告，识别 SQL 注入及查询资源消耗风险，提供证据、分级和修复建议。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28; fixture_sha256=ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6; output_sha256=48c526f6bf086850e8fb8180f3317e38539c3ea44b61bbf0daf3d56659742268; snapshot_sha256=d51433a6eeff6c34f27639f8fe083fee68da437c617d13afaf82c0365c2d321a
- Behavior: 完成了基本安全发现和建议并生成报告，但交付文件缺少协议要求的 frontmatter 和 Executive Summary 结构。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
