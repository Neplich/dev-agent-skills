# Eval Result: eval-013-change-tier-hotfix-e2e-direct-path

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-013-change-tier-hotfix-e2e-direct-path`
- Workspace: `eval-13-change-tier-hotfix-e2e-direct-path`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-013-change-tier-hotfix-e2e-direct-path/`.

## Latest result:

- Behavior result: FAIL — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 3/3 with-skill assertion scenarios were exercised.
Overall result: FAIL

## Assertion Results

- `hotfix_direct_path_only`: with-skill **FAIL**; without-skill **FAIL** — 两份最终回复仅判定为 hotfix 并说明无法定位文件；均未明确说明 hotfix QA/E2E 可限制到 directly affected path。with_skill trace 仅提到“只处理登录页对应文案”，不足以满足该断言。
- `evidence_still_required`: with-skill **FAIL**; without-skill **FAIL** — with_skill 最终回复说无法验证并请求提供项目目录，但未要求记录 verification evidence、验证结果和 blocked checks；trace 也未形成该要求。without_skill 同样缺失。
- `no_full_suite_required`: with-skill **FAIL**; without-skill **FAIL** — 两份最终回复均未说明不需要完整 E2E suite，或仅在风险/范围升级到 standard/major 时需要全量套件。

## With-Skill Behavior

with_skill 正确识别 hotfix，并如实报告工作区缺少源码、无法修改或验证；status 显示零文件变更，trace 仅执行读取与仓库状态检查。但最终回复没有覆盖三项 hotfix QA 输出要求。

## Fresh Without-Skill Baseline

without_skill 同样如实报告空工作区并保持零写入，但也未覆盖任何断言要求。

The baseline is comparison evidence only; its outcome does not affect `Overall result`.

## Failures

- with_skill 未说明 QA/E2E 覆盖可限制到 directly affected path。
- with_skill 未要求记录 verification evidence、结果及 blocked checks。
- with_skill 未说明无需完整 E2E suite，除非升级为 standard/major。

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
