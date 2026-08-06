# Eval Result: eval-015-route-docs-site-deployment-gap

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-015-route-docs-site-deployment-gap`
- Workspace: `eval-015-route-docs-site-deployment-gap`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-015-route-docs-site-deployment-gap/`.

## Latest result:

- Behavior result: FAIL — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 3/3 with-skill assertion scenarios were exercised.
Overall result: FAIL

## Assertion Results

- `blocks_unknown_evidence`: with-skill **PASS**; without-skill **PASS** — 两组最终回复及 trace 都保留了初始 unknown、Public 已集成、Internal 缺失，并明确未验证部署/不推断 ready handoff。
- `builds_repo_wide_deployment_packet`: with-skill **FAIL**; without-skill **FAIL** — with_skill 未生成或呈现 deployment handoff packet，缺少 request_type、N/A feature fields、空 feature_path_evidence 及结构化 source_documents/blockers_risks。without_skill 仅生成完整性报告。
- `routes_devops_ordered_chain`: with-skill **FAIL**; without-skill **FAIL** — 两组最终回复均未按 devops-agent:deployment-planner → devops-agent:cicd-bootstrap → devops-agent:env-config-auditor → docs-agent:formal-docs-sync 给出有序 handoff，也未证明 Docs 仅同步已落地且验证的运维事实。

## With-Skill Behavior

证据不确定性处理正确，但未完成所需的 repo-wide deployment packet 和有序 DevOps/Docs 路由。status 显示零 fresh 文件写入；trace 仅执行读取与回复，无外部 mutation。

## Fresh Without-Skill Baseline

正确保留 unknown/缺口边界，但同样未生成 deployment packet 或完成有序路由；status 显示新增 docs-site-completeness-report.md。

The baseline is comparison evidence only; its outcome does not affect `Overall result`.

## Failures

- with_skill 未满足 builds_repo_wide_deployment_packet。
- with_skill 未满足 routes_devops_ordered_chain。

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
