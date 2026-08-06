# Eval Result: eval-010-change-tier-hotfix-fast-lane

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-010-change-tier-hotfix-fast-lane`
- Workspace: `eval-10-change-tier-hotfix-fast-lane`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-010-change-tier-hotfix-fast-lane/`.

## Latest result:

- Behavior result: FAIL — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 3/3 with-skill assertion scenarios were exercised.
Overall result: FAIL

## Assertion Results

- `classify_hotfix`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确给出 change_tier: hotfix，并说明范围仅为 README 链接、功能预期不变且已有本地验证；without_skill 未给出 hotfix 分类。
- `allow_fast_lane`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确写出可走 hotfix fast lane；without_skill 未提及 fast lane。
- `preserve_evidence`: with-skill **FAIL**; without-skill **FAIL** — with_skill 提到了范围和验证，但未明确要求保留 source evidence；without_skill 也未要求保留 scope、source evidence、verification evidence。

## With-Skill Behavior

完成 hotfix 分类并允许 fast lane，但未完整落实三类证据的保留要求。状态正常返回且无文件变化；trace 未显示写入或外部 mutation。

## Fresh Without-Skill Baseline

未完成 PM 分类和 fast-lane 判断，仅检查工作区后报告无法修改。状态正常返回且无文件变化。

The baseline is comparison evidence only; its outcome does not affect `Overall result`.

## Failures

- with_skill 未满足 preserve_evidence：缺少 source evidence 的明确保留要求。

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
