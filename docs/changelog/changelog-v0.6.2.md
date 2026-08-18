---
feature: release-changelog
version: 0.6.2
date: 2026-08-18
last_updated: 2026-08-18
---

# Changelog - v0.6.2

## [v0.6.2] - 2026-08-18

本版本修正 docs-agent manual-gen 的全量手册范围与覆盖门禁。本版本覆盖 v0.6.1 之后合并到 `main` 的 1 个 PR。

### Fixed

- **manual-gen:** 修正全量手册范围与覆盖门禁 ([#307](https://github.com/Neplich/dev-agent-skills/pull/307))。手册覆盖范围与目录处理方式拆分为独立的 `scope_mode` 和 `change_mode`，支持局部补增、完整手册以及完整站点中的手册切片；完整手册增加写前覆盖矩阵、按独立用户任务拆页、全量计划分批执行，以及写后双向覆盖校验和独立复核；修正 Chrome 截图契约，分别记录实际窗口与内容视口，保持截图自然宽高比，不再强制内容视口等于 1920×1080。

## 发布说明

- 发版清单：`.claude-plugin/marketplace.json` 的 `metadata.version` 更新为 `0.6.2`；7 个 `agents/*/.claude-plugin/plugin.json` 与 `.kimi-plugin/plugin.json` 的 `version` 同步为 `0.6.2`（由 `check_repository_contract.py` 强制校验）。
- 行为变更：manual-gen 的入口门禁、执行协议与结果报告字段有变化；宿主 `doc-granularity.md` 的 Manual 页面粒度标准更新，已有宿主需重跑 `docs-site-bootstrap` 或显式合并该标准文件。
