# Eval Result: eval-001-explore-web-app

## Evaluation Target

- Skill: `exploratory-tester`
- Eval: `eval-001-explore-web-app`
- Prompt target: 基于搜索刷新上下文制定并执行探索协议。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `778b042`
- Fresh run: `2026-07-30 19:26:38 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-pr-b-20260730-192638/qa/agents/qa/test/exploratory-tester/evals/workspace/eval-1-explore-web-app/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **FULL**
- 所有 assertions 均可由静态 preflight/blocked 输出判定；无 `NOT EXERCISED`。
- 非 E2E 路径变更检查：该 fixture 是 E2E `feature-update` 场景，未触发 `docs/qa/{feature_path}/exploratory-report.md`。

Overall result: FAIL

## Assertion Results

- FAIL `assertion_1`: charter 有 surface、heuristics、escalation signals，但缺少上下文给出的 timebox，且未说明重试时由何来源确定 timebox。
- PASS `assertion_2`: 读取 suite、flow、既有 TC，复用同义流程并避免重复 TC。
- FAIL `assertion_3`: changed surface 与 nearby risks 正确，但 timebox 来源未闭环。
- PASS `assertion_4`: observed、unconfirmed、gaps 三层清楚，未把风险当缺陷。
- PASS `assertion_5`: 输出是 chartered exploration，不是随机点击日志。
- PASS `assertion_6`: 含 charter、timebox 状态、covered path、evidence 与 next actions。
- PASS `deduplicates_existing_flows`: 复用 `TC-001-filter-results`，只建议增量更新。

## With-Skill Behavior

缺少 `QA_BASE_URL` 时停止浏览器执行是正确 blocked 行为；FAIL 仅来自 timebox 契约未闭环，而非“没有实跑”。

## Fresh Without-Skill Baseline

同一 prompt/fixture 的全新 baseline 已生成，未读取 skill、QA README 或历史 baseline。candidate/verdict 均成功；baseline 同样缺 timebox 来源，semantic verdict 为 FAIL。

## Failures

- 未给出上下文驱动 timebox，也未指出重试时确定 timebox 的来源。

## Next Steps

- 后续候选在执行被 URL 阻塞时仍应声明“未启动执行 timebox”，并指出由用户或 handoff 提供的时长决定重试 timebox。

## Runtime Artifact Policy

- 两条 candidate、两条 verdict、diagnostics 与 `comparison.auto.md` 均在上述 `tmp/eval-runs/`，返回码均为 0、无 timeout。
- Runtime 不提交；durable 结果仅为本文件。
