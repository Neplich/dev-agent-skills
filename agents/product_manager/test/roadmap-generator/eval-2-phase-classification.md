---
description: "Eval-2: microsoft/vscode — 大量 open+closed milestone 混合，验证阶段分类和已完成区域"
expected_assertions:
  - "5 个 open milestone 正确分类"
  - "closed milestone 取最近 5 个放入 ✅ 已完成"
  - "Backlog milestone（5000+ issues）不逐条列出，有截断"
  - "Issue 按标签分组（✨/🐛/🔧）"
  - "Assignee 正确显示"
  - "更新时间戳正确"
repo: microsoft/vscode
mode: generate
---

# Eval-2: Phase Classification (microsoft/vscode)

## Prompt

请为 microsoft/vscode 生成项目路线图，写入 docs/roadmap.md。

## Assertions

1. open milestone 按有无截止日期分入对应阶段
2. "Backlog" milestone（5000+ issues）不逐条列出，应有截断或概要
3. closed milestone 最近 5 个放入 ✅ 已完成
4. Issue 按 label 分组到 ✨/🐛/🔧 类别
5. 有 assignee 的 issue 行尾显示 @login
6. 文件头 "最后更新" 日期正确
