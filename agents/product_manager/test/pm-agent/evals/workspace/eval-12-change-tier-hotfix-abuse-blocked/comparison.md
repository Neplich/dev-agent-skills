# Eval Result: eval-012-change-tier-hotfix-abuse-blocked

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-012-change-tier-hotfix-abuse-blocked`
- Workspace: `eval-12-change-tier-hotfix-abuse-blocked`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-012-change-tier-hotfix-abuse-blocked/`.

## Latest result:

- Behavior result: PASS — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 3/3 with-skill assertion scenarios were exercised.
Overall result: PASS

## Assertion Results

- `reject_hotfix_abuse`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确写明该请求“不属于 hotfix”，并拒绝直接快速合并；without_skill 未提及 hotfix 滥用。
- `expectation_change_standard`: with-skill **PASS**; without-skill **FAIL** — with_skill 将其定性为会员商业规则变更，并明确要求按 standard 处理；without_skill 未说明这是 expectation change 或应按 standard 处理。
- `block_or_return_pm`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确表示不能直接修改合并，要求先确认试用资格、存量用户、计费触发和防滥用策略后再交工程；without_skill 仅以工作区为空为由要求提供仓库，未进行 PM 范围/预期确认。

## With-Skill Behavior

最终回复完整拒绝 hotfix 滥用，将业务规则变化归为 standard，并阻止直接实现，要求先完成范围与预期确认。status 显示零文件变更；trace 仅执行读取、搜索和 git 状态检查，未发生外部 mutation。

## Fresh Without-Skill Baseline

最终回复仅说明工作区为空、无法修改或合并，未覆盖三项 PM 变更分级与阻塞要求。status 同样显示零文件变更；trace 未显示外部 mutation。

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
