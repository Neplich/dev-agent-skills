# Eval Result: eval-001-test-from-spec

## Evaluation Target

- Agent: `qa`
- Skill: `spec-based-tester`
- Eval: `eval-001-test-from-spec`
- Test case: test-from-spec
- Workspace: `workspace/eval-1-test-from-spec`
- Latest result: PARTIAL - prior skill validation evidence is preserved; without-skill baseline was not generated for this historical comparison.
- Prior validation note: fresh Codex subagent validation completed on 2026-06-04

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that spec-based-tester handles test-from-spec and produces the expected role-specific artifact.
- Expected output: 测试报告，包含通过/失败统计和失败用例详情
- Fixture context: `docs/test-spec.md`, `docs/prd.md`, `docs/trd.md`, `docs/qa/e2e/commerce/checkout/discount-code/TEST_SUITE.md`, `FLOW_INDEX.md`, `cases/TC-001-discount-code.md`, and `package.json`.

## Assertions

- `assertion_1`: 上下文基线
- `assertion_2`: 独立用例复用
- `assertion_3`: 执行路径选择
- `assertion_4`: 结果分级
- `assertion_5`: 结构化证据
- `e2e`: E2E 单文件约束
- `assertion_7`: 交接边界

## With Skill

Observed behavior:

- PASS. 当前 `spec-based-tester` 要求执行前读取 PM/spec、TRD、实现上下文、仓库指令和现有 QA 功能树，并记录 scope、环境假设、unknowns、blocked checks。
- PASS. 当 PM 未提供具体 E2E 用例时，skill 要求先读取 `docs/qa/e2e/{feature_path}/TEST_SUITE.md`、`FLOW_INDEX.md`、`cases/*.md`、`scripts/*.spec.md`、历史 `results/` 和 `_reports/`；fixture 已有 `commerce/checkout/discount-code` 功能树和 `TC-001-discount-code`，所以应优先复用现有 TC，不回退到旧的单层 QA 目录。
- PASS. 执行路径规则明确为 repo acceptance/e2e/integration/manual QA harness 优先，其次 Chrome plugin / browser connector，最后才是 standalone Playwright fallback；fixture 的 TRD 和 TEST_SUITE 均指向 `npm test -- checkout-discount` 作为 repo harness。
- PASS. Evidence contract 要求 requirement matrix 使用 `pass`、`fail`、`blocked` 或 `assumed`，并明确不把 blocked 或 assumed 项误写成 confirmed defect。
- PASS. 输出要求包含 scoped validation summary、requirement matrix、execution path、evidence references、risk notes、blocked items 和 handoff notes。
- PASS. Shared QA directory contract 要求 E2E TC 单文件存放到 `cases/TC-NNN-<short-slug>.md`，并维护 `FLOW_INDEX.md`、`TEST_SUITE.md` 和 matching `scripts/TC-NNN-<short-slug>.spec.md`；fixture 当前已有 case，若后续补充脚本或新增 TC，skill 会按该目录契约处理。
- PASS. E2E 运行前必须确认 `feature-update` 或 `release` 场景和 platform version；缺失版本时 blocked，不写 `unknown`。结果归档和主报告路径按 `e2e-test-report.md` reference 写入 `results/TC-NNN-<short-slug>/{platform-version}/` 和对应 `_reports/{platform-version}/test-reports-{test-time}.md`。
- PASS. Bug handoff 只允许 confirmed reproducible failure with evidence；blocked、assumed、flaky 或证据不足的观察不会升级为 bug-analyzer handoff。

## Without Skill / Baseline
- BLOCKED: No actual without-skill baseline result is recorded for this historical comparison. This file is not treated as a full eval PASS until a baseline result is generated and written here.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None.

## Next Steps

- 无运行期文件需要生成。Eval fixture 中 `TC-001-discount-code` 当前没有 matching script 文件；本次评测判断的是当前 skill 协议是否满足 assertions，实际执行或新增脚本时应按 skill 的 `scripts/TC-NNN-<short-slug>.spec.md` 契约补齐。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
