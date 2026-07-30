# Eval Result: eval-001-test-from-spec

## Evaluation Target

- Skill: `spec-based-tester`
- Eval: `eval-001-test-from-spec`
- Prompt target: 从 checkout discount test spec 选择并报告规范验证。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `cdfc879`
- Fresh run: `2026-07-30 19:56:59 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-pr-b-spec-20260730-195659-eval001/qa/agents/qa/test/spec-based-tester/evals/workspace/eval-1-test-from-spec/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
- `e2e` 的“新增/补充 TC”分支为 **NOT EXERCISED**：fixture 已有 TC，本轮未扩充。
- `versioned_report_archive` 的真实 result/snapshot/report 写入分支为 **NOT EXERCISED**：本轮没有产品测试结果；场景与版本确认子项已覆盖。

Overall result: FAIL

## Assertion Results

- FAIL `assertion_1`: 候选引用了 test spec、PRD、TRD 和 `package.json`，但未把缺失变更说明、环境假设、未知项和 blocked 检查整理成执行前基线。
- FAIL `assertion_2`: 候选引用了 suite、flow 和既有 TC，但未明确声明复用该 TC，也未记录缺失的 `scripts/*.spec.md`、历史 `results/` 与 `_reports/`。
- PASS `assertion_3`: 选择 repo harness `npm test -- checkout-discount`，没有臆造浏览器或 Playwright 入口。
- PASS `assertion_4`: requirement matrix 使用 `blocked`，未把未执行项写成失败或缺陷。
- PASS `assertion_5`: 包含 requirement matrix、execution path、evidence references 和 risk notes，并保留逐项状态与说明。
- NOT EXERCISED `e2e`: 未新增或补充 TC；现有单文件 TC 被正确引用，没有发现约束回归。
- PASS `versioned_report_archive`: 已确认 `feature-update` 与 `v0.3.0-dev`；没有执行结果时未伪造 archive。实际归档分支未覆盖。
- PASS `assertion_7`: 没有把 blocked/unknown 项交给 `bug-analyzer`。

## With-Skill Behavior

候选正确收敛范围、选择 repo harness、输出结构化证据并诚实保持 blocked。Behavior 仍为 FAIL，因为 preflight 没有完整记录上下文缺口和 QA memory 缺失项，无法证明按 specialist 协议完成执行前检查。

## Fresh Without-Skill Baseline

同一 prompt/fixture 的全新 baseline 已生成，未读取或应用 skill 与 QA README。candidate 和 fresh judge 均成功；baseline 同样遗漏变更说明状态、执行前未知项以及 `scripts`、历史 `results/`、`_reports/` 的缺失记录，semantic verdict 为 FAIL。

## Failures

- 执行前基线未显式记录变更说明缺失、环境假设、未知项与 blocked 检查。
- 未完整记录 QA memory 的读取/缺失状态，也未明确声明复用既有 TC。

## Next Steps

- 后续候选应在执行前逐项记录 fixture 已读来源与缺失项，再进入执行路径和 requirement matrix。

## Runtime Artifact Policy

- 两条 candidate、两条 fresh judge verdict、diagnostics 与 `comparison.auto.md` 均在上述 `tmp/eval-runs/`；所有 Codex 调用返回码为 0，且无 timeout。
- Runtime 不提交；durable 结果仅为本文件。
