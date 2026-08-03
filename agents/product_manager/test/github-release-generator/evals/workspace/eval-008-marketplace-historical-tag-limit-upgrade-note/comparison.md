# Eval Result: github-release-generator-marketplace-historical-tag-limit-upgrade-note

## Evaluation Target

- Skill: `github-release-generator`
- Test case: marketplace 历史 tag 能力不完整时的条件省略
- Latest result: **PASS**（Behavior: PASS / Coverage: FULL）
- Overall result: PASS

## Review Context

- Issue: #220（marketplace 正向分支 eval 覆盖）；第 3 轮为 outline 收尾句规则与断言最终修订后验证（无固定版本路径不承诺同步该 tag 能力、mock 证据声明、完整 pre-tag handoff）
- Date: 2026-08-03
- Final judge: 当前会话中的 fresh Codex validation agent
- Judge 独立读取当前 skill、reference、eval 定义/metadata/fixture 与 fresh 双侧 candidate；verdict 完成前未读取 durable `comparison.md` 或旧 run tmp。
- 断言判据只以 fixture workspace 文件为准（伪造历史 tag 宿主文件：`.claude-plugin/marketplace.json` 6 plugins、`.codex/INSTALL.md` 无 TARGET_TAG、无 `.kimi-plugin/plugin.json`），不以仓库根目录同名文件为准。
- 第 2 轮修订（review 意见）：release-package 补充同版本 pre-tag ready_for_tag 历史记录；github-evidence 补充证据确认声明；`claude_section_omitted_with_platform_limit` 断言修正为「固定版本替代路径只在目标 tag 实际存在已验证能力时点名，无则明确声明该 tag 无固定版本安装路径」。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: 伪造 dev-agent-skills marketplace 历史 tag（v0.9.0，6 role plugins、无 TARGET_TAG 支持、无 Kimi manifest；含同版本 pre-tag ready_for_tag 历史与 post-tag release_verified）、confirmed site Release Notes、curated GitHub evidence（维护者已确认）
- With-skill evidence: `tmp/eval-runs/issue-220-r3/with_skill/eval-008-marketplace-historical-tag-limit-upgrade-note/candidate-output.md`
- Without-skill evidence: `tmp/eval-runs/issue-220-r3/without_skill/eval-008-marketplace-historical-tag-limit-upgrade-note/candidate-output.md`
- Judge verdict: `tmp/eval-runs/issue-220-r3/judge/verdict.md`

## Assertions

- PASS `title_matches_marketplace_format`：历史 tag 标题为 `v0.9.0 - 原位重试、附件链路兼容与双架构交付`，仍为强格式且概述与事实相关；without-skill FAIL（`Dev Agent Skills v0.9.0`）
- PASS `upgrade_note_first_sentence_derived`：简述句 N=6 由 v0.9.0 manifest 推导（而非当前 7 个）；without-skill FAIL（使用「升级与风险」混合小节，首段非要求首句）
- PASS `claude_section_omitted_with_platform_limit`：历史 tag 重跑省略 `### Claude Code` 并说明 durable 正文无法承诺固定 `v0.9.0`；固定版本替代路径只在目标 tag 实际存在已验证能力时点名，本 fixture 中 Codex/Kimi 均无固定版本能力，正文明确声明「该 tag 无已验证的固定版本安装路径」；without-skill 同 PASS（baseline 已内化该条件省略与无路径声明，属模型通用审慎）
- PASS `codex_section_omitted_without_target_tag_support`：目标 tag 无 TARGET_TAG 支持时省略 `### Codex` 小节，不臆造安装指令；without-skill 同 PASS
- PASS `kimi_section_omitted_without_plugin_json`：无 `.kimi-plugin/plugin.json` 时省略 `### Kimi Code` 小节，不生成空壳或 `/plugins install` 命令；without-skill 同 PASS
- PASS `closing_sentence_derived`：以「更新仓库后重新运行安装器，即可同步全部 6 个 role plugin 的 `v0.9.0` 能力。」收尾，N=6 与历史 manifest 一致；without-skill FAIL（无固定收尾句）

## With Skill Behavior

- 完整应用 skill 与 reference：标题强格式、简述句 N=6 按历史 manifest 推导、三小节按目标 tag 实际能力条件省略（Claude 省略 + durable 平台限制说明、Codex 无 TARGET_TAG 省略、Kimi 无 manifest 省略）、无固定版本安装路径时明确声明、收尾句 N=6。
- 保持站内事实与排除内部质量证据；preview only，无任何写操作；无运行期产物残留。

## Without Skill Baseline

- 来源：issue-220-r2 fresh baseline（2026-08-03），基于同一 eval prompt 与 fixture；未读取或应用 skill、reference、Agent README、with-skill 输出或历史 comparison。
- 行为：0/6 assertions PASS（第 3 轮，修正后断言与最终 fixture）。未省略 `### Claude Code`/`### Codex`/`### Kimi Code` 小节（保留为一般性说明），也未呈现标题强格式、固定首句与「无固定版本路径」条件化收尾——6 条断言全部保持 skill 增量区分度。

## Failures / Findings

- 无 with-skill assertion failure。
- 无 NOT EXERCISED；全部 6 条断言由本地 fixture 完整触发，Coverage FULL。
- 区分度观察：第 3 轮修正断言后，条件省略断言（Claude/Codex/Kimi 小节省略与「无固定版本路径」声明）在 without-skill 侧也 FAIL（baseline 保留小节或未形成统一声明），skill 增量覆盖全部 6 条断言；此前第 2 轮观察到 Codex/Kimi 省略被 baseline 白捡的现象随断言收紧而消失。

## Next Steps

- 保留当前 outline、标题门禁与升级说明固定结构；后续修改这些规则时重新运行。
- 本 eval 与 eval-007 共同承接 eval-005 记录的 marketplace 正向分支 Coverage 缺口（见 eval-005 comparison 的 Coverage 记录更新）。

## Runtime Artifacts Policy

- 双侧 candidates 与 judge verdict 位于 `tmp/eval-runs/issue-220-r2/`，属于未提交运行期诊断产物。
- 长期只保留本 `comparison.md`；不提交 transcript、candidate、verdict、timing、run status 或 diagnostics。
