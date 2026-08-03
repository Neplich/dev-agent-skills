# Eval Result: github-release-generator-outline-sections-quality-exclusion

## Evaluation Target

- Skill: `github-release-generator`
- Test case: outline 四节结构、内部质量证据排除与风险事实保持
- Latest result: **PASS**（Behavior: PASS / Coverage: FULL）
- Overall result: PASS

## Review Context

- Issue: #190（Release 标题与升级说明质量门禁修复）
- Date: 2026-08-03
- Final judge: 当前会话中的 fresh Codex validation agent
- Judge 独立读取当前 skill、两份 reference、eval 定义/metadata/fixture 与 issue-190 fresh 双侧 candidate；verdict 完成前未读取 durable `comparison.md` 或旧 run tmp。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: confirmed site Release Notes、curated GitHub evidence、adjacent presentation suggestions 与 internal quality evidence
- With-skill evidence: `tmp/eval-runs/issue-190/with_skill/eval-005-outline-sections-quality-exclusion/candidate-output.md`
- Without-skill evidence: `tmp/eval-runs/issue-190/without_skill/eval-005-outline-sections-quality-exclusion/candidate-output.md`
- Judge verdict: `tmp/eval-runs/issue-190/judge/verdict.md`

## Assertions

- PASS `follows_outline_sections`：正文只有重点更新、其他改进、升级说明、变更明细四个 H2；without-skill FAIL（使用用户功能/架构与兼容/数据库/部署与资产等约定外结构）
- PASS `excludes_internal_quality_evidence`：双侧都排除 skill eval、assertion 数、review 轮次与 QA 汇总
- PASS `preserves_confirmed_facts`：双侧都保留两项独立功能、统一附件兼容链路、nullable JSONB 迁移与删列风险、部署顺序和开关、双架构资产、升级步骤及旧浏览器限制
- PASS `title_matches_gate`（issue-190 新增）：标题为 `v1.0.0 - 文件卡片、原位重试与统一附件交付`，满足版本加主题概述格式、非裸 tag；without-skill FAIL（`AI Hub v1.0.0` 不符合）
- PASS `upgrade_note_fixed_structure`（issue-190 新增）：升级说明含实质简述、`### Claude Code`/`### Codex`/`### Kimi Code` 三个指令小节与收尾句，未臆造 fixture 之外的 plugin 更新声明；without-skill FAIL（仅普通升级段落）

## With Skill Behavior

- 生成四节正文，排除全部内部质量材料与相邻版式建议。
- 标题按 `vX.Y.Z - 主题概述` 门禁呈现；升级说明按固定结构呈现，plugin 声明句严格受事实源约束（fixture 无 plugin 事实时不写入）。
- current latest 缺失时保守 `--latest=false`，只预览不写入。

## Without Skill Baseline

- 来源：issue-190 fresh baseline（2026-08-03），基于同一 eval prompt 与 fixture；未读取或应用 skill、reference、Agent README、with-skill 输出或历史 comparison。
- 行为：3/5 assertions PASS；能保留事实与排除内部质量证据，但不遵守四节 outline、标题格式门禁与升级说明固定结构——新增两条断言在 without-skill 侧保持区分度。

## Failures / Findings

- 无 with-skill assertion failure。
- issue-190 首轮 judge finding（已解决）：升级说明固定结构曾被无条件套入不含 plugin 事实的宿主场景；模板条件化后 with-skill 不再臆造 plugin 声明。

## Next Steps

- 保留当前 outline、标题门禁与升级说明固定结构；后续修改这些规则时重新运行。

## Runtime Artifacts Policy

- 双侧 candidates 与 judge verdict 位于 `tmp/eval-runs/issue-190/`，属于未提交运行期诊断产物。
- 长期只保留本 `comparison.md`；不提交 transcript、candidate、verdict、timing、run status 或 diagnostics。
