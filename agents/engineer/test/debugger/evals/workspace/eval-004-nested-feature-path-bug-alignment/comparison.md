# Eval Result: eval-004-nested-feature-path-bug-alignment

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
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


未覆盖说明：`classifies_before_repair_plan` 仅以候选形式触发——with-skill 记录了 `implementation_deviation` 候选但因 fixture 缺少实现与复现证据而停在证据收集阶段，未完整执行分类决策。fixture 补充失败样例后该断言才能完整覆盖。

## Next Steps

保留该用例覆盖嵌套 feature path 与证据不足时的分类边界；后续可在 fixture 增加最小排序实现和失败样例，使 `implementation_deviation` 从候选变为可确认结论。

## Runtime Artifact Policy

paired candidates、verdict 与诊断只保存在 ignored runtime 目录，不提交。
