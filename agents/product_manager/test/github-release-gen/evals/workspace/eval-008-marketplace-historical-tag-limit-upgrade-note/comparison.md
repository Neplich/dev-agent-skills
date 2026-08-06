# Eval Result: eval-008-marketplace-historical-tag-limit-upgrade-note

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-008-marketplace-historical-tag-limit-upgrade-note`
- Test case: `marketplace 历史 tag 能力不完整时的条件省略`
- Prompt:

> 请根据 `release-package.md`、`docs/site/release-notes/v0.9.0.md` 和 `github-evidence.md` 准备 GitHub Release 预览。本仓库是 dev-agent-skills marketplace 宿主，历史 tag v0.9.0 的插件内容见 `.claude-plugin/marketplace.json` 与 `.codex/INSTALL.md`，该版本没有 `.kimi-plugin/plugin.json`。

- Expected output:

> 标题为 `v0.9.0 - {主题概述}` 强格式；升级说明按固定结构呈现：简述句按 v0.9.0 manifest 推导（6 个 role plugin 均更新到 `v0.9.0`）；`### Claude Code` 小节省略并在正文说明平台限制（/plugin update 无版本 pin，durable 正文无法承诺 v0.9.0 固定安装）；`### Codex` 小节省略（该版本 .codex/INSTALL.md 不含 TARGET_TAG 安装支持）；`### Kimi Code` 小节省略（该版本无 .kimi-plugin/plugin.json）；该 tag 无已验证固定版本安装路径，不得推荐不可用替代路径，收尾句包含由历史 manifest 推导的 6 个 plugin 并明确按默认分支（main）更新、不得承诺同步该 tag 能力；不生成空壳小节或臆造安装命令。

## Test Set / Fresh Run

- Eval schema: `evals.json` v1.0。
- Fixture manifest: `6e0fc2447801f563813c5383f41902c94ab8b2ed2718e0b1475207eeab32d777`（5 个可见文件；两侧逐字节一致）。
- Repository HEAD: `47adbbc9`。
- Fresh run window: 2026-08-07 00:58–01:14（Asia/Shanghai）。
- Runtime: 3 个独立会话，均为 `gpt-5.6-luna`、`model_reasoning_effort=medium`：fresh without-skill、fresh with-skill、fresh judge。
- Controlled variable: 两个 candidate 使用完全相同的 prompt、fixture manifest、HOME/CODEX_HOME 目录形态与同一份 `auth.json`；唯一变量是 with-skill lane 安装并加载目标 specialist skill。
- Physical isolation: 按 skill 先完成并销毁全部 baseline 随机顶层根，再创建 with-skill 根；32 个 candidate 全部完成并销毁后才创建第三套 judge 根。
- Candidate visibility: lane 中未放入 `eval_metadata.json`、`evals.json`、`expected_output`、assertions、历史 `comparison.md`、README 脚手架或 judge 材料；泄漏扫描为 0 命中。
- External data rule: 实时实体因 GitHub 认证、网络或当时集合缺失而不可得时，相关 assertion 记为 `NOT EXERCISED`，只影响 Coverage，不伪造成 Behavior 的 PASS/FAIL。

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **FULL**
- Overall result: FAIL
- With-skill summary: github-release-gen 已实际加载（status skill_load_hits=2；transcript 首先读取 SKILL.md 及其 references）。with_skill 仅生成预览，快照无写入，但升级说明未按历史 tag 能力条件省略相关小节。未发现读取评测脚手架泄漏。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

github-release-gen 已实际加载（status skill_load_hits=2；transcript 首先读取 SKILL.md 及其 references）。with_skill 仅生成预览，快照无写入，但升级说明未按历史 tag 能力条件省略相关小节。未发现读取评测脚手架泄漏。

## Without-Skill Baseline

without_skill 未加载 skill（skill_load_hits=0），仅作为对照；其 candidate.md 只报告已生成预览及包含三宿主限制，未改变 with_skill 判定。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `title_matches_marketplace_format` | **PASS** | with_skill candidate 的预览标题为 `v0.9.0 - 失败消息重试与统一附件模型兼容`，符合非空主题概述格式。 | without_skill candidate.md 仅报告生成预览，未提供可核验的标题正文。 |
| `upgrade_note_first_sentence_derived` | **PASS** | with_skill 正文 `## 升级说明` 后首段为“无破坏性变更，也没有新增 plugin。6 个 role plugin 均更新到 `v0.9.0`。”；fixture 的 marketplace.json 注册了 6 个 plugin，且 release note 明确为 6 个 role plugin。 | without_skill candidate.md 仅声称包含六个 plugin 清单，未提供首句以供核验。 |
| `claude_section_omitted_with_platform_limit` | **FAIL** | with_skill 正文实际包含 `### Claude Code` 小节；该 assertion 要求历史 tag 重跑时省略该小节，并在正文说明限制。虽然正文提到 `/plugin update` 无版本 pin，也声明无已验证固定版本路径，但小节未省略。 | without_skill candidate.md 报告包含 Claude 历史版本升级限制，但未提供正文结构细节。 |
| `codex_section_omitted_without_target_tag_support` | **FAIL** | with_skill 正文实际包含 `### Codex` 小节，且加入了 `Fetch and follow instructions from https://raw.githubusercontent.com/.../refs/tags/v0.9.0/.codex/INSTALL.md` 指令；fixture 与 trace 已确认目标 `.codex/INSTALL.md` 不含 TARGET_TAG 支持，断言要求省略小节且不得臆造该安装指令。 | without_skill candidate.md 报告包含 Codex 历史版本限制，但未提供正文结构细节。 |
| `kimi_section_omitted_without_plugin_json` | **FAIL** | with_skill 正文实际包含 `### Kimi Code` 小节。虽然其中如实说明无 `.kimi-plugin/plugin.json`、无 Kimi plugin 入口，但断言要求目标 tag 缺少 manifest 时省略该小节，不生成空壳小节。trace 第 15 行也显示 Kimi 文件 absent。 | without_skill candidate.md 报告包含 Kimi 历史版本限制，但未提供正文结构细节。 |
| `closing_sentence_derived` | **FAIL** | with_skill 正文虽写有“该 tag 无已验证的固定版本安装路径”，但收尾句未包含由 manifest 推导的 6 个 role plugin 数量，也未明确按默认分支 `main` 更新；因此没有满足要求的 closing sentence。 | without_skill candidate.md 仅报告包含六个 plugin 清单，未提供收尾句正文。 |

## Failures

- with_skill 实际加载了目标 skill，但违反了历史 marketplace 能力不完整时的条件省略要求：Claude、Codex、Kimi 三个小节均被保留。
- with_skill 臆造了目标 tag 的 Codex fetch 安装指令，尽管 trace 与 fixture 已确认该版本仅有不支持 TARGET_TAG 的普通安装文件。
- with_skill 缺少要求的、包含 6 个 plugin 且明确按默认分支 main 更新的收尾句。

## Not Exercised

- 无；本轮覆盖全部 assertions。

## Next Steps

- 重生成升级说明：省略 Claude Code、Codex、Kimi 三个小节；正文集中说明无已验证固定版本安装路径，并以 6 个 role plugin 和默认分支 main 完成收尾。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `141.175s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `112.661s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `78.547s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
