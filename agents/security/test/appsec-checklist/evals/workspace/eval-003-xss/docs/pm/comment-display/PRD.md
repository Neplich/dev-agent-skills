---
feature: comment-display
feature_path: comment-display
parent_feature: N/A
feature_level: 1
version: 1.0.0
date: 2026-07-21
last_updated: 2026-07-21
---

# 评论展示

## 当前状态

评论页面从 API 获取用户提交的评论正文，并在评论列表中展示作者名和正文。评论正文按纯文本处理，不支持用户提供 HTML。

## 已确认范围

- 审查评论正文从 API 响应进入浏览器 DOM 的渲染路径。
- 确认用户生成内容不能执行脚本、事件处理器或任意 HTML。
- 安全报告需要包含代码位置、影响、严重度依据与可执行修复建议。

## 非目标

- 引入富文本或 Markdown 渲染。
- 修改评论排序、分页或审核流程。

## 验收期望

- 评论作者名和正文均必须作为文本渲染。
- 含 HTML 标签或事件属性的评论不得改变 DOM 结构或执行脚本。
