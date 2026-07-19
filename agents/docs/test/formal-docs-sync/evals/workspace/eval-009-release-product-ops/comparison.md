# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-009-release-product-ops`

## Test Set / Fixture Version

- Fixture version: `issue #117 cross-doc audit 2026-07-19`
- Fresh run: `tmp/eval-runs/117-adjacent/formal-docs-sync/eval-009-release-product-ops/`
- Source head: `00c9741dabc24f6b6df377c69c42adb989722648` plus the current issue #117 working tree

## Latest Result

**PASS（5/5 assertions）** — with-skill 仅同步 v1.5.0 受影响的 product/ops 当前页，Release Notes surfaces 零变化，两页保持 `unverified`，并携带维护者确认版本及来源 handoff #117 pre-tag。

## Assertions

- `limits_release_to_affected_product_ops`：PASS。只修改 dashboard product/runtime ops 两页；现有映射准确，无其他类型扩张。
- `reconciles_confirmed_version_facts`：PASS。核对上限 25、v1.5.0 镜像与配置，排除旧值及 v1.5.1 计划。
- `preserves_release_notes_surfaces`：PASS。Release Notes 正文、index、metadata、navigation 零变化，并指向 #116 owner。
- `keeps_release_pages_unverified`：PASS。两页均为 `last_verified_version: unverified`，未自行盖 v1.5.0。
- `runs_release_host_checks_and_handoffs`：PASS。`npm run test:docs` 73/73 通过；handoff 明确 `target_release_version: v1.5.0`、维护者确认来源与 complete affected set。

## With-Skill Behavior

- 只读取 product/ops 类型模块，未操作 GitHub Release、tag、部署或 Release Notes。
- #117 handoff 进入 pre-tag，版本来自 `release-handoff.md` 的维护者确认，而非 branch/ref 推测。

## Without-Skill Baseline

- 来源：同一 prompt 与 pristine fixture 的本轮 fresh `without_skill`；不含目标 skill、Docs README、旧 comparison 或 with-skill 输出，未复用历史 baseline。
- baseline 完成主要页面事实、保持 Release Notes 零变化并通过检查，但 handoff 没有维护者确认来源，反而报告“version anchor unavailable”，未稳定满足新的 `target_release_version` pre-tag 消费面。

## Failures

- 无 with-skill assertion failure。
- Harness limitation：baseline 父仓库 Git 命令只暴露文件名/状态，未读取目标 skill/README 内容；未影响版本来源与 handoff 字段判断。后续应隔离 scratch Git 元数据。

## Next Steps

- 保持 release mode 的 product/ops 窄范围、Release Notes 零写入与确认版本来源回归。

## Runtime Artifact Policy

- workspace 副本、依赖、candidate、transcript、manifest、diff 与状态仅位于 `tmp/eval-runs/117-adjacent/`，不提交到 git。
