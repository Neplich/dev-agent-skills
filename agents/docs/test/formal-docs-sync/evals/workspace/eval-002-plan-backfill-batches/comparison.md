# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-002-plan-backfill-batches`

## Test Set / Fixture Version

- Fixture: `issue-121-s2-final`
- Run date: `2026-07-19`

## Latest Result

**PASS** — 最终 fresh judge 判定 with-skill 5/5 assertions 通过；without-skill baseline 2/5。

## With-Skill Behavior

- 优先使用 catalog，将 Accounts 与 owner `identity-team` 保留为单一候选批次。
- 明确提出 `src/api/accounts/**`、`docs/site/api/accounts.md`、证据与 seed 映射。
- 未确认批次保持页面和 change map 零写入，并说明无 catalog 时的有限发现门禁。

## Without-Skill Baseline

- 全新 baseline 未给出完整 code_glob、目标页面与 seed 对齐，也未完整保留 owner。

## Failures

- with-skill 无 assertion failure。

## Next Steps

- catalog/backfill 协议变化时重跑。

## Runtime Artifact Policy

- 运行期证据仅保留在 `tmp/eval-runs/121/`，不提交。
