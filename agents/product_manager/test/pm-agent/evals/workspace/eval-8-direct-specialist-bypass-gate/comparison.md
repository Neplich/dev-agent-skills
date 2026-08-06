# Eval Result: eval-008-direct-specialist-bypass-gate

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-008-direct-specialist-bypass-gate`
- Workspace: `eval-8-direct-specialist-bypass-gate`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-008-direct-specialist-bypass-gate/`.

## Latest result:

- Behavior result: FAIL — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 3/3 with-skill assertion scenarios were exercised.
Overall result: FAIL

## Assertion Results

- `specialist_gate_runs`: with-skill **FAIL**; without-skill **FAIL** — with_skill 未说明 direct specialist invocation 仍执行 PM handoff entry gate；trace 也无 specialist gate 执行证据。without_skill 同样未提及。
- `requires_handoff_or_docs`: with-skill **FAIL**; without-skill **FAIL** — with_skill 未要求 PM handoff packet，也未明确已确认 PRD/TRD 与 implementation scope 是进入实现的条件。without_skill 也未满足该门槛。
- `blocks_implementation`: with-skill **FAIL**; without-skill **FAIL** — with_skill 只阻止直接写代码，未明确阻止创建 plan 或测试实现，也返回了 idea-to-spec 而非 pm-agent。without_skill 还表示可整理实施计划。

## With-Skill Behavior

虽识别为 new_feature 并阻止立即写代码，但未完整执行 specialist gate 要求。status 显示正常完成且 added/removed/modified 均为空；trace 仅有读取操作。

## Fresh Without-Skill Baseline

仅要求补充需求，未满足断言要求；status 显示正常完成且零文件变化。

The baseline is comparison evidence only; its outcome does not affect `Overall result`.

## Failures

- with_skill specialist_gate_runs 未通过
- with_skill requires_handoff_or_docs 未通过
- with_skill blocks_implementation 未通过

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
