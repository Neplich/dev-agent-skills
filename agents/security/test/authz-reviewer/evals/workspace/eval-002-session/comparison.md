# Eval Result: eval-002-session

## Evaluation Target

- Agent: `security`
- Skill: `authz-reviewer`
- Eval: `eval-002-session`
- Test case: Session Management
- Workspace: `workspace/eval-002-session`
- Natural user prompt:

> Check the session management security, using the confirmed PRD and code as evidence.

- Expected artifact: Structured authorization review that identifies access-control risks, affected roles or resources, evidence, severity, and remediation guidance.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/authz-reviewer--eval-002-session/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `63b039d9c786dd32ac2a298722e0ce7cb53b7adcb57752d6375b08aac458cf6b`。
- Lane isolation: 先完成并销毁全部 `without_skill` 独立顶层临时目录，再创建任何 `with_skill` 目录；每条 lane 使用独立的顶层临时 workspace、`HOME` 与 `CODEX_HOME`，不存在可供另一条 candidate 读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt 与相同初始 fixture；仅 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 skill，`without_skill` 未安装任何目标 skill。
- Evidence isolation: 所有 candidate 会话结束并删除各自临时根后，才将内存中的最终 workspace 快照与 transcript 持久化到 runtime root；candidate transcript 泄漏扫描未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、judge/verdict 或 expected output/assertion 脚手架。
- Judge: candidate 全部结束后，由第三个独立、只读的 fresh Codex 会话依据当前 assertions、两条 candidate 输出、transcript 与最终 workspace 快照判定。

## Latest Result

- Behavior result: **PASS**（PASS 4 / FAIL 0 / NOT EXERCISED 0）
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Historical Contract Note

上一份 durable comparison 基于 issue #234 修复前会向 baseline 泄漏规则的旧契约，因此标记为 `BLOCKED`。本轮使用当前无泄漏 prompt/fixture 重新生成两条 lane，未复用旧 baseline 或旧结论。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `authorization_model`<br>识别角色、资源、权限边界和关键授权路径 | PASS | 最终快照中的 authz-review.md 含角色/权限矩阵、资源边界及 login→createSession→getSession→logout 授权路径。 | PASS | baseline 报告同样包含角色矩阵、资源边界和会话授权流程图。 |
| `access_control_findings`<br>指出越权、会话、JWT 或权限检查缺陷 | PASS | 报告明确指出可预测会话 ID、无 30 分钟空闲过期、退出不撤销服务端会话，并说明无法验证的 Cookie/轮换/受保护路由控制。 | PASS | baseline 报告明确指出相同的会话、过期和退出失效缺陷，并标注集成控制的证据缺口。 |
| `evidence_and_impact`<br>说明证据、影响范围和风险后果 | PASS | 每项主要发现均给出 session-store.js 定位证据、违反 PRD 的对应关系、会话劫持/账户接管或持续访问影响。 | PASS | baseline 报告提供了代码位置、PRD 对照及影响范围和风险后果。 |
| `remediation`<br>提供可执行的授权修复和回归验证建议 | PASS | 最终报告给出 CSPRNG token、服务端空闲过期、撤销/删除、Cookie 与集成补证建议，并列出具体回归验证场景。 | PASS | baseline 报告同样提供了可执行修复和回归测试建议。 |

## With-Skill Behavior

With-skill 明确识别角色、资源、会话信任边界和授权路径；报告包含可定位证据、影响、严重度、修复及回归建议。

## Fresh Without-Skill Baseline

Without-skill 也完成了合格的会话审查报告，作为 baseline 各项 assertions 均满足。

## Failures

- 无。

## Not Exercised

- fixture 未提供登录处理器、Cookie 设置/解析、受保护端点或会话中间件，因此登录轮换、安全 Cookie 属性、匿名拒绝和端点级授权覆盖只能标记为不可验证，未形成可直接核验的实现分支。

## Next Steps

- 如需 FULL coverage，应补充登录、Cookie、会话解析和受保护端点实现后复审。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` workspace 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
