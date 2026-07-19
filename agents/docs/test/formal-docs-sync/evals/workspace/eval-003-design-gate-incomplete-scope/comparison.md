# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-003-design-gate-incomplete-scope`

## Test Set / Fixture Version

- Fixture: `issue-121-s2-final`
- Run date: `2026-07-19`

## Latest Result

**PASS** — with-skill 3/3 assertions 通过；without-skill baseline 2/3。

## With-Skill Behavior

- 只加载 design 模块，识别实施计划仍有未完成范围。
- design 页面与 change-map 均零变化，并将解锁动作交回 Engineer / feature-implementor owner。

## Without-Skill Baseline

- baseline 同样停止写入，但未明确指名 Engineer / feature-implementor owner。

## Failures

- with-skill 无 assertion failure。

## Next Steps

- design closeout gate 变化时重跑。

## Runtime Artifact Policy

- 运行期证据仅保留在 `tmp/eval-runs/121/`，不提交。
