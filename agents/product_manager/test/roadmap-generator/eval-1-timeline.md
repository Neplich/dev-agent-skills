---
description: "Eval-1: flutter/flutter — 多个有截止日期的 milestone，验证 Gantt 图和时间线分类"
expected_assertions:
  - "🔴/🟡/🔵 阶段分类正确（Q2=当前冲刺或近期，Q3/Q4=远期）"
  - "进度条格式正确（█░ 16字符宽）"
  - "Mermaid gantt 图包含有日期的 milestone"
  - "无日期 milestone 归入 ⚪ 未排期"
  - "Issue 带 [x]/[ ] 状态和 GitHub 链接"
  - "Backlog 截断 ≤20 条"
repo: flutter/flutter
mode: generate
---

# Eval-1: Timeline & Gantt (flutter/flutter)

## Prompt

请为 flutter/flutter 生成一份完整的项目路线图，写入 docs/roadmap.md。

## Assertions

1. 有截止日期的 milestone（Q2/Q3/Q4 2026）按时间分入正确阶段
2. 无截止日期的 milestone（Impeller on Android 等）归入 ⚪ 未排期
3. 进度条使用 █░ 格式，16 字符宽
4. 底部有 Mermaid gantt 图，包含有日期的 milestone
5. 已关闭 milestone 归入 ✅ 已完成
6. 每个 issue 带 `[#{N} 标题](URL)` 格式链接
7. Backlog 最多 20 条

## Iteration-1 Results ✅ PASS

| # | Assertion | 结果 |
|---|-----------|------|
| 1 | Q2→🔴当前冲刺, Q3/Q4→🔵远期规划 | ✅ |
| 2 | Impeller/Infra/GPU → ⚪ 未排期 | ✅ |
| 3 | 进度条 16 字符 █░ | ✅ |
| 4 | Mermaid gantt 包含 Q2/Q3/Q4 | ✅ |
| 5 | 已关闭 milestone → ✅ 已完成 | ✅ |
| 6 | issue 链接格式正确 | ✅ |
| 7 | Backlog 截断 20 条 + 汇总行 | ✅ |
