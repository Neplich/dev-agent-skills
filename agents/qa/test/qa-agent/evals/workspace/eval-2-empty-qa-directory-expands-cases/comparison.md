# Eval Result: eval-002-empty-qa-directory-expands-cases

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-002-empty-qa-directory-expands-cases`
- Test case: empty-qa-directory-expands-cases
- Workspace: `workspace/eval-2-empty-qa-directory-expands-cases`
- Natural user prompt:

> 用户说：请对 profile-settings 做一次 E2E QA。docs/qa/e2e/account/profile-settings/profile-form/ 已存在，但 TEST_SUITE.md、FLOW_INDEX.md 和 cases/ 里没有测试用例。我确认这个功能有新更新，请主动查看项目文件并完成验证。

- Expected artifact: QA 路由决策与执行协议，明确空 E2E 功能树目录需要触发目标文件探索、更新 TEST_SUITE.md 和 FLOW_INDEX.md、创建独立 TC 与 script 文件，并要求后续验证基于这些用例执行

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/qa-agent--eval-002-empty-qa-directory-expands-cases/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `4b523a57597194309a66e74261387466f919e128463a54f5f7cd87e452b26823`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **FAIL**（PASS 1 / FAIL 3 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: FAIL

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `assertion_1`<br>空目录识别 | PASS | transcript 的初始文件读取显示 TEST_SUITE.md 明确写着无 active TC，FLOW_INDEX.md 为空且目标目录仅含既有文档；最终快照仍在同一 profile-form 路径下新增用例，没有回退到旧的单层 profile-settings 目录。 | PASS | transcript 读取并确认同一目标目录为空；最终快照在目标 profile-form 路径新增 3 个用例，没有使用旧的单层 QA 目录。 |
| `assertion_2`<br>授权后传递探索范围 | FAIL | 用户已在 prompt.txt 中确认有新功能更新并授权探索，但 transcript item_2/item_5 进入了实现检查和资产执行，最终消息也只报告补齐 cases；没有路由输出把项目文件、environment/qa-env.md 和选定 specialist 作为下游上下文，也没有明确 specialist 接手。 | FAIL | candidate/transcript 直接执行测试资产补齐，没有输出授权后的 specialist 路由、项目文件/环境上下文传递或门禁适用声明。 |
| `specialist_gate_pointer`<br>Specialist 权威门禁指针 | FAIL | transcript 仅声明按 qa-agent 流程工作，未声明选中的 spec-based-tester 或 exploratory-tester，也未指出其 E2E memory、platform version、credential、execution entry、PRD/TRD/implementation plan 与 blocked-condition 指针适用。 | FAIL | without_skill transcript 没有 specialist 选择或权威门禁指针，仅自行补齐 cases/scripts。 |
| `assertion_6`<br>路由边界 | FAIL | 未选择一个最窄主 route。transcript item_0/item_2 说按 qa-agent 流程检查，但后续直接执行静态检查、创建 4 个 case/script 和结果文件；这属于下游 QA 执行而非完成路由输出，且最终消息没有明确 specialist 接手。 | FAIL | 未声明主 route 或 specialist，直接执行 3 个 case、script 和静态验证；因此无证据表明完成了要求的窄路由。 |

## With-Skill Behavior

with_skill 正确识别了目标 QA 目录为空，并在最终快照中创建了 4 个 case、4 个 script 和结果文件；但未完成 qa-agent 所要求的路由输出，未选择具体 specialist，也未声明 specialist 权威门禁指针，且实际执行了下游 QA 资产补齐工作。

## Fresh Without-Skill Baseline

without_skill 同样识别并补齐了目标目录，最终快照中有 3 个 case 和 3 个 script；但同样缺少路由选择与 specialist 门禁指针，作为 baseline 仅供对照，不影响当前结果。

## Failures

- with_skill 的 assertion_2、specialist_gate_pointer、assertion_6 均为 FAIL；已触发的 with_skill assertion 存在 FAIL，因此 Behavior=FAIL、Overall=FAIL。
- 最终快照证实 with_skill 创建了声称的文件；没有出现“候选声称创建但快照不存在”的额外失败。
- 两条 lane 均将浏览器执行标为 blocked；这不是本组 assertions 的覆盖缺失，但不能替代要求的路由输出。

## Not Exercised

- 无。

## Next Steps

- 补充明确的 qa-agent 路由输出：选择最窄主 route，按本请求应为 spec-based-tester，并传递目标项目文件与 environment/qa-env.md。
- 只保留 specialist 权威门禁的指针式声明，不在 qa-agent 路由中展开 specialist 内部协议。
- 将测试资产创建和执行交由选定 specialist，qa-agent 仅负责路由、上下文传递和预期证据产物说明。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
