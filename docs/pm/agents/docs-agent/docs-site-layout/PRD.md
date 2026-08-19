---
title: "Docs Site Layout — Product Requirements Document"
type: PRD
feature: "docs-site-layout"
feature_path: "agents/docs-agent/docs-site-layout"
parent_feature: "agents/docs-agent"
feature_level: "3"
version: "1.3.0"
status: Approved
author: "Neplich Codex"
date: "2026-08-18"
last_updated: "2026-08-19"
related_issues:
  - "https://github.com/Neplich/dev-agent-skills/issues/303"
  - "https://github.com/Neplich/dev-agent-skills/issues/304"
related_docs:
  - "docs/pm/agents/docs-agent/PRD.md"
  - "docs/engineer/agents/docs-agent/docs-site-layout/TRD.md"
  - "docs/engineer/agents/docs-agent/docs-site-layout/IMPLEMENTATION_PLAN.md"
changelog:
  - version: "1.3.0"
    date: "2026-08-19"
    changes: "无右侧目录页面保留空目录列，使正文视觉中心与 Kimi 一致"
  - version: "1.2.0"
    date: "2026-08-19"
    changes: "将无右侧目录页面的正文阅读列限制为与 Kimi 一致的 688px"
  - version: "1.1.0"
    date: "2026-08-19"
    changes: "采用 Kimi 文档站的 VitePress 默认栏位骨架并保留现有配色"
  - version: "1.0.0"
    date: "2026-08-18"
    changes: "固化双站点入口顺序、页面骨架、宽屏居中和导航层级要求"
---

# Docs Site Layout PRD

## 当前事实

`docs-site-bootstrap` 通过 `custom.css` 覆盖 VitePress 默认桌面布局，固定整体、
左侧栏、正文和目录列宽，并让不透明顶部栏覆盖左侧栏顶部区域。该关系会遮住左侧栏
滚动条顶部。

Kimi 文档站使用 VitePress 默认栏位骨架：顶部栏内容从左侧栏右侧开始，左侧栏滚动
区域保持完整；正文阅读列在桌面端限制为 688px。现有蓝色品牌色和 Mermaid 样式
不依赖自定义栏位尺寸。

## 产品目标

1. 为 public docs 与 docs-internal 分别定义独立、稳定的入口顺序。
2. 保证每个目标内部顶部导航与根首页入口的 `text`、`link` 和顺序逐项一致。
3. 使用 Kimi 文档站采用的 VitePress 默认栏位骨架。
4. 保留现有品牌色、页面分类、目录显隐、Mermaid 和移动端交互。
5. 让桌面左侧栏滚动区域不被顶部栏覆盖，顶部导航保持可点击。
6. 让无右侧目录页面的正文保持最大 688px 阅读列，避免在超宽屏拉伸。
7. 无右侧目录时保留同宽空目录列，使正文不因目录消失而向右偏移。

## 范围

- Public 入口固定为：产品、操作手册、发布说明。
- Internal 入口固定为：规范、产品、操作手册、设计、API、数据库、运维、发布说明。
- 根首页 `/` 使用首页骨架，只显示顶部栏和首页内容。
- 所有非根页面使用 VitePress 默认文档页骨架，包含顶部栏、左侧栏和主内容。
- `/product/` 等一级分区首页属于文档页骨架，但隐藏右侧文档目录。
- 具体文档页仅在存在可用 `h2` 或 `h3` 时显示右侧文档目录。
- Public 与 internal 共用页面布局规则，但各自维护入口顺序和可见分区。
- `custom.css` 保留现有品牌色和 Mermaid 样式；无右侧目录页面限制正文阅读列，并在
  桌面端补一个不显示内容的目录占位列；不覆盖顶部栏、左侧栏或主布局的位置和层级。
- 自动化检查覆盖双站点入口一致性、页面分类、品牌色和默认栏位保护。

## 非目标与职责边界

- 不要求左侧栏分区标题与顶部入口文案相同。
- 不增加新的文档分区、页面正文或可见性类型。
- 不改变品牌色变量、VitePress 版本、顶部栏高度、移动端断点或既有折叠交互。
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

文档目录继续只收录 `h2`、`h3`。目录隐藏时不得留下空的视觉或交互组件。

### 默认栏位与配色

顶部栏、左侧栏和右侧目录使用 VitePress 1.6.4 默认主题的栏位、层级和断点。
顶部栏内容从左侧栏右侧开始，左侧栏滚动条顶部完整可见。桌面端无右侧目录页面的
正文内容容器限制为 688px，并在 1280px 以上保留 256px 空目录占位列，与 Kimi 的
正文和目录列关系一致；移动端仍使用默认流式宽度。
`--vp-c-brand-1` 保持 `#2563eb`，`--vp-c-brand-2` 保持 `#1d4ed8`；Mermaid 样式
保持不变。

## 验收标准

1. Public 和 internal 的根首页入口分别与各自顶部导航逐项一致。
2. 根首页没有左侧栏或右侧目录；所有非根页面具有左侧栏。
3. 一级分区首页隐藏右侧目录；具体文档页按可用 `h2/h3` 决定是否显示目录。
4. 1280px 和 2560px 下使用 VitePress 默认栏位，左侧栏滚动条顶部不被覆盖；无右侧
   目录页面保留 256px 空目录占位列，正文宽度不超过 688px，正文中心与屏幕中心的
   偏差不超过 8px。
5. 两种宽度下顶部导航可点击；sidebar、目录和上一页/下一页可用。
6. 品牌色变量、导航内容和 Mermaid 样式与修改前一致。
7. 移动端继续使用 VitePress 既有导航、侧栏和目录折叠行为。
8. Node 测试、public/internal build、真实页面检查和仓库契约验证全部通过。

## 依赖与开放问题

实现依赖当前锁定的 VitePress 1.6.4 默认主题类名、变量和 outline 输出结构。
当前无阻塞开放问题；若入口顺序、页面分类、默认栏位或移动端边界变化，必须
先更新本 PRD 与同路径 TRD。
