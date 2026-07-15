# Consumption Regression Comparison

## Evaluation Target

- Skill: `spec-based-tester`
- Eval: `eval-003-mapped-doc-acceptance`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

**PASS** — with-skill 对规范 80 vs 实现 64 给出 FAIL 判定并附静态断言证据，运行时边界诚实标记 BLOCKED，验收矩阵结构化落档。

## With-Skill Behavior

- 按契约读取映射规范后以实现配置核证，FAIL/BLOCKED 判定均有证据支撑，不虚构运行时行为。
- 产出结构化验收报告与需求矩阵，分歧可直接供后续 QA/工程消费。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 同样确认不一致且不越权宣称运行时验证，但验收产物组织较松散，未形成结构化判定矩阵。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
