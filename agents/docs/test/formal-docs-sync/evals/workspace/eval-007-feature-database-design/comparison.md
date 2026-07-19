# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-007-feature-database-design`

## Test Set / Fixture Version

- Fixture version: `issue #117 cross-doc audit 2026-07-19`
- Fresh run: `tmp/eval-runs/117-adjacent/formal-docs-sync/eval-007-feature-database-design/`
- Source head: `00c9741dabc24f6b6df377c69c42adb989722648` plus the current issue #117 working tree

## Latest Result

**PASS（6/6 assertions）** — with-skill 通过七项 design closeout，只同步 database/design 当前状态和原子映射，两页保持 `unverified`，宿主检查通过后正确交接 #117。

## Assertions

- `loads_only_database_design_contracts`：PASS。读取 standards、change map、database/design 模板与对应两个类型模块，未读取其他类型模块内容。
- `passes_design_closeout_gate`：PASS。逐项核对 PRD、TRD、计划完成度、diff、required tests 与候选范围确认，七项全部通过后才写入。
- `synchronizes_database_current_state`：PASS。记录组合唯一约束、三种 role、必填 `created_at` 与应用层逻辑引用，不虚构外键。
- `synchronizes_delivered_design`：PASS。记录 workspace/user 顺序校验和 repository upsert，不写 inherited role 或未来架构。
- `updates_atomic_map_and_unverified_pages`：PASS。两页和共享 change-map 原子更新、回读并稳定排序，均保持 `unverified`。
- `runs_host_checks_and_handoffs_audit`：PASS。锁定安装后 `npm run test:docs` 73/73 通过，并 handoff #117 complete affected set。

## With-Skill Behavior

- 没有维护者确认的 `target_release_version`，因此 pre-tag audit 明确 blocked，未推测版本或盖章。
- 初次检查因锁定依赖未安装失败，随后按 lockfile 安装并完整重跑成功，失败证据未被隐藏。

## Without-Skill Baseline

- 来源：同一 prompt 与 pristine fixture 的本轮 fresh `without_skill`；不含目标 skill、Docs README、旧 comparison 或 with-skill 输出，未复用历史 baseline。
- baseline 能生成正确页面、映射并通过检查，但没有读取类型模块的 progressive-loading 证据，最终报告也没有逐项展开七项 closeout 与确认版本缺失时的 blocked pre-tag 语义。

## Failures

- 无 with-skill assertion failure。
- Harness limitation：父仓库 Git 元数据仅暴露文件名/状态，未读取目标 skill/README 内容；未影响页面事实、原子范围或盖章边界判断。后续应隔离 scratch Git 元数据。

## Next Steps

- 保持 design closeout、原子 map/page 更新与缺少确认版本时 blocked 的联合回归。

## Runtime Artifact Policy

- workspace 副本、依赖、candidate、transcript、manifest、diff 与状态仅位于 `tmp/eval-runs/117-adjacent/`，不提交到 git。
