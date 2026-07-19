# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-008-deployment-ops-upgrade`

## Test Set / Fixture Version

- Fixture version: `issue #117 cross-doc audit 2026-07-19`
- Fresh run: `tmp/eval-runs/117-adjacent/formal-docs-sync/eval-008-deployment-ops-upgrade/`
- Source head: `00c9741dabc24f6b6df377c69c42adb989722648` plus the current issue #117 working tree

## Latest Result

**PASS（5/5 assertions）** — with-skill 仅基于已执行 Compose 证据同步 Ops 当前状态，排除 Kubernetes/Helm 计划，页面和映射保持原子且 `unverified`，检查通过后交接 #117。

## Assertions

- `uses_executed_deployment_evidence`：PASS。使用 Compose、实际命令退出状态、健康结果和环境差异，不把计划当事实。
- `writes_current_ops_upgrade_rollback`：PASS。记录默认 v1.4.2、启动/升级、`/healthz` 200 与回滚 v1.4.1 后复检。
- `does_not_promote_plan_to_current_state`：PASS。明确 Kubernetes/Helm 未执行、当前不支持。
- `keeps_ops_scope_atomic_and_unverified`：PASS。只更新目标 Ops 页面与 `deploy/**` 映射，回读后页面为 `unverified`，其他类型与 Release Notes 零变化。
- `runs_ops_host_checks_and_handoffs`：PASS。锁定安装后 `npm run test:docs` 73/73 通过，handoff #117，未执行部署。

## With-Skill Behavior

- pre-tag handoff 等待维护者确认 `target_release_version`，未从运行镜像或 refs 推测版本。
- 初次缺依赖失败后按 lockfile 安装并完整重跑成功，保留真实执行轨迹。

## Without-Skill Baseline

- 来源：同一 prompt 与 pristine fixture 的本轮 fresh `without_skill`；不含目标 skill、Docs README、旧 comparison 或 with-skill 输出，未复用历史 baseline。
- baseline 借助强 fixture 也完成主要页面事实和宿主检查，但没有显式报告 `unverified`、原子范围及“等待维护者确认 target_release_version”的 pre-tag blocked 语义。

## Failures

- 无 with-skill assertion failure。
- Harness limitation：baseline 可见父仓库文件名/状态但未读目标 skill/README 内容；未影响部署证据与未执行计划的判定。后续应隔离 scratch Git 元数据。

## Next Steps

- 继续将“已执行证据、计划排除、unverified、确认版本门禁”作为一组回归标准。

## Runtime Artifact Policy

- workspace 副本、依赖、candidate、transcript、manifest、diff 与状态仅位于 `tmp/eval-runs/117-adjacent/`，不提交到 git。
