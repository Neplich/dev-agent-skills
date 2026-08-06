# Eval Result: eval-002-single-version-mode

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-002-single-version-mode`
- Test case: `single-version-mode`
- Prompt:

> 在 https://github.com/anthropics/anthropic-sdk-python 仓库，帮我生成最新 release 版本的 changelog 条目，使用 Keep a Changelog 格式，包含该版本对应的所有 PR 引用，并写入 docs/changelog/changelog-v{version}.md。

- Expected output:

> 生成最新 release tag 的版本块，格式为 ## [v{VERSION}] - YYYY-MM-DD，包含该版本窗口内的 PR，分组写入，每条带 PR 链接，并写入 docs/changelog/changelog-v{version}.md

## Test Set / Fresh Run

- Eval schema: `evals.json` v1.0。
- Fixture manifest: `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`（0 个可见文件；两侧逐字节一致）。
- Repository HEAD: `47adbbc9`。
- Fresh run window: 2026-08-07 00:58–01:14（Asia/Shanghai）。
- Runtime: 3 个独立会话，均为 `gpt-5.6-luna`、`model_reasoning_effort=medium`：fresh without-skill、fresh with-skill、fresh judge。
- Controlled variable: 两个 candidate 使用完全相同的 prompt、fixture manifest、HOME/CODEX_HOME 目录形态与同一份 `auth.json`；唯一变量是 with-skill lane 安装并加载目标 specialist skill。
- Physical isolation: 按 skill 先完成并销毁全部 baseline 随机顶层根，再创建 with-skill 根；32 个 candidate 全部完成并销毁后才创建第三套 judge 根。
- Candidate visibility: lane 中未放入 `eval_metadata.json`、`evals.json`、`expected_output`、assertions、历史 `comparison.md`、README 脚手架或 judge 材料；泄漏扫描为 0 命中。
- External data rule: 实时实体因 GitHub 认证、网络或当时集合缺失而不可得时，相关 assertion 记为 `NOT EXERCISED`，只影响 Coverage，不伪造成 Behavior 的 PASS/FAIL。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **PARTIAL**
- Overall result: PASS (partial coverage)
- With-skill summary: changelog-gen 实际加载（skill_load_hits=2，transcript item_1 读取 SKILL.md），成功写入目标版本文件；GitHub 实时数据查询受认证/网络失败影响。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

changelog-gen 实际加载（skill_load_hits=2，transcript item_1 读取 SKILL.md），成功写入目标版本文件；GitHub 实时数据查询受认证/网络失败影响。

## Without-Skill Baseline

对照侧未加载 skill（skill_load_hits=0），但也写入了目标文件；仅作基线，不影响 with_skill 判定。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `v_version_yyyy_mm_dd` | **PASS** | trace item_16 显示文件内容含 `## [v0.120.2] - 2026-07-28`，candidate.md 也报告相同版本和日期。 | without_skill 文件为 `## [0.120.2] - 2026-07-28`，缺少 v 前缀。 |
| `release_tag` | **NOT EXERCISED** | with_skill 尝试了 `gh release list`（trace item_4），但因未认证失败；随后 `git ls-remote` 因无法解析 github.com 失败（item_5）。candidate 的 release 声明没有可用实时证据或 fixture 支撑。 | without_skill 也报告 v0.120.2，但其外部 release 查询没有可用结果。 |
| `pr_conventional_commit` | **NOT EXERCISED** | PR #300 的实时元数据/原始标题不可用：trace item_4 认证失败、item_5 网络失败，web_search 项无返回内容；因此无法验证是否确实清除了 conventional commit 前缀。 | without_skill 输出 `Support MCP SDK v2 alongside v1`，表面上已清洗前缀，但无可验证原始 PR 标题。 |
| `breaking_change_breaking` | **NOT EXERCISED** | 无法取得 PR 标题和 body，不能判断该版本是否存在 breaking change；trace 中没有可用的 PR 元数据结果。 | without_skill 未添加 `⚠️ BREAKING`，但同样无法确认条件是否触发。 |
| `section` | **PASS** | trace item_16 展示写入内容仅包含有条目的 `### Fixed` section，且该 section 下有 PR #300 条目，没有空 section；after-snapshot 证明目标文件已写入。 | without_skill 也只输出有内容的 `### Fixed` section。 |

## Failures

- 无 with-skill assertion failure。

## Not Exercised

- release_tag
- pr_conventional_commit
- breaking_change_breaking

## Next Steps

- 保留当前回归覆盖；目标 skill、fixture 或 assertion 契约变化时重新执行 fresh paired validation。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `100.176s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `62.473s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `62.677s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
