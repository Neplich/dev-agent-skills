# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-006-design-gate-all-passed`

## Test Set / Fixture Version

- Fixture: `issue-121-s2-final`
- Run date: `2026-07-19`

## Latest Result

**PASS** — with-skill 3/3 assertions 通过；without-skill baseline 3/3。

## With-Skill Behavior

- 七项 design closeout 证据全部通过后仍停在候选范围确认，不提前写入。
- 候选内容仅使用最终代码与通过测试支持的当前事实，并保持后续 `unverified` 纪律。

## Without-Skill Baseline

- 全新 baseline 在该明确 fixture 上同样满足 3/3。

## Failures

- with-skill 无 assertion failure。

## Next Steps

- closeout 条件或候选确认协议变化时重跑。

## Runtime Artifact Policy

- 运行期证据仅保留在 `tmp/eval-runs/121/`，不提交。
