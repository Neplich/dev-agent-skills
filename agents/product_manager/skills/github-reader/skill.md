---
name: github-reader
description: Read and summarize GitHub repository project state for a PM. Use this skill whenever the user asks about project status, issue backlog, milestone progress, PR queue, what's blocking a release, what the team is working on, or wants a health check of a GitHub repo. Trigger on phrases like "项目状态", "milestone 进度", "有哪些 PR 在等 review", "backlog 里有什么", "哪些 issue 没有 assignee", "本周合并了什么", "release 准备好了吗", or any question about repo health. Also use this skill proactively when another skill (roadmap-generator, weekly-report) needs fresh GitHub data as input.
---

# GitHub Reader

Read a GitHub repository's current state and produce a structured Markdown summary. All data comes from `gh` CLI — no MCP needed.

This skill serves two purposes:
1. **Direct answer**: respond to the user's question about the repo
2. **Data feed**: provide structured input for downstream skills like `roadmap-generator` or `weekly-report`

## Step 1 — Establish repo context

```bash
gh repo view --json nameWithOwner,url,defaultBranchRef,description
```

If the user specified a repo (e.g. `owner/repo`), use that. Otherwise use the current directory's remote. Capture `OWNER`, `REPO`, and `REPO_URL` for link formatting.

## Step 2 — Determine query scope

Read the user's request to decide what to fetch. Three modes:

| Mode | When | What to fetch |
|------|------|---------------|
| **Full status** | "项目状态" / "health check" / no specific focus | Milestones + open issues summary + PR queue |
| **Focused query** | Specific question ("哪些 PR 等 review", "milestone X 进度") | Only the relevant data |
| **Feed mode** | Called by another skill needing raw data | Full status, output structured for downstream use |

Default to **Full status** if the intent is ambiguous.

## Step 3 — Fetch data

Run only what the scope requires. Commands below are the full toolkit — use selectively.

### Milestones
```bash
gh api repos/{OWNER}/{REPO}/milestones \
  --jq '.[] | {title, state, open_issues, closed_issues, due_on, html_url}' \
  -X GET -f state=open
```

### Open issues (grouped by milestone)
```bash
gh issue list \
  --json number,title,state,labels,milestone,assignees,createdAt,updatedAt \
  --state open --limit 100
```

### Recently closed issues (last 14 days)
```bash
gh issue list \
  --json number,title,closedAt,milestone \
  --state closed --limit 50 \
  --search "closed:>$(date -d '14 days ago' +%Y-%m-%d 2>/dev/null || date -v-14d +%Y-%m-%d)"
```

### PR queue
```bash
gh pr list \
  --json number,title,state,author,reviewDecision,createdAt,labels,isDraft \
  --state open --limit 100
```

> **[强制规则] PR 分类处理流程：**
> 1. 先按 `author.login` 过滤 bot（含 `[bot]` 后缀）→ 归入 Bot 区域
> 2. 再按 `isDraft` 过滤草稿 → 归入草稿区域
> 3. 剩余按 `reviewDecision` 分：`CHANGES_REQUESTED` → 需作者跟进；其余 → 待 Review
> 4. 待 Review 表格必须包含 `labels` 列（取 label name，逗号分隔；无标签写 `-`）
> 5. Full-status 模式下待 Review 表格最多 10 行，超出写汇总行

### Recently merged PRs (last 14 days)
```bash
gh pr list \
  --json number,title,mergedAt,author \
  --state merged --limit 30 \
  --search "merged:>$(date -d '14 days ago' +%Y-%m-%d 2>/dev/null || date -v-14d +%Y-%m-%d)"
```

## Step 4 — Compute health signals

From the fetched data, derive:

- **Milestone completion %** = `closed_issues / (open_issues + closed_issues) * 100`
- **Overdue milestones** = milestones with `due_on` in the past and `open_issues > 0`
- **Stale issues** = open issues not updated in > 30 days
- **Unassigned open issues** = issues with empty `assignees`
- **PRs waiting review** = open PRs where `reviewDecision` is `REVIEW_REQUIRED` or null, and not draft
- **Draft PRs** = open PRs where `isDraft` is true

## Step 5 — Format the output

Use this structure. Omit sections that have no relevant data.

```markdown
## 项目状态：{OWNER}/{REPO} — {TODAY}

### Milestones
| Milestone | 进度 | 截止日期 | 状态 |
|-----------|------|---------|------|
| [v2.0]({URL}) | 12/20 (60%) | 2024-04-01 | 🟡 进行中 |
| [v1.5]({URL}) | 8/8 (100%) | 2024-03-01 | ✅ 完成 |

> 状态图例：✅ 完成 / 🟢 顺利 / 🟡 进行中 / 🔴 逾期 / ⚪ 无截止日期

### Open Issues ({N} 个)

**按 Milestone 分组：**
- **v2.0**（{N} 个）：[#{N} 标题]({URL})、...
- **无 Milestone**（{N} 个）：[#{N} 标题]({URL})、...

**需关注：**
- 🙋 无 assignee：{N} 个
- 😴 30 天未更新：{N} 个

### PR 队列

**待 Review — 人工贡献（{N} 个，按等待时间排序）：**

| # | 标题 | 作者 | 等待 | 标签 |
|---|------|------|------|------|
| [#{N}]({URL}) | 标题 | @author | {N} 天 | external, needs-triage |

> **[强制规则] Full-status 模式下，此表格最多显示 10 条**。超出部分只写一行汇总："还有 {N} 个待 review PR 未列出，最老的是 #{X}（{Y} 天）"。Focused 模式不受此限制，显示全部。

**Bot/自动化 PR（{N} 个，可批量处理）：**
- Dependabot: {N} 个，Renovate: {N} 个

> **[强制规则] Bot PR 必须从"待 Review"表格中剥离。** 判断标准：author 为 `dependabot[bot]`、`renovate[bot]`、`github-actions[bot]`、`stainless-app[bot]`、`copilot-swe-agent[bot]` 或任何 `[bot]` 后缀的 author。这些 PR 只在此 Bot 区域统计，不出现在上方人工 PR 表格中。

**草稿（{N} 个）：**
- [#{N} 标题]({URL}) — @{author}，{N} 天

**需作者跟进（Changes Requested，{N} 个）：**
- [#{N} 标题]({URL}) — @{author}

**近 14 天已合并（{N} 个）：**
- [#{N} 标题]({URL})

### 健康摘要
- 共 {N} 个 open issue，{N} 个 open PR
- {N} 个 milestone 进行中，{N} 个逾期
- 近 14 天：合并 {N} 个 PR，关闭 {N} 个 issue
- ⚠️ 积压风险（等待 > 90 天的人工 PR）：{N} 个
```

**Milestone 状态判断：**
- `due_on` 为空 → ⚪ 无截止日期
- 完成率 100% → ✅ 完成
- `due_on` 已过期且 `open_issues > 0` → 🔴 逾期
- 完成率 ≥ 70% → 🟢 顺利
- 其他 → 🟡 进行中

## Feed mode output

When called by another skill, append a `---` separator and a machine-friendly YAML block after the Markdown report:

```yaml
---
github_reader_data:
  repo: owner/repo
  fetched_at: 2024-03-20
  open_issues_total: 15
  milestones:
    - title: v2.0
      completion_pct: 60
      open: 8
      closed: 12
      due_on: 2024-04-01
      overdue: false
  prs_awaiting_review: 3
  prs_draft: 1
  unassigned_issues: 4
  stale_issues: 2
```

This lets downstream skills parse state without re-fetching.

## Edge cases

- **No milestones**: skip that section, note "暂无 milestone" in the summary
- **Large repos (100+ issues)**: paginate with `--limit 200` or narrow by `--milestone` / `--label`
- **No GitHub auth**: `gh auth status` will fail — surface the error clearly and tell the user to run `gh auth login`
- **Focused query shortcut**: if the user only asks about PRs, skip issue fetching entirely to save time
