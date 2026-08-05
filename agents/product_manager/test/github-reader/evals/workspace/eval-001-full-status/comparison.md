# Eval Result: eval-001-full-status

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-001-full-status`
- Test case: Full status
- Workspace: `workspace/eval-001-full-status`
- Classification: `(c)` 依赖实时外部数据；验证 `github-reader` 是否通过已认证 `gh` 获取真实仓库状态。
- Behavior result: **PASS** — 当前会话中的 fresh validator 严格按 no-leak 顺序生成并锁定两个独立 live arm 后才读取 assertions。with-skill 在实际触发的 4 条 assertions 上满足 4/4，未发现行为回归；原记录的 4/5 来自将未触发的 `milestone` 计入分母。without-skill 原记录为 3/5。
- Coverage result: **PARTIAL** — `milestone` 为 **NOT EXERCISED**：目标仓库当时没有 open milestone，无法触发 assertion 要求的“有标题、进度百分比”的表格；skill 正确执行了“暂无 milestone” edge case，没有虚构数据。
- Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。
。
- 证据来源：2026-07-28 fresh run（沿用既有记录，本轮仅做结果模型迁移，未重新执行 eval）。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: `eval-001-full-status` 当前 prompt 与 metadata；不包含静态 GitHub 快照。
- Prompt: `帮我看一下 anthropics/anthropic-sdk-python 现在的项目状态，包括 milestone 进度、open issue 数量和 PR 队列情况`
- Live repository: `anthropics/anthropic-sdk-python`
- Live dependency: GitHub API、网络、已认证 `gh` CLI。
- Fixture/eval revision: 2026-07-28 工作树中的当前 `eval_metadata.json` 与 `evals.json`。
- with-skill query: 2026-07-28 17:58:04–17:58:50 CST。
- without-skill query: 2026-07-28 18:00:11–18:00:40 CST。
- with-skill recent-activity window: `>2026-07-14` 至查询时点。

## Fresh Validation Method

1. 先只读取 `eval_metadata.json` 提取原始 prompt；未读取 `evals.json`、旧 comparison 或 assertions。
2. with-skill arm 完整读取当前 `github-reader/SKILL.md` 与 Product Manager Agent README，使用已认证 `gh` 独立查询，并把命令、时间、原始 JSON、最终报告保存到隔离 runtime 目录后以 SHA-256 锁定。
3. 锁定 with-skill 后，without-skill arm 不读取或应用 skill/README，只凭原始 prompt 重新调用 `gh`，保存独立命令、时间、原始 JSON、报告并锁定；没有复用 with-skill 查询结果。
4. 两个 arm 均锁定并通过 checksum 复核后，才读取 eval-001 当前 5 条 assertions 与旧 comparison，逐条判定。
5. canonical fixture 中只更新本 `comparison.md`；运行期证据未纳入 git。

## Independent Live Snapshots

| 指标 | With skill | Without skill | 漂移判断 |
| --- | ---: | ---: | --- |
| Open milestones | 0 | 0 | 无漂移 |
| Open issues | 143 | 143 | 无漂移 |
| Open PRs | 213 | 213 | 无漂移 |
| Draft PRs | 6 | 6 | 无漂移 |
| Changes Requested | 2 | 2 | 无漂移 |

with-skill 通过 Search API `total_count` 与独立计算集合确认：

- Open issues 143/143、open PRs 213/213。
- 近 14 天 merged PRs 6/6、closed issues 1/1。
- 所有集合均未截断。
- Open issues 中无 assignee 140 个、30 天未更新 111 个。
- PR 互斥分类为：bot 0、draft 6、Changes Requested 2、其余人工待 Review 205；其中等待超过 90 天 87 个。

without-skill 从独立 `gh list --limit 1000` 返回集合统计 143 个 open issue 与 213 个 open PR；PR 原始 review 分布为非草稿 Review Required 198、Changes Requested 2、Approved 3、无 decision 4，另有 draft 6。两个集合的返回量均小于 1000 上限。

## With-Skill Behavior

- 正确识别 Full status scope，并查询 repo metadata、精确集合总数、open milestones、open issues、open PRs、近 14 天 merged PRs 与 closed issues。
- 仓库没有 open milestone；报告明确写“暂无 open milestone”，未虚构进度百分比。
- Open Issues 给出 143 的精确总数、milestone 分组、无 assignee 与 stale 风险。
- PR 按 bot → draft → Changes Requested → 待 Review 的互斥顺序分类；待 Review 表格限制为 10 条且包含标签列，具体条目使用 `[#NUMBER](URL)`。
- 单列近 14 天已合并 PR，并在末尾给出数字化健康摘要、截断状态及长期积压风险。

## Without-Skill Baseline

baseline 只依据原始 prompt 重新查询 GitHub：

- 报告 0 个 open milestone、143 个 open issue、213 个 open PR，并指出 140 个 issue 未分配。
- 把 open PR 按原始 review decision 与 draft 状态分类，列出最老 5 个 PR，具体条目使用正确 Markdown 链接。
- 提供包含关键数字的风险判断，并声明查询使用最多 1000 条的集合且实际返回均小于上限。
- 没有查询近期 merged PR，因此没有把“待 review”与“已合并”分区；也没有 with-skill 的 Search API 精确总数、stale issue、bot 隔离、10 行展示和近期 closed issue 口径。

## Assertion Results

| Assertion | With skill | Without skill | Fresh judge 结论 |
| --- | --- | --- | --- |
| `milestone`：包含有标题、进度百分比的 Milestone 表格 | **NOT EXERCISED** | **NOT EXERCISED** | 两个独立查询均返回 0 个 open milestone，场景前提不成立。现行 skill 要求此时说明“暂无 milestone”而不是虚构表格。 |
| `pr`：PR 队列区分待 review 和已合并 | **PASS** | **FAIL** | with-skill 单列人工待 Review 和近 14 天 merged；baseline 只报告 open PR 队列。 |
| `assertion_3`：末尾有数字化健康摘要 | **PASS** | **PASS** | with-skill 有独立健康摘要；baseline 的总体判断也用 open issue、open PR 与等待时长数字归纳风险。 |
| `pr_2`：PR 条目使用 `[#NUMBER](URL)` | **PASS** | **PASS** | 两份报告的具体 PR 条目都符合要求。 |
| `data_completeness`：总数、分类及截断有明确数据基础 | **PASS** | **PASS** | with-skill 明确给出四组 fetched/total 且均无截断；baseline 明确说明集合上限与实际返回均小于上限，分类基于该完整返回集合。 |

## Failures

- 未发现已触发路径的 with-skill 回归。
- Coverage gap：`milestone` live-data/assertion mismatch；查询成功，但仓库没有 assertion 假定的实体，因此记为 `NOT EXERCISED`。生成虚假 milestone 或百分比会违反 skill。
- without-skill 额外失败 `pr`：没有查询或展示 merged PR，无法区分待 review 与已合并。
- GitHub、网络、认证和仓库访问均成功，本轮不是 infrastructure failure，也没有发现 Full status 数据完整性回归。

## Next Steps

- 保持 Behavior result **PASS**、Coverage result **PARTIAL** 和 Overall result **PASS (partial coverage)**，不为满足 `milestone` assertion 而虚构数据。
- 若维护者希望“无 milestone”也是成功场景，应另行调整 assertion，使其接受明确的 edge-case 声明；本轮不修改 eval 定义。
- 后续 fresh run 必须重新查询 live GitHub，不复用本轮快照。

## Runtime Artifact Policy

- runtime 命令、时间、原始 JSON、两个报告、checksums 与 verdict 保存在 `tmp/eval-runs/github-reader-eval-001-2026-07-28/`，不纳入 git。
- canonical workspace 不保存 transcripts、raw outputs、timing、diagnostics 或 verdict；durable 结果仅更新本 `comparison.md`。
- fresh validation 过程未修改 canonical fixture、`evals.json` 或 specialist `SKILL.md`；本 issue 的协议与 assertion 修改由主流程维护。
