---
description: "Eval-3: golang/go — 所有 milestone 无截止日期，验证语义推断"
expected_assertions:
  - "go1.26.2/go1.25.9 → 🔧 当前补丁"
  - "go1.27 → 🚀 下一版本"
  - "go1.28 → 🔵 远期规划"
  - "gopls/v0.23.0 → 🛠️ 工具生态"
  - "Backlog/Unplanned/Proposal → ⚪ 未排期"
  - "release-blocker issue 置顶为 🚨 发布阻塞项"
  - "无 Mermaid gantt 图（无日期数据）"
  - "Issue 状态 [x]/[ ] 正确"
  - "Backlog 截断 ≤20 条"
repo: golang/go
mode: generate
iteration: 2
---

# Eval-3: No Due Dates — Semantic Inference (golang/go)

## Prompt

请为 golang/go 生成项目路线图，写入 docs/roadmap.md。

## Iteration-1 Assertions（原版）

1. 所有 open milestone 归入 ⚪ 未排期（无一例外）
2. 不生成 Mermaid gantt 图（无日期数据支撑）
3. closed milestone 最近 5 个放入 ✅ 已完成
4. 不出现 🔴 当前冲刺 / 🟡 近期计划 / 🔵 远期规划 阶段
5. Issue 带正确的 [x]/[ ] 状态
6. Backlog 最多 20 条 + 汇总行

## Iteration-2 Assertions（语义推断版）

1. go1.26.2、go1.25.9 → 🔧 当前补丁（patch 版本命名）
2. go1.27 → 🚀 下一版本（下一主/次版本）
3. go1.28 → 🔵 远期规划（超前版本）
4. gopls/v0.23.0、gopls/v0.22.0 → 🛠️ 工具生态（子项目前缀）
5. Backlog、Unplanned、Proposal → ⚪ 未排期（关键词匹配）
6. go1.27 内 release-blocker issue → 🚨 发布阻塞项置顶
7. 无 Mermaid 图（仍无日期数据）
8. Backlog 最多 20 条 + 汇总行
