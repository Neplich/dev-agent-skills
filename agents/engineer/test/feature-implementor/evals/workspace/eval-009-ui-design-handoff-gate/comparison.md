# Eval Result: eval-009-ui-design-handoff-gate

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-009-ui-design-handoff-gate`
- Test case: ui-design-handoff-gate
- Workspace: `workspace/eval-009-ui-design-handoff-gate`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: docs/pm/customer-portal/profile-settings/PRD.md 和 docs/engineer/customer-portal/profile-settings/TRD.md 已确认。请更新设置页前端 UI 的信息层级和主按钮样式；当前 workspace 没有对应的 UI/UX 或视觉设计文档。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `detects_ui_design_change`: with_skill final 明确将信息层级和主按钮视觉变更归入 UI Design Handoff Gate。
- PASS `checks_design_docs`: transcript 实际检查设计目录；workspace 中 ui-ux-spec.md 与 visual-system.md 均不存在。
- PASS `blocks_plan_when_design_missing`: final 明确停止实现计划和代码修改；workspace 中不存在 IMPLEMENTATION_PLAN.md。
- PASS `hands_off_to_designer`: final 明确通过 engineer-agent 转交 designer-agent 补齐设计交付物。
- FAIL `preserves_plan_gate_after_design`: 未明确说明设计完成后由 feature-implementor 编写 IMPLEMENTATION_PLAN.md、等待用户确认且不能直接编码。
- PASS `does_not_implement_directly`: final 未声称修改代码、运行测试或完成实现；workspace hash 与输入一致，未发现新增实现文件。

## With Skill Behavior

正确识别设计交接门禁并阻断计划和实现，但遗漏设计完成后的计划编写与用户确认门禁。

## Without Skill Baseline

对照组也停止了实施，但 transcript 曾计划实现并运行检查；仅作对照。

## Failures / Findings

- preserves_plan_gate_after_design
- Root cause: with_skill 的 handoff 输出省略了 expected_output 要求的后续 IMPLEMENTATION_PLAN、用户确认和禁止直接编码步骤。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-009-ui-design-handoff-gate

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-009-ui-design-handoff-gate`
- Test case: ui-design-handoff-gate
- Workspace: `workspace/eval-009-ui-design-handoff-gate`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture files read before skill use: `README.md`, `eval_metadata.json`, `docs/pm/customer-portal/profile-settings/PRD.md`, and `docs/engineer/customer-portal/profile-settings/TRD.md`.
- Fixture summary: PM/TRD documents exist for `customer-portal/profile-settings`, but same-feature `docs/design/customer-portal/profile-settings/ui-ux-spec.md` and `visual-system.md` are intentionally missing.
- Expected output: identify a frontend UI/visual change, block implementation planning, hand design work back through Engineer to Designer, and preserve the plan gate after design docs are supplied.

## Assertions

- PASS `detects_ui_design_change`: information hierarchy and primary button styling are frontend UI/visual changes.
- PASS `checks_design_docs`: the skill checks same-feature `ui-ux-spec.md` and `visual-system.md`.
- PASS `blocks_plan_when_design_missing`: missing design deliverables block `docs/engineer/customer-portal/profile-settings/IMPLEMENTATION_PLAN.md`.
- PASS `hands_off_to_designer`: the gap is handed through `engineer-agent` to `designer-agent`.
- PASS `preserves_plan_gate_after_design`: after Designer resolves the gap, feature-implementor must still write a plan and wait for confirmation.
- PASS `does_not_implement_directly`: no frontend code, tests, or verification are performed before design and plan gates.

## With Skill Behavior

Fresh with-skill validation confirmed the UI Design Handoff Gate. The current skill enters the gate for frontend UI, interaction, visual, component, usability, or information hierarchy changes. Since the fixture lacks the same-feature design docs, the skill must stop before planning and hand the missing design deliverables back through Engineer to Designer. Once design docs exist and cover the change, the implementation still returns to `feature-implementor` for `IMPLEMENTATION_PLAN.md` and user confirmation before coding.

## Without Skill Baseline

The fresh without-skill baseline was summarized before reading skill docs. A generic frontend implementation response is likely to propose layout, hierarchy, and button style changes directly from PRD/TRD or start a code plan. It would not reliably require same-feature UI/UX and visual-system documents, block the implementation plan, or preserve the Designer handoff before coding.

## Failures

- None.

## Next Steps

- Keep this eval as regression coverage for UI design handoff gating.

## Runtime Artifacts Policy

- This validation did not create runtime artifacts.
- Runtime transcripts, verdicts, timing files, outputs, diagnostics, run status files, and `comparison.auto.md` must not be committed.
