# Eval Result: eval-003-missing-trd-handoff

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-003-missing-trd-handoff`
- Test case: missing-trd-handoff
- Workspace: `workspace/eval-003-missing-trd-handoff`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 请根据 docs/pm/capture-loop/PRD.md 实现 Capture Loop 队列重试能力。当前 workspace 没有 docs/engineer/capture-loop/TRD.md。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `detects_missing_engineer_trd`: final.md 明确指出缺少 `docs/engineer/capture-loop/TRD.md`。
- PASS `hands_off_to_trd_gen`: final.md 明确要求转回 `engineer-agent:trd-gen` 补齐并确认 TRD。
- PASS `does_not_write_plan_or_code`: final.md 明确写明未创建计划、未修改代码；workspace 输出 hash 与输入 hash 一致，且无 IMPLEMENTATION_PLAN、代码或测试文件。
- PASS `names_required_trd_decisions`: final.md 列出重试策略、受影响组件/API/集成、幂等并发持久化、验证命令/测试、发布迁移回滚风险等缺失决策。
- FAIL `keeps_finder_trd_gen_boundary`: 虽要求转回 `engineer-agent:trd-gen`，但未明确说明发现者只负责说明 TRD 缺口、由 trd-gen 负责补完整 TRD。

## With Skill Behavior

with_skill 正确识别缺失 TRD、停止实现并完成大部分 gap packet；但缺少明确的 finder/trd-gen 职责边界表述。transcript 仅记录该最终回复，workspace hash 未发生变化。

## Without Skill Baseline

without_skill 仅以缺少源码、测试和 TRD 为由阻止实现，未按要求交回 `engineer-agent:trd-gen`，也未列出完整 TRD gap packet；transcript 中曾出现实现计划意图，但 workspace hash 未发生变化。

## Failures / Findings

- keeps_finder_trd_gen_boundary 未满足：最终输出没有明确声明发现者仅说明缺口、trd-gen 负责补完整 TRD。
- Root cause: 最终 handoff 文案缺少 skill 要求的显式职责边界句。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-003-missing-trd-handoff

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-003-missing-trd-handoff`
- Test case: missing-trd-handoff
- Workspace: `workspace/eval-003-missing-trd-handoff`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture files read before skill use: `README.md`, `eval_metadata.json`, and `docs/pm/capture-loop/PRD.md`.
- Fixture summary: PM scope exists for Capture Loop retry behavior, but `docs/engineer/capture-loop/TRD.md` is intentionally absent.
- Expected output: stop before `IMPLEMENTATION_PLAN.md` and code, hand off to `engineer-agent:trd-gen`, and provide a complete TRD gap packet.

## Assertions

- PASS `detects_missing_engineer_trd`: the alignment gate requires `docs/engineer/{feature_path}/TRD.md` before planning.
- PASS `hands_off_to_trd_gen`: missing, stale, incomplete, path-mismatched, or conflicting TRDs return to `engineer-agent:trd-gen`.
- PASS `does_not_write_plan_or_code`: planner stops before implementation plan, code, tests, or file-change plan when TRD is missing.
- PASS `names_required_trd_decisions`: the TRD gap packet must cover technical decisions, components, data/API/integration impacts, validation commands, rollout risks, and error handling/observability/security strategy.
- PASS `keeps_finder_trd_gen_boundary`: planner states the finder only clarifies gaps and `trd-gen` completes the TRD.

## With Skill Behavior

Fresh with-skill validation confirmed that the direct specialist gate remains strict: a PRD alone is not an equivalent confirmed document chain. The current skill should resolve `feature_path: capture-loop`, detect the missing mirrored Engineer TRD, and stop before creating `docs/engineer/capture-loop/IMPLEMENTATION_PLAN.md`. It should hand the work to `engineer-agent:trd-gen` with the required TRD gap packet and boundary statement.

## Without Skill Baseline

The fresh without-skill baseline was summarized before reading skill docs. Because the prompt explicitly says the TRD is missing and says not to code, a generic response might still block direct implementation. Its likely weakness is an incomplete handoff: it may not name all missing technical decisions, may omit validation and rollout/error strategy, and may not clearly separate the finder role from `engineer-agent:trd-gen`.

## Failures

- None.

## Next Steps

- Keep this eval focused on missing-TRD blocking and full TRD gap handoff.

## Runtime Artifacts Policy

- This validation did not create runtime artifacts.
- Runtime transcripts, verdicts, timing files, outputs, diagnostics, run status files, and `comparison.auto.md` must not be committed.
