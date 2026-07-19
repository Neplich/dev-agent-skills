# Eval Result: github-release-generator-preserve-facts-and-add-traceability

## Evaluation Target

- Skill: `github-release-generator`
- Test case: fact preservation and curated GitHub traceability
- Latest result: PASS - 2026-07-20 fresh paired validation 与独立 judge 完成，4/4 assertions 通过

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: AI Hub-shaped confirmed seven-category page 与 scoped GitHub evidence
- Runtime evidence: `tmp/eval-runs/120/eval-003-preserve-facts-and-add-traceability/`

## Assertions

- PASS `preserves_confirmed_release_facts`: 七类已确认事实逐项保留，未新增、省略或泛化改写。
- PASS `adds_verified_traceability_links`: 使用范围内 compare、PR、direct commit 和贡献者链接，并区分 pre-tag/final endpoint。
- PASS `curates_instead_of_dumping`: 只列代表性维护证据，未堆叠其余 18 个维护 commit。
- PASS `blocks_on_fact_conflict`: 冲突或新事实返回 Docs 重新确认，不在 GitHub Release 中覆盖。

## With Skill Behavior

- 以站内页面为事实源，保留功能、架构、兼容、数据库、部署、资产、升级与风险语义。
- GitHub evidence 仅用于追溯与格式增强；完整维护 feed 被审计但不直接作为用户说明。
- 预览模式保持 `docs/site/`、GitHub 与 tag 零写入。

## Without Skill Baseline

- 同一 prompt/fixture 于 2026-07-20 全新生成，未应用或引用 skill、README、旧 baseline 或历史 comparison。
- baseline 能保留多数事实与链接，但未说明冲突回流，也未明确筛除无用户事实增益的完整维护 feed；with-skill 显示明确协议增益。

## Failures

- 无。独立 judge 未发现 skill、fixture、harness 或断言问题。

## Next Steps

- 当事实源优先级、compare 规则或 traceability outline 变化时重新执行 paired validation。

## Runtime Artifacts Policy

- 本轮 `with_skill.md`、`without_skill.md` 与 `verdict.md` 仅位于 `tmp/eval-runs/120/`，不提交 transcript、verdict、with_skill、without_skill、outputs 或 diagnostics。
