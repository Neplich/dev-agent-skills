# Eval Result: eval-001-gdpr

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-001-gdpr`
- Test case: GDPR Compliance Check
- Workspace: `workspace/eval-001-gdpr`
- Natural user prompt:

> pm-agent has completed entry classification and routed this confirmed `data-collection` security scope to privacy-surface-mapper. Use the PM handoff packet in workspace `PM_HANDOFF.md` and the confirmed source document `docs/pm/data-collection/PRD.md`. Map the personal data collection and check GDPR compliance.

- Expected artifact: Structured privacy surface map that identifies personal data, processing purpose, third-party sharing, user-rights gaps, and compliance risks.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/privacy-surface-mapper--eval-001-gdpr/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `364f34fef102662b30171eb4eaf54d781e387c635f07b6d450fd6bf48dadfdb6`。
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
| `data_inventory`<br>识别个人数据类型、收集入口和处理目的 | PASS | 最终 privacy-map.md 明确列出姓名、邮箱、IP、User-Agent/设备信息、用户 ID 和行为事件，并以 registration.js、PRD 和 analytics.json 为证据，说明收集入口及账号创建、运营安全和产品分析目的。 | PASS | 最终 PRIVACY_SURFACE_REPORT.md 明确列出个人数据、入口、证据和处理目的。 |
| `sharing_and_retention`<br>识别第三方共享、存储或保留相关风险 | PASS | 报告明确识别 ExampleAnalytics 第三方共享、共享字段和未记录的 DPA/子处理者/地区/跨境传输信息，并指出 retentionDays=null 及数据库、日志保留期限未定义。 | PASS | 报告明确识别 ExampleAnalytics 共享、提供方治理/传输缺口及无界分析保留和其他保留期限缺失。 |
| `user_rights`<br>检查访问、删除、导出或同意等用户权利支持情况 | PASS | 报告逐项检查访问、删除、纠正、可携带/导出，并补充限制、反对和撤回同意；明确说明未发现对应 endpoint、workflow 或分析侧传播机制。 | PASS | 报告逐项评估访问、纠正、删除、限制、反对、可携带和同意撤回支持，并给出未实现/未证明结论。 |
| `compliance_gaps`<br>给出隐私合规缺口和改进建议 | PASS | 报告明确指出默认启用分析且无需同意、目的/法律依据缺失、数据最小化不足、保留未定义、第三方治理与跨境证据缺失、权利流程缺失，并给出按 Engineer、DevOps、Security/Privacy 分工的整改建议。 | PASS | 报告系统列出 GDPR 控制缺口并提供分角色、分优先级的整改建议。 |

## With-Skill Behavior

with-skill 正确读取 handoff、PRD、源码和分析配置，创建了要求路径下的 privacy-map.md，并完整覆盖数据清单、共享/保留、用户权利及合规缺口与建议。

## Fresh Without-Skill Baseline

without-skill 也创建了内容充分的隐私报告，四项 assertion 均有明确证据通过；其报告文件名不同于 skill 契约要求，但不影响本轮 assertion 内容核验。

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
