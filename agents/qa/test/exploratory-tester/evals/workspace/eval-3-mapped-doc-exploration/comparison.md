# Consumption Regression Comparison

## Evaluation Target

- Skill: `exploratory-tester`
- Eval: `eval-003-mapped-doc-exploration`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

**PASS** — with-skill 发现文档 15 分钟与代码 10 分钟的超时分歧并结构化记录，探索章程以代码事实为主探针、文档值为兼容探针，同时正确识别 E2E 持久化资产缺失。

## With-Skill Behavior

- 命中映射文档后回代码规则核证超时值，分歧以文档声明/代码事实/影响表结构化输出。
- 探索设计不把 unverified 文档值当预期，PM 确认前只作为兼容性探针；并按 QA 契约说明 E2E 资产沉淀路径与执行入口优先级。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 也识别了 10/15 分钟差异并建议确认预期，但分歧记录为叙述式，未形成契约格式的证据结构。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
