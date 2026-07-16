# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-001-route-formal-docs-sync`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Commit: `c05f689`

## Latest Result

**PASS** — with-skill 校验 PM handoff 后正确分流 formal-docs-sync，保留 packet 字段与下游注意事项，只引用 specialist gate 不复制正文，未启用 auto-continue 时停在分流结果。

## With-Skill Behavior

- 入口凭据检查、最窄 specialist 选择与 handoff 保留完整执行。
- 明确下游需保留'不覆盖人工 change-map 条目'等证据边界。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 文档。
- baseline 也完成了入口检查与分流方向判断，但 packet 字段保留与 gate 指针边界的组织依赖临场推断。

## Failures

- 无。

## Next Steps

- 保留本结果。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
