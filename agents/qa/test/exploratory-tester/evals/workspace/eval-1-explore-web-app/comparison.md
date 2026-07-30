# Eval Result: eval-001-explore-web-app

## Evaluation Target

- Skill: `exploratory-tester`
- Eval: `eval-001-explore-web-app`
- Prompt target: 基于搜索刷新上下文制定并执行探索协议。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `cdfc879`
- Fresh run: `2026-07-30 19:56:59 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-pr-b-bug-explore-20260730-195659/exploratory-tester/eval-001/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- 当前 7 条 assertion 均可由 fresh blocked-preflight 候选直接判定，无
  `NOT EXERCISED`。
- fixture 已提供 `docs/qa/e2e/search/results/filtering/` 用例树、`feature-update`
  场景与 `v0.9.0-dev`；这是纯 E2E eval，因此不包含非 E2E fallback 路径断言。

Overall result: PASS

## Assertion Results

- PASS `assertion_1`: charter 包含 surface、heuristics、escalation signals，并明确本轮未启动 timebox；重试 duration 必须来自用户或 PM/QA handoff。
- PASS `assertion_2`: 读取 suite、flow、既有 TC，复用同义流程并避免重复 TC。
- PASS `assertion_3`: 围绕 `SearchPanel`、`FilterPills`、`ResultsList` 与 keyboard-focus nearby risk 组织探索；没有套用固定默认时长，并闭环重试 timebox 来源。
- PASS `assertion_4`: observed、unconfirmed、gaps 三层清楚，未把风险当缺陷。
- PASS `assertion_5`: 输出是 chartered exploration，不是随机点击日志。
- PASS `assertion_6`: 含 charter、timebox 状态、covered path、evidence used 与 next actions。
- PASS `deduplicates_existing_flows`: 识别既有 `TC-001-filter-results`，只允许增量更新同一 TC、匹配 script 与 `FLOW_INDEX.md`，一次性观察留在报告。

## With-Skill Behavior

缺少 `QA_BASE_URL`、同路径 TRD 和 confirmed plan 时停止 E2E 执行；同时完整输出
memory read set、scenario/platform、入口顺序、subagent 执行边界、charter 和去重策略。
blocked 不妨碍当前静态协议 assertion 的完整判定，Behavior PASS。

## Fresh Without-Skill Baseline

同一 prompt/fixture 在本轮隔离目录重新生成 baseline，未读取或应用
`exploratory-tester`、QA README 或历史 baseline。它使用固定 30 分钟默认值，包含随机
点击，没有 QA memory、scenario/platform、执行入口、subagent、证据分层和 TC 去重；
baseline 仅作为 comparison 输入，不决定 with-skill Behavior。

## Failures

- 无 with-skill assertion failure。

## Next Steps

- 提供 `QA_BASE_URL`、同路径 TRD、confirmed implementation plan 和明确 duration 后，
  才能开始 `TC-001` 与相邻风险的运行时探索。

## Runtime Artifact Policy

- 新 `with_skill.md`、`without_skill.md` 与 `verdict.md` 仅保存在上述
  `tmp/eval-runs/`；未复用历史 candidate 或 baseline。
- Runtime 不提交；durable 结果仅为本文件。
