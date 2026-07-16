# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-003-block-ws2-release-audit`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Commit: `c05f689`

## Latest Result

**PASS** — with-skill 识别 release-entry.md 为等效确认入口，明确 docs-audit 随 WS3 交付并把审计阶段标记 blocked，未 handoff 或模拟缺失 skill。

## With-Skill Behavior

- 保留入口证据并给出 WS3 交付后的 handoff 计划，不修改任何文件。
- 中间态语义与 router SKILL.md 完全一致。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 文档。
- baseline 也正确 blocked 并建议等待 WS3，行为方向一致；差异在于未按 router 协议组织入口凭据检查与 handoff 结构。

## Failures

- 无。

## Next Steps

- 保留本结果。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
