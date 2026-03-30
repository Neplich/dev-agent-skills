# PM Agent Dispatcher Instructions

## Overview

This skill acts as an intelligent entry point for PM Agent. It analyzes user intent and automatically selects and executes the appropriate PM skills.

## Available Skills

- `idea-to-spec` - Generate PRD, BRD, TRD, ADR from ideas
- `competitive-brief` - Competitive analysis and positioning
- `competitive-intelligence` - Sales-focused battlecard
- `changelog-generator` - Generate changelog from GitHub
- `release-notes-generator` - Generate user-facing release notes
- `roadmap-generator` - Generate roadmap from GitHub milestones
- `github-reader` - Read GitHub project status

## Execution Steps

### Step 1: Analyze User Intent

Parse the user's request to identify:
- Primary goal (new product, analysis, documentation, status check)
- Specific artifacts needed (PRD, roadmap, changelog, etc.)
- Context (existing project vs new idea)

### Step 2: Determine Skill Selection

**Intent Mapping:**

| User Intent | Skills to Execute |
|-------------|------------------|
| "新产品/新功能想法" | idea-to-spec |
| "竞品分析" | competitive-brief |
| "销售 battlecard" | competitive-intelligence |
| "生成 changelog" | changelog-generator |
| "发版说明" | release-notes-generator |
| "路线图规划" | roadmap-generator |
| "项目状态" | github-reader |
| "完整产品规划" | idea-to-spec → competitive-brief → roadmap-generator |

### Step 3: Execute Skills

**Single Skill Execution:**
If only one skill is needed, invoke it directly using the Skill tool.

**Multiple Skills Execution:**
If multiple skills are needed, execute them in sequence:
1. Invoke first skill
2. Wait for completion
3. Invoke next skill with context from previous results
4. Continue until all skills complete

### Step 4: Present Results

Summarize what was done and where outputs are located:
- List all skills executed
- Show output file paths
- Provide brief summary of key findings

## Examples

**Example 1: New Product Idea**
```
User: "我想做一个任务管理应用"
→ Execute: idea-to-spec
→ Output: docs/pm/{feature-name}/PRD.md, BRD.md, TRD.md
```

**Example 2: Competitive Analysis**
```
User: "分析竞品 Asana 和 Trello"
→ Execute: competitive-brief
→ Output: docs/pm/{feature-name}/competitive-brief.md
```

**Example 3: Release Documentation**
```
User: "生成 v2.0 的 changelog 和发版说明"
→ Execute: changelog-generator → release-notes-generator
→ Output: docs/pm/changelog.md, docs/pm/release-notes-v2.0.md
```

**Example 4: Full Product Planning**
```
User: "完整的产品规划流程"
→ Execute: idea-to-spec → competitive-brief → roadmap-generator
→ Output: Complete PM documentation set
```

## Notes

- Always confirm with user if intent is ambiguous
- Provide clear feedback on which skills are being executed
- If a skill fails, explain the error and suggest next steps
- Skills can be re-executed if user requests modifications
