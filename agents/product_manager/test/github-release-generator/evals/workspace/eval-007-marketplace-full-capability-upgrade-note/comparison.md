# Eval Result: github-release-generator-marketplace-full-capability-upgrade-note

## Evaluation Target

- Skill: `github-release-generator`
- Test case: marketplace 当前 tag 能力齐全的标题强格式与升级说明正向分支
- Latest result: **PASS**（Behavior: PASS / Coverage: FULL）
- Overall result: PASS

## Review Context

- Issue: #220（marketplace 正向分支 eval 覆盖）；第 3 轮为 outline 收尾句规则修订后最终验证（无固定版本路径不承诺同步该 tag 能力）
- Date: 2026-08-03
- Final judge: 当前会话中的 fresh Codex validation agent
- Judge 独立读取当前 skill、reference、eval 定义/metadata/fixture 与 issue-220 fresh 双侧 candidate；verdict 完成前未读取 durable `comparison.md` 或旧 run tmp。
- 断言判据只以 fixture workspace 文件为准（伪造目标 tag 宿主文件：`.claude-plugin/marketplace.json` 7 plugins、`.codex/INSTALL.md` 含 TARGET_TAG、`.kimi-plugin/plugin.json` 存在），不以仓库根目录同名文件为准。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: 伪造 dev-agent-skills marketplace 宿主目标 tag（v1.0.0，7 role plugins、TARGET_TAG 支持、Kimi manifest 存在）、confirmed site Release Notes、curated GitHub evidence
- With-skill evidence: `tmp/eval-runs/issue-220-r3/with_skill/eval-007-marketplace-full-capability-upgrade-note/candidate-output.md`
- Without-skill evidence: `tmp/eval-runs/issue-220-r3/without_skill/eval-007-marketplace-full-capability-upgrade-note/candidate-output.md`
- Judge verdict: `tmp/eval-runs/issue-220-r3/judge/verdict.md`

## Assertions

- PASS `title_matches_marketplace_format`：标题为 `v1.0.0 - 文件卡片、原位重试与统一附件链路`，符合 `v1.0.0 - {概述}` 强格式且概述与已确认事实相关；without-skill FAIL（`Dev Agent Skills v1.0.0`，无破折号概述形态）
- PASS `upgrade_note_first_sentence`：简述句「无破坏性变更，也没有新增 plugin。7 个 role plugin 均更新到 `v1.0.0`。」，N=7 由 fixture manifest 推导；without-skill FAIL（改写为「本版本没有……」，未呈现要求首句形态）
- PASS `claude_section_verbatim`：`### Claude Code` 小节含 `/plugin marketplace update`、7 行 `/plugin update {role}@dev-agent-skills`、`/reload-plugins` 与无版本 pin 限制说明；without-skill FAIL（只有概括说明，无小节与逐字命令）
- PASS `codex_section_pinned_install`：`### Codex` 引用目标 tag raw `INSTALL.md` URL 并设 `TARGET_TAG=v1.0.0`；without-skill FAIL（只概述安装方式）
- PASS `kimi_section_plugin_install`：`### Kimi Code` 含 `/plugins install https://github.com/Neplich/dev-agent-skills/releases/tag/v1.0.0`；without-skill FAIL（未呈现小节与命令）
- PASS `plugin_list_derived_from_manifest`：指令列表恰好覆盖 fixture manifest 7 个 role plugin，无增删；without-skill PASS（按 manifest 列出 7 个 plugin，成员一致——第 3 轮 without-skill 唯一满足的断言）
- PASS `closing_sentence_present`：以「更新仓库后重新运行安装器，即可同步全部 7 个 role plugin 的 `v1.0.0` 能力。」收尾；without-skill FAIL（无固定收尾句）

## With Skill Behavior

- 完整应用 skill 与 reference：标题强格式、四节正文、升级说明三小节（Claude 逐字命令 + 无版本 pin 限制、Codex pinned install、Kimi release URL）、收尾句 N 按目标 tag manifest 推导。
- 保持站内事实与排除内部质量证据；preview only，无任何写操作；无 `release-preview.md`/`release-action.md` 残留。

## Without Skill Baseline

- 来源：issue-220 fresh baseline（2026-08-03），基于同一 eval prompt 与 fixture；未读取或应用 skill、reference、Agent README、with-skill 输出或历史 comparison。
- 行为：1/7 assertions PASS（第 3 轮，修正后断言与最终 fixture）。仅 `plugin_list_derived_from_manifest` 满足（能按 manifest 列出 7 个 plugin）；标题强格式、固定首句、三小节逐字命令模板、收尾句均缺失——skill 增量区分度明确。

## Failures / Findings

- 无 with-skill assertion failure。
- 无 NOT EXERCISED；全部 7 条断言由本地 fixture 完整触发，Coverage FULL。

## Next Steps

- 保留当前 outline、标题门禁与升级说明固定结构；后续修改这些规则时重新运行。
- 本 eval 与 eval-008 共同承接 eval-005 记录的 marketplace 正向分支 Coverage 缺口（见 eval-005 comparison 的 Coverage 记录更新）。

## Runtime Artifacts Policy

- 双侧 candidates 与 judge verdict 位于 `tmp/eval-runs/issue-220-r3/`，属于未提交运行期诊断产物。
- 长期只保留本 `comparison.md`；不提交 transcript、candidate、verdict、timing、run status 或 diagnostics。
