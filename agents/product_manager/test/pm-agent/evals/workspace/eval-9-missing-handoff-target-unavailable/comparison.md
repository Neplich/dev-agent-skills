# Eval Result: eval-009-missing-handoff-target-unavailable

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-009-missing-handoff-target-unavailable`
- Workspace: `eval-9-missing-handoff-target-unavailable`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-009-missing-handoff-target-unavailable/`.

## Latest result:

- Behavior result: PASS — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 3/3 with-skill assertion scenarios were exercised.
Overall result: PASS

## Assertion Results

- `detect_missing_target`: with-skill **PASS**; without-skill **PASS** — with_skill 明确指出 designer-agent 未安装或无法访问；without_skill 也明确指出设计能力未安装。
- `mark_handoff_blocked`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确将设计阶段和当前状态标记为 blocked，并要求安装/启用设计能力；without_skill 未明确使用 blocked 状态。
- `do_not_perform_missing_role`: with-skill **PASS**; without-skill **PASS** — 两份回复均未代替 Designer 产出视觉规范或设计交付物。with_skill 还明确表示不会代行设计角色。

## With-Skill Behavior

最终回复完整满足三项断言。状态 changes 为空，trace 仅读取 pm-agent skill，无外部 mutation。

## Fresh Without-Skill Baseline

识别了设计能力不可用且未代行 Designer 职责，但未明确将 handoff 标记为 blocked。

The baseline is comparison evidence only; its outcome does not affect `Overall result`.

## Failures

- without_skill 未明确标记 handoff stage 为 blocked；该 baseline 失败不影响 Overall。

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
