# Eval Result: eval-001-full-status

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-001-full-status`
- Test case: `full-status`
- Prompt:

> 帮我看一下 anthropics/anthropic-sdk-python 现在的项目状态，包括 milestone 进度、open issue 数量和 PR 队列情况

- Expected output:

> 结构化的项目状态报告，包含 Milestone 进度表、Open Issues 分组、PR 队列（待 review / 草稿 / 近期合并），以及健康摘要

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
- With-skill summary: with_skill 实际加载 github-reader（status.json 的 skill_load_hits=2，transcript 中完整读取 SKILL.md），按要求先执行仓库上下文查询；GitHub CLI 因未认证失败，随后如实报告无法读取并未伪造项目数据。快照前后仅有 fixture-manifest.json 且哈希不变，无写入。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

with_skill 实际加载 github-reader（status.json 的 skill_load_hits=2，transcript 中完整读取 SKILL.md），按要求先执行仓库上下文查询；GitHub CLI 因未认证失败，随后如实报告无法读取并未伪造项目数据。快照前后仅有 fixture-manifest.json 且哈希不变，无写入。

## Without-Skill Baseline

without_skill 仅作对照：尝试网页/API 查询后输出了项目数字，但未提供完整的 milestone 表、PR 分类队列或数字化健康摘要。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `milestone` | **NOT EXERCISED** | 所需实时 milestone 数据不可用：with_skill transcript 中 gh repo view 因未认证以 exit_code=4 失败，candidate 明确说明无法读取仓库状态，因此不能判定 milestone 表格要求。 | without_skill 声称无 milestone，但未输出带进度百分比的 Milestone 表格。 |
| `pr` | **NOT EXERCISED** | 所需实时 PR 队列数据不可用：with_skill 在仓库上下文认证失败后未能继续获取 PR 数据，candidate 明确要求先 gh auth login，因此不能判定 PR 分类要求。 | without_skill 仅给出 open/closed PR 数字和概述，未区分待 review、草稿及已合并队列。 |
| `assertion_3` | **NOT EXERCISED** | 健康摘要依赖实时 issue、PR、milestone 及近期活动数据；with_skill 因 GitHub CLI 未认证无法获取这些集合，candidate 未伪造摘要。 | without_skill 有文字性整体判断，但没有输出末尾数字化健康摘要。 |
| `pr_2` | **NOT EXERCISED** | with_skill 未获得任何 PR 条目，故无法验证 PR 条目的 [#NUMBER](URL) 格式；这是认证导致的实时数据不可用。 | without_skill 的 PR 相关内容没有 PR 条目链接可供核验。 |
| `data_completeness` | **NOT EXERCISED** | 各集合总数与分类统计所需的实时 GitHub 查询不可用；with_skill 如实报告无法读取，没有声称部分数据完整，因此该数据完整性断言不具备可执行覆盖。 | without_skill 仅对 open_issues_count 的 issue+PR 混合口径作了说明，但未提供各集合总数与分类统计的数据基础声明。 |

## Failures

- 无 with-skill assertion failure。

## Not Exercised

- milestone
- pr
- assertion_3
- pr_2
- data_completeness

## Next Steps

- 在 GitHub CLI 认证可用后重新运行 with_skill，以覆盖实时数据相关断言。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `32.257s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `71.423s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `62.277s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
