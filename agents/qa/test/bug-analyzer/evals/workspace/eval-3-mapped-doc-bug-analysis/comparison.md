# Consumption Regression Comparison

## Evaluation Target

- Skill: `bug-analyzer`
- Eval: `eval-003-mapped-doc-bug-analysis`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

**PASS** — with-skill 确认文档 3 次与规则 2 次的静态冲突，运行时未证实部分诚实分类为 suspected / needs more evidence，并遵守 E2E 前置门禁不越权建用例。

## With-Skill Behavior

- 命中映射文档后回规则配置核证重试次数，产出结构化缺陷分析报告（severity/confidence 显式分级）。
- 证据边界清晰：静态冲突与运行时行为分开陈述，缺 feature_path 与 PRD/TRD 时不创建 E2E 用例。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 结论方向一致且同样保持证据谨慎，но分歧证据组织与门禁引用由临场推断承担，协议化程度低于 with-skill。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
