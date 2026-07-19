# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-003-route-release-audit`

## Test Set / Fixture Version

- Fixture version: `issue #117 cross-doc audit 2026-07-19`
- Fresh run: `tmp/eval-runs/117-adjacent/docs-agent/eval-003-route-release-audit/`
- Source head: `00c9741dabc24f6b6df377c69c42adb989722648` plus the current issue #117 working tree

## Latest Result

**PASS（3/3 assertions）** — with-skill 接受等效确认 release chain，保留 v0.4.0 与 release 证据，正确路由 `docs-audit`，并只引用 specialist gate，没有执行审计协议。

## Assertions

- `accepts_equivalent_chain`：PASS。识别已确认 scope、v0.4.0、changelog、contract/CI 证据和既有站点为有效入口。
- `routes_docs_audit`：PASS。明确选择 `docs-audit`，保留版本与证据，当前轮停在路由 handoff。
- `references_audit_gate_only`：PASS。只指向 `docs-audit/SKILL.md` 及内部指令，没有复制双阶段审计、状态或盖章协议。

## With-Skill Behavior

- fresh candidate 读取本轮注入的 router skill、Docs README、共享 frontmatter 指针和 eval definition。
- 输出仅做入口检查、分流与上下文保留；workspace 无业务文件差异。

## Without-Skill Baseline

- 来源：同一 prompt 与 pristine fixture 的本轮 fresh `without_skill`，不含目标 skill、内部指令、Docs README、旧 comparison 或 with-skill 输出；未复用历史 baseline。
- baseline 能识别入口并路由 `docs-audit`，但没有引用权威 specialist gate，因此不稳定满足 gate-only assertion。

## Failures

- 无 with-skill assertion failure。
- Harness limitation：baseline 执行 `git status`/`git diff` 时可见父仓库文件名与状态；transcript 未读取目标 skill 或 Docs README 内容，判断该噪声未改变本用例路由语义。后续应使用隔离 scratch Git 仓库或 Git ceiling。

## Next Steps

- 保持 router 只引用 specialist gate；后续 router 或 docs-audit 入口语义变化时重新 fresh 验证。

## Runtime Artifact Policy

- candidate、transcript、manifest、diff 与状态文件仅保留在 `tmp/eval-runs/117-adjacent/`，不提交到 git。
