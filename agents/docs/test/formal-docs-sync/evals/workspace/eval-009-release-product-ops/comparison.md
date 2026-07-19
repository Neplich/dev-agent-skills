# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-009-release-product-ops`

## Test Set / Fixture Version

- Fixture: `issue-121-s2-final`
- Run date: `2026-07-19`

## Latest Result

**PASS** — with-skill 5/5 assertions 通过；without-skill baseline 4/5。

## With-Skill Behavior

- 仅加载 product 与 ops 模块，只更新 dashboard product/runtime ops 页面及映射。
- 核对 v1.5.0 上限 25 和镜像版本，排除 v1.5.1 计划；Release Notes surfaces 零变化。
- 两页保持 `unverified`，`npm run test:docs` 真实通过 73/73，并 handoff #117。

## Without-Skill Baseline

- baseline 完成主要页面同步，但缺少一项稳定的协议边界证据。

## Failures

- with-skill 无 assertion failure。

## Next Steps

- release mode、版本证据或 product/ops 模块变化时重跑。

## Runtime Artifact Policy

- 运行期证据仅保留在 `tmp/eval-runs/121/`，不提交。
