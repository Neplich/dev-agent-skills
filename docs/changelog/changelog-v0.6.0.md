---
feature: release-changelog
version: 0.6.0
date: 2026-08-18
last_updated: 2026-08-18
---

# Changelog - v0.6.0

## [v0.6.0] - 2026-08-18

本版本移除整套 skill eval 机制，Skill 迭代依据转向用户体验；安装策略统一为全量安装，不再提供 routers-only 选项。本版本覆盖 v0.5.1 之后合并到 `main` 的 7 个 PR 与 2 个直接提交。

### Removed

- 移除整套 skill eval 机制，迭代依据转向用户体验 ([#301](https://github.com/Neplich/dev-agent-skills/pull/301))。eval 脚本、fixture、durable `comparison.md` 与相关 CI 检查一并删除；本窗口内的 eval 校准与修复（[#296](https://github.com/Neplich/dev-agent-skills/pull/296)、[#297](https://github.com/Neplich/dev-agent-skills/pull/297)、[#298](https://github.com/Neplich/dev-agent-skills/pull/298)）随机制移除不再单独列出。

### Changed

- 移除 routers-only 安装策略，统一全量安装 ([#293](https://github.com/Neplich/dev-agent-skills/pull/293))
- 精简 Skill 描述（直接提交，无关联 PR）
- 收敛文档权威与共享契约（直接提交，无关联 PR）
- 修正安装文档中不存在的版本示例与过期发布表述 ([#294](https://github.com/Neplich/dev-agent-skills/pull/294))
- 补全 release cookbook 的版本同步面 ([#295](https://github.com/Neplich/dev-agent-skills/pull/295))

## 发布说明

- 发版清单：`.claude-plugin/marketplace.json` 的 `metadata.version` 更新为 `0.6.0`；7 个 `agents/*/.claude-plugin/plugin.json` 与 `.kimi-plugin/plugin.json` 的 `version` 同步为 `0.6.0`（由 `check_repository_contract.py` 强制校验）。
- ⚠️ 行为变更：skill eval 机制整体移除，依赖 eval runner、`evals.json` 或 durable `comparison.md` 的本地工作流不再可用；routers-only 安装方式取消，安装即全量。
