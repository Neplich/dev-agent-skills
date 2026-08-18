---
feature: release-changelog
version: 0.6.1
date: 2026-08-18
last_updated: 2026-08-18
---

# Changelog - v0.6.1

## [v0.6.1] - 2026-08-18

本版本统一 docs-agent 文档站的导航与页面骨架。本版本覆盖 v0.6.0 之后合并到 `main` 的 1 个 PR。

### Fixed

- **docs-site-bootstrap:** 统一站点导航与页面骨架 ([#305](https://github.com/Neplich/dev-agent-skills/pull/305))。public docs 与 docs-internal 各自定义独立入口顺序，根首页与顶部导航消费同一份目标配置；固定根首页、分区首页与具体文档页的页面骨架，按页面类型控制左侧栏与右侧文档目录；修正顶部栏与左侧栏层级，宽屏文档骨架限制为 1440px 居中布局。

## 发布说明

- 发版清单：`.claude-plugin/marketplace.json` 的 `metadata.version` 更新为 `0.6.1`；7 个 `agents/*/.claude-plugin/plugin.json` 与 `.kimi-plugin/plugin.json` 的 `version` 同步为 `0.6.1`（由 `check_repository_contract.py` 强制校验）。
- 行为变更：docs-site-bootstrap 生成的文档站导航顺序与页面骨架（左侧栏、右侧目录、宽屏布局）有可见变化，重新运行脚手架或升级站点时以新骨架为准。
