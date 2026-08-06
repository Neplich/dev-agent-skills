# Eval Result: github-release-gen-preserve-facts-and-add-traceability

## Evaluation Target

- Skill: `github-release-generator` → `github-release-gen`（改名后新入口待重跑验证）
- Test case: fact preservation and curated GitHub traceability
- Latest result: **PASS**（Behavior: PASS / Coverage: FULL）
- Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

- Overall result: PASS

## Review Context

- Issue: #190（Release 标题与升级说明质量门禁修复）
- Date: 2026-08-03
- Final judge: 当前会话中的 fresh Codex validation agent
- Judge 独立读取当前 skill、两份 reference、eval 定义/metadata/fixture 与 issue-190 fresh 双侧 candidate；verdict 完成前未读取 durable `comparison.md` 或旧 run tmp。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: AI Hub confirmed release page、pre-tag audited range、intended final compare 与 curated GitHub evidence
- With-skill evidence: `tmp/eval-runs/issue-190/with_skill/eval-003-preserve-facts-and-add-traceability/candidate-output.md`
- Without-skill evidence: `tmp/eval-runs/issue-190/without_skill/eval-003-preserve-facts-and-add-traceability/candidate-output.md`
- Judge verdict: `tmp/eval-runs/issue-190/judge/verdict.md`

## Assertions

- PASS `preserves_confirmed_release_facts`：保留两项独立用户功能、统一附件兼容链路、nullable JSONB 迁移与删列风险、部署顺序与开关、双架构资产、升级步骤和旧浏览器限制，未泛化合并，也未新增事实源之外的 plugin 发布声明；without-skill 同 PASS
- PASS `adds_verified_traceability_links`：使用 fixture 的 pre-tag/final compare、PR #116/#117、direct commit `8b6a1f2` 与贡献者链接，tag 与 compare endpoint 一致；without-skill 同 PASS
- PASS `curates_instead_of_dumping`：只选取支撑已确认事实的代表性链接，明确排除其余 18 个维护 commit；without-skill 同 PASS
- PASS `blocks_on_fact_conflict`：证据冲突或暴露新事实时 blocked 并返回 `docs-agent:release-notes-gen`；without-skill FAIL（只说明 GitHub 证据用于追溯，无冲突回退协议）

## With Skill Behavior

- 接受 confirmed site page 为事实源并记录 handoff/window；GitHub evidence 只增强 traceability。
- 生成完整 outline preview，区分 pre-tag audited compare 与 future final compare。
- current latest 缺失时保守使用 `--latest=false`，只预览不写入。

## Without Skill Baseline

- 来源：issue-190 fresh baseline（2026-08-03），基于同一 eval prompt 与 fixture；未读取或应用 skill、reference、Agent README、with-skill 输出或历史 comparison。
- 行为：3/4 assertions PASS；事实保真与链接筛选接近 with-skill，但缺冲突阻塞与上游重新确认门禁。

## Failures / Findings

- 无 with-skill assertion failure。
- 历史 finding（issue-190 首轮 judge 已解决）：固定升级结构曾被无条件套入不含 plugin 事实的宿主场景，新增「7 个 role plugin 均更新」等事实源之外声明；已通过模板条件化（plugin 声明句绑定已确认事实源）修复，本轮 with-skill 未再臆造。

## Next Steps

- 保留事实源优先级、compare 双态与 traceability outline；后续修改事实转换规则时重新执行 paired validation。

## Runtime Artifacts Policy

- 双侧 candidates 与 judge verdict 位于 `tmp/eval-runs/issue-190/`，属于未提交运行期诊断产物。
- 长期只保留本 `comparison.md`；不提交 transcript、candidate、verdict、timing、run status 或 diagnostics。
