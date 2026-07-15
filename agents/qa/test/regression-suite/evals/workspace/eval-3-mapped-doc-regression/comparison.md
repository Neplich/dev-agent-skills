# Consumption Regression Comparison

## Evaluation Target

- Skill: `regression-suite`
- Eval: `eval-003-mapped-doc-regression`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

**PASS** — with-skill 以代码阈值 3 核证出文档声明 2 的分歧，回归判定诚实标记 blocked（缺证据链），并制定锚定代码事实的定向边界范围。

## With-Skill Behavior

- 命中映射文档后回规则文件核证阈值，分歧结构化记录且不采信 unverified 文档值。
- 回归门禁行为正确：缺 feature_path/PRD/TRD/实施计划与原始失败证据时不宣称验证通过，产出结构化回归报告。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 同样静态确认阈值并区分 hotfix/预期变更路径，判断合格，但报告组织与证据结构较松散。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
