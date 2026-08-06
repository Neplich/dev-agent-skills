# Eval Result: eval-002-thin-evidence-suspected-bug

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-002-thin-evidence-suspected-bug`
- Test case: thin-evidence-suspected-bug
- Workspace: `workspace/eval-2-thin-evidence-suspected-bug`
- Natural user prompt:

> 用户只提供一句反馈：偶尔点击保存后页面好像没反应，没有截图、日志、复现步骤、环境信息或版本号。请分析是否能生成 Bug 报告。

- Expected artifact: 证据不足的缺陷分析，明确 suspected / needs more evidence、缺失证据、下一步收集计划，并避免创建 confirmed bug

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/bug-analyzer--eval-002-thin-evidence-suspected-bug/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `10fdf1909715a6b1da7d96cc3c254a697af93b4cc9a6354268fbce4960a8ceb1`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **PASS**（PASS 4 / FAIL 0 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: PASS

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `assertion_1`<br>薄证据分类 | PASS | candidate 明确写出“疑似问题 / 待补证据”和“suspected / needs more evidence”，并明确不能生成已确认 Bug；transcript 与快照无相反证据。 | PASS | candidate 明确称只能作为疑似问题，不能标记为已确认 Bug。 |
| `assertion_2`<br>缺失证据 | PASS | candidate 列出复现步骤、实际/期望结果、截图或录屏、日志、环境、版本、权限、数据状态、发生频率，并建议收集控制台、网络请求、错误日志等。 | FAIL | 列出了复现步骤、期望/实际结果、截图或录屏、日志、环境和版本，但未明确列出 console output、network output 或 trace 等关键缺口；“网络环境”不等于网络请求输出。 |
| `assertion_3`<br>结构化输出 | PASS | 输出包含分类（疑似问题/待补证据）、证据状态、低置信度陈述、缺失信息和建议补充证据等结构化内容。 | FAIL | 虽有当前证据、缺失信息和建议追问，但没有明确的 confidence statement，结构化段落不完整。 |
| `assertion_4`<br>持久化边界 | PASS | with_skill transcript 仅有读取技能文件和输出消息；最终 workspace-snapshot 只有 feedback/customer-note.md，未见 GitHub issue、confirmed bug artifact 或其他新文件。 | PASS | transcript 无写入/外部工具调用，最终快照同样只有原始 customer-note.md，candidate 仅建议登记疑似问题。 |

## With-Skill Behavior

with_skill 将反馈分类为 suspected / needs more evidence，明确列出证据缺口和下一步收集计划；最终快照仅保留原始 fixture，未创建确认缺陷或 GitHub artifact。

## Fresh Without-Skill Baseline

without_skill 同样避免确认 Bug，但结构化证据缺口不完整，且缺少明确的 confidence statement。

## Failures

- 无。

## Not Exercised

- 无。

## Next Steps

- 无。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
