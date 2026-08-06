# Eval Result: eval-007-marketplace-full-capability-upgrade-note

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-007-marketplace-full-capability-upgrade-note`
- Test case: `marketplace 当前 tag 能力齐全的标题强格式与升级说明正向分支`
- Prompt:

> 请根据 `release-package.md`、`docs/site/release-notes/v1.0.0.md` 和 `github-evidence.md` 准备 GitHub Release 预览。本仓库是 dev-agent-skills marketplace 宿主，目标 tag 的插件内容见 `.claude-plugin/marketplace.json`、`.codex/INSTALL.md` 与 `.kimi-plugin/plugin.json`。

- Expected output:

> 标题为 `v1.0.0 - {主题概述}` 强格式；正文四节中「升级说明」按固定结构呈现：简述句（无破坏性变更，也没有新增 plugin。7 个 role plugin 均更新到 `v1.0.0`。）、### Claude Code 小节（9 行指令 + 无版本 pin 限制说明）、### Codex 小节（引用目标 tag 的 .codex/INSTALL.md 并设 TARGET_TAG=v1.0.0）、### Kimi Code 小节（/plugins install 目标 release URL）与收尾句（更新仓库后重新运行安装器，即可同步全部 7 个 role plugin 的 `v1.0.0` 能力。）；plugin 指令列表按目标版本 marketplace.json 推导。

## Test Set / Fresh Run

- Eval schema: `evals.json` v1.0。
- Fixture manifest: `edc8f94a65adc55e0678ac62eedc62d16f0ef2ba75af261ea8c90725c12656ab`（6 个可见文件；两侧逐字节一致）。
- Repository HEAD: `47adbbc9`。
- Fresh run window: 2026-08-07 00:58–01:14（Asia/Shanghai）。
- Runtime: 3 个独立会话，均为 `gpt-5.6-luna`、`model_reasoning_effort=medium`：fresh without-skill、fresh with-skill、fresh judge。
- Controlled variable: 两个 candidate 使用完全相同的 prompt、fixture manifest、HOME/CODEX_HOME 目录形态与同一份 `auth.json`；唯一变量是 with-skill lane 安装并加载目标 specialist skill。
- Physical isolation: 按 skill 先完成并销毁全部 baseline 随机顶层根，再创建 with-skill 根；32 个 candidate 全部完成并销毁后才创建第三套 judge 根。
- Candidate visibility: lane 中未放入 `eval_metadata.json`、`evals.json`、`expected_output`、assertions、历史 `comparison.md`、README 脚手架或 judge 材料；泄漏扫描为 0 命中。
- External data rule: 实时实体因 GitHub 认证、网络或当时集合缺失而不可得时，相关 assertion 记为 `NOT EXERCISED`，只影响 Coverage，不伪造成 Behavior 的 PASS/FAIL。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- Overall result: PASS
- With-skill summary: with_skill 实际加载 github-release-gen（status.json skill_load_hits=2；transcript item_1/item_2 读取技能及其 references），按正确顺序读取发布证据和三个宿主元数据，未执行写入；candidate 输出满足全部 7 条断言。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

with_skill 实际加载 github-release-gen（status.json skill_load_hits=2；transcript item_1/item_2 读取技能及其 references），按正确顺序读取发布证据和三个宿主元数据，未执行写入；candidate 输出满足全部 7 条断言。

## Without-Skill Baseline

without_skill 未加载目标 skill（skill_load_hits=0），仅作对照：输出使用裸版本标题、非固定升级结构且未给出完整指令列表。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `title_matches_marketplace_format` | **PASS** | with_skill candidate 的 Title 为 `v1.0.0 - 文件卡片、统一附件契约与失败消息重试`，符合 `v{VERSION} - {主题概述}`，且概述对应发布事实。trace item_1/item_2 显示先读取 github-release-gen 及 release-outline；未发现脚手架泄漏。 | without_skill candidate 仅输出 `# Dev Agent Skills v1.0.0`，不符合 marketplace 强格式。 |
| `upgrade_note_first_sentence` | **PASS** | candidate 的「升级说明」首段精确为「无破坏性变更，也没有新增 plugin。7 个 role plugin 均更新到 `v1.0.0`。」；trace item_7 通过 marketplace 一致性检查确认 7 个 plugins。 | without_skill 只在后文笼统写“没有新增 plugin，marketplace 保持 7 个 role plugins”，未按要求首句固定呈现。 |
| `claude_section_verbatim` | **PASS** | candidate 含 `### Claude Code`，先给出无版本 pin 限制及固定版本需用 Codex/Kimi 的说明，随后完整列出 marketplace update、7 个指定 role 的 update 和 reload-plugins，共 9 行指令，成员与顺序均匹配 marketplace.json。 | without_skill 仅用安装方式概述，没有完整的 9 行固定指令，也未给出所需的明确 durable 正文限制说明。 |
| `codex_section_pinned_install` | **PASS** | candidate 含 `### Codex`，引用 `https://raw.githubusercontent.com/Neplich/dev-agent-skills/refs/tags/v1.0.0/.codex/INSTALL.md` 并明确 setting `TARGET_TAG=v1.0.0`；fixture-manifest 与 trace item_2 证明目标 `.codex/INSTALL.md` 已读取。 | without_skill 使用 GitHub blob URL 的泛化安装描述，不符合要求的 raw tag URL 结构。 |
| `kimi_section_plugin_install` | **PASS** | candidate 含 `### Kimi Code`，指令精确为 `/plugins install https://github.com/Neplich/dev-agent-skills/releases/tag/v1.0.0`；目标 `.kimi-plugin/plugin.json` 在 fixture-manifest 和 trace item_2 中有证据。 | without_skill 仅概述使用 `/plugins install`，未给出精确 release URL 指令。 |
| `plugin_list_derived_from_manifest` | **PASS** | candidate 的 Claude Code 列表正好包含 pm-agent、designer-agent、engineer-agent、qa-agent、devops-agent、security-agent、docs-agent 7 个成员；trace item_7 输出 `marketplace ... 7 plugins`，与 `.claude-plugin/marketplace.json` 一致。 | without_skill 未列出 7 个 role plugin 的完整指令列表。 |
| `closing_sentence_present` | **PASS** | candidate 的升级说明以「更新仓库后重新运行安装器，即可同步全部 7 个 role plugin 的 `v1.0.0` 能力。」收尾，文本精确匹配要求。 | without_skill 没有该固定收尾句。 |

## Failures

- 无 with-skill assertion failure。

## Not Exercised

- 无；本轮覆盖全部 assertions。

## Next Steps

- 保留当前回归覆盖；目标 skill、fixture 或 assertion 契约变化时重新执行 fresh paired validation。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `120.418s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `107.237s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `83.485s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
