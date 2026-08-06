# Eval Result: eval-011-change-tier-standard-full-gate

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-011-change-tier-standard-full-gate`
- Workspace: `eval-11-change-tier-standard-full-gate`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-011-change-tier-standard-full-gate/`.

## Latest result:

- Behavior result: PASS — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 3/3 with-skill assertion scenarios were exercised.
Overall result: PASS

## Assertion Results

- `classify_standard`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确判定 change_tier 为 standard 且不能按 hotfix；without_skill 未分类变更等级。
- `require_prd_trd_alignment`: with-skill **PASS**; without-skill **FAIL** — with_skill 因缺少 PRD/TRD 和功能目录而阻塞，未进行下游 handoff；trace 加载的 PM 规则要求 existing_update 先完成产品文档/预期与 TRD 对齐。without_skill 直接提出修改实现，未要求对齐。
- `request_type_existing_update`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确写出 request_type: existing_update；without_skill 未作该分类。

## With-Skill Behavior

三项断言均满足。回复正确识别为 existing_update、standard，并因缺少项目文档和范围证据而暂停下游执行；trace 仅读取技能/文档，没有写入或外部 mutation，status changes 为空。

## Fresh Without-Skill Baseline

未完成 PM 分类或门禁判断，直接按工程实现方向回应；status changes 为空，trace 仅执行读取和 git status 检查。

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
