# Eval Result: eval-002-explore-with-custom-duration

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-002-explore-with-custom-duration`
- Test case: explore-with-custom-duration
- Workspace: `workspace/eval-2-explore-with-custom-duration`
- Latest result: PARTIAL - prior skill validation evidence is preserved; without_skill baseline was not generated for this historical comparison.
- Prior validation note: fresh Codex subagent validation completed on 2026-06-04

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that exploratory-tester handles explore-with-custom-duration and produces the expected role-specific artifact.
- Expected output: 5 分钟探索测试报告

## Assertions

- `assertion_1`: 上下文驱动范围
- `assertion_2`: 独立探索确认
- `version_entry_and_subagent`: 版本、执行入口与 subagent
- `assertion_3`: 异常分层
- `assertion_4`: 证据输出
- `assertion_5`: 风险交接

## With Skill

Observed behavior:

- 当前 skill 要求 timebox 来自上下文而非固定默认值；fixture 中用户指定 5 分钟、目标 URL 为 `https://qa.example.test/settings`，并提供 SettingsPanel、EmailPreferenceForm 和 toast 风险，因此 skill 能建立包含 URL、时长、changed surface、可用环境信息和未验证前提的探索章程。
- 当前 skill 要求 standalone exploratory 或 E2E 请求先确认 function-tree scope 和 scenario；E2E 执行前必须确认 platform version，缺失时 blocked，不能写入 `unknown`。fixture 中 `TEST_SUITE.md` 明确 scenario 为 `feature-update` 且 platform version missing，所以符合预期的 skill 行为是阻塞执行 TC，并保留 charter 和 evidence plan。
- 当前 skill 要求先读取 `docs/qa/e2e/account/settings/email-preferences/TEST_SUITE.md`、`FLOW_INDEX.md`、既有 cases、scripts、历史 results 和 reports；fixture 当前没有 active TC，若扩充覆盖应先更新 `FLOW_INDEX.md`，再按单独 TC 文件和对应 script 沉淀可复用流程，避免重复 save/cancel 语义用例。
- 当前 skill 要求 E2E 执行入口按 repo harness > Chrome plugin / browser connector > Playwright fallback 选择并说明原因，实际执行 TC 默认由 subagent 执行。由于 fixture 平台版本缺失且目标环境可达性未确认，正确结果是 blocked before execution，而不是绕过版本门禁启动浏览器或 Playwright。
- 当前 skill 要求报告分开记录 observed issues、suspicious but unconfirmed signals、gaps not explored，并包含实际执行路径、evidence references、risk notes 和 recommended next actions；这满足异常分层、证据输出和风险交接 assertions。

## Without Skill / Baseline
- BLOCKED: No actual without_skill baseline result is recorded for this historical comparison. This file is not treated as a full eval PASS until a baseline result is generated and written here.
- This comparison records whether the skill-specific protocol, routing, evidence, or artifact expectations are preserved.

## Failures

- None. Fresh Codex subagent validation found the current `SKILL.md` satisfies all eval assertions, including platform-version blocking, execution-entry precedence, subagent default, and function-tree QA memory reuse.

## Next Steps

- 保持该 eval 覆盖用户指定时长、版本门禁、执行入口选择、subagent 默认执行和证据分层行为。Residual risk: this validation is static against the skill contract and fixture files; no browser session, repo harness, or model transcript was executed.

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
