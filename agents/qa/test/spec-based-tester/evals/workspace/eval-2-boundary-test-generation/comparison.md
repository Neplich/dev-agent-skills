# Eval Result: eval-002-boundary-test-generation

## Evaluation Target

- Agent: `qa`
- Skill: `spec-based-tester`
- Eval: `eval-002-boundary-test-generation`
- Test case: boundary-test-generation
- Workspace: `workspace/eval-2-boundary-test-generation`
- Natural user prompt:

> 根据 docs/pm/login-refresh/PRD.md、docs/engineer/login-refresh/TRD.md、实现变更说明和仓库测试命令，对登录表单执行边界验证；覆盖空值、超长字符串、特殊字符、非法邮箱格式和锁定账号状态。

- Expected artifact: 结构化边界验证报告，包含 requirement matrix、execution path、evidence references、risk notes 和 handoff decision

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/spec-based-tester--eval-002-boundary-test-generation/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `336322ee7071e710178b8474774a3477df3a2f6ee1c62bd86c7f14b7f3783bed`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **FAIL**（PASS 4 / FAIL 3 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: FAIL

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `assertion_1`<br>范围与假设 | PASS | transcript 中在 npm 执行前记录了五类边界、缺少 IMPLEMENTATION_PLAN.md、QA_BASE_URL、依赖和实现文件等阻塞项；最终报告也包含 Preflight baseline。 | FAIL | transcript 在执行前仅记录范围，未记录输入约束、未知依赖、环境假设和 IMPLEMENTATION_PLAN.md 等 blocked 条件。 |
| `assertion_2`<br>用例目录优先 | FAIL | transcript 先执行了 auth/validators.ts 和测试引用的项目探索，之后才读取 TEST_SUITE.md、FLOW_INDEX.md、cases 和 scripts，违反 QA 用例目录优先顺序。 | PASS | transcript 在执行命令前读取了 QA TEST_SUITE.md、FLOW_INDEX.md、cases 和 scripts；未在其前探索实现源文件。 |
| `assertion_3`<br>边界执行 | PASS | transcript 执行的是与 TC-001 对应的定向命令 npm test -- login-boundaries，且最终快照的五项边界均被列入 scope；因 vitest 缺失，实际结果按 blocked 记录。 | PASS | transcript 执行了 QA 文档指定的 login-boundaries 定向命令，最终 result.md 逐项记录五类边界为未执行/blocked。 |
| `assertion_4`<br>证据与分层 | PASS | 最终快照中的报告和 result.md 对空值、超长、特殊字符、非法邮箱、锁定账号逐项标记 blocked，并引用 vitest 缺失、QA_BASE_URL 缺失等可由 transcript/tool trace 追踪的证据。 | PASS | 最终 result.md 对每项边界保留状态和阻塞原因，transcript 提供了 npm 命令及退出码 127 的工具证据。 |
| `assertion_5`<br>硬性结构 | FAIL | 报告有 requirement matrix 和 Risks，但没有独立、明确的 execution path、evidence references、handoff decision 结构化段落；“Validation summary”“Blocked items and recovery”不能完整替代这些要求。 | FAIL | 最终快照仅有执行结果和后续行动，没有 requirement matrix、execution path、evidence references、risk notes、handoff decision 的完整结构化报告。 |
| `assertion_6`<br>风险与交接 | PASS | 最终报告包含 Risks、Blocked items and recovery、未覆盖项及恢复条件，并明确“Confirmed failures: None”；没有将 blocked/assumed 项升级为 bug-analyzer 缺陷。 | FAIL | 最终 result.md 有 Follow-up，但没有明确的风险 notes、未覆盖项汇总或 handoff decision，证据不足以证明完整风险与交接处理。 |
| `alignment_plan_gate`<br>PRD/TRD 和实施计划门禁 | FAIL | transcript 明确发现同路径 IMPLEMENTATION_PLAN.md 缺失，但随后仍执行 npm test -- login-boundaries；技能门禁要求在执行验收 TC 前先确认计划，缺失时应直接 blocked 并回 feature-implementor。 | FAIL | transcript 未检查或记录同路径 IMPLEMENTATION_PLAN.md，也未执行缺失计划的 feature-implementor handoff；最终快照也无该门禁说明。 |

## With-Skill Behavior

with_skill 实际读取并归档了边界验证资料，记录了 blocked 状态；但在完成 QA 目录读取前探索了实现文件，并在缺少 IMPLEMENTATION_PLAN.md 的门禁条件下仍执行了验收命令。最终报告也缺少要求的完整结构化段落。

## Fresh Without-Skill Baseline

without_skill 成功读取了规格、QA 用例并执行了仓库命令，也在最终快照中落盘结果文件；但没有记录 IMPLEMENTATION_PLAN.md 门禁、风险 notes 或明确 handoff 决策。

## Failures

- with_skill 违反 QA 用例目录优先读取顺序：在读取 QA 用例前探索了 auth/validators.ts 和项目测试引用。
- with_skill 在缺少 IMPLEMENTATION_PLAN.md 时仍执行验收命令，违反 alignment plan gate。
- with_skill 报告未完整包含 execution path、evidence references、handoff decision 等硬性结构。
- without_skill 缺少 assertion_1、assertion_5、assertion_6 和 alignment_plan_gate 要求的完整预检、结构化报告、风险交接与计划门禁证据。

## Not Exercised

- 无。

## Next Steps

- 补齐 docs/engineer/login-refresh/IMPLEMENTATION_PLAN.md，并在计划确认前不要执行验收 TC。
- 重跑时先完整读取 QA 目录，再进行必要的实现探索；报告增加 execution path、evidence references 和 handoff decision 独立段落。
- 安装项目依赖并重新运行 npm test -- login-boundaries；如需浏览器验证，提供 QA_BASE_URL。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
