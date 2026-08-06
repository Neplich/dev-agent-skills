# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-004-design-gate-failing-tests`

## Test Set / Fixture Version

- Fixture: `issue-121-s2-final`
- Run date: `2026-07-19`

## Latest Result

- Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

**PASS** — with-skill 3/3 assertions 通过；without-skill baseline 2/3。

## With-Skill Behavior

- 只加载 design 模块，核对并复现 required test failure。
- design 页面与 change-map 保持零变化，明确由 Engineer / test owner 修复并重跑后解锁。

## Without-Skill Baseline

- baseline 停止写入，但缺少明确 owner 与完整解锁路径。

## Failures

- with-skill 无 assertion failure。

## Next Steps

- design 测试门禁或 fixture 变化时重跑。

## Runtime Artifact Policy

- 运行期证据仅保留在 `tmp/eval-runs/121/`，不提交。
