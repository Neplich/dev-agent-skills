# Eval Result: eval-006-small-bug-fix-plan-gate

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-006-small-bug-fix-plan-gate`
- Test case: small-bug-fix-plan-gate
- Workspace: `workspace/eval-006-small-bug-fix-plan-gate`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 通知中心 active 列表没有排除 archived，已经确认这是实现偏离 PRD/TRD，不是需求变更；根因是 src/api/notifications.ts 的过滤条件少了 archived。请修复这个单文件问题。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- FAIL `treats_bug_fix_as_spec_backed`: with_skill 错误称无法确认 PRD/TRD 已批准行为，并要求补充 PM/Engineer 文档；未按 prompt 说明 debugger 已确认这是实现偏离，且不应要求 DECISIONS.md。
- FAIL `writes_bug_fix_implementation_plan`: final 明确表示不能创建 IMPLEMENTATION_PLAN.md；workspace 中也不存在该文件。
- FAIL `records_no_complex_split`: 未说明这是单文件小修复、无需复杂 sub-agent split。
- PASS `waits_before_fixing`: transcript 明确表示计划确认前不会改代码；final 未声称已修复或验证通过，workspace 也无目标代码修改。
- FAIL `prepares_e2e_handoff_after_fix`: 未说明修复后向 QA E2E 文档流程交接所需内容，也未说明计划确认前不得更新 E2E TC。

## With Skill Behavior

with_skill 实际读取了 workspace 和 planner 规则，但将 prompt 已确认的 spec-backed bug fix 错误阻塞，未产出实施计划。hash 与 workspace 文件清单一致，未见写入目标文件。

## Without Skill Baseline

without_skill 作为对照，发现工作区为空且无目标文件，未执行修复。

## Failures / Findings

- 未将 bug fix 视为 debugger 已确认的实现偏离。
- 未创建或更新 IMPLEMENTATION_PLAN.md。
- 未记录无需复杂 sub-agent split。
- 未准备 QA E2E 文档交接说明。
- Root cause: with_skill 过度依赖 workspace 中缺失的 PM/TRD 文档链，忽略了用户 prompt 明确提供的 debugger 根因与 PRD/TRD 确认事实，导致错误阻塞。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-006-small-bug-fix-plan-gate

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-006-small-bug-fix-plan-gate`
- Test case: small-bug-fix-plan-gate
- Workspace: `workspace/eval-006-small-bug-fix-plan-gate`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture files read before skill use: `eval_metadata.json` and the `eval-006-small-bug-fix-plan-gate` item in `evals.json`.
- Fixture note: this workspace stores metadata only; the prompt declares debugger has confirmed the issue is an implementation deviation from approved PRD/TRD, not a requirements change.
- Expected output: treat the bug fix as spec-backed implementation work, produce or update `docs/engineer/notifications/IMPLEMENTATION_PLAN.md`, record `src/api/notifications.ts` and verification commands, wait for confirmation, and do not fix code yet.

## Assertions

- PASS `treats_bug_fix_as_spec_backed`: the skill allows spec-backed bug fixes after debugger or Engineer routing confirms approved PRD/TRD behavior.
- PASS `writes_bug_fix_implementation_plan`: even single-file bug fixes require `IMPLEMENTATION_PLAN.md`, file scope, and verification commands.
- PASS `records_no_complex_split`: the small-fix path can skip complex sub-agent split while still documenting that decision.
- PASS `waits_before_fixing`: implementor entry gate blocks code and test edits until the exact plan is confirmed.
- PASS `prepares_e2e_handoff_after_fix`: after implementation and self-review, QA E2E handoff needs PRD/TRD alignment, confirmed plan, changed files, verification commands/results, risks, and suggested feature tree directory.

## With Skill Behavior

Fresh with-skill validation confirmed that the small bug-fix path still runs through planner. Because the prompt says debugger already established this is a deviation from approved PRD/TRD behavior, the request may enter `feature-implementor`; it must not be sent back to PM just because there is no standalone `DECISIONS.md`. The plan should target `docs/engineer/notifications/IMPLEMENTATION_PLAN.md`, name `src/api/notifications.ts`, record deterministic verification commands, state no complex implementation/validation split is needed, and wait for confirmation before any code change or QA E2E update.

## Without Skill Baseline

The fresh without-skill baseline was summarized before reading skill docs. A generic worker is likely to honor "but first don't edit code" and produce some repair notes, but it may not create a durable implementation plan, may not distinguish spec-backed bug fix from generic debugging, may skip the split decision, and may omit the post-fix QA E2E handoff constraints.

## Failures

- None.

## Next Steps

- Keep this eval focused on spec-backed bug fixes requiring a plan and confirmation even when the code change is single-file.

## Runtime Artifacts Policy

- This validation did not create runtime artifacts.
- Runtime transcripts, verdicts, timing files, outputs, diagnostics, run status files, and `comparison.auto.md` must not be committed.
