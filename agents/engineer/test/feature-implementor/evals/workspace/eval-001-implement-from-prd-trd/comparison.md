# Eval Result: eval-001-implement-from-prd-trd

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-001-implement-from-prd-trd`
- Test case: implement-from-prd-trd
- Workspace: `workspace/eval-001-implement-from-prd-trd`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 根据 docs/pm/notification-center/PRD.md 和 docs/engineer/notification-center/TRD.md 实现用户通知功能
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- FAIL `writes_implementation_plan`: final.md 未包含实现计划、文件变更清单或实现顺序；workspace 中也不存在 IMPLEMENTATION_PLAN.md。
- FAIL `requires_user_confirmation`: 仅说明补齐文档后才能创建计划，未明确要求用户确认实施计划后再编码。
- PASS `does_not_implement_directly`: final.md 和 with_skill transcript 均未声称已创建/修改代码、运行实现步骤或完成自检。workspace 仅有既有指令文件，无代码变更。
- FAIL `maintains_plan_metadata`: 输出未说明 IMPLEMENTATION_PLAN.md frontmatter 的 version、last_updated 或版本维护规则。

## With Skill Behavior

with_skill 正确识别工作区缺少 PRD/TRD，并未直接写代码；但未按 expected_output 生成计划内容、文件清单、顺序、确认门禁或计划元数据说明。output.sha256 与 workspace 文件逐项校验通过。

## Without Skill Baseline

without_skill 同样发现工作区为空并停止；仅作对照，不影响 with_skill 判定。其 input/output hash 文件为空，workspace 无 .git。

## Failures / Findings

- writes_implementation_plan
- requires_user_confirmation
- maintains_plan_metadata
- Root cause: 实际 fixture workspace 不含用户指定的 PRD/TRD，with_skill 因门禁阻塞而只输出缺失文档提示；该输出未满足 eval.json 明确要求的计划与确认协议。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-001-implement-from-prd-trd

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-001-implement-from-prd-trd`
- Test case: implement-from-prd-trd
- Workspace: `workspace/eval-001-implement-from-prd-trd`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: metadata-only case whose prompt supplies the confirmed `notification-center` PRD/TRD paths and whose expected output defines the planning behavior.
- Fixture version: current HEAD `a452319`.
- Fresh run time: `2026-08-03 11:58:13 +0800`.
- Runtime directory: `tmp/eval-runs/issue-198-brd/engineer/20260803-115813/feature-implementor/eval-001-implement-from-prd-trd/`.
- Expected output: produce or update `docs/engineer/notification-center/IMPLEMENTATION_PLAN.md` with the file change list, implementation order, metadata rules, and user-confirmation gate; do not code directly.

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


All 4 assertions were exercised and passed. Removing BRD from the planner input list did not weaken PRD/TRD alignment, durable plan metadata, or the pre-code confirmation gate.

## Assertion Results

- PASS `writes_implementation_plan`: identifies `docs/engineer/notification-center/IMPLEMENTATION_PLAN.md` and requires a source-traceable file list, ordered implementation steps, tests, and verification before implementation.
- PASS `requires_user_confirmation`: stops after presenting the exact plan and requires explicit user confirmation before loading the implementation phase.
- PASS `does_not_implement_directly`: does not claim code changes, implementation execution, tests, or self-review have occurred.
- PASS `maintains_plan_metadata`: requires an initial `version`, `last_updated`, feature-path linkage, and synchronized version/date updates for substantive plan changes while allowing typo-only edits not to bump the version.

## With-Skill Behavior

The fresh with-skill run applies the planner phase only, carries the prompt-declared same-path PRD/TRD through the fixture's metadata-only convention, and states the full alignment checks required in a real host workspace. It produces the durable plan path, the required file-list and dependency-order behavior, verification and delegation fields, and the frontmatter maintenance contract, then waits for confirmation without coding. The planner now consumes PRD plus `DECISIONS.md` or equivalent product decisions and TRD; no removed BRD prerequisite remains.

## Fresh Without-Skill Baseline

The without-skill baseline was newly generated in this run from the same prompt and fixture without applying `feature-implementor`, the Engineer README, with-skill output, historical comparison, or any prior baseline. It suggests reading the specs and planning before implementation, but does not require the durable plan path, exact metadata/version rules, or a hard confirmation boundary. Baseline assertion result: 1/4.

## Failures

- None.

## Next Steps

- Keep this eval focused on the PRD/TRD-to-plan gate, plan metadata maintenance, and no-direct-code boundary after BRD removal.

## Runtime Artifact Policy

- Fresh runtime evidence is under `tmp/eval-runs/issue-198-brd/engineer/20260803-115813/feature-implementor/eval-001-implement-from-prd-trd/`.
- `with_skill.md`, `without_skill.md`, and `verdict.md` are ignored scratch evidence and must not be committed.
- This `comparison.md` is the only durable result for this case.
