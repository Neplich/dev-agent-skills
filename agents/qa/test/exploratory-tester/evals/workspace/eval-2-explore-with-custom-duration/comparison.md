# Eval Result: eval-002-explore-with-custom-duration

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-002-explore-with-custom-duration`
- Test case: explore-with-custom-duration
- Workspace: `workspace/eval-2-explore-with-custom-duration`
- Natural user prompt:

> 对用户指定的目标应用进行 5 分钟探索测试，按探索章程验证 changed surface、相邻风险和证据分层

- Expected artifact: 5 分钟探索测试报告

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/exploratory-tester--eval-002-explore-with-custom-duration/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `309d7645fa902999f9cc011ad12d0dc566cf30afa564d27b0c546cf8e149fa0b`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **PASS**（PASS 6 / FAIL 0 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: PASS

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `assertion_1`<br>上下文驱动范围 | PASS | 最终快照中的 FLOW_INDEX.md 和阻塞报告包含目标 URL、5 分钟时长、changed surface、具体启发式、阻塞原因及未验证范围；transcript 记录了读取环境和改动面。 | FAIL | transcript/candidate 仅记录目标、改动面和风险，未形成完整探索章程，缺少明确的升级信号和未验证前提记录。 |
| `assertion_2`<br>独立探索确认 | PASS | transcript 在任何运行前读取 TEST_SUITE.md、FLOW_INDEX.md、PRD 和环境/改动信息；最终快照确认无 cases、scripts、results。阻塞后实际更新了 FLOW_INDEX.md，未创建 TC/script。 | PASS | transcript 读取了 TEST_SUITE.md、FLOW_INDEX.md、PRD、环境和改动面；最终快照确认没有可读的 cases/scripts/results，且未声称扩充用例。 |
| `version_entry_and_subagent`<br>版本、执行入口与 subagent | PASS | TEST_SUITE.md 明确平台版本缺失；transcript 及最终阻塞报告明确因此 blocked、未启动计时，并记录 repo harness → Chrome/browser connector → Playwright fallback 顺序及 subagent 执行约定。 | FAIL | 虽读取到版本缺失并执行 curl 探测，但 transcript/candidate 未确认规定的执行入口顺序、选择理由或默认 subagent 执行约定。 |
| `assertion_3`<br>异常分层 | PASS | 最终阻塞报告明确区分 Observed issues（None）、Suspicious but unconfirmed signals（toast 风险）和 Gaps not explored；transcript 证明未进行 UI/运行时操作。 | PASS | candidate 明确将 DNS/HTTP 000 作为 L0 环境证据，并区分文档证据与没有 UI/日志证据，未把未确认信号升级为缺陷。 |
| `assertion_4`<br>证据输出 | PASS | 最终阻塞报告包含实际覆盖路径（preflight only）、读取的 QA/PM/环境文件、目标 URL 和阻塞原因；transcript 还提供了实际读取命令及文件变更 trace。 | PASS | transcript 提供实际 rg/sed/curl 命令，candidate 给出目标 URL、DNS/HTTP 000 结果及 implementation/changed-surface.md 证据引用，不是随机操作清单。 |
| `assertion_5`<br>风险交接 | PASS | 最终阻塞报告包含具体风险 notes（toast 可能遮蔽校验错误）及三项重试/补齐版本、TRD、IMPLEMENTATION_PLAN 的下一步建议。 | PASS | candidate 记录保存/取消、未保存状态、账户联动和 toast 风险，并建议提供可解析地址或浏览器环境后重测。 |

## With-Skill Behavior

with_skill 完成了阻塞前置检查、章程、证据分层和风险交接；未伪造运行结果。最终快照确认 FLOW_INDEX 与阻塞报告确实落盘。

## Fresh Without-Skill Baseline

without_skill 未完成版本/执行入口/subagent 前置要求，但进行了可审计的环境探测；仅作为 baseline 对照。

## Failures

- 无。

## Not Exercised

- 无。

## Next Steps

- 补充确切平台/浏览器版本及可达 QA 地址后重跑 5 分钟探索。
- 补齐或确认对应 TRD 与 IMPLEMENTATION_PLAN，并在发现可复用场景时生成匹配 TC/script。
- fixture-manifest.json 的五个初始 fixture 在两条 lane 中一致；with_skill 的 FLOW_INDEX 差异是已验证的运行后更新，非初始 fixture 差异。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
