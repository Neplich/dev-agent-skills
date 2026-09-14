---
feature: release-changelog
version: 0.6.7
date: 2026-09-14
last_updated: 2026-09-14
---

# Changelog - v0.6.7

2026-09-14 发布版本的历史记录。

本版将仓库重构为按需专业知识库：移除 PM 准入、固定 PRD/TRD/计划链、角色隔离和逐阶段审批，助手从用户请求、issue、代码、测试和已有资料建立工作依据，Skill 入口由 8,865 行收敛至 1,049 行。Designer 插件及 UIUX 能力移除后，库内保留六个插件、37 个 Skill。同期恢复各级 README 的完整说明，许可证切换为标准 MIT，并修复治理台账与实际分支保护配置的不一致。

## 适用模型范围

随着 GPT-6-Astra、Fable-5.1 等模型的发布，本仓库的 skill 流程对这类模型已过于冗杂，反而限制了它们的能力释放。本仓库推荐的适用范围是 gpt-5.6-sol、opus-4.8 及以下模型，配合 harness 使用。

关联变更：[PR #337](https://github.com/Neplich/dev-agent-skills/pull/337)、[PR #338](https://github.com/Neplich/dev-agent-skills/pull/338)、[PR #339](https://github.com/Neplich/dev-agent-skills/pull/339)、[PR #340](https://github.com/Neplich/dev-agent-skills/pull/340)。

[对应版本源码](https://github.com/Neplich/dev-agent-skills/tree/v0.6.7) · [版本索引](../../CHANGELOG.md)
