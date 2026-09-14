---
name: roadmap-gen
description: "根据 GitHub 里程碑、issue、PR 与发布证据生成或更新路线图，说明计划阶段、依赖和真实进度。"
---

# 路线图

读取现有路线图与用户计划，再获取实际 GitHub milestone、issue 和发布状态。支持带采集时间和完整性说明的导出。现有人工注释与已确认计划保留。

```bash
gh repo view --json nameWithOwner,url,description
gh api repos/{OWNER}/{REPO}/milestones --paginate -X GET -f state=all
gh issue list --state all --limit 1000 --json number,title,state,labels,assignees,milestone
```

用截止日期、里程碑语义、依赖、版本范围和用户意图确定当前、近期、远期与 backlog。日期缺失时使用语义阶段并说明推断依据；关键排期歧义向用户询问。阻塞依据来自明确标签、依赖或 issue 内容。

每项保留标题、状态、标签、负责人和来源链接。进度按实际开放与关闭数量计算，未分配项标明 unassigned。数据截断或不完整时说明统计范围，方法见 [github-reader](../github-reader/SKILL.md)。

按用户需要写入 `docs/roadmap.md` 或宿主既有位置。用里程碑表格组织目标、范围、进度、依赖和时间；时间线有助阅读时使用 Mermaid，日期以真实计划为准。正文维护当前计划，历史由 Git 承载。
