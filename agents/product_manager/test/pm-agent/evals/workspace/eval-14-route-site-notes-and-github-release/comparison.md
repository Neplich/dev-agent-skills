# Eval Result: pm-agent-route-site-notes-and-github-release

## Evaluation Target

- Skill: `pm-agent`
- Test case: split site Release Notes and GitHub Release routing
- Latest result: PASS - 2026-07-20 fresh paired validation 与独立 judge 完成，4/4 assertions 通过

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: issue #120 rename 后两个 AI Hub-shaped release communication outcomes
- Runtime evidence: `tmp/eval-runs/120/eval-014-route-site-notes-and-github-release/`

## Assertions

- PASS `routes_site_notes_to_docs_specialist`: A 精确 handoff `docs-agent:release-notes-generator`。
- PASS `routes_github_release_to_pm_specialist`: B 精确 route PM `github-release-generator`。
- PASS `preserves_release_sequence`: 先完成站内确认与 Docs gates，再消费 ready handoff 与 release audit evidence。
- PASS `does_not_use_old_pm_skill_name`: PM owner 不回退旧名，朴素 `release-notes-generator` 只指 Docs specialist。

## With Skill Behavior

- 应用当前 pm-agent、PM README 与 skill-map 路由段，区分站点写作/确认职责与 GitHub Release preview/draft/publish 职责。
- 为 Docs handoff 保留站内产物与 gate，PM 内部 route 保留事实源和审计前置，不执行任何实际写入或发布。

## Without Skill Baseline

- 同一 prompt/fixture 于 2026-07-20 全新生成，未应用或引用 pm-agent、README、skill-map、旧 baseline 或历史 comparison。
- baseline 能给出一般角色方向和 site-first 顺序，但没有精确 specialist 名、ready handoff、`ready_for_tag` 或发布三门禁；with-skill 形成可执行仓库路由合同。

## Failures

- 无。独立 judge 未发现 skill、fixture、harness 或断言问题。

## Next Steps

- 当 pm-agent release_notes 分类、Docs handoff 或 PM specialist 名称变化时重新执行 paired validation。

## Runtime Artifacts Policy

- 本轮 `with_skill.md`、`without_skill.md` 与 `verdict.md` 仅位于 `tmp/eval-runs/120/`，不提交 transcript、verdict、with_skill、without_skill、outputs 或 diagnostics。
