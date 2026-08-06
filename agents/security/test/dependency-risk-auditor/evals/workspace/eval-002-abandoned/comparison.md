# Eval Result: eval-002-abandoned

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-002-abandoned`
- Test case: Abandoned Packages
- Workspace: `workspace/eval-002-abandoned`
- Natural user prompt:

> pm-agent has completed entry classification and routed this confirmed `dependency-inventory` security scope to dependency-risk-auditor. Use the PM handoff packet in workspace `PM_HANDOFF.md` and the confirmed source document `docs/pm/dependency-inventory/PRD.md`. Check for abandoned or outdated dependencies.

- Expected artifact: Structured dependency risk audit that identifies vulnerable, outdated, or abandoned packages with severity, evidence, and upgrade or mitigation guidance.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/dependency-risk-auditor--eval-002-abandoned/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `78690f73cc6febd2097ea7892857fa979d64f69bbf14c879133bbbd07d659103`。
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
| `dependency_inventory`<br>识别依赖生态、关键包和风险来源 | PASS | 最终快照中的 docs/security/dependency-inventory/dependency-audit.md 明确识别 package.json 中的 2 个生产依赖：request@2.88.2 与 node-uuid@1.4.8，并说明无 lockfile。 | PASS | AUDIT.md 明确盘点同样的两个直接生产依赖及缺失 lockfile。 |
| `risk_classification`<br>区分漏洞、废弃、过期或供应链风险并说明严重度 | PASS | 报告区分并分级了废弃/维护风险、供应链与传递依赖限制，并明确“Confirmed vulnerabilities: 0”及无法确认 exploitability；request 为 High，node-uuid 为 Medium。 | PASS | AUDIT.md 区分 abandoned/deprecated、public security report、direct vulnerability 未确立及 transitive 风险未评估，并给出 P0/P1 优先级。 |
| `evidence`<br>引用依赖文件、版本或已知风险作为证据 | PASS | 报告引用 package.json 中的具体包名和版本，并提供 npm/GitHub 维护状态证据；transitive 结论有 ENOLOCK 和无 runtime/tree 的明确依据。 | PASS | AUDIT.md 引用 package.json:6/7、具体版本、npm 页面及上游 SSRF 报告。 |
| `upgrade_plan`<br>给出升级、替换或缓解建议 | PASS | 报告给出按 P0/P1/P2 排序的替换计划：request 迁移至 fetch/undici，node-uuid 迁移至 crypto.randomUUID()/uuid，并包含测试、SSRF 控制、lockfile 和发布门禁建议。 | PASS | AUDIT.md 给出 request 和 node-uuid 的替换、隔离、测试及 lockfile/audit 后续计划。 |

## With-Skill Behavior

with-skill 正确读取 handoff/PRD，盘点 2 个直接依赖，创建了符合要求的 dependency-audit.md；明确记录 npm audit 的 ENOLOCK 限制，并分类废弃、供应链/传递依赖风险及严重度。

## Fresh Without-Skill Baseline

without-skill 也创建了 AUDIT.md，覆盖同一依赖盘点、风险证据与替换建议；作为 baseline，各 assertion 均满足。

## Failures

- 无。

## Not Exercised

- 没有 lockfile 或 node_modules，因此具体传递依赖、树深度和可验证 CVE 修复版本路径未被客观触发；报告已诚实标注 ENOLOCK 限制。
- 未触发需要实际确认具体漏洞的分支；当前 fixture 的主要触发条件是废弃/过时依赖。

## Next Steps

- 无。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` workspace 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
