# Skill Eval Comparison

## Evaluation Target

- Skill: `release-notes-generator`
- Eval: `eval-001-generate-site-release-notes`

## Test Set / Fixture Version

- Fixture version: `issue #117 cross-doc audit 2026-07-19`
- Fresh run: `tmp/eval-runs/117-adjacent/release-notes-generator/eval-001-generate-site-release-notes/`
- Source head: `00c9741dabc24f6b6df377c69c42adb989722648` plus the current issue #117 working tree

## Latest Result

**PASS（5/5 assertions）** — with-skill 完成六类证据页面、确认后派生写入和真实宿主检查，页面保持 `unverified`，并输出字段完整的 issue #117 pre-tag ready handoff。

## Assertions

- `preserves_six_evidence_categories`：PASS。功能、架构、数据库、部署、资产、升级兼容与风险均保留关键事实和来源。
- `uses_release_frontmatter_contract`：PASS。七字段完整，`doc_type: release`，owners/related_code 非空，`last_verified_version: unverified`。
- `enforces_confirmation_before_derived_writes`：PASS。候选页先生成并回读，应用 `confirmation-record.md` 后才更新 index/metadata；导航由宿主生成且未手工修改。
- `runs_real_host_docs_checks`：PASS。在 `docs/site/` 执行 `npm ci --ignore-scripts` 和 `npm run test:docs`，最终 74/74 通过。
- `returns_complete_ready_handoff`：PASS。仅在版本与正文确认、宿主检查全部满足后 ready，包含规定字段且 `release_execution_authorized: false`。

## With-Skill Behavior

- 页面等待 #117 统一盖章，没有把站内 Release Notes 描述为已发布。
- handoff 直接进入 issue #117 pre-tag，并保留 issue #120 downstream owner 与 GitHub Release/tag 边界。

## Without-Skill Baseline

- 来源：同一 prompt 与 pristine fixture 的本轮 fresh `without_skill`；不含目标 skill、Docs README、旧 comparison 或 with-skill 输出，未复用历史 baseline。
- baseline 虽生成页面并通过检查，却把 `last_verified_version` 直接写成 `v1.0.0`，还写入 `verifiedDocs`；其 handoff 缺少规定的 confirmation source、`next_gate`、`release_execution_authorized`、完整 updated surfaces/source evidence/blockers 语义，未满足双阶段边界。

## Failures

- 无 with-skill assertion failure。
- Harness limitation：baseline 的父仓库 Git 命令只暴露文件名/状态，未读取目标 skill/README 内容；这不能解释其提前盖章和 handoff 字段缺失。后续应隔离 scratch Git 元数据。

## Next Steps

- 继续以 `unverified` 页面和完整 #117 pre-tag handoff 作为回归门禁。

## Runtime Artifact Policy

- 页面副本、依赖、candidate、transcript、manifest、diff 与状态仅位于 `tmp/eval-runs/117-adjacent/`，不提交到 git。
