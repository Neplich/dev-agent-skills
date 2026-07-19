# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-007-feature-database-design`

## Test Set / Fixture Version

- Fixture: `issue-121-s2-final`
- Run date: `2026-07-19`

## Latest Result

**PASS** — with-skill 6/6 assertions 通过；without-skill baseline 3/6。

## With-Skill Behavior

- 仅加载 database 与 design 模块，七项 design closeout 全通过。
- 同步当前 schema、逻辑引用和最终控制流；页面与 change map 原子更新并保持 `unverified`。
- 锁定安装后 `npm run test:docs` 真实通过 73/73，并完整 handoff `docs-agent:docs-audit`（#117）。

## Without-Skill Baseline

- baseline 缺 progressive-loading 证据，误执行版本盖章，且 #117 handoff 不完整。

## Failures

- with-skill 无 assertion failure。

## Next Steps

- database/design 模块、模板或 closeout gate 变化时重跑。

## Runtime Artifact Policy

- 运行期证据仅保留在 `tmp/eval-runs/121/`，不提交。
