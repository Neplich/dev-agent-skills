---
feature: user-search
feature_path: user-search
parent_feature: N/A
feature_level: 1
version: 1.0.0
date: 2026-07-21
last_updated: 2026-07-21
---

# 用户搜索

## 当前状态

已登录用户可通过 `GET /api/users/search?name=<keyword>` 按姓名搜索用户目录。服务端读取 `name` 查询参数并访问关系型数据库，返回匹配用户的公开资料。

## 已确认范围

- 审查 HTTP 查询参数到 SQL 查询的完整输入路径。
- 确认搜索不能改变原定查询语义、读取未授权数据或破坏数据库内容。
- 安全报告需要包含代码位置、影响、严重度依据与可执行修复建议。

## 非目标

- 调整用户目录字段。
- 修改搜索排序或分页规则。

## 验收期望

- 用户输入必须作为数据值处理，不能作为 SQL 语法执行。
- 恶意或畸形搜索条件不得造成额外数据读取、数据修改或服务异常。
