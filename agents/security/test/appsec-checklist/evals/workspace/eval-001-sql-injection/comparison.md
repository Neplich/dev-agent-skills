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
- target_skill_sha256: `812b371fc30792cb2b0cf8d96079b3244c95b93efab7638e085d4e955d6ea42c`
- eval_definition_sha256: `8fc30622b3de679ebf38da0b0fc7b8032d774fb8a425496383ba9ed0da1fdbb0`
- metadata_sha256: `c7304df99ba027e455b94ef86d8c2964c99813b4b7afb5bd532e0bf494b29d15`
- fixture_sha256: `ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `01ca86a4951823e3b6c703072ce5be09764c747ae9938b66975b80e4d41e39dd`
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
| `security_findings` | PASS | with_skill 报告识别了 SQL 注入，并以 req.query.name 直接进入 SQL 模板和 db.query 为证据。 |
| `evidence_and_impact` | PASS | 报告给出 src/api/user-search.js:2-4、受影响的已认证入口，以及数据越权、暴露、篡改风险和可用性影响。 |
| `severity_rationale` | PASS | 报告明确标为 Critical，并说明严重度依据及数据库驱动、权限等影响条件。 |
| `remediation` | PASS | 报告提供参数化查询、输入约束、LIKE 转义、最小权限和恶意输入回归测试等可执行建议。 |
| `writes_protocol_shaped_security_report` | PASS | 锁定 delivery_snapshot 中的文件包含完整 frontmatter（feature、feature_path、version、date 等）、Executive Summary、问题数量、风险分布、总体态势及逐问题位置、风险和修复建议；git 证据显示未修改其他文档。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28; fixture_sha256=ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6; output_sha256=3bb2ed6e2d200af56b04c6e4bb92d414ab143ce07ef5b6bdd1650860f08e72ea; snapshot_sha256=0fe28283de94c78c25c5530f04cd49363b137af36c390cea325e35f905a9a1b1
- Behavior: 完成安全审查并落盘符合协议的 user-search 应用安全报告。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bb6bd5dae7cb984c9a3912af15f420906d99ddbd232c9c6777c774fceb165a28; fixture_sha256=ede96965e7d44efbe6d4a7e610af20046168e4331047764663820caf76860ea6; output_sha256=70ade284fce141dd113a49fa8b9e5621de0c8d6ba16dd0ae5c176b8a0bf9a02d; snapshot_sha256=1bb36b1679473a6b63751c556edc5db493cff2010a81a00aacef08df0be08db0
- Behavior: 基线识别了 SQL 注入和宽泛查询/资源耗尽风险，并声称写入报告；仅作对比，不用于否定 with_skill 断言。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
