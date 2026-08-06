# Eval Result: eval-008-feature-path-mismatch-blocked

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-008-feature-path-mismatch-blocked`
- Test case: feature-path-mismatch-blocked
- Workspace: `workspace/eval-008-feature-path-mismatch-blocked`
- Evaluation date: 2026-08-07
- Overall result: PASS
- Behavior result: PASS
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 请根据 docs/pm/chat-interface/history-search/PRD.md 和 docs/engineer/chat-interface/TRD.md 实现 Chat History Search。两份文档记录的功能路径不一致：PRD 是 chat-interface/history-search，TRD 是 chat-interface。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `detects_prd_trd_path_mismatch`: 明确指出 PRD feature_path 为 `chat-interface/history-search`、TRD feature_path 为 `chat-interface`，且 transcript 实际读取并确认了两者。
- PASS `checks_related_prd`: 明确指出 TRD related_prd 指向 `docs/pm/chat-interface/PRD.md`，而非目标 PRD 路径。
- PASS `blocks_implementation_plan`: 明确表示未创建计划、未修改代码；transcript 无写入命令，目标 IMPLEMENTATION_PLAN.md 不存在，workspace 文档哈希与 fixture 一致。
- PASS `hands_off_to_trd_gen`: 明确要求交回 `engineer-agent:trd-gen`，生成与目标 PRD 对齐的 TRD。

## With Skill Behavior

with_skill 四项断言均满足，且 exit_code 为 0、JSONL transcript 有效、workspace 未发生实现性变更。

## Without Skill Baseline

without_skill 仅作对照：识别了路径冲突，但未明确检查 related_prd，也未交回 engineer-agent:trd-gen。

## Failures / Findings

- None.
- Root cause: None.

## Next Steps

- 后续修改该 skill、fixture 或 assertions 时，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-008-feature-path-mismatch-blocked

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-008-feature-path-mismatch-blocked`
- Test case: feature-path-mismatch-blocked
- Workspace: `workspace/eval-008-feature-path-mismatch-blocked`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture files read before skill use: `README.md`, `eval_metadata.json`, `docs/pm/chat-interface/history-search/PRD.md`, and `docs/engineer/chat-interface/TRD.md`.
- Fixture summary: the PRD declares `feature_path: chat-interface/history-search`; the TRD declares parent `feature_path: chat-interface` and `related_prd: docs/pm/chat-interface/PRD.md`.
- Expected output: detect PRD/TRD metadata and related PRD mismatch, block implementation planning, and hand back to `engineer-agent:trd-gen`.

## Assertions

- PASS `detects_prd_trd_path_mismatch`: the skill requires matching PRD/TRD `feature_path`, `parent_feature`, and `feature_level`.
- PASS `checks_related_prd`: output conventions and planner require TRD `related_prd` to point to `docs/pm/{feature_path}/PRD.md`.
- PASS `blocks_implementation_plan`: mismatched TRD blocks `docs/engineer/chat-interface/history-search/IMPLEMENTATION_PLAN.md`, code, and tests.
- PASS `hands_off_to_trd_gen`: stale, incomplete, path-mismatched, or conflicting TRDs return to `engineer-agent:trd-gen`.

## With Skill Behavior

Fresh with-skill validation confirmed that Batch 3's direct specialist gate is not diluted by a parent TRD. The current skill should compare the nested PRD with the supplied parent TRD, explicitly report `chat-interface/history-search` versus `chat-interface`, detect that `related_prd` points to `docs/pm/chat-interface/PRD.md` instead of the nested PRD, and stop before writing any plan. The correct handoff is to `engineer-agent:trd-gen` to create or correct the mirrored nested TRD.

## Without Skill Baseline

The fresh without-skill baseline was summarized before reading skill docs. A generic response could accept the parent Chat Interface TRD as close enough and proceed with a plan, or mention mismatch without validating `related_prd`. It would not reliably enforce the mirrored feature path and related-PRD gates before planning.

## Failures

- None.

## Next Steps

- Keep this eval focused on blocking parent/child feature path mismatches before implementation planning.

## Runtime Artifacts Policy

- This validation did not create runtime artifacts.
- Runtime transcripts, verdicts, timing files, outputs, diagnostics, run status files, and `comparison.auto.md` must not be committed.
