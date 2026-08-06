# Eval Result: eval-003-feature-path-missing-plan-blocked

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-003-feature-path-missing-plan-blocked`
- Test case: feature-path-missing-plan-blocked
- Workspace: `workspace/eval-3-feature-path-missing-plan-blocked`
- Natural user prompt:

> 用户说：account/profile/preferences 已经开发完成，请基于 docs/pm/account/profile/preferences/PRD.md 和 docs/engineer/account/profile/preferences/TRD.md 更新并执行 E2E 验收。docs/qa/e2e/account/profile/preferences/ 目录也存在。

- Expected artifact: QA 路由决策必须识别 feature_path account/profile/preferences，读取同路径 PRD/TRD 和 QA 功能树，但因为缺少 docs/engineer/account/profile/preferences/IMPLEMENTATION_PLAN.md 而 blocked，不创建、更新或执行 E2E acceptance TC

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/qa-agent--eval-003-feature-path-missing-plan-blocked/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `dc46f6e9c1ab17c986802148894541b71552a8bbd96ec33756b90f15b25e1a45`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **FAIL**（PASS 2 / FAIL 1 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: FAIL

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `reads_same_feature_path`<br>同路径上下文 | PASS | transcript item_2 明确将请求归类为基于 PRD/TRD 的文档化 E2E 验收；item_1/3/5 读取同路径 PRD、TRD、FLOW_INDEX、TEST_SUITE，并确认 feature_path 为 account/profile/preferences。最终快照保留四个同路径文件。 | PASS | transcript item_1/2 读取同路径 PRD、TRD、FLOW_INDEX、TEST_SUITE；快照保留相同四个文件，PRD/TRD 中的 feature_path 与 QA 路径均一致。 |
| `specialist_gate_pointer`<br>Specialist 权威门禁指针 | FAIL | 虽然 transcript item_2 和最终 candidate.md 选择了 spec-based-tester，但输出没有完整声明该 specialist 的权威 E2E memory、platform version、credential、execution entry、PRD/TRD/implementation plan 与 blocked-condition 门禁适用；并且 item_6/candidate.md 详细展开了缺少 IMPLEMENTATION_PLAN、禁止创建/更新/执行 TC、技能缺失等阻塞与交接协议。断言明确规定展开复述即 FAIL。 | FAIL | candidate.md 未声明选中的 specialist，也未提供 required gate pointer；仅说明缺少 IMPLEMENTATION_PLAN 并复述阻塞条件。该无条件路由输出要求缺失，判 FAIL。 |
| `keeps_single_route`<br>单一路由 | PASS | transcript item_2 只选择一个最窄 route：spec-based-tester；没有并行调用多个 QA skill、执行 specialist 协议、修改实现或修复代码。item_1/3/5 仅为文档读取和缺失文件检查。 | FAIL | transcript 与 candidate.md 没有选择明确的 QA route/specialist；仅停止于前置文件检查。因此未满足必须选择一个最窄 QA route 的无条件要求。 |

## With-Skill Behavior

with_skill 正确识别并读取同路径 PRD/TRD 与 QA 功能树，选择 spec-based-tester，且最终快照无写入、无执行产物；但路由输出复述了缺少 implementation plan、阻塞和交接协议，违反 specialist gate pointer。

## Fresh Without-Skill Baseline

without_skill 的 fixture 与最终快照和 with_skill 完全一致，也未写入或执行 E2E；但未完成 specialist 路由指针输出，且未明确选择唯一 QA route，仅作 baseline 对照。

## Failures

- with_skill 的 specialist_gate_pointer 失败：路由输出缺失完整权威门禁指针，并展开复述了 blocked-condition、交接和执行阻塞协议。
- without_skill 的 specialist_gate_pointer 与 keeps_single_route 均失败；这是 baseline 对照，不改变当前 with_skill 结果。

## Not Exercised

- 无。

## Next Steps

- 补齐并确认 docs/engineer/account/profile/preferences/IMPLEMENTATION_PLAN.md 后，重新运行该 QA 路由评估。
- 修正 qa-agent 输出：只声明 spec-based-tester 及其权威门禁适用，不在 router 层复述 specialist 的阻塞、交接或执行协议。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
