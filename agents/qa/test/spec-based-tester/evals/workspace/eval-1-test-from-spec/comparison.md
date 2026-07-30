# Eval Result: eval-001-test-from-spec

## Evaluation Target

- Skill: `spec-based-tester`
- Eval: `eval-001-test-from-spec`
- Prompt target: 从 checkout discount test spec 选择并报告规范验证。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `778b042`
- Fresh run: `2026-07-30 19:26:38 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-pr-b-20260730-192638/qa/agents/qa/test/spec-based-tester/evals/workspace/eval-1-test-from-spec/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
- `e2e` 的“新增/补充 TC”分支为 **NOT EXERCISED**：fixture 已有 TC，本轮未扩充。
- `versioned_report_archive` 的真实 result/snapshot/report 写入分支为 **NOT EXERCISED**：本轮没有产品测试结果；场景与版本确认子项已覆盖。
- 非 E2E 路径变更检查：该 fixture 是 E2E `feature-update`，未触发 `docs/qa/{feature_path}/spec-validation.md`。

Overall result: FAIL

## Assertion Results

- FAIL `assertion_1`: 候选未显式证明已读 PRD/TRD/package、变更说明状态，也未完整记录环境假设、未知项和 blocker。
- FAIL `assertion_2`: 引用了既有 TC，但未记录 `FLOW_INDEX.md`、缺失 scripts、历史 results/reports 的读取/缺失状态。
- PASS `assertion_3`: 选择 repo harness `npm test -- checkout-discount`，不臆造浏览器入口。
- PASS `assertion_4`: requirement matrix 使用 blocked，未把未执行项当缺陷。
- FAIL `assertion_5`: 有 matrix、execution path、risk notes，但缺显式 evidence references 段落与逐项可追踪来源。
- NOT EXERCISED `e2e`: 未新增或补充 TC；没有证据表明单文件约束回归。
- PASS `versioned_report_archive`: 已确认 `feature-update` 与 `v0.3.0-dev`；没有执行结果时未伪造 archive。实际归档分支未覆盖。
- PASS `assertion_7`: 没有把 blocked/unknown 交给 bug-analyzer。

## With-Skill Behavior

不执行产品测试时保持 blocked 是正确的；FAIL 来自 preflight 与 evidence traceability 不完整，而非缺少实跑本身。

## Fresh Without-Skill Baseline

同一 prompt/fixture 的全新 baseline 已生成，未读取 skill、QA README 或历史 baseline。candidate/verdict 均成功；baseline 也缺完整 E2E memory，semantic verdict 为 FAIL。

## Failures

- Preflight read set、未知项与 evidence references 不完整。

## Next Steps

- 后续候选应显式记录缺失 scripts/results/reports；非 E2E 路径另需专门 fixture。

## Runtime Artifact Policy

- 两条 candidate、两条 verdict、diagnostics 与 `comparison.auto.md` 均在上述 `tmp/eval-runs/`，返回码均为 0、无 timeout。
- Runtime 不提交；durable 结果仅为本文件。
