---
name: weekly-report-gen
description: Generate a weekly progress report from git logs, task lists, or user notes. Use when users say "write weekly report", "周报", "weekly summary", "progress report", "status update", or need to summarize work accomplished, blockers, and next-week plans.
---

# Weekly Report Generator

Generate a structured weekly progress report from various inputs.

## When to use

- End of week and need to write a status report
- Summarizing work from git history and task trackers
- Creating a team-facing progress update
- **Lightweight** utility skill — no schema reference needed

## Inputs

- **Required** (at least one):
  - `git_log`: Git commit history (or path to repo for auto-extraction)
  - `task_list`: Completed/in-progress tasks
  - `notes`: Free-form bullet points of accomplishments
- **Optional**:
  - `date_range`: Week range (default: last 7 days)
  - `author`: Filter git log by author
  - `format`: standard / brief / detailed (default: standard)
  - `language`: en / zh (default: zh)

## Workflow

1. **Gather data**: Parse provided inputs:
   - If git repo path given → run `git log --oneline --since="7 days ago"` (with optional author filter)
   - Parse task lists and notes

2. **Categorize**: Group work items by:
   - Feature development
   - Bug fixes
   - Documentation
   - Infrastructure / DevOps
   - Meetings / Communication

3. **Generate report**:
   - **本周完成** (This Week's Accomplishments): Categorized list with key highlights
   - **进行中** (In Progress): Items started but not completed
   - **遇到的问题** (Blockers): Issues encountered and current status
   - **下周计划** (Next Week Plan): Planned work items
   - **关键指标** (Key Metrics, optional): PR count, commits, issues closed

4. **Present**: Clean markdown output.

## Output Contract

- **Format**: Markdown (no YAML frontmatter — informal document)
- **Structure**:
  ```markdown
  # 周报 — YYYY.MM.DD ~ YYYY.MM.DD

  ## 本周完成
  ### 功能开发
  - ...
  ### Bug 修复
  - ...

  ## 进行中
  - ...

  ## 遇到的问题
  - ...

  ## 下周计划
  - ...
  ```

## Conventions

This is a **utility skill** (no formal document schema). Follow `agents/product_manager/skills/idea-to-spec/_internal/_shared/gen-conventions.md` for safety boundaries. No YAML frontmatter in output.

## Failure Handling

- No git access → rely on provided notes/task list only
- Empty week → produce minimal report noting "No major deliverables this week"
- Mixed languages in input → output in user's preferred language
- Do not include commit messages containing secrets or credentials
- Sanitize internal project names if report is for external stakeholders

## Examples

### Example 1: From git log + notes

**User**: 帮我写周报，这周主要做了用户认证模块重构，修了 3 个 bug，还做了 code review。

**Expected Output**:

```markdown
# 周报 — 2025.01.13 ~ 2025.01.17

## 本周完成

### 功能开发
- 完成用户认证模块重构
  - 迁移至 OAuth 2.0 标准流程
  - 统一 token 管理机制

### Bug 修复
- 修复 3 个线上 Bug（具体编号待补充）

### 代码评审
- 完成团队 Code Review

## 进行中
- （待补充）

## 遇到的问题
- （无）

## 下周计划
- （待补充）
```
