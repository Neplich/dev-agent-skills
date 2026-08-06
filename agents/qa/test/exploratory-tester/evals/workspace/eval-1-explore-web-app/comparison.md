# Eval Result: eval-001-explore-web-app

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-001-explore-web-app`
- Test case: explore-web-app
- Workspace: `workspace/eval-1-explore-web-app`
- Natural user prompt:

> 对当前可访问的目标应用进行探索测试，基于产品上下文、变更范围和环境说明发现潜在问题。

- Expected artifact: 探索测试报告，包含发现的问题列表和复现路径

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/exploratory-tester--eval-001-explore-web-app/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `184eaa5af2608524f96a97cb3aec674698e5b2340f026f0d70e0c799bc12ffaa`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **PASS**（PASS 6 / FAIL 0 / NOT EXERCISED 1）
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `assertion_1`<br>探索章程 | PASS | transcript 先读取技能规范，最终报告含 surface、timebox（未开始）、heuristics、escalation signal。 | FAIL | 报告虽有章程目标和路径，但未明确 timebox 与 escalation signals。 |
| `assertion_2`<br>探索记忆沉淀 | PASS | transcript 先读取 TEST_SUITE.md、FLOW_INDEX.md、TC-001；确认无 scripts、results、历史报告，且最终未新增 E2E 场景或脚本。 | PASS | transcript 也先读取 TEST_SUITE.md、FLOW_INDEX.md、cases/TC-001；未新增 E2E 场景。 |
| `assertion_3`<br>范围与时限 | PASS | 报告明确 timebox 未开始，原因是 QA_BASE_URL 缺失，并围绕 SearchPanel、FilterPills、ResultsList 及焦点风险组织 charter。 | FAIL | 报告未给出 timebox；仅说明环境阻塞，未形成来自上下文的明确时限处理。 |
| `assertion_4`<br>证据分层 | PASS | 最终报告明确分出 Observed issues、Suspicious but unconfirmed signals、Gaps not explored，且未把阻塞伪装成产品缺陷。 | FAIL | 报告没有分开的 observed issues、suspicious signals、gaps not explored 三类章节。 |
| `assertion_5`<br>探索方法 | PASS | 报告明确实际覆盖为 preflight only，并列出未执行的 UI、console、network、timing 路径；没有随机点击日志。 | PASS | 报告提供了结构化探索路径和执行记录，未使用随机操作日志替代探索方法。 |
| `assertion_6`<br>可交接产物 | PASS | 最终快照中的 test-reports-2026-08-07.md 含 Charter、Timebox、Exploration path covered、evidence/preflight evidence、Recommended next actions。 | FAIL | 报告有章程、路径和恢复建议，但未明确 timebox，且缺少完整的 evidence used 交接段落。 |
| `deduplicates_existing_flows`<br>不重复创建同义 TC | NOT EXERCISED | 由于 QA_BASE_URL 缺失，未实际发现或执行既有 TC-001 流程；因此没有触发“发现同义流程后增量更新”的条件。快照未新增同义 TC。 | NOT EXERCISED | 同样未进入应用、未发现可复用流程，去重更新条件未触发。 |

## With-Skill Behavior

with_skill 按要求完成前置读取、章程和阻塞报告；未启动浏览器，未产生运行时探索证据。

## Fresh Without-Skill Baseline

without_skill 完成基本上下文读取和章程草案，但缺少完整章程字段及分层报告结构。

## Failures

- 无。

## Not Exercised

- deduplicates_existing_flows：两条 lane 均未启动应用，未触发发现既有同义流程的条件。

## Next Steps

- 提供 QA_BASE_URL、浏览器/平台版本及同路径 TRD 与 IMPLEMENTATION_PLAN 后重试。
- 重试时执行 TC-001，并在实际发现重复流程或新增可复用场景时验证 TC、scripts 与 FLOW_INDEX 的增量更新。
- 补充运行时 UI、console、network 和截图证据，覆盖空结果、焦点切换、刷新/返回及异常响应。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
