# Eval Result: eval-004-route-ui-update-request

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-004-route-ui-update-request`
- Workspace: `eval-4-route-ui-update-request`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-004-route-ui-update-request/`.

## Latest result:

- Behavior result: PASS — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 4/4 with-skill assertion scenarios were exercised.
Overall result: PASS

## Assertion Results

- `request_type_design_or_update`: with-skill **PASS**; without-skill **FAIL** — with_skill 最终回复明确分类为 existing_update；without_skill 直接判为 Engineer 路径，未作所需 PM 分类。
- `pm_designer_engineer_decision`: with-skill **PASS**; without-skill **FAIL** — with_skill 指出先由 PM 收敛需求，并按是否需要设计产物转 Designer、范围确认后转 Engineer；without_skill 将 Engineer 作为主要执行者，未完成 PM 路由判断。
- `implementation_waits_for_alignment`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确要求先确认设计和技术范围，再修改前端；without_skill 直接建议 Engineer 执行。
- `no_fresh_writes_or_external_mutation`: with-skill **PASS**; without-skill **PASS** — 两份 status 的 changes 均为空；trace 仅显示读取技能文件和输出回复，无写入或外部 mutation。

## With-Skill Behavior

正确走 PM 路径，分类为 existing_update；先收敛产品范围，再按需交接 Designer，设计和技术范围确认后交接 Engineer。

## Fresh Without-Skill Baseline

错误地直接走 Engineer 路径，仅将 Designer 作为可选参与者。

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
