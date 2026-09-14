---
name: github-reader
description: "读取 GitHub issue、PR、milestone 与发布状态，提供有来源和完整性说明的项目状态。"
---

# GitHub 状态读取

从当前仓库 remote 或用户指定仓库确定目标，通过 Connector 或已认证 gh 读取所需状态。用户只询问某一集合时聚焦该集合；全局盘点包含 issue、PR、milestone 与近期交付。

```bash
gh repo view --json nameWithOwner,url,defaultBranchRef
gh issue list --state open --limit 1000 --json number,title,state,labels,milestone,assignees,createdAt,updatedAt
gh pr list --state open --limit 1000 --json number,title,state,author,reviewDecision,createdAt,labels,isDraft
gh api repos/{OWNER}/{REPO}/milestones --paginate -X GET -f state=open
```

读取总数时使用 search 的 `total_count`，同时检查 `incomplete_results`。获取数量低于总数时写明“已获取 N/M 条，分类基于已获取部分”。milestone 使用分页。时间范围按当前时间计算并明确起止日期；用户提供导出时保留仓库、采集时间和完整性说明。

```bash
gh api search/issues -X GET -f q='repo:{OWNER}/{REPO} is:issue is:open' --jq '{total_count, incomplete_results}'
gh api search/issues -X GET -f q='repo:{OWNER}/{REPO} is:pr is:open' --jq '{total_count, incomplete_results}'
```

PR 可按 bot、draft、CHANGES_REQUESTED 和待 review 分类，附作者、标签、等待时间和链接。Milestone 完成率为 closed/(open+closed)，过期且有开放事项时标记逾期；缺少截止日时如实说明。issue 可标注未分配及长期未更新状态。

输出围绕需要用户关注的结果，详细列表按规模裁剪并链接原记录。其他任务需要复用数据时，可提供含 repo、fetched_at、总数、milestones、truncated_collections 和 incomplete_totals 的 `github_reader_data`；数据含义与实际查询保持一致。
