# Skill Eval Comparison

## Evaluation Target

- Skill: `release-notes-generator`
- Eval: `eval-002-confirmation-gate`

## Test Set / Fixture Version

- Fixture version: `issue #117 cross-doc audit 2026-07-19`
- Fresh run: `tmp/eval-runs/117-adjacent/release-notes-generator/eval-002-confirmation-gate/`
- Source head: `00c9741dabc24f6b6df377c69c42adb989722648` plus the current issue #117 working tree

## Latest Result

**PASS（3/3 assertions）** — with-skill 只生成并完整展示候选页，index、metadata、导航零变化，明确 blocked/unconfirmed 并等待维护者确认。

## Assertions

- `keeps_derived_surfaces_unchanged`：PASS。哈希与 diff 证明 index、`.meta/releases.json`、导航配置及 `.generated` 均未变化。
- `reports_unconfirmed_not_ready`：PASS。报告 `confirmation_status: unconfirmed`、`handoff_status: blocked`，没有把候选页描述为 ready。
- `waits_for_explicit_confirmation`：PASS。完整展示正文、证据与确认后计划路径，不模拟确认，也不执行确认后检查或派生写入。

## With-Skill Behavior

- 候选页保持 `last_verified_version: unverified`；结构化 handoff 明确两个 blocker。
- `npm ci` 与 `npm run test:docs` 正确保留在确认后阶段，本轮均记录为 `not_run`。

## Without-Skill Baseline

- 来源：同一 prompt 与 pristine fixture 的本轮 fresh `without_skill`；不含目标 skill、Docs README、旧 comparison 或 with-skill 输出，未复用历史 baseline。
- baseline 保持派生面不变并 blocked，但实际运行了确认后宿主检查，且最终输出没有展示完整候选正文、确认后修改计划与结构化 blocked handoff，因此确认门禁表达不完整。

## Failures

- 无 with-skill assertion failure。
- Harness limitation：父仓库 Git 元数据仅向 baseline 暴露文件名/状态，未读取目标 skill/README 内容；未改变确认前后时序判断。后续应隔离 scratch Git 元数据。

## Next Steps

- 保持“候选展示与明确确认”作为派生写入和宿主 ready 检查的前置门禁。

## Runtime Artifact Policy

- 候选页、candidate、transcript、manifest、diff 与状态仅位于 `tmp/eval-runs/117-adjacent/`，不提交到 git。
