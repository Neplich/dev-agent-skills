# Eval Result: eval-001-test-from-spec

## Evaluation Target

- Skill: `spec-based-tester`
- Eval: `eval-001-test-from-spec`
- Prompt target: 从 checkout discount test spec 选择并报告规范验证。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `2506764`
- Fresh run: `2026-08-03 11:20:59 +0800`
- Runtime directory: `tmp/eval-runs/issue-201-spec-based-tester/eval-001-test-from-spec/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **PARTIAL**
- `e2e` 的“新增/补充 TC”分支为 **NOT EXERCISED**：fixture 已有 TC，本轮未扩充。
- `versioned_report_archive` 的真实 result/snapshot/report 写入分支为 **NOT EXERCISED**：本轮没有产品测试结果；场景与版本确认子项已覆盖。

Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- PASS `assertion_1`: 新增的 `Preflight baseline` 在执行前逐项记录 test spec、PRD、TRD、`package.json`、变更说明 absent、范围、环境假设、未知项和 blocked 检查；没有把缺失上下文静默跳过。
- PASS `assertion_2`: 明确先读 suite、flow 和既有 TC，逐项记录 `scripts/*.spec.md`、历史 `results/`、`_reports/` absent，并声明直接复用 `TC-001-discount-code`、不从零探索项目。
- PASS `assertion_3`: 选择 repo harness `npm test -- checkout-discount`，没有臆造浏览器或 Playwright 入口。
- PASS `assertion_4`: requirement matrix 使用 `blocked`，未把未执行项写成失败或缺陷。
- PASS `assertion_5`: 包含 requirement matrix、execution path、evidence references 和 risk notes，并保留逐项状态与说明。
- NOT EXERCISED `e2e`: 未新增或补充 TC；现有单文件 TC 被正确引用，没有发现约束回归。
- PASS `versioned_report_archive`: 已确认 `feature-update` 与 `v0.3.0-dev`；没有执行结果时未伪造 archive。实际归档分支未覆盖。
- PASS `assertion_7`: 没有把 blocked/unknown 项交给 `bug-analyzer`。

## With-Skill Behavior

修复后的报告模板把 preflight 门禁接入最终输出：候选完整呈现上下文基线、QA memory 读取/缺失状态和 TC 复用声明，再选择 repo harness，并在同路径文档链与可执行环境不足时诚实保持 blocked。此前失败的两项均通过，原已通过断言无回归。

## Fresh Without-Skill Baseline

同一 prompt/fixture 的 without-skill baseline 已在本轮重新生成，未读取或应用 skill 与 QA README，且未复用历史 baseline。它读取直接点名的规范与测试命令，但未读取 QA memory，也未逐项记录变更说明、`scripts`、历史 `results/`、`_reports/` 的缺失状态和 TC 复用决定，因此仍不满足 `assertion_1` / `assertion_2`。

## Failures

- 无 behavior failure。

## Next Steps

- 若需覆盖当前 NOT EXERCISED 分支，应在具备同路径确认文档链与可执行产品环境的独立 fixture 中验证新增 TC 和真实 result/snapshot/report 归档；本轮不扩大 fixture。

## Runtime Artifact Policy

- 本轮 with-skill 候选、重新生成的 without-skill baseline 与 judge 笔记均在上述 `tmp/eval-runs/`。
- Runtime 不提交；durable 结果仅为本文件。
