---
name: roadmap-generator
description: "Internal PM specialist—not a direct entry point. Invoked by pm-agent after entry classification to create or update roadmap docs from GitHub milestones, issues, PRs, and release context."
visibility: internal
---

# Roadmap Generator

Generate or update `docs/roadmap.md` from GitHub Milestones, Issues, and PRs. All data comes from `gh` CLI.

This skill has two modes:
1. **Generate**: create a fresh roadmap from current GitHub state
2. **Update**: read existing `docs/roadmap.md`, sync with latest GitHub data, preserve manual annotations

## Step 1 — Establish repo context

```bash
gh repo view --json nameWithOwner,url,description
```

Capture `OWNER`, `REPO`, `REPO_URL`. If the user specified a repo, use that; otherwise use the current directory's remote.

## Step 2 — Check for existing roadmap

```bash
cat docs/roadmap.md 2>/dev/null
```

- If exists → **Update mode**: preserve manual sections (marked with `<!-- manual -->` comments), update data-driven sections
- If not exists → **Generate mode**: create from scratch

## Step 3 — Fetch GitHub data

### Milestones (open + recently closed)
```bash
# Open milestones
gh api repos/{OWNER}/{REPO}/milestones \
  --jq '.[] | {title, state, open_issues, closed_issues, due_on, html_url, description}' \
  -X GET -f state=open -f sort=due_on -f direction=asc

# Recently closed milestones (for "已完成" section)
gh api repos/{OWNER}/{REPO}/milestones \
  --jq '.[] | {title, state, open_issues, closed_issues, due_on, html_url}' \
  -X GET -f state=closed -f sort=due_on -f direction=desc -f per_page=5
```

### Issues per milestone
```bash
gh issue list \
  --json number,title,state,labels,assignees,milestone \
  --state all --milestone "{MILESTONE_TITLE}" --limit 100
```

### Open issues without milestone (backlog candidates)
```bash
gh issue list \
  --json number,title,labels,assignees,createdAt \
  --state open --search "no:milestone" --limit 50
```

### Labels for categorization
```bash
gh label list --json name,color,description --limit 100
```

Use labels to categorize issues into roadmap themes. Common patterns:
- `feature` / `enhancement` → 功能
- `bug` → 修复
- `tech-debt` / `refactor` → 技术优化
- `docs` → 文档
- Priority labels (`P0`, `P1`, `priority:high`) → 排序依据

## Step 4 — Build roadmap structure

Organize milestones into timeline phases:

### Phase classification rules

| Condition | Phase |
|-----------|-------|
| Milestone `state=closed` | ✅ 已完成 |
| Milestone `due_on` is within 30 days or past due with open issues | 🔴 当前冲刺 |
| Milestone `due_on` is 31-90 days out | 🟡 近期计划 |
| Milestone `due_on` is 90+ days out | 🔵 远期规划 |
| Milestone `due_on` is null → apply semantic inference (see below) | varies |
| Issues with no milestone | 📋 Backlog |

### Semantic inference for no-date milestones

When `due_on` is null, infer phase from the milestone **name pattern**:

| Name pattern | Inferred phase | Rationale |
|---|---|---|
| Patch version: `v1.2.3`, `1.26.2`, `go1.25.9`, `v0.22.1` | 🔧 当前补丁 | Patch releases are typically imminent |
| Minor/major version: `v2.0`, `go1.27`, `v1.114.0` (higher minor) | 🚀 下一版本 | Next planned release |
| Far-future major: `v3.0`, `go1.28` (2+ versions ahead) | 🔵 远期规划 | Longer horizon |
| Tool/sub-project version: `gopls/v0.23.0`, `tools/v1.2` | 🛠️ 工具生态 | Sub-project versioning |
| Named: `Backlog`, `Unplanned`, `backlog`, `unplanned`, `未排期` | ⚪ 未排期 | Explicitly unscheduled |
| Named: `On Deck`, `Next`, `Planned` | 🟡 近期计划 | Queued for planning |
| Named: `Proposal`, `RFC`, `Ideas` | 💡 提案 | Pre-planning ideas |
| Anything else with no date | ⚪ 未排期 | Default fallback |

Apply semantic inference **only when `due_on` is null**. If `due_on` exists, always use date-based classification.

### Issue grouping within each milestone

**Step 1: Always surface release blockers first.**
If any issues have a `release-blocker` label, create a dedicated section at the top of the milestone:
```
**🚨 发布阻塞项**
- [ ] [#{N} 标题](URL)
```

**Step 2: Group remaining issues by domain area.**
First try label-based domain grouping (use the most specific domain label):
- Labels containing `auth`, `login`, `oauth` → 🔐 认证
- Labels containing `ui`, `ux`, `design`, `theme`, `layout` → 🎨 界面
- Labels containing `mcp`, `plugin`, `extension` → 🔌 扩展
- Labels containing `terminal`, `shell`, `cli` → 💻 终端
- Labels containing `perf`, `performance`, `speed` → ⚡ 性能
- Labels containing `security`, `cve`, `vuln` → 🛡️ 安全
- Labels containing `docs`, `documentation` → 📖 文档
- Labels `bug`, `fix`, `regression` → 🐛 修复
- Labels `feature`, `enhancement` → ✨ 新功能
- Labels `tech-debt`, `refactor`, `chore`, `debt` → 🔧 技术优化
- Everything else → 📝 其他

If fewer than 3 distinct domain groups exist, fall back to bug/feature/tech-debt/其他 grouping.

## Step 5 — Format the output

Write to `docs/roadmap.md` using this structure:

```markdown
# 项目路线图

> 最后更新：{TODAY}
> 数据来源：[{OWNER}/{REPO}]({REPO_URL}) GitHub Milestones & Issues
> 自动生成，手动标注区域请用 `<!-- manual -->` 包裹以防覆盖

---

## 🔴 当前冲刺

### [{MILESTONE_TITLE}]({MILESTONE_URL}) — 截止 {DUE_DATE}

进度：██████████░░░░░░ 65% ({CLOSED}/{TOTAL})

**✨ 新功能**
- [x] [#{N} 标题]({URL}) @assignee
- [ ] [#{N} 标题]({URL}) @assignee

**🐛 修复**
- [x] [#{N} 标题]({URL})
- [ ] [#{N} 标题]({URL})

**🔧 技术优化**
- [ ] [#{N} 标题]({URL})

---

## 🟡 近期计划

### [{MILESTONE_TITLE}]({MILESTONE_URL}) — 截止 {DUE_DATE}

进度：████░░░░░░░░░░░░ 25% ({CLOSED}/{TOTAL})

**✨ 新功能**
- [ ] [#{N} 标题]({URL})

---

## 🔵 远期规划

### [{MILESTONE_TITLE}]({MILESTONE_URL})

{MILESTONE_DESCRIPTION}

- [ ] [#{N} 标题]({URL})

---

## ⚪ 未排期

### [{MILESTONE_TITLE}]({MILESTONE_URL})

- [ ] [#{N} 标题]({URL})

---

## ✅ 已完成

### [{MILESTONE_TITLE}]({MILESTONE_URL}) — {CLOSED_DATE}

{CLOSED}/{TOTAL} 完成

---

## 📋 Backlog（未关联 Milestone）

> 以下 issue 尚未分配到任何 milestone，可作为后续版本的候选。

| # | 标题 | 标签 | 创建时间 |
|---|------|------|---------|
| [#{N}]({URL}) | 标题 | `label1`, `label2` | {DATE} |
```

### Progress bar generation rules

Generate a text-based progress bar (16 chars wide):

```
0%:   ░░░░░░░░░░░░░░░░
25%:  ████░░░░░░░░░░░░
50%:  ████████░░░░░░░░
75%:  ████████████░░░░
100%: ████████████████
```

Formula: `filled = round(percentage / 100 * 16)`, use `█` for filled, `░` for empty.

### Mandatory formatting rules

> **[强制规则] Issue 状态映射：**
> - Issue `state=closed` → `- [x]`（已完成）
> - Issue `state=open` → `- [ ]`（待完成）
> - 每个 issue 必须带 GitHub 链接 `[#{N} 标题]({URL})`

> **[强制规则] Assignee 显示：**
> - 有 assignee → 在行尾加 `@{login}`
> - 无 assignee → 不显示，但在 milestone 级别汇总 "🙋 {N} 个 issue 无 assignee"

> **[强制规则] 空 milestone 处理：**
> - 如果 milestone 下没有 issue → 仍然显示 milestone 标题和描述，注明 "暂无关联 issue"

> **[强制规则] Backlog 截断：**
> - 最多显示 20 条，超出写汇总行 "还有 {N} 个未关联 issue 未列出"

## Step 6 — Update mode specifics

When updating an existing roadmap:

1. **Preserve manual sections**: any content between `<!-- manual -->` and `<!-- /manual -->` is kept as-is
2. **Merge strategy**:
   - New milestones → insert into correct phase
   - Closed milestones → move to "已完成" section
   - Issue state changes → update checkbox `[x]` / `[ ]`
   - New issues in existing milestones → append
   - Removed issues (closed + removed from milestone) → remove from list
3. **Update header timestamp**: always refresh "最后更新" date

## Step 7 — Generate Mermaid timeline (optional)

If the repo has 2+ milestones with due dates, append a Mermaid gantt chart:

```markdown
## 📊 时间线视图

```mermaid
gantt
    title 项目路线图
    dateFormat YYYY-MM-DD

    section 当前冲刺
    {MILESTONE_1} :active, m1, {START}, {DUE}

    section 近期计划
    {MILESTONE_2} :m2, {START}, {DUE}

    section 远期规划
    {MILESTONE_3} :m3, {START}, {DUE}
```​
```

Gantt chart rules:
- `start` = milestone creation date or earliest issue creation date
- `end` = milestone `due_on`
- Milestones without `due_on` are excluded from the chart
- Completed milestones use `:done` tag
- Current sprint uses `:active` tag

## Edge cases

- **No milestones**: skip milestone sections, only output Backlog section, suggest user create milestones
- **No issues**: output milestone titles with descriptions only, note "暂无关联 issue"
- **No due dates on any milestone**: skip Mermaid chart, classify all as ⚪ 未排期
- **Mixed: some milestones have dates, some don't**: dated ones go into timeline phases, undated ones go to ⚪ 未排期
- **Very large backlog (100+ unassigned issues)**: cap at 20, show count summary
- **Update mode with no existing roadmap**: fall back to Generate mode silently
- **No GitHub auth**: surface error clearly, tell user to run `gh auth login`
