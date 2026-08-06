# Eval Result: eval-003-python

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-003-python`
- Test case: Python Dependency Audit
- Workspace: `workspace/eval-003-python`
- Natural user prompt:

> pm-agent has completed entry classification and routed this confirmed `dependency-inventory` security scope to dependency-risk-auditor. Use the PM handoff packet in workspace `PM_HANDOFF.md` and the confirmed source document `docs/pm/dependency-inventory/PRD.md`. Review Python dependencies for security issues.

- Expected artifact: Structured dependency risk audit that identifies vulnerable, outdated, or abandoned packages with severity, evidence, and upgrade or mitigation guidance.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/dependency-risk-auditor--eval-003-python/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `6e2bb4aec3b87f9503c5fc46324b2258d9ef732b80318b6d5c0ebb7bb9b3f56c`。
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
| `dependency_inventory`<br>识别依赖生态、关键包和风险来源 | PASS | 报告明确识别 Python 生态，并列出 requests==2.19.1、urllib3==1.23、Jinja2==2.10.1 及其 HTTP、TLS、模板相关风险。 | PASS | 报告列出三项 Python 直接依赖及对应 HTTP、TLS、模板风险。 |
| `risk_classification`<br>区分漏洞、废弃、过期或供应链风险并说明严重度 | PASS | 报告区分漏洞、过期/不受支持版本和供应链/补丁滞后风险，并按 Critical、High、Medium 说明严重度及可利用条件。 | PASS | 报告区分已知漏洞、不受支持版本和模板风险，并给出 High/Medium 严重度与利用条件。 |
| `evidence`<br>引用依赖文件、版本或已知风险作为证据 | PASS | 报告引用 requirements.txt 中的精确版本和行号，并提供多个 CVE/GHSA 及外部 advisory 链接作为证据。 | PASS | 报告引用 requirements.txt:1-3、精确版本及多个 CVE/GHSA advisory。 |
| `upgrade_plan`<br>给出升级、替换或缓解建议 | PASS | 报告给出协调升级到 requests 2.34.2、urllib3 2.7.0、Jinja2 3.1.6+ 的优先级、测试要求、CI 审计和升级延迟时的临时缓解措施。 | PASS | 报告给出替换全部 pin、协调升级、DevOps 临时控制和 lockfile/SBOM 后续计划。 |

## With-Skill Behavior

With-skill 明确读取 handoff、PRD 和 requirements.txt，创建了符合契约的 dependency-audit.md，包含三项依赖、版本证据、漏洞/过期分类、严重度、CVE、限制条件及升级和缓解建议。

## Fresh Without-Skill Baseline

Without-skill 也完成了依赖审计并创建报告，作为 baseline 各项断言均满足。

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
