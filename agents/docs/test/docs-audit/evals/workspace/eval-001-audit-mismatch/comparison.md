# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-001-audit-mismatch`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Commit: `c05f689`

## Latest Result

**PASS** — with-skill 核证出文档声明 POST 与代码事实 GET 的直接冲突判 mismatch，release blocked 并把归属交回负责团队确认修文档还是修代码；不修改任何文件、不盖章。

## With-Skill Behavior

- 冲突证据以文档声明/代码事实结构化呈现，审计报告完整归档。
- blocked 语义正确：mismatch 需先确认设计意图，不自行选边修复。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 文档。
- baseline 同样得出 blocked 结论且保持只读，判断方向一致；差异在三态协议与报告归档的执行。

## Failures

- 无。

## Next Steps

- 保留本结果。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
