# Eval Result: eval-001-explore-web-app

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-001-explore-web-app`
- Test case: explore-web-app
- Workspace: `workspace/eval-1-explore-web-app`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-06-04

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that exploratory-tester handles explore-web-app and produces the expected role-specific artifact.
- Expected output: 探索测试报告，包含发现的问题列表和复现路径

## Assertions

- `assertion_1`: 探索章程
- `assertion_2`: 探索记忆沉淀
- `assertion_3`: 范围与时限
- `assertion_4`: 证据分层
- `assertion_5`: 探索方法
- `assertion_6`: 可交接产物
- `deduplicates_existing_flows`: 不重复创建同义 TC

## With Skill

Observed behavior:

- 当前 skill 要求先读 QA 记忆、PM 上下文、changed surface、风险和环境说明，再产出包含 surface、timebox、heuristics、escalation signals 的 exploration charter；fixture 提供 search-refresh PRD、SearchPanel/FilterPills/ResultsList 改动面和 QA_BASE_URL 阻塞规则，能满足 charter、上下文驱动范围、证据分层和可交接报告 assertions。
- 当前 skill 明确把 `docs/qa/e2e/{feature_path}/` 作为 durable QA memory，要求先读取 `TEST_SUITE.md`、`FLOW_INDEX.md`、`cases/*.md`、`scripts/*.spec.md`、历史结果和报告。fixture 中已有 `docs/qa/e2e/search/results/filtering/TEST_SUITE.md`、`FLOW_INDEX.md` 和 `cases/TC-001-filter-results.md`，且这些文件明确要求同一 filter-results flow 增量更新既有 TC，不创建同义重复 TC；skill 的 deduplication 规则与 fixture 预期一致。
- 当前 skill 要求如果读取源码或配置来推导覆盖面，需要更新 `FLOW_INDEX.md` 记录读取文件、原因和覆盖影响；如果识别出可复用 E2E 场景，需要写入单独 case，并在需要可重复执行时写对应 script。一次性观察保留在探索报告，不沉淀为重复 TC。
- 当前 skill 要求 E2E 执行入口按 repo harness > Chrome plugin / browser connector > Playwright fallback 选择，并默认由 subagent 执行 E2E TC；本 eval 未要求真实执行，`QA_BASE_URL` 缺失时应报告 browser execution blocked，同时仍产出 charter 和 evidence plan。

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None. Fresh Codex subagent validation found the current `SKILL.md` satisfies all eval assertions, including QA memory reuse, durable function-tree updates, and duplicate TC avoidance.

## Next Steps

- 无需修改 fixture。Residual risk: this validation is static against the skill contract and fixture files; no browser session, repo harness, or model transcript was executed.

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
