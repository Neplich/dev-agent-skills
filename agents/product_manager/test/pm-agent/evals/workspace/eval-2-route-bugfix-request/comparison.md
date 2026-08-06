# Eval Result: eval-002-route-bugfix-request

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-002-route-bugfix-request`
- Workspace: `eval-2-route-bugfix-request`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-002-route-bugfix-request/`.

## Latest result:

- Behavior result: PASS — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 3/3 with-skill assertion scenarios were exercised.
Overall result: PASS

## Assertion Results

- `request_type_bug_report`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确分类为 `bug_report`；without_skill 仅称为登录/鉴权模块前端缺陷，未使用要求的 `bug_report` 分类。
- `expectation_first`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确要求先确认 token 过期后的正确预期，并核对 PRD/TRD 或登录流程文档；without_skill 未要求对照 approved PRD/TRD 或等价产品预期。
- `debugger_handoff_after_confirmation`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确表示只有确认是实现偏差后才交给 `engineer-agent` 调试；without_skill 直接建议交给前端登录/鉴权负责人，未设置“确认实现偏差后”门槛。

## With-Skill Behavior

最终回复完整满足三项 PM 路由断言：分类为 bug_report，先确认 approved PRD/TRD 预期及复现证据，确认实现偏差后再交给 Engineer/debugger。status 显示无 added/removed/modified，trace 仅读取技能与文件，没有外部 mutation。

## Fresh Without-Skill Baseline

回复提供了部分排查信息，但未按要求进行稳定的 bug_report 分类，未先核对 approved PRD/TRD 预期，并在确认实现偏差前直接提出工程负责人路由。status 显示无文件变更；trace 仅执行读取命令。

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
