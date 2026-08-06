# Eval Result: eval-014-route-site-notes-and-github-release

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-014-route-site-notes-and-github-release`
- Workspace: `eval-14-route-site-notes-and-github-release`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-014-route-site-notes-and-github-release/`.

## Latest result:

- Behavior result: PASS — determined only from the with-skill lane by an independent judge.
- Coverage result: PARTIAL — 0/4 with-skill assertion scenarios were exercised.
Overall result: PASS (partial coverage)

## Assertion Results

- `routes_site_notes_to_docs_specialist`: with-skill **NOT_EXERCISED**; without-skill **NOT_EXERCISED** — 两份最终回复均未执行或承诺具体 handoff；v1.0.0 的确认范围/实体不存在，无法实际触发 A 路由。
- `routes_github_release_to_pm_specialist`: with-skill **NOT_EXERCISED**; without-skill **NOT_EXERCISED** — 两份最终回复均未生成 GitHub Release preview，也未展示 PM github-release-gen 路由；v1.0.0 来源不足。
- `preserves_release_sequence`: with-skill **NOT_EXERCISED**; without-skill **NOT_EXERCISED** — 未进入站内说明确认或 Release audit gates 阶段，因此无法核对 site-first 顺序。
- `does_not_use_old_pm_skill_name`: with-skill **NOT_EXERCISED**; without-skill **NOT_EXERCISED** — 最终回复和工具轨迹未发生实际 PM owner 命名或路由，无法核对旧名回退。

## With-Skill Behavior

行为未触发断言失败；轨迹识别为 release_notes 工作流并先检查资料，但因缺少 v1.0.0 的项目内容、Git 历史和确认范围而停止澄清。status 显示零新增、零删除、零修改。

## Fresh Without-Skill Baseline

行为未触发断言失败；轨迹通过只读 GitHub 查询确认目标仓库当前为 v0.5.7-fix1、没有 v1.0.0 依据后停止澄清。status 显示零文件变更，未见外部写入或发布调用。

The baseline is comparison evidence only; its outcome does not affect `Overall result`.

## Failures

- None.

## Coverage Gaps

- 四项 with_skill assertions 均未实际执行，无法验证具体 specialist handoff、顺序或旧名约束。
- 缺少 v1.0.0 的确认版本范围、变更依据或可消费的 release handoff。

## Blockers

- 实时数据中不存在断言所需的 v1.0.0 版本实体/确认范围。

## Historical Result (Pre-#234)

- The previous durable result recorded Behavior **PASS**, Coverage **FULL**, and Overall **BLOCKED** after issue #234 identified prompt/fixture leakage.
- That pre-remediation result is retained only as history and is superseded by this strict fresh run.

## Next Steps

- Keep the passing behavior result, and rerun when the missing live entities or fixture conditions can exercise the listed coverage gaps.

## Runtime Artifacts Policy

- Candidate responses, traces, status manifests, isolation records, and judge evidence remain under the gitignored runtime path above and are not committed.
