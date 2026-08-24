---
feature: release-changelog
version: 0.6.5
date: 2026-08-24
last_updated: 2026-08-24
---

# Changelog - v0.6.5

## [v0.6.5] - 2026-08-24

本版本修复 eval 机制移除后文档中遗留的失效引用，校正实施计划的归档状态，并清理外部项目遗留，覆盖 v0.6.4 之后合并到 `main` 的 1 个 PR。

### Fixed

- 修复失效 eval 引用、计划归档状态与外部项目遗留 ([#324](https://github.com/Neplich/dev-agent-skills/pull/324))。为已交付的实施计划补充六字段 Closeout 对账，写入归档批准信息并移动到各自 `archive/` 路径；清理 61 份活跃文档中指向已删除 eval 文件、脚本、runner、workflow 和持久化证据步骤的引用，保留明确记录既往决策或执行事实的历史叙述；匿名化 `human-writing` 文档中的外部项目名称，补充文档站整站优化 user story，并移除无法追踪的一次性人工验收承诺。

## 发布说明

- 发版清单：`.claude-plugin/marketplace.json` 的 `metadata.version` 更新为 `0.6.5`；7 个 `agents/*/.claude-plugin/plugin.json` 与 `.kimi-plugin/plugin.json` 的 `version` 同步为 `0.6.5`（由 `check_repository_contract.py` 强制校验）。
- 行为变更：无。本版本为纯文档修正，不改变任何 skill 行为或契约。
