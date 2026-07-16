# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-006-design-gate-all-passed`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Commit: `c05f689`

## Latest Result

**PASS** — with-skill 确认前六项完成态证据全部通过后，提出设计页 + design map 的原子候选范围（页面/代码范围/证据/排除项），正确停在第七项维护者范围确认，零写入。

## With-Skill Behavior

- 正向路径不越权：证据全过≠可写入，候选范围确认门禁保留。
- 候选内容只描述代码与测试证明的 current state。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 文档。
- baseline 同样停在确认点零写入，行为一致；差异在七项门禁的逐项核验记录与候选范围的协议化呈现。

## Failures

- 无。

## Next Steps

- 保留本结果。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
