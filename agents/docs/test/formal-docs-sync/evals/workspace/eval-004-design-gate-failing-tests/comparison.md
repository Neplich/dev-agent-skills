# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-004-design-gate-failing-tests`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Commit: `c05f689`

## Latest Result

**PASS** — with-skill 识别计划必测项 test_compact_summary_handles_empty_values 为 FAILED 后 blocked：设计页与 map 零变化，指名失败测试与解锁路径（Engineer 修复后全部计划测试重跑全绿再重入门禁）。

## With-Skill Behavior

- 完成态门禁第 6 项精确触发，不因代码与范围完整而放行。
- blocked 输出含失败证据、owner 与重入条件。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 文档。
- baseline 同样阻塞并要求先修复测试，方向一致；差异在门禁清单执行与原子范围声明的协议化程度。

## Failures

- 无。

## Next Steps

- 保留本结果。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
