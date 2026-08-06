# Eval Result: eval-001-unreleased-mode

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-001-unreleased-mode`
- Test case: `unreleased-mode`
- Prompt:

> 我在 https://github.com/anthropics/anthropic-sdk-python 这个仓库里工作。帮我生成 Unreleased 章节 —— 也就是最新 release tag 之后合并的所有 PR，写成 Keep a Changelog 格式，输出到 docs/changelog/changelog-unreleased.md。

- Expected output:

> 生成 ## [Unreleased] 章节，包含最新 release 之后的 PR 列表，按 Added/Changed/Fixed 分组，每条带 PR 链接，写入 docs/changelog/changelog-unreleased.md

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
- With-skill summary: with_skill 实际加载了 changelog-gen（status.json skill_load_hits=2；transcript item_1 读取 SKILL.md），按要求创建并写入目标文件。trace 显示 Git/gh 查询分别因非 Git 工作区和未认证失败，网络查询也无可验证结果；因此 PR 相关断言无法覆盖。未发现读取评测脚手架泄漏。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

with_skill 实际加载了 changelog-gen（status.json skill_load_hits=2；transcript item_1 读取 SKILL.md），按要求创建并写入目标文件。trace 显示 Git/gh 查询分别因非 Git 工作区和未认证失败，网络查询也无可验证结果；因此 PR 相关断言无法覆盖。未发现读取评测脚手架泄漏。

## Without-Skill Baseline

without_skill 未加载 skill（skill_load_hits=0），但其 trace 也创建了目标文件并包含 Unreleased 标题；该结果仅作为对照，不影响 with_skill 判定。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `unreleased` | **PASS** | with_skill trace item_16 读取到写入内容，其中包含 `## [Unreleased]`；after-snapshot.json 也确认目标文件已生成。 | without_skill trace item_17 的文件内容同样包含 `## [Unreleased]`。 |
| `pr` | **NOT EXERCISED** | PR 范围属于实时 GitHub 数据；with_skill 的 git 查询因 `not a git repository` 失败，gh 查询因未认证失败，网络查询无可验证返回，不能确认实际 PR 集合或据此判定链接格式。 | without_skill 也没有 PR 条目，trace item_17 仅写入 `No changes yet.`，因此 PR 链接格式未被实际练习。 |
| `bot_pr_dependabot` | **NOT EXERCISED** | 没有可验证的实时 PR 实体可供判断是否跳过 dependabot 等 bot PR；不能把无法取得数据等同于 PASS。 | without_skill 没有 PR 条目，bot PR 过滤未被实际练习。 |
| `chore_ci_test` | **NOT EXERCISED** | 没有可验证的实时 PR 实体及其标题/内容可供判断 chore/ci/test 过滤；相关查询基础设施不可用。 | without_skill 没有 PR 条目，内部变更过滤未被实际练习。 |
| `versioned_changelog_file` | **PASS** | with_skill trace item_14 创建目录，item_15 明确新增 `docs/changelog/changelog-unreleased.md`；after-snapshot.json 确认该路径存在，candidate.md 也提供了该文件链接。 | without_skill trace item_16 的 file_change 同样明确写入 `docs/changelog/changelog-unreleased.md`。 |

## Failures

- 无 with-skill assertion failure。

## Not Exercised

- pr
- bot_pr_dependabot
- chore_ci_test

## Next Steps

- 提供可用的 GitHub/Git 数据或预置 PR fixture 后重跑，以覆盖 PR 链接与过滤断言。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `85.978s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `115.481s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `90.851s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
