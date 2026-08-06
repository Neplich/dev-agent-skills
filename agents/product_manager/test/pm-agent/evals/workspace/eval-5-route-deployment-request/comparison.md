# Eval Result: eval-005-route-deployment-request

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-005-route-deployment-request`
- Workspace: `eval-5-route-deployment-request`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-005-route-deployment-request/`.

## Latest result:

- Behavior result: PASS — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 3/3 with-skill assertion scenarios were exercised.
Overall result: PASS

## Assertion Results

- `request_type_deployment`: with-skill **PASS**; without-skill **PASS** — with_skill 最终回复明确 request_type: deployment；without_skill 虽未使用稳定枚举，但语义明确为仓库级 CI/CD 与发布 DevOps。
- `repo_wide_scope_allowed`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确使用 feature_path/feature/parent_feature: N/A、feature_level: repository，且 feature_path_evidence: []；without_skill 未记录 N/A feature fields。
- `devops_handoff_packet`: with-skill **PASS**; without-skill **FAIL** — with_skill 在交接 DevOps 前记录了 CI/发布就绪目标、仓库级 scope、未确定的环境/发布范围/回滚要求及 blockers_risks，并指定 downstream_owner: DevOps；without_skill 未完整记录 operational goal 与 release scope。

## With-Skill Behavior

三项断言均满足。最终回复包含 deployment 分类、仓库级 N/A scope、空证据列表，以及补齐运维上下文后交接 DevOps 的结构化 packet。

## Fresh Without-Skill Baseline

正确识别为仓库级 DevOps/CI/CD 请求，也指出环境和回滚等信息，但未遵循 N/A feature-scope 契约，且交接上下文不完整。

The baseline is comparison evidence only; its outcome does not affect `Overall result`.

## Failures

- without_skill 未使用仓库级非 feature 工作要求的 N/A feature fields。
- without_skill 未完整补齐 operational goal 和 release scope 后再形成 DevOps handoff packet。

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
