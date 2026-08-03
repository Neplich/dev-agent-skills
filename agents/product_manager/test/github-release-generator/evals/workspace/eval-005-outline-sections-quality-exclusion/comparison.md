# Eval Result: github-release-generator-outline-sections-quality-exclusion

## Evaluation Target

- Skill: `github-release-generator`
- Test case: outline 四节结构、内部质量证据排除与风险事实保持
- Latest result: **PASS**（Behavior: PASS / Coverage: PARTIAL）
- Overall result: PASS (partial coverage)

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
- PASS `title_matches_gate`（issue-190 新增）：标题为 `v1.0.0 - 文件卡片、原位重试与统一附件交付`，非裸版本号且含事实主题概述（本 fixture 未定义宿主标题惯例，含主题概述为合格输出）；without-skill 同 PASS（`AI Hub v1.0.0` 非裸版本号，非 marketplace 宿主不强制概述——本断言在非 marketplace fixture 下无法测 marketplace 强格式分支）
- PASS `upgrade_note_fixed_structure`（issue-190 新增）：升级说明按事实源完整呈现实质简述与收尾动作，fixture 未确认 coding-agent 客户端升级入口时未生成 `Claude Code`/`Codex`/`Kimi Code` 空壳小节或安装命令，未臆造 plugin 更新声明；without-skill 同 PASS（语义上给出完整非占位的备份/部署/验证内容，仅排版不同）

## With Skill Behavior

- 生成四节正文，排除全部内部质量材料与相邻版式建议。
- 标题含事实相关主题概述（非 marketplace 宿主不强格式）；升级说明按事实源完整呈现实质内容，fixture 未确认客户端升级入口时未生成空壳指令小节，plugin 声明句严格受事实源约束（fixture 无 plugin 事实时不写入）。
- current latest 缺失时保守 `--latest=false`，只预览不写入。

## Without Skill Baseline

- 来源：issue-190 fresh baseline（2026-08-03），基于同一 eval prompt 与 fixture；未读取或应用 skill、reference、Agent README、with-skill 输出或历史 comparison。
- 行为：4/5 assertions PASS；能保留事实、排除内部质量证据、给出非占位升级内容并产出非裸版本号标题，但不遵守四节 outline——`follows_outline_sections` 在 without-skill 侧保持区分度。

## Failures / Findings

- 无 with-skill assertion failure。
- issue-190 首轮 judge finding（已解决）：升级说明固定结构曾被无条件套入不含 plugin 事实的宿主场景；模板条件化后 with-skill 不再臆造 plugin 声明。
- **Coverage PARTIAL（未覆盖分支）**：`title_matches_gate` 与 `upgrade_note_fixed_structure` 的 marketplace 正向分支（`vX.Y.Z - 概述` 强格式、三小节指令模板、按 marketplace.json 推导的 plugin 列表、TARGET_TAG/Kimi 能力条件）在本 fixture（非 marketplace 宿主）下未执行，仅验证了非 marketplace 分支（不空壳化、不臆造 plugin 声明）。

## Next Steps

- 保留当前 outline、标题门禁与升级说明固定结构；后续修改这些规则时重新运行。
- 建议新增 marketplace 场景 eval（当前 tag：7 个 role plugin、三小节能力齐全；历史 tag：能力不完整时的条件省略），覆盖正向分支断言后再恢复 Coverage FULL。

## Runtime Artifacts Policy

- 双侧 candidates 与 judge verdict 位于 `tmp/eval-runs/issue-190/`，属于未提交运行期诊断产物。
- 长期只保留本 `comparison.md`；不提交 transcript、candidate、verdict、timing、run status 或 diagnostics。
