# Eval Result: eval-003-route-test-writing-request

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-003-route-test-writing-request`
- Workspace: `eval-3-route-test-writing-request`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-003-route-test-writing-request/`.

## Latest result:

- Behavior result: PASS — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 3/3 with-skill assertion scenarios were exercised.
Overall result: PASS

## Assertion Results

- `request_type_validation`: with-skill **PASS**; without-skill **FAIL** — with_skill-final 明确分类为 `validation`；without_skill 仅称“测试补充/回归测试”，未使用 validation 或等价路由分类。
- `test_basis_first`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确要求先确认 PRD、DECISIONS、TRD/API 契约、实现计划及验收记录，并因依据缺失而阻塞；without_skill 罗列状态机、接口契约等测试内容，但未明确先确认指定的 PRD/TRD/IMPLEMENTATION_PLAN/既有验收记录。
- `qa_or_test_writer_handoff`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确说明预期和来源文档确认前不能 handoff，确认后自动化测试交 Engineer、测试用例/验证交 QA；without_skill 建议交 QA/测试工程师，但未明确以预期稳定且来源文档明确作为前置条件。

## With-Skill Behavior

准确完成 validation 路由；明确测试依据必须先确认，并在依据缺失时阻塞后续 handoff，同时区分 Engineer 与 QA 的职责。status 显示无文件变更，trace 仅读取技能和上下文，无外部 mutation。

## Fresh Without-Skill Baseline

能识别退款异常测试主题并列出测试依据与覆盖点，但未完成规范的 validation 分类，也未满足指定依据和稳定预期后的条件式 handoff。无文件变更，trace 仅读取空工作区。

The baseline is comparison evidence only; its outcome does not affect `Overall result`.

## Failures

- None.

## Coverage Gaps

- None.

## Blockers

- None.

## Historical Result (Pre-#234)

- The previous durable result recorded Behavior **PASS**, Coverage **FULL**, and Overall **BLOCKED** after issue #234 identified prompt/fixture leakage.
- That pre-remediation result is retained only as history and is superseded by this strict fresh run.

## Next Steps

- Keep this case as a regression gate and rerun it after changes to `pm-agent`, its routing contract, or this fixture.

## Runtime Artifacts Policy

- Candidate responses, traces, status manifests, isolation records, and judge evidence remain under the gitignored runtime path above and are not committed.
