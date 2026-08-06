# Eval Result: eval-003-mapped-doc-exploration

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-003-mapped-doc-exploration`
- Test case: mapped-doc-exploration
- Workspace: `workspace/eval-3-mapped-doc-exploration`
- Natural user prompt:

> 围绕 src/checkout/session.rules 的结账会话超时行为制定最小探索章程，并指出应重点验证的边界。

- Expected artifact: 以映射文档定位、代码事实核证的探索章程和风险记录。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/exploratory-tester--eval-003-mapped-doc-exploration/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `df8fd85df6e085de7b81dd75f9024f74dbb28600bd3bdebc72a765cb13a763a9`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **PASS**（PASS 3 / FAIL 0 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: PASS

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `reads_mapped_docs_first`<br>先消费命中的结账会话文档 | PASS | transcript 显示先定位规则，随后读取 change-map，并在同一命令中读取其命中的 docs/site/api/checkout-session.md；最终仅有三份 fixture 文件，没有遍历整个 docs/site。 | FAIL | transcript 顺序为先读规则、再做全局 rg，最后在同一命令中先读取 checkout-session.md、后读取 change-map，未体现命中 change-map 后优先消费文档。 |
| `verifies_against_code`<br>探索边界以代码事实为准 | PASS | tool trace 两次读取 src/checkout/session.rules，最终内容为 session_timeout_minutes = 10；candidate 明确指出文档写 15 分钟，并将差异及其对时间边界、配置一致性的影响列为风险，而非直接采用文档值。 | PASS | transcript 读取并核对规则文件和文档；candidate 明确区分代码 10 分钟与文档 15 分钟，并要求将该差异作为待验证风险。 |
| `treats_unverified_as_low_trust`<br>未核证文档不作为确认事实 | PASS | 最终快照和 transcript 均显示 change-map 与 API 文档的 last_verified_version 为 unverified；candidate 不把文档值当作事实，采用代码的 10 分钟作为当前配置事实，并明确尚未执行、需用时间控制/测试再次验证行为。 | PASS | transcript 读取到两处 last_verified_version: unverified；candidate 将文档声明列为需验证的不一致项，并把实际行为、规则文件和文档一致性作为验证标准，没有据未核证文档直接下结论。 |

## With-Skill Behavior

with_skill 三项断言均有 transcript、tool trace、candidate 与最终快照支持；未发生实际探索执行，因此没有把候选的计划误判为执行结果。两条 lane 的 fixture 快照一致。

## Fresh Without-Skill Baseline

without_skill 作为 baseline：也核证了代码与文档差异，但未遵循 change-map 命中后的优先文档读取顺序。

## Failures

- 无。

## Not Exercised

- 无。

## Next Steps

- 执行章程中的 9:59、10:00、10:01、活动续期、过期提交及并发边界测试。
- 修正文档中的 15 分钟声明，或确认代码配置应改为产品契约值，并更新验证版本。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
