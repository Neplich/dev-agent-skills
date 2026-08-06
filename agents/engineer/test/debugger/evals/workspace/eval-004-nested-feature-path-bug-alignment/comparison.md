# Eval Result: eval-004-nested-feature-path-bug-alignment

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-004-nested-feature-path-bug-alignment`
- Test case: nested-feature-path-bug-alignment
- Workspace: `workspace/eval-004-nested-feature-path-bug-alignment`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: PARTIAL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 用户说：Message History Search 的搜索结果排序不对，这是 bug，请修一下。相关预期文档在 docs/pm/chat-interface/messages/history/search/PRD.md 和 docs/engineer/chat-interface/messages/history/search/TRD.md。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- FAIL `reads_nested_expected_behavior_docs`: with_skill 的 final.md 仅写 `chat-interface/messages/history/search`，未引用要求的两个完整 PRD/TRD 路径；transcript 中虽有读取命令证据，但最终输出未满足引用要求。
- NOT EXERCISED `validates_trd_related_prd`: transcript 读取了 `related_prd` 字段且其值匹配，但没有可观测的明确校验结论；未触发不匹配分支。
- FAIL `classifies_before_repair_plan`: final.md 与 transcript 的 agent_message 均未明确分类为 `implementation_deviation`、`requirement_change`、`missing_docs` 或 `trd_gap`。
- NOT EXERCISED `blocks_wrong_path_or_requirement_change`: 实际 PRD/TRD 的 feature_path、parent_feature、feature_level 与 related_prd 均匹配，未触发路径不清、需求变化或 TRD 不一致条件。
- PASS `does_not_fix_directly`: final.md 明确表示没有源码、测试或构建入口，未声称修改代码、更新测试、应用修复或验证修复通过；workspace 文件哈希也未显示文档被修改。

## With Skill Behavior

with_skill 读取了嵌套 PRD/TRD，并确认排序规则及路径一致；但最终输出缺少完整文档路径引用和四选一分类。runtime exit_code 为 0，输入与输出哈希对应的 workspace 文档未变更。

## Without Skill Baseline

without_skill 仅读取并总结了 PRD/TRD，未引用完整路径、未校验或报告 related_prd、未分类；未修改 workspace，作为对照。

## Failures / Findings

- reads_nested_expected_behavior_docs：最终输出未引用两个完整文档路径。
- classifies_before_repair_plan：未输出规定的分类。
- Root cause: with_skill 在确认文档对齐并因缺少源码阻断后，没有把完整路径引用和强制分类写入最终输出。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-004-nested-feature-path-bug-alignment

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-004-nested-feature-path-bug-alignment`
- Workspace: `workspace/eval-004-nested-feature-path-bug-alignment`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- 日期：2026-07-30
- Fixture：`chat-interface/messages/history/search` 四级 Approved PRD/TRD，`related_prd` 同路径匹配。
- Fresh run：`tmp/eval-runs/issue-196-l2-2-debugger-20260730-220643/`
- 本轮全新 paired validation，未复用历史 baseline。

## Assertion Results

- PASS `reads_nested_expected_behavior_docs`：引用 PRD/TRD 并核对 `feature_path`、`parent_feature`、`feature_level`。
- PASS `validates_trd_related_prd`：确认 `related_prd` 同路径，并说明不匹配时分类 `trd_gap`。
- PASS `classifies_before_repair_plan`：在任何计划前记录 `implementation_deviation` 候选，因缺少实现与复现证据而等待确认。
- PASS `blocks_wrong_path_or_requirement_change`：路径/PRD/需求问题回 PM，TRD 字段不一致回 `trd-gen`，均阻断计划、代码与 E2E。
- PASS `does_not_fix_directly`：未修改代码、测试或声称修复。

## With-Skill Behavior

候选精确核对四级文档关系；在缺少实现、失败测试和复现命令时不猜根因，但仍在允许的四类中记录实现偏离候选，并停在证据收集阶段。

## Without-Skill Baseline

来源为本轮隔离子代理基于同一 prompt/fixture 的新候选，未读取 skill、Engineer README 或 with-skill。baseline 完成路径与阻断核对，但明确表示当前不属于四种分类中的任何一种，改用“缺少复现与实现证据”，因此 `classifies_before_repair_plan` 失败；其余 4/5 通过。

## Failures

- With-skill：无。
- Baseline：`classifies_before_repair_plan` FAIL。

## Latest Result

- Behavior result: PASS
- Coverage result: PARTIAL
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


未覆盖说明：`classifies_before_repair_plan` 仅以候选形式触发——with-skill 记录了 `implementation_deviation` 候选但因 fixture 缺少实现与复现证据而停在证据收集阶段，未完整执行分类决策。fixture 补充失败样例后该断言才能完整覆盖。

## Next Steps

保留该用例覆盖嵌套 feature path 与证据不足时的分类边界；后续可在 fixture 增加最小排序实现和失败样例，使 `implementation_deviation` 从候选变为可确认结论。

## Runtime Artifact Policy

paired candidates、verdict 与诊断只保存在 ignored runtime 目录，不提交。
