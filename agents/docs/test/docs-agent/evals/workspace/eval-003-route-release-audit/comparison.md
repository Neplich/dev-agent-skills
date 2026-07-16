# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-003-route-release-audit`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Commit: `c05f689`

## Latest Result

**PASS** — with-skill 识别等效已确认发布链后把审计请求正常分流 docs-audit，保留 release scope/tag/changelog/证据，只引用 specialist gate，停在 handoff 确认点（WS3 分流启用后的复跑验证）。

## With-Skill Behavior

- 首轮运行暴露 fixture 残留 WS2 时代的 unresolved_blocker 表述导致误判 blocked；修正 fixture 至 WS3 现实后复跑通过。
- 分流语义与 4-skill 终态一致。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 文档。
- baseline 也指向 docs-audit gate 作为权威，但入口凭据校验与 handoff 字段保留由临场组织。

## Failures

- 无。

## Next Steps

- 保留本结果。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
