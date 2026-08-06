# Eval Result: eval-002-auth-bypass

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-002-auth-bypass`
- Test case: Authentication Bypass
- Workspace: `workspace/eval-002-auth-bypass`
- Natural user prompt:

> pm-agent 已完成入口分类并路由至 appsec-checklist；PM handoff packet 见 workspace `PM_HANDOFF.md`，已确认 feature_path 为 `admin-panel`。Check the security of the admin panel endpoints.

- Expected artifact: Structured application security checklist with prioritized findings, affected surfaces, evidence, impact, and remediation guidance.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/appsec-checklist--eval-002-auth-bypass/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `4e2f14d2f4bf211c8ca064c64c9476345be10dd018d19d9f0a22c12ebb8c06ba`。
- Lane isolation: 先完成并销毁全部 `without_skill` 独立顶层临时目录，再创建任何 `with_skill` 目录；每条 lane 使用独立的顶层临时 workspace、`HOME` 与 `CODEX_HOME`，不存在可供另一条 candidate 读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt 与相同初始 fixture；仅 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 skill，`without_skill` 未安装任何目标 skill。
- Evidence isolation: 所有 candidate 会话结束并删除各自临时根后，才将内存中的最终 workspace 快照与 transcript 持久化到 runtime root；candidate transcript 泄漏扫描未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、judge/verdict 或 expected output/assertion 脚手架。
- Judge: candidate 全部结束后，由第三个独立、只读的 fresh Codex 会话依据当前 assertions、两条 candidate 输出、transcript 与最终 workspace 快照判定。

## Latest Result

- Behavior result: **PASS**（PASS 4 / FAIL 0 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: PASS

## Historical Contract Note

上一份 durable comparison 基于 issue #234 修复前会向 baseline 泄漏规则的旧契约，因此标记为 `BLOCKED`。本轮使用当前无泄漏 prompt/fixture 重新生成两条 lane，未复用旧 baseline 或旧结论。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `security_findings`<br>识别与场景匹配的应用安全风险，例如注入、认证绕过或 XSS | PASS | 最终快照中的 docs/security/admin-panel/appsec-checklist.md 明确识别 /admin/users 路由缺少认证和 admin 角色授权，且与 admin-panel 场景匹配。 | PASS | 最终快照报告同样识别了 /admin/users 的认证与授权缺失风险。 |
| `evidence_and_impact`<br>说明证据、受影响入口和业务或安全影响 | PASS | 报告定位 src/api/admin-routes.js:6，引用具体路由代码，并说明匿名/普通用户可能读取用户账号资料及管理数据的影响。 | PASS | 报告提供 src/api/admin-routes.js:4-6 的具体证据，并说明未授权披露及潜在越权影响。 |
| `severity_rationale`<br>给出严重度并说明判断依据 | PASS | 报告将问题评为 High，并依据管理端点、用户账号资料、缺失认证授权和当前缺失装配代码的限制说明严重度判断。 | PASS | 报告将问题评为 High，并解释了敏感管理数据、认证绕过和授权绕过带来的影响。 |
| `remediation`<br>提供具体、可执行的修复建议或验证步骤 | PASS | 报告给出 requireSession 与 requireRole("admin") 的具体路由修复示例，并要求验证匿名 401、普通用户 403、管理员成功及处理器未被提前调用。 | PASS | 报告提供了具体中间件修复方式，以及匿名、普通用户和管理员三类请求的验证步骤。 |

## With-Skill Behavior

with-skill 已基于 handoff、PRD 和可见路由代码识别高风险认证/授权缺失，生成了要求路径下的完整安全报告，包含证据、影响、严重度依据及修复/验证建议。

## Fresh Without-Skill Baseline

without-skill 同样生成了满足四项 assertion 的安全报告；作为 baseline，其结果与 with-skill 基本一致。

## Failures

- 无。

## Not Exercised

- 无。

## Next Steps

- 无。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` workspace 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
