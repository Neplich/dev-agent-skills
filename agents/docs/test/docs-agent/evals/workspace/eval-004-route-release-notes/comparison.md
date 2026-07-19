# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-004-route-release-notes`

## Test Set / Fixture Version

- Fixture version: `issue #117 cross-doc audit 2026-07-19`
- Fresh run: `tmp/eval-runs/117-adjacent/docs-agent/eval-004-route-release-notes/`
- Source head: `00c9741dabc24f6b6df377c69c42adb989722648` plus the current issue #117 working tree

## Latest Result

**PASS（4/4 assertions）** — with-skill 接受完整 Release Notes entry basis，保留全部 handoff 上下文，选择 `release-notes-generator`，且没有复制或执行 specialist 协议。

## Assertions

- `accepts_release_notes_entry_basis`：PASS。识别宿主、维护者确认版本、scope、证据与站内页面/下游 handoff 要求。
- `routes_release_notes_generator`：PASS。明确选择 `release-notes-generator`，排除 sync、audit、bootstrap 与 GitHub Release 当前执行。
- `preserves_handoff_context`：PASS。保留 request、tier、feature、version、scope、host、source、evidence、output 与 risk 字段。
- `references_release_notes_gate_only`：PASS。仅指向 specialist SKILL 及内部指令，没有复制七步流程或执行正文、metadata、checks、#117/#120 handoff。

## With-Skill Behavior

- fresh candidate 只完成 router 入口检查和分流，workspace 零写入。
- 输出明确正文确认与宿主检查仍由 specialist gate 处理，当前轮未自动继续。

## Without-Skill Baseline

- 来源：同一 prompt 与 pristine fixture 的本轮 fresh `without_skill`；不含目标 skill、Docs README、旧 comparison 或 with-skill 输出，未复用历史 baseline。
- baseline 能识别大方向，但未命名 `release-notes-generator`、未完整保留 request/host 等字段，也未引用权威 gate，协议稳定性明显较弱。

## Failures

- 无 with-skill assertion failure。
- Harness limitation：baseline 可通过父仓库 Git 命令看到文件名/状态，但未读取目标 skill 或 README 内容；未影响本用例的语义差异。后续应隔离 scratch Git 元数据。

## Next Steps

- 保持 Release Notes 窄路由与 specialist 单一真源；入口字段或边界变化时重跑。

## Runtime Artifact Policy

- candidate、transcript、manifest、diff 与状态文件仅保留在 `tmp/eval-runs/117-adjacent/`，不提交到 git。
