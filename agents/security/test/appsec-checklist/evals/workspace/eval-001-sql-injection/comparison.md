# Eval Result: eval-001-sql-injection

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-001-sql-injection`
- Test case: SQL Injection Vulnerability
- Workspace: `workspace/eval-001-sql-injection`
- Natural user prompt:

> pm-agent 已完成入口分类并路由至 appsec-checklist；PM handoff packet 见 workspace `PM_HANDOFF.md`，已确认 feature_path 为 `user-search`。Review the security of this user search API endpoint.

- Expected artifact: Structured application security checklist with prioritized findings, affected surfaces, evidence, impact, and remediation guidance.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/appsec-checklist--eval-001-sql-injection/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `5a1ccb91721f3d503cb9163a80457c474d68b0ce57a95930c83942362f24cb1a`。
- Lane isolation: 先完成并销毁全部 `without_skill` 独立顶层临时目录，再创建任何 `with_skill` 目录；每条 lane 使用独立的顶层临时 workspace、`HOME` 与 `CODEX_HOME`，不存在可供另一条 candidate 读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt 与相同初始 fixture；仅 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 skill，`without_skill` 未安装任何目标 skill。
- Evidence isolation: 所有 candidate 会话结束并删除各自临时根后，才将内存中的最终 workspace 快照与 transcript 持久化到 runtime root；candidate transcript 泄漏扫描未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、judge/verdict 或 expected output/assertion 脚手架。
- Judge: candidate 全部结束后，由第三个独立、只读的 fresh Codex 会话依据当前 assertions、两条 candidate 输出、transcript 与最终 workspace 快照判定。

## Latest Result

- Behavior result: **PASS**（PASS 5 / FAIL 0 / NOT EXERCISED 0）
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Historical Contract Note

上一份 durable comparison 保留的是增强前 4 条断言结果，并因新增第 5 条报告落盘断言而标记为 `BLOCKED`。本轮使用当前 5 条断言重新生成`with_skill` 与 `without_skill`，未复用旧 baseline 或旧结论。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `security_findings`<br>识别与场景匹配的应用安全风险，例如注入、认证绕过或 XSS | PASS | 报告明确识别了 src/api/user-search.js:2-4 的 SQL 注入，以及输入/结果无界导致的资源耗尽风险，且与 user-search 场景匹配。 | PASS | Baseline 报告同样明确识别 SQL 注入、认证/授权验证风险、资源耗尽和用户枚举风险。 |
| `evidence_and_impact`<br>说明证据、受影响入口和业务或安全影响 | PASS | 逐项提供 file:line 证据，并说明越权读取、数据泄露、潜在数据破坏、数据库/API 资源耗尽等影响。 | PASS | 逐项提供 file:line 证据，并说明数据读取、数据库完整性/可用性、枚举和拒绝服务影响。 |
| `severity_rationale`<br>给出严重度并说明判断依据 | PASS | 报告将 SQL 注入定为 Critical、资源限制问题定为 Medium，并结合可利用性、数据机密性、完整性和可用性说明依据。 | PASS | Baseline 对 SQL 注入定为 Critical、认证风险定为条件性 High、资源耗尽和枚举定为 Medium，并给出依据。 |
| `remediation`<br>提供具体、可执行的修复建议或验证步骤 | PASS | 报告建议参数化 SQL、输入校验、结果上限/分页、超时、限流、最小权限，并列出针对注入和异常输入的回归验证步骤。 | PASS | Baseline 提供参数化查询、认证授权、边界控制、限流/超时和具体测试验证步骤。 |
| `writes_protocol_shaped_security_report`<br>报告按 SKILL.md 协议结构落盘（frontmatter + Executive Summary 分区） | PASS | 最终快照存在 docs/security/user-search/appsec-checklist.md；报告含 feature、feature_path、version、date、last_updated frontmatter，Executive Summary 含问题总数、风险分布和总体态势，并有逐问题位置、风险和修复建议；其他角色文档未被修改。 | FAIL | 最终快照虽存在目标报告，但缺少 SKILL.md 要求的 YAML frontmatter 和 Executive Summary 分区，不能满足协议结构要求。 |

## With-Skill Behavior

With-skill 明确识别 SQL 注入和资源耗尽风险，提供了证据、影响、严重度依据及可执行修复/验证建议，并按协议生成了报告。

## Fresh Without-Skill Baseline

Without-skill 也识别主要风险并生成报告，但报告缺少契约要求的 frontmatter 和 Executive Summary 结构。

## Failures

- 无。

## Not Exercised

- 实际路由注册层的认证/授权是否缺失，fixture 未提供路由或中间件，因此仅能作为发布前验证项。
- XSS、命令注入、密码/会话、依赖漏洞和生产配置等分支未被当前最小 fixture 实际触发。

## Next Steps

- 补充路由、中间件、数据库连接配置和依赖清单后，复核认证授权、最小权限、多语句配置和依赖风险。
- 修复 SQL 参数化及输入/结果边界后执行恶意输入、授权和资源耗尽回归测试。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` workspace 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
