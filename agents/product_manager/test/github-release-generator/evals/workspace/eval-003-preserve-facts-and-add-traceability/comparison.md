# Eval Result: github-release-generator-preserve-facts-and-add-traceability

## Evaluation Target

- Skill: `github-release-generator`
- Test case: fact preservation and curated GitHub traceability
- Latest result: **PASS** - 2026-07-22 issue #154 r2 fresh paired validation；with-skill 4/4、without-skill 4/4 assertions 通过

## Review Context

- Review issue: #154
- Final judge: 当前会话中的 fresh Codex validation agent
- 独立 verdict 在读取 durable `comparison.md` 前完成，且未读取旧首轮 tmp；证据来自当前 skill/reference、eval fixture 与 issue #154 r2 fresh 双侧 candidate。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: AI Hub confirmed release page、pre-tag audited range、intended final compare 与 curated GitHub evidence
- With-skill evidence: `tmp/eval-runs/issue-154/r2-final/with_skill/eval-003-preserve-facts-and-add-traceability/candidate-output.md`
- Without-skill evidence: `tmp/eval-runs/issue-154/r2/without_skill/eval-003-preserve-facts-and-add-traceability/candidate-output.md`
- Judge verdict: `tmp/eval-runs/issue-154/r2-final/judge/verdict.md`

## Assertions

- PASS `preserves_confirmed_release_facts`: 双侧都保留两项独立用户功能、统一附件兼容链路、nullable/backfill 数据库事实与删列风险、部署顺序/开关、双架构/static asset、升级步骤和旧浏览器限制。
- PASS `adds_verified_traceability_links`: 双侧都使用同一窗口的 final compare、PR #116/#117、direct commit `8b6a1f2` 与贡献者链接。
- PASS `curates_instead_of_dumping`: 双侧都只选择支撑已确认事实的代表性链接，明确排除其余 maintenance feed。
- PASS `blocks_on_fact_conflict`: 双侧都在 GitHub 证据冲突或暴露新事实时返回 `docs-agent:release-notes-generator`，不自行覆盖或扩写。

## With Skill Behavior

- 接受 confirmed site page 为事实源并记录 handoff/window；GitHub evidence 只增强 traceability。
- 生成完整 outline preview，区分 pre-tag audited compare 与 future final compare。
- current latest 缺失时保守使用 `--latest=false`，只预览不写入。

## Without Skill Baseline

- 来源：issue #154 fresh baseline，使用同一 prompt 和 fixture，未读取或应用 skill、Agent README、with-skill 输出或历史 comparison。
- 行为：同样 4/4 assertions PASS，完整保留事实、精选链接并声明冲突回流。
- 差异：baseline 没有 release-outline 的标题/日期 framing，也未报告 current latest 缺失下的 prerelease/latest 决定；这些不是本 eval 当前 assertions 的失败条件。

## Failures / Findings

- 无 with-skill assertion failure 或 blocker。
- 非阻塞 finding：assertions 与 fixture 已直接给出事实清单、精选链接和冲突处理，baseline 也全部通过。

## Next Steps

- 当事实源优先级、compare 双态或 traceability outline 变化时重新执行 paired validation。
- 若需评估完整 preview 协议增益，可增加 exact title/date 与 latest/prerelease evidence assertions。

## Runtime Artifacts Policy

- issue #154 双侧 candidates 与 judge verdict 位于上列精确 r2 scratch 路径，是短期诊断产物，不提交。
- 长期只保留本 `comparison.md`；不提交 transcript、candidate、manifest、verdict、outputs、timing、run status 或 diagnostics。
