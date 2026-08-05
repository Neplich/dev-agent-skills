# Eval Result: eval-003-mapped-doc-acceptance

## Evaluation Target

- Skill: `spec-based-tester`
- Eval: `eval-003-mapped-doc-acceptance`
- Prompt target: 由 change-map 定位昵称长度文档并以代码形成验收矩阵。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `778b042`
- Fresh run: `2026-07-30 19:26:38 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-pr-b-20260730-192638/qa/agents/qa/test/spec-based-tester/evals/workspace/eval-3-mapped-doc-acceptance/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- 无 `NOT EXERCISED` assertion。
- 非 E2E 路径变更检查：prompt 要求矩阵和证据结论但未要求持久化报告；`docs/qa/{feature_path}/spec-validation.md` 未覆盖。

Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- PASS `reads_mapped_docs_first`: 先由 change-map 命中 `profile-validation.md`，未遍历无关文档。
- PASS `verifies_against_code`: 文档 80、代码 64 的路径、声明、事实与验收影响均完整记录。
- PASS `treats_unverified_as_low_trust`: 将 `unverified` 文档作为低信任定位线索，关键判断由代码支撑。

## With-Skill Behavior

候选提供结构化 requirement matrix，并清楚区分映射定位成功、代码核证成功与规范一致性失败。

## Fresh Without-Skill Baseline

同一 prompt/fixture 的全新 baseline 已生成，未读取 skill、QA README 或历史 baseline。candidate/verdict 均成功；baseline 同样满足三条 assertions，semantic verdict 为 PASS。

## Failures

- 无 assertion failure。

## Next Steps

- PR-B 非 E2E 路径需独立要求持久化报告的 fixture；本次不改现有 eval。

## Runtime Artifact Policy

- 两条 candidate、两条 verdict、diagnostics 与 `comparison.auto.md` 均在上述 `tmp/eval-runs/`，返回码均为 0、无 timeout。
- Runtime 不提交；durable 结果仅为本文件。
