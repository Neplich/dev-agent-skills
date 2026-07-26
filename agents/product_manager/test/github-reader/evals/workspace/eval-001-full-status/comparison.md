# Eval Result: eval-001-full-status

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-001-full-status`
- Test case: full-status
- Workspace: `workspace/eval-001-full-status`
- Classification: `(c)` 依赖实时外部数据。该用例验证 `github-reader` 能否通过 `gh` 读取公共仓库现状，不应增加静态 mock fixture 冒充真实运行。
- Latest result: **PARTIAL** — 本轮由当前会话中的同一个 fresh Codex subagent 按 no-leak 顺序重新生成 `with_skill` 与新的 `without_skill`。with-skill 满足 3/4 assertions；目标仓库实时不存在 milestone，现行 skill 要求跳过空表并说明“暂无 milestone”，因此既有 `milestone` assertion 的场景前提不成立。该项不是 GitHub 读取或 skill 行为回归。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: 只有 prompt 与 metadata，没有静态 GitHub 快照；这符合实时数据场景。
- Prompt: `帮我看一下 anthropics/anthropic-sdk-python 现在的项目状态，包括 milestone 进度、open issue 数量和 PR 队列情况`
- Fresh repository: `anthropics/anthropic-sdk-python`
- Live dependency: GitHub API、网络与已认证 `gh` CLI。
- with-skill queried at: `2026-07-26T16:23:33+08:00`（Asia/Shanghai；首次 repo metadata 请求发生一次 TLS handshake timeout，随后在同一 arm 内重试成功）
- without-skill queried at: `2026-07-26T16:25:45+08:00`（Asia/Shanghai）
- Query window for recent activity: `2026-07-12` 至各自抓取时点（近 14 天）。

## Same-Agent No-Leak Fresh Validation Method

1. 当前会话中的唯一 fresh Codex subagent 先只从 `eval_metadata.json` 提取原始 prompt，未读取 `evals.json`、assertions、expected output 或旧 `comparison.md`。
2. 同一 agent 的 with-skill arm 随后完整读取 Product Manager Agent README 与当前 `github-reader/SKILL.md`，自行用 `gh` 查询 prompt 指定仓库并锁定候选结果。
3. with-skill 锁定后，同一 agent 切换到 without-skill arm；该 arm 不应用 skill 或 README，只凭原始 prompt 重新独立调用 `gh`，未使用父代理预计算 snapshot，也未复用 with-skill 的查询结果。
4. 两个 arm 均锁定后，同一 fresh agent 才读取 canonical eval 定义、assertions、expected output 与旧 comparison，并亲自按当前 assertions 评审。
5. 两个 arm 分别查询 GitHub，没有共享预计算快照；运行期 transcript、verdict、diagnostics 或 outputs 均未落盘。

## Independent Live Snapshots and Drift

| 指标 | With skill（16:23:33 起） | Without skill（16:25:45） | 漂移判断 |
| --- | ---: | ---: | --- |
| Open milestones | 0 | 0 | 无漂移 |
| Open issues（排除 PR） | 144 | 144 | 无漂移 |
| Open PRs | 212 | 212 | 无漂移 |
| Draft PRs | 6 | 6 | 无漂移 |
| Changes requested | 2 | 2 | 无漂移 |

- with-skill 按当前 skill 的互斥展示规则统计：人工非草稿且非 `CHANGES_REQUESTED` 的待 Review `204` 个、草稿 `6` 个、需作者跟进 `2` 个、bot `0` 个；近 14 天 merged PR `6` 个、closed issue `1` 个。
- without-skill 报告 `204` 个 `REVIEW_REQUIRED`、`3` 个 approved、`2` 个 changes requested、`3` 个无 review decision，并统计到 `206` 个非草稿 PR。这里是分类口径不同，不是仓库状态漂移。
- with-skill 还统计 open issue 中无 assignee `141` 个、超过 30 天未更新 `111` 个，以及等待超过 90 天的人工非草稿且非 `CHANGES_REQUESTED` PR `83` 个。
- 两次查询相隔约 2 分钟，核心计数一致；本 comparison 只证明上述抓取时点，后续复验必须重新查询。

## Fresh With Skill

fresh with-skill 应用当前 Full status 流程，结果包括：

- 正确识别指定仓库，并从 GitHub 获取 milestone、open issue、open PR、近 14 天 merged PR 与近 14 天 closed issue 数据。
- API 返回 0 个 milestone；按 skill 的 `No milestones` edge case 不生成虚假进度表，并明确说明当前暂无 milestone。
- Open Issues 按“无 Milestone”归纳，并提供总数、无 assignee 与 stale 风险数字。
- PR 队列按互斥顺序区分 bot、草稿、changes requested 与其余待 Review；待 Review 最多展示 10 条，条目带 `[#NUMBER](URL)` 链接，超出部分用汇总说明。
- 单列近 14 天 merged PR，并在末尾给出 open issue、open PR、milestone、近期活动与长期积压的数字化健康摘要。

## Fresh Without Skill / Baseline

同一 fresh agent 的 baseline arm 未应用 `github-reader` skill 与 Product Manager Agent README，只凭原始 prompt 重新实时查询后返回：

- 0 个开放及已关闭 milestone、144 个 open issue、212 个 open PR。
- 给出 6 个 draft、206 个非草稿，以及 204 `REVIEW_REQUIRED`、3 approved、2 changes requested、3 无 review decision 的通用 PR 数字，并列出最老 10 个 open PR 的 number、author、createdAt 与原始 URL。
- 没有另查近期 merged PR，因而没有把当前待 review 与已合并 PR 分区；具体 PR 也未格式化为 `[#NUMBER](URL)`。
- 给出含关键数字的总体判断，但未覆盖 with-skill 的 stale、unassigned、bot 隔离、10 行展示规则与近期 closed issue 口径。

## Assertion Results

| Assertion | With skill | Without skill | Fresh judge 结论 |
| --- | --- | --- | --- |
| `milestone`：包含有标题、进度百分比的 Milestone 表格 | **FAIL（场景前提不成立）** | **FAIL（场景前提不成立）** | 两次 API 查询均返回 0 个 milestone。现行 skill 要求此时不生成空表；不能虚构进度百分比。 |
| `pr`：PR 队列区分待 review 和已合并 | **PASS** | **FAIL** | with-skill 单列当前待 Review 与近 14 天 merged；baseline 只描述当前 open PR。 |
| `assertion_3`：末尾有数字化健康摘要 | **PASS** | **PASS** | 两者均以数字总结状态；with-skill 的风险及近期活动口径更完整。 |
| `pr_2`：PR 条目使用 `[#NUMBER](URL)` | **PASS** | **FAIL** | with-skill 的具体 PR 条目使用正确链接格式；baseline 虽返回 number 与原始 URL，但未组成 assertion 要求的 Markdown 链接。 |

## Failures and Interpretation

- 唯一 with-skill failure 是 `milestone`。GitHub 查询成功，但仓库没有 assertion 假定的实体；伪造 milestone 表或百分比会违反当前 skill。
- same-agent fresh pair 消除了历史 baseline 与父代理预计算快照共用所造成的 answer-key / snapshot leakage：两个 arm 本轮各自实时查询，且同一 agent 在两个候选均锁定后才读取答案键并亲自 judge。
- 未修改 fixture、`evals.json`、assertions 或 specialist `SKILL.md`。

## External Failure vs Skill Regression

- **外部服务 / 基础设施失败**：GitHub API 超时、限流、DNS/网络不可达、`gh` 未认证、目标仓库不可访问或分页未完成。此类情况应记为 `BLOCKED` 或 infrastructure failure，不能判定 skill 回归。
- **Skill 回归**：外部查询成功且返回有效数据，但 with-skill 漏查 prompt 要求的 scope、错误计算数量、未分页导致截断、PR 分类错误、把 bot 混入人工队列、缺少近期 merged 分区、健康摘要或正确链接。
- **Live-data/assertion mismatch**：查询成功但仓库没有 assertion 假定的实体。本轮为 milestone 不存在，应保留真实 edge-case 输出并把该 assertion 记为场景前提不成立。

## Time-Sensitivity Risk

GitHub 数据会随 issue、PR、review 与 milestone 状态立即变化。本 comparison 不把任何数字作为固定 expected value；未来运行必须记录仓库、两条路径各自的精确抓取时间、查询窗口与独立快照，并区分真实漂移、分类口径差异和外部服务失败。

## Next Steps

- 本轮无需增加 fixture；保留实时 GitHub 查询设计。
- 在“不放宽 assertion”的本任务约束下，结果如实保持 `PARTIAL`。若维护者以后希望无 milestone 时也能通过，需要另行评估 assertion 是否接受 skill 已定义的 edge case。

## Runtime Artifacts Policy

- 没有向 canonical workspace 写入 transcripts、verdicts、timing、outputs 或 diagnostics。
- durable 结果只保留本 `comparison.md` 中必要的两份独立快照、行为摘要与 fresh judge 结论。
- 后续运行仍应把临时产物留在隔离 scratch 环境，并只将人工确认后的最新结论汇总回 canonical `comparison.md`。
