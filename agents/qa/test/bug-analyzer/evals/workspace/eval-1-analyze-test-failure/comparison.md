# Eval Result: eval-001-analyze-test-failure

## Evaluation Target

- Skill: `bug-analyzer`
- Eval: `eval-001-analyze-test-failure`
- Prompt target: 从登录 500 测试失败形成证据化 Bug 报告。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `cdfc879` + current PR-B `evals.json` assertion update
- Fresh run: `2026-07-30 19:56:59 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-pr-b-bug-explore-20260730-195659/bug-analyzer/eval-001/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- 当前 7 条 assertion 全部被新 with-skill 候选直接覆盖，无 `NOT EXERCISED`。
- 本轮按新增 `non_e2e_report_path` 判定非 E2E fallback：候选明确使用
  `docs/qa/authentication/login/bug-login-form-500.md`，文件名无日期且不使用
  `docs/qa-reports/`。

Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- PASS `assertion_1`: 摄取 failing scenario、500、console、branch/commit/environment，并逐项标明 server stack、response body、截图、trace、runtime、flags 等证据缺口。
- PASS `assertion_2`: 使用 `confirmed but environment-sensitive`，并将 evidence status 与 confidence 分开。
- PASS `assertion_3`: severity 有影响理由，confidence 独立陈述。
- PASS `assertion_4`: 选择 repo 内本地 Markdown artifact，明确不做 GitHub-first。
- PASS `assertion_5`: 当前不满足 reusable E2E 沉淀条件；候选明确将 TC/script 创建标为 blocked，并列出缺失的 feature path、PRD/TRD/plan、platform 与用例树。
- PASS `assertion_6`: 包含 release impact 与 evidence references。
- PASS `non_e2e_report_path`: 使用 `docs/qa/{feature_path}/bug-<short-slug>.md`
  形态，文件名无日期且未使用旧 `docs/qa-reports/`。

## With-Skill Behavior

候选完整分离 evidence status、confidence 与 severity，保留可追踪 fixture 引用，
对证据缺口、release impact、reusable E2E blocker 和 PR-B 新非 E2E 路径均给出
直接证据，Behavior PASS。

## Fresh Without-Skill Baseline

同一 prompt/fixture 在本轮隔离目录重新生成 baseline，未读取或应用
`bug-analyzer`、QA README 或历史 baseline。它把一次 fixture 直接写成已确认缺陷，
GitHub-first，未分离 evidence status / confidence，未声明 repo durable path，也未处理
reusable E2E gate；baseline 仅作为 comparison 输入，不决定 with-skill Behavior。

## Failures

- 无 with-skill assertion failure。

## Next Steps

- 可在后续 fixture 中提供正式 handoff `feature_path`，使报告路径无需从登录场景收敛为
  `authentication/login`；这不影响本轮路径契约判定。

## Runtime Artifact Policy

- 新 `with_skill.md`、`without_skill.md` 与 `verdict.md` 仅保存在上述
  `tmp/eval-runs/`；未复用历史 candidate 或 baseline。
- Runtime 不提交；durable 结果仅为本文件。
