# Eval Result: eval-005-mapped-search-security

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-005-mapped-search-security`
- Test case: Mapped Search Security Documentation
- Workspace: `workspace/eval-005-mapped-search-security`
- Natural user prompt:

> 请审查 src/api/search-handler.js 的用户搜索安全性，重点检查查询参数如何进入数据查询，并给出证据、影响和修复建议。

- Expected artifact: 优先读取 change-map 命中的搜索 API 文档，再以代码核对查询构造；将 unverified 文档按最低信任处理并报告参数化声明与代码插值事实的不一致。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/appsec-checklist--eval-005-mapped-search-security/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `246474747e13b38824929dd18bb0b6743805302db0f636f44fbd4479602b83cc`。
- Lane isolation: 先完成并销毁全部 `without_skill` 独立顶层临时目录，再创建任何 `with_skill` 目录；每条 lane 使用独立的顶层临时 workspace、`HOME` 与 `CODEX_HOME`，不存在可供另一条 candidate 读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt 与相同初始 fixture；仅 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 skill，`without_skill` 未安装任何目标 skill。
- Evidence isolation: 所有 candidate 会话结束并删除各自临时根后，才将内存中的最终 workspace 快照与 transcript 持久化到 runtime root；candidate transcript 泄漏扫描未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、judge/verdict 或 expected output/assertion 脚手架。
- Judge: candidate 全部结束后，由第三个独立、只读的 fresh Codex 会话依据当前 assertions、两条 candidate 输出、transcript 与最终 workspace 快照判定。

## Latest Result

- Behavior result: **FAIL**（PASS 2 / FAIL 2 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: FAIL

## Historical Contract Note

上一份 durable comparison 基于 issue #234 修复前会向 baseline 泄漏规则的旧契约，因此标记为 `BLOCKED`。本轮使用当前无泄漏 prompt/fixture 重新生成两条 lane，未复用旧 baseline 或旧结论。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `reads_mapped_docs_first`<br>命中 change-map 后优先读取搜索 API required_docs | FAIL | transcript 显示先读取目标代码（item_3），随后在同一命令中先读 user-search.md、再读 change-map.yaml（item_5）；未按 change-map 反查后优先读取 required_docs。 | FAIL | transcript 未读取 change-map 后按 required_docs 顺序探索；先读代码，之后同一命令先读 API 文档再读 change-map。 |
| `verifies_against_code`<br>以处理器代码核对查询参数安全声明 | PASS | 候选结论明确引用 src/api/search-handler.js:1-2 的模板字符串直接插入 query，并指出其与文档所称参数化查询不一致。 | PASS | 候选结论明确核对 src/api/search-handler.js:2 的直接插值，并给出可形成恒真条件的输入示例。 |
| `treats_unverified_as_low_trust`<br>将 unverified 搜索文档按最低信任处理 | PASS | transcript 读取了文档的 last_verified_version: unverified；最终结论以代码事实为依据，未采信参数化声明，并扩大说明调用方、数据库适配层等尚未确认的范围。 | PASS | transcript 读取了文档的 last_verified_version: unverified；结论仍以代码中的直接 SQL 插值为核心证据，并将文档声明列为不一致。 |
| `escalates_fact_changing_conclusion_to_pm`<br>改变正式文档事实的结论升级 | FAIL | 结论明确改变了正式 API 文档关于参数化查询的事实，但最终工作区仅有源代码、change-map 和 API 文档，没有 docs/security/{feature_path}/appsec-checklist.md；transcript 也没有回交 pm-agent、分类或创建 issue 的证据。 | FAIL | 同样指出正式 API 文档与代码不一致，但最终工作区没有 Security-owned 报告，且无 PM 回交、分类或 issue 创建证据。 |

## With-Skill Behavior

发现代码与文档不一致及 SQL 注入风险，但未按契约完成 PM 升级、创建 issue 或产出 Security-owned 报告。

## Fresh Without-Skill Baseline

同样识别了代码中的直接 SQL 插值和文档不一致；未完成映射文档优先顺序及升级产物。

## Failures

- with-skill 未满足 mapped-doc 优先读取顺序。
- with-skill 在触发正式文档事实变更升级时未产出 Security 报告，也未回交 pm-agent 并创建 issue。

## Not Exercised

- 无。

## Next Steps

- 补充 docs/security/{feature_path}/appsec-checklist.md，并将代码/文档不一致及证据回交 pm-agent 分类和创建 issue。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` workspace 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
