# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-008-deployment-ops-upgrade`

## Test Set / Fixture Version

- Fixture: `issue-121-s2-final`
- Run date: `2026-07-19`

## Latest Result

**PASS** — with-skill 5/5 assertions 通过；without-skill baseline 4/5。

## With-Skill Behavior

- 仅加载 ops 模块，以 Compose 配置和已执行结果同步启动、升级、健康检查与回滚。
- 明确排除尚未执行的 Kubernetes/Helm 计划；页面与映射保持原子、`unverified`。
- `npm run test:docs` 真实通过 73/73，并 handoff #117。

## Without-Skill Baseline

- baseline 基本完成当前事实同步，但未完整保持审计前 `unverified` 边界。

## Failures

- with-skill 无 assertion failure。

## Next Steps

- deployment evidence 或 ops 模块变化时重跑。

## Runtime Artifact Policy

- 运行期证据仅保留在 `tmp/eval-runs/121/`，不提交。
