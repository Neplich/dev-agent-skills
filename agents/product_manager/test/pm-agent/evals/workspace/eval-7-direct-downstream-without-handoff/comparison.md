# Eval Result: eval-007-direct-downstream-without-handoff

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-007-direct-downstream-without-handoff`
- Workspace: `eval-7-direct-downstream-without-handoff`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-007-direct-downstream-without-handoff/`.

## Latest result:

- Behavior result: FAIL — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 4/4 with-skill assertion scenarios were exercised.
Overall result: FAIL

## Assertion Results

- `reject_direct_downstream`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确拒绝直接修改/代替 Engineer；without_skill 仅说明工作区为空。
- `return_to_pm_agent`: with-skill **FAIL**; without-skill **FAIL** — 两者均未明确返回 pm-agent 并完成 request_type、scope、feature_path、handoff readiness 分类。
- `require_handoff_or_docs`: with-skill **FAIL**; without-skill **FAIL** — 两者均未要求 PM handoff packet 或等价已确认 PRD/TRD/design/test/deployment/security 文档。
- `_status_and_trace_zero_write_check`: with-skill **PASS**; without-skill **PASS** — 两份 status 均无 added/removed/modified；trace 仅有读取命令，无写入或外部 mutation。

## With-Skill Behavior

拒绝直接修改成立，但缺少 PM 分类回流和 handoff/document 门禁。

## Fresh Without-Skill Baseline

未执行 PM 路由门禁。

The baseline is comparison evidence only; its outcome does not affect `Overall result`.

## Failures

- with_skill 未满足 return_to_pm_agent
- with_skill 未满足 require_handoff_or_docs
- without_skill 未满足三项行为断言

## Coverage Gaps

- None.

## Blockers

- None.

## Historical Result (Pre-#234)

- The previous durable result recorded Behavior **PASS**, Coverage **FULL**, and Overall **BLOCKED** after issue #234 identified prompt/fixture leakage.
- That pre-remediation result is retained only as history and is superseded by this strict fresh run.

## Next Steps

- Fix the with-skill failures listed above, then rerun this eval with the same strict isolation and independent-judge protocol.

## Runtime Artifacts Policy

- Candidate responses, traces, status manifests, isolation records, and judge evidence remain under the gitignored runtime path above and are not committed.
