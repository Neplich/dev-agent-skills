# Eval Result: eval-001-sql-injection

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-001-sql-injection`
- Test case: SQL Injection Vulnerability
- Workspace: `workspace/eval-001-sql-injection`
- Review context: issue #143 thin fixture 补齐后的 Fresh Codex 复验
- Latest result: PASS（4/4 assertions）- fresh Codex paired validation completed on 2026-07-21

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt/fixture: issue #143 当前 fixture；包含 `PM_HANDOFF.md`、`docs/pm/user-search/PRD.md` 与 `src/api/user-search.js`
- Fresh run: 当前会话中新启动的 fresh Codex validator 在 `tmp/eval-runs/issue-143/batch-a` 建立隔离副本；with_skill 读取当前 `appsec-checklist` 与 Security Agent README，without_skill 对同 prompt/fixture 不读取或应用 skill/Agent README，并于本轮重新生成 baseline，未读取历史 comparison、未复用历史 baseline
- Source head: `test/issue-143-security-thin-fixtures` (`d70a8c4`)
- Validation date: 2026-07-21

## Assertions

- PASS `security_findings`：识别 `src/api/user-search.js:3-4` 中查询参数直接插入原始 SQL 的可利用 SQL 注入
- PASS `evidence_and_impact`：定位 source-to-sink 路径，并说明越权读取用户目录及潜在完整性、可用性影响
- PASS `severity_rationale`：按直接可利用路径和 skill 分级规则判为 Critical
- PASS `remediation`：给出参数化 `LIKE` 查询、通配符语义约束及恶意输入回归验证步骤

## With Skill Behavior

Fresh candidate 通过 PM handoff gate 后按 `feature_path=user-search` 精准读取 PRD 与代码。报告以 Critical finding 形式给出 `req.query.name` 到 SQL 执行的代码位置、示例攻击语义、资产影响和参数化修复，并补充 quote/comment/boolean/wildcard/畸形输入验证；同时遵守只审查不改代码、结论回 PM 分类且修复交 Engineer 的边界。

## Without Skill Baseline

本轮 fresh baseline 仅使用同一 prompt 与 fixture 重新生成，未读取 skill、Security Agent README 或历史 comparison。Baseline 同样识别 SQL 注入、Critical 严重度、影响和参数化修复，满足 4/4 assertions；但输出更像单项漏洞答复，未形成完整 checklist，也未体现 Security→PM closeout 与角色交付边界。

## Failures

- 无 assertion failure。
- 未发现基础设施阻塞；issue #143 补齐的 handoff、PRD 与代码 fixture 已解除旧版入口阻塞。

## Next Steps

- 当前 eval 无需修正；后续 skill 或 fixture 行为变更时，继续执行同 prompt 的 fresh Codex paired run，并重新生成 without_skill baseline。

## Runtime Artifacts Policy

- 本轮隔离副本、candidate/baseline 证据与临时输出仅位于 `tmp/eval-runs/issue-143/batch-a`，验证后删除，不提交到 git。
- Runtime transcripts、verdicts、timing、diagnostics、lockfile 及 with_skill / without_skill 目录均不得提交；durable 结果仅为本 `comparison.md`。
