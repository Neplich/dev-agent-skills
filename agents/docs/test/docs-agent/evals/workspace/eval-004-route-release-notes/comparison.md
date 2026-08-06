# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-004-route-release-notes`

## Test Set / Fixture Version

- Fixture version: `release-handoff.md`（fixture 身份文本 2026-07-29 更新后）
- Fresh run（2026-08-03，#188）：`tmp/eval-runs/issue-188-docs/with_skill/eval-004-route-release-notes/candidate-output.md` 与 `tmp/eval-runs/issue-188-docs/without_skill/eval-004-route-release-notes/candidate-output.md`
- Judge verdict: `tmp/eval-runs/issue-188-docs/judge/verdict.md`

## Latest Result

- Behavior result: `FAIL`（with）/ `FAIL`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `FULL`（with）/ `FULL`（without）— 本轮重跑实际触发的断言场景
- Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| accepts_release_notes_entry_basis | FAIL | FAIL | with_skill 仅笼统称 `release-handoff.md` 为完整交接包，未逐项保留宿主、scope、证据来源等依据；without_skill 只确认 `existing_update`、`major` 和 `v1.0.0`，并称相关证据文件不存在，未接受完整 specialist entry basis。 |
| routes_release_notes_generator | PASS | FAIL | with_skill 明确路由至 `docs-agent:release-notes-gen`；without_skill 仅写“由 Docs specialist 生成”，未选择 `release-notes-gen`。 |
| preserves_handoff_context | FAIL | FAIL | 两条 lane 均未在结果中保留完整的 `request_type`、`change_tier`、`feature_path`、`release_scope`、`host_repository`、`source_documents`、`evidence_sources`、`required_output` 和 `blockers_risks`。 |
| references_release_notes_gate_only | FAIL | FAIL | 两条 lane 均未指向 `release-notes-gen/SKILL.md` 或其内部指令；未复制详细协议，但缺少必要的 specialist gate 指针。 |

未满足断言（with/without 任一 FAIL）：`accepts_release_notes_entry_basis`、`routes_release_notes_generator`、`preserves_handoff_context`、`references_release_notes_gate_only`



## Fixture Drift Notice

fixture 身份文本已于 2026-07-29 从 issue 编号更新为 skill 名，旧 PASS 反映变更前 run。**2026-08-03（#188）已对当前 fixture 完成 fresh re-baseline**（with/without 双侧验证，judge 独立判定，证据见 `tmp/eval-runs/issue-188-docs/`），BLOCKED 状态消解；本节保留作为历史记录。

## Historical Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 2026-07-19（fixture 下游指向修正前）：**PASS（4/4 assertions）** — with-skill 接受完整 Release Notes entry basis，保留全部 handoff 上下文，选择 `release-notes-gen`，且没有复制或执行 specialist 协议。

## Assertions
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `accepts_release_notes_entry_basis`：PASS。识别宿主、维护者确认版本、scope、证据与站内页面/下游 handoff 要求。
- `routes_release_notes_generator`：PASS。明确选择 `release-notes-gen`，排除 sync、audit、bootstrap 与 GitHub Release 当前执行。
- `preserves_handoff_context`：PASS。保留 request、tier、feature、version、scope、host、source、evidence、output 与 risk 字段。
- `references_release_notes_gate_only`：PASS。仅指向 specialist SKILL 及内部指令，没有复制七步流程或执行正文、metadata、checks、#117/#120 handoff。

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- fresh candidate 只完成 router 入口检查和分流，workspace 零写入。
- 输出明确正文确认与宿主检查仍由 specialist gate 处理，当前轮未自动继续。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：同一 prompt 与 pristine fixture 的本轮 fresh `without_skill`；不含目标 skill、Docs README、旧 comparison 或 with-skill 输出，未复用历史 baseline。
- baseline 已命名并正确路由 `docs-agent:release-notes-gen`（accepts 与 routes 两条断言 PASS），但未完整保留 handoff context（缺 `host_repository`、原始 `release_scope`），且复制了 specialist 流程、未引用权威 gate——2/4 PASS。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 无 with-skill assertion failure。
- Harness limitation：baseline 可通过父仓库 Git 命令看到文件名/状态，但未读取目标 skill 或 README 内容；未影响本用例的语义差异。后续应隔离 scratch Git 元数据。

## Next Steps

- 保持 Release Notes 窄路由与 specialist 单一真源；入口字段或边界变化时重跑。

## Runtime Artifact Policy

- candidate、transcript、manifest、diff 与状态文件仅保留在 `tmp/eval-runs/issue-188-docs/`，不提交到 git。
