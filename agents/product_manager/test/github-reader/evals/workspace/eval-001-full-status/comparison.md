# Eval Result: eval-001-full-status

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-001-full-status`
- Test case: full-status
- Workspace: `workspace/eval-001-full-status`
- Classification: `(c)` 依赖实时外部数据。该用例的目的就是验证 `github-reader` 能否通过 `gh` 读取公共仓库现状；不应增加静态 mock fixture 冒充真实运行。
- Latest result: **PARTIAL** — 本轮已生成 fresh `with_skill` 与 fresh `without_skill` 成对结果；with-skill 满足 3/4 assertions，并正确执行现行 skill 的 “No milestones” edge case，但目标仓库在抓取时没有开放 milestone，因此无法同时满足既有 `milestone` assertion 对“Milestone 表格”的字面要求。该缺口是 live 数据前提与 assertion 的不匹配，不是 GitHub 读取或 skill 行为回归。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: 只有 prompt 与 metadata，未提供静态 GitHub 快照；这对实时数据场景是正确设计。
- Prompt: `帮我看一下 anthropics/anthropic-sdk-python 现在的项目状态，包括 milestone 进度、open issue 数量和 PR 队列情况`
- Expected output: 结构化的项目状态报告，包含 Milestone 进度表、Open Issues 分组、PR 队列（待 review / 草稿 / 近期合并），以及健康摘要。
- Fresh snapshot repository: `anthropics/anthropic-sdk-python`
- Fresh snapshot fetched at: `2026-07-26T15:19:54+08:00`（CST / Asia/Shanghai）
- Live dependency: GitHub API 与已认证 `gh` CLI；本轮 `gh auth status`、仓库读取、REST/GraphQL 查询均成功。
- Query window for recent activity: `2026-07-12` 至抓取时点（近 14 天）。

## Live Snapshot

同一份 live snapshot 被用于 fresh with-skill 与 fresh without-skill，避免两条路径因仓库状态变化产生不可比结果：

- Open milestones: `0`
- Open issues: `144`，其中无 assignee `141`，超过 30 天未更新 `111`，带 milestone `0`
- Open PRs: `212`
  - Awaiting review: `201`
  - Drafts: `6`
  - Changes requested: `2`
  - Approved: `3`
  - Bot PRs: `0`
  - 等待超过 90 天的人工 PR: `81`
- 近 14 天 merged PRs: `6`（包括 [#1780](https://github.com/anthropics/anthropic-sdk-python/pull/1780)、[#1775](https://github.com/anthropics/anthropic-sdk-python/pull/1775)、[#1772](https://github.com/anthropics/anthropic-sdk-python/pull/1772)）
- 近 14 天 closed issues: `1`
- 最老的 awaiting-review PR: [#543](https://github.com/anthropics/anthropic-sdk-python/pull/543)，创建于 `2024-06-18T09:52:52Z`

数据由 `gh repo view`、`gh api repos/.../milestones`、`gh api graphql`、`gh issue list` 与 `gh pr list` 实时获取。GraphQL `totalCount` 与分页后的列表数量交叉核对，确认 open issue 与 open PR 数量没有被默认 `--limit 100` 截断。

## Fresh With Skill

本轮 fresh judge 读取当前 Product Manager Agent README、`github-reader/SKILL.md`、eval 定义与 metadata 后，按 Full status 路径应用 skill，并基于上述 live snapshot 生成结果。观察到：

- 正确识别指定仓库并通过 `gh` 获取 milestone、issue、open PR、近期 merged PR 与近期 closed issue 数据。
- 目标仓库没有开放 milestone；按 skill 的 `No milestones` edge case 跳过空表，并在健康摘要明确写出“暂无开放 milestone / 0 个进行中”，没有伪造 milestone 行或完成率。
- Open Issues 按“无 Milestone”分组，并给出 open、无 assignee、stale 数字。
- PR 队列区分 awaiting review、draft、changes requested、bot 与近 14 天 merged；awaiting-review 表按等待时间排序且限制为 10 行，超出部分使用汇总行。
- PR 条目使用 `[#NUMBER](URL)` 格式，例如 [#543](https://github.com/anthropics/anthropic-sdk-python/pull/543)；近期 merged 条目也带 GitHub 链接。
- 结尾健康摘要包含 open issue、open PR、开放 milestone、近期 merged/closed 与超过 90 天的人工 PR 数量。

## Fresh Without Skill / Baseline

本轮 fresh baseline 不读取或应用 `github-reader` skill 与 Product Manager Agent README，仅使用相同 prompt 和同一份 live snapshot 重新回答，未复用历史 baseline。观察到：

- 能给出通用数字概览：0 个开放 milestone、144 个 open issue、212 个 open PR。
- 能按通用 GitHub 字段简要列出 awaiting review、draft、changes requested、approved 数量，并为代表性 PR 提供链接。
- 因 prompt 只明确询问“PR 队列”，baseline 没有主动拉入或单列近 14 天 merged PR，因而未满足 skill-specific 的“待 review / 已合并”区分。
- 同样基于真实数据说明“没有开放 milestone”，没有为了满足 assertion 伪造 Milestone 进度表。
- 能给出简短数字摘要，但缺少 with-skill 的 issue 风险信号、10 行上限、bot 隔离、等待超过 90 天积压风险和近期 closed issue 口径。

## Assertion Results

| Assertion | With skill | Without skill | Fresh judge 结论 |
| --- | --- | --- | --- |
| `milestone`：包含有标题、进度百分比的 Milestone 表格 | **FAIL（场景前提不成立）** | **FAIL（场景前提不成立）** | API 返回 0 个开放 milestone。现行 skill 明确要求此时跳过该 section 并注明“暂无 milestone”；伪造空表或虚构百分比会违背 skill。 |
| `pr`：PR 队列区分待 review 和已合并 | **PASS** | **FAIL** | with-skill 单列 awaiting review 与近 14 天 merged；baseline 只回答当前 open PR 队列。 |
| `assertion_3`：末尾有数字化健康摘要 | **PASS** | **PASS** | 两者均有数字摘要；with-skill 额外覆盖 stale、unassigned、近期活动和长期积压。 |
| `pr_2`：PR 条目使用 `[#NUMBER](URL)` | **PASS** | **PASS** | 两者的代表性 PR 均使用正确 GitHub 链接格式。 |

## Failures and Interpretation

- 唯一 with-skill assertion failure 是 `milestone`。抓取时目标仓库没有开放 milestone，而 skill 的当前 edge case 与 assertion 的字面要求冲突；这不应被解释为 skill 回归。
- Fresh pair 已消除历史 comparison 缺少 without-skill baseline 的证据债务，但在不修改 assertion、目标仓库状态不变的前提下，Latest result 仍应如实保持 `PARTIAL`。
- 未修改 `evals.json` assertion，也未新增静态 GitHub fixture。

## External Failure vs Skill Regression

- **外部服务失败 / 基础设施失败**：`gh auth status` 失败、GitHub API 超时或限流、DNS/网络不可达、目标仓库不可访问、分页未完成。这些情况应记录为 `BLOCKED` 或 infrastructure failure，不能据此判定 skill 回归。
- **Skill 回归**：外部查询成功且返回有效数据，但应用 skill 后漏查 prompt 要求的 scope、错误计算数量/完成率、未分页导致计数截断、未按规则分类 PR、把 bot 混入人工待 review、缺少健康摘要或生成错误链接。
- **Live-data/assertion mismatch**：外部查询成功但仓库没有 assertion 假定的实体（本轮为开放 milestone）。应保留真实 edge-case 输出并把该 assertion 记为场景前提不成立，不能制造数据令其通过。

## Time-Sensitivity Risk

GitHub 数据会在提交 issue、关闭 issue、创建/合并 PR、review 状态变化或维护 milestone 时立即变化。本 comparison 只证明上述抓取时点的 fresh pair；未来复验必须重新记录仓库、精确时间、查询窗口和快照数字，不能把本轮数字当成固定预期或复用本轮 baseline。

## Next Steps

- 本轮无需增加 fixture；保留实时 GitHub 查询设计。
- 若维护者希望该 live eval 在“没有开放 milestone”时也能判为 PASS，需要另行评估 assertion 是否应接受 skill 已定义的 edge-case 文案。本任务禁止放宽 assertions，因此本轮不修改。

## Runtime Artifacts Policy

- 本轮没有把 transcripts、verdicts、timing、outputs 或 diagnostics 写入 canonical workspace。
- Live CLI 输出仅用于当前 fresh judge；durable 结果只保留本 `comparison.md` 中的必要快照、成对行为摘要与判断。
- 后续运行仍应在隔离 scratch 环境生成临时产物，并只把人工确认后的最新结论汇总回 canonical `comparison.md`。
