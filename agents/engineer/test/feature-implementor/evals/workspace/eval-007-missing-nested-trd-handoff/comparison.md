# Eval Result: eval-007-missing-nested-trd-handoff

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-007-missing-nested-trd-handoff`
- Test case: missing-nested-trd-handoff
- Workspace: `workspace/eval-007-missing-nested-trd-handoff`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 请根据 docs/pm/chat-interface/history-search/PRD.md 实现 Chat History Search。该 PRD 记录的功能路径是 chat-interface/history-search，但 workspace 没有 docs/engineer/chat-interface/history-search/TRD.md。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `detects_missing_mirrored_trd`: with_skill final 明确指出缺失 docs/engineer/chat-interface/history-search/TRD.md；transcript 也记录了该精确路径检查。
- FAIL `hands_off_to_trd_gen_with_feature_path`: final 确实交回 engineer-agent:trd-gen，并包含 PRD/TRD 路径，但 TRD gap packet 未包含 feature_path、parent_feature、feature_level 这些字段。
- PASS `does_not_write_plan_or_code`: with_skill workspace 仅保留既有 PRD 与规则文件，没有 IMPLEMENTATION_PLAN、代码或测试变更；transcript 未出现 file_change。
- FAIL `keeps_pm_trd_boundary`: final 说明缺 TRD 回 trd-gen，且说明 Finder 不补写 TRD；但没有说明缺 PRD 应回 PM。

## With Skill Behavior

正确识别嵌套路径下缺失的镜像 TRD，并停止计划与实现；但缺口包缺少要求的 feature 元数据，也未完整说明 PRD 缺失时应回 PM 的边界。with_skill output hash 与 workspace 文件哈希一致。

## Without Skill Baseline

without_skill 创建了 docs/engineer/chat-interface/history-search/TRD.md，违反缺失 TRD 时应停止并交回 trd-gen 的预期；其 output hash 与 workspace 文件哈希一致。

## Failures / Findings

- TRD gap packet 未携带 feature_path: chat-interface/history-search、parent_feature: chat-interface、feature_level: 2。
- 未说明缺 PRD 回 PM、缺 TRD 回 trd-gen 的完整 PM/TRD 边界。
- Root cause: with_skill 虽执行了路径和门禁检查，但最终交接摘要没有把已读取的 PRD 元数据结构化带入 TRD gap packet，且边界说明只覆盖了 TRD 缺口，遗漏了缺 PRD 时的 PM 路由。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-007-missing-nested-trd-handoff

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-007-missing-nested-trd-handoff`
- Test case: missing-nested-trd-handoff
- Workspace: `workspace/eval-007-missing-nested-trd-handoff`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture files read before skill use: `README.md`, `eval_metadata.json`, and `docs/pm/chat-interface/history-search/PRD.md`.
- Fixture summary: the PRD declares `feature_path: chat-interface/history-search`, `parent_feature: chat-interface`, and `feature_level: 2`; the mirrored `docs/engineer/chat-interface/history-search/TRD.md` is intentionally absent.
- Expected output: stop before implementation planning, hand off to `engineer-agent:trd-gen`, and include nested feature path metadata and expected PRD/TRD paths.

## Assertions

- PASS `detects_missing_mirrored_trd`: the feature path gate requires the mirrored TRD at `docs/engineer/chat-interface/history-search/TRD.md`.
- PASS `hands_off_to_trd_gen_with_feature_path`: the TRD gap packet includes `feature_path`, `parent_feature`, `feature_level`, PRD path, and expected TRD path.
- PASS `does_not_write_plan_or_code`: no `IMPLEMENTATION_PLAN.md`, code, tests, or file-change plan are written.
- PASS `keeps_pm_trd_boundary`: missing PRD returns to PM, while the current missing TRD returns to `trd-gen`; feature-implementor does not invent TRD decisions.

## With Skill Behavior

Fresh with-skill validation confirmed the nested feature path gate. The current skill reads canonical `feature_path` metadata before planning, so it should not look only for `docs/engineer/history-search/TRD.md`, a parent `docs/engineer/chat-interface/TRD.md`, or a flattened fallback. It must block planning for `docs/engineer/chat-interface/history-search/IMPLEMENTATION_PLAN.md`, route to `engineer-agent:trd-gen`, and carry the nested feature metadata and expected mirrored TRD path.

## Without Skill Baseline

The fresh without-skill baseline was summarized before reading skill docs. A generic worker may notice the prompt says the nested TRD is missing, but it could still look for a flattened or parent TRD path, provide an incomplete handoff, or blur the PM/TRD boundary by suggesting that feature-implementor fill in technical decisions.

## Failures

- None.

## Next Steps

- Keep this eval focused on mirrored nested `feature_path` TRD requirements.

## Runtime Artifacts Policy

- This validation did not create runtime artifacts.
- Runtime transcripts, verdicts, timing files, outputs, diagnostics, run status files, and `comparison.auto.md` must not be committed.
