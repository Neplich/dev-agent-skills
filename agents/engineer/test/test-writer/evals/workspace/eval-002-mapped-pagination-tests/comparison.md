# Consumption Regression Comparison

## Evaluation Target

- Skill: `test-writer`
- Eval: `eval-002-mapped-pagination-tests`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

**PASS** — with-skill 以代码事实 25 为测试基准，拒绝采用 unverified 文档声明的 50，且不臆造缺失运行时的边界行为测试。

## With-Skill Behavior

- 命中映射文档后核证默认值，测试锚定代码事实并显式记录文档不一致。
- 对无实现证据的边界行为（0、101 的截断/报错）明确不臆造，保持证据边界。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 停在'以哪个值为准'的询问上未产出测试；行为稳妥但未按契约以代码为 ground truth 直接推进可交付产物。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
