---
title: "Docs Site Layout — Product Requirements Document"
type: PRD
feature: "docs-site-layout"
feature_path: "agents/docs-agent/docs-site-layout"
parent_feature: "agents/docs-agent"
feature_level: "3"
version: "1.0.0"
status: Approved
author: "Neplich Codex"
date: "2026-08-18"
last_updated: "2026-08-18"
related_issues:
  - "https://github.com/Neplich/dev-agent-skills/issues/303"
  - "https://github.com/Neplich/dev-agent-skills/issues/304"
related_docs:
  - "docs/pm/agents/docs-agent/PRD.md"
  - "docs/engineer/agents/docs-agent/docs-site-layout/TRD.md"
  - "docs/engineer/agents/docs-agent/docs-site-layout/IMPLEMENTATION_PLAN.md"
changelog:
  - version: "1.0.0"
    date: "2026-08-18"
    changes: "固化双站点入口顺序、页面骨架、宽屏居中和导航层级要求"
---

# Docs Site Layout PRD

## 问题

`docs-site-bootstrap` 的顶部导航与根首页内容入口分别维护，当前内部站已经出现
文案漂移，后续也可能只修改其中一处而破坏数量、链接或顺序的一致性。Public
docs 与 docs-internal 的可见分区不同，不能用一套顺序隐式派生另一套站点。

现有骨架同时依赖 VitePress 默认宽屏公式。根首页、分区首页和具体文档页没有
明确的页面分类、列宽和居中关系；左侧栏在部分状态下还可能覆盖顶部栏。结果是
正文起点和元素密度随页面类型及屏幕宽度明显变化，超宽屏会放大无用途留白。

## 产品目标

1. 为 public docs 与 docs-internal 分别定义独立、稳定的入口顺序。
2. 保证每个目标内部顶部导航与根首页入口的 `text`、`link` 和顺序逐项一致。
3. 固定根首页和文档页两类骨架，以及分区首页和具体文档页的目录栏差异。
4. 让顶部栏始终位于桌面左侧栏之上，不被遮挡且保持可点击。
5. 让桌面和超宽屏的文档元素整体居中、总宽受限，并保持相同或相近的排列和密度。

## 范围

- Public 入口固定为：产品、操作手册、发布说明。
- Internal 入口固定为：规范、产品、操作手册、设计、API、数据库、运维、发布说明。
- 根首页 `/` 使用首页骨架，只显示顶部栏和居中限宽的首页内容。
- 所有非根页面使用文档页骨架，包含顶部栏、左侧栏和居中主内容。
- `/product/` 等一级分区首页属于文档页骨架，但隐藏右侧文档目录。
- 具体文档页仅在存在可用 `h2` 或 `h3` 时显示右侧文档目录。
- Public 与 internal 共用页面布局规则，但各自维护入口顺序和可见分区。
- 自动化检查覆盖双站点入口一致性、页面分类和固定布局参数。

## 非目标与职责边界

- 不要求左侧栏分区标题与顶部入口文案相同。
- 不增加新的文档分区、页面正文或可见性类型。
- 不改变 VitePress 顶部栏高度、移动端断点或既有折叠交互。
- 不新增依赖，不修改宿主 CI、其他 Skill、Router、README 或注册信息。
- 不重写 sidebar 生成、Bootstrap 冲突处理、manifest 或 zero-diff 语义。
- 不为现有宿主静默覆盖资产；宿主升级仍遵循 re-bootstrap 冲突门禁。

## 关键产品决策

### 双站点入口

| 目标 | 根首页与顶部导航的固定顺序 |
| --- | --- |
| public | 产品 → 操作手册 → 发布说明 |
| internal | 规范 → 产品 → 操作手册 → 设计 → API → 数据库 → 运维 → 发布说明 |

每套入口独立声明，不从另一套入口过滤或重排。站点内部必须对入口数量及每一项的
文案、链接和顺序做完整比较，任一差异均阻塞测试。

### 页面骨架

| 页面状态 | 顶部栏 | 左侧栏 | 居中主内容 | 右侧文档目录 |
| --- | --- | --- | --- | --- |
| 根首页 `/` | 显示 | 隐藏 | 显示 | 隐藏 |
| 一级分区首页 | 显示 | 显示 | 显示 | 隐藏 |
| 有 `h2/h3` 的具体文档页 | 显示 | 显示 | 显示 | 显示 |
| 无 `h2/h3` 的具体文档页 | 显示 | 显示 | 显示 | 隐藏 |

文档目录继续只收录 `h2`、`h3`。目录隐藏时不得留下空的视觉或交互组件；分区
首页仍保持与具体文档页相同的正文基线和元素密度。

### 居中与层级

桌面布局以固定最大宽度的整体骨架居中。屏幕继续变宽时，只增加骨架两侧空白，
不拉宽正文或改变列间关系。顶部栏覆盖左侧栏的顶部区域，左侧栏不得遮挡顶部栏、
截获顶部栏点击或改变顶部栏高度。

## 验收标准

1. Public 和 internal 的根首页入口分别与各自顶部导航逐项一致。
2. 根首页没有左侧栏或右侧目录；所有非根页面具有左侧栏。
3. 一级分区首页隐藏右侧目录；具体文档页按可用 `h2/h3` 决定是否显示目录。
4. 1280px 和超宽屏下，整体骨架居中且总宽不超过约定值，额外宽度只形成两侧空白。
5. 两种宽度下根首页与文档页保持相近正文起点、可读宽度和元素密度。
6. 桌面顶部栏层级高于左侧栏，导航可点击；sidebar、目录和上一页/下一页可用。
7. 移动端继续使用 VitePress 既有导航、侧栏和目录折叠行为。
8. Node 测试、public/internal build、真实页面检查和仓库契约验证全部通过。

## 依赖与开放问题

实现依赖当前锁定的 VitePress 1.6.4 默认主题类名、变量和 outline 输出结构。
当前无阻塞开放问题；若入口顺序、页面分类、固定列宽或移动端边界变化，必须
先更新本 PRD 与同路径 TRD。
