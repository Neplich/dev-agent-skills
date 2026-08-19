---
feature: release-changelog
version: 0.6.3
date: 2026-08-19
last_updated: 2026-08-19
---

# Changelog - v0.6.3

## [v0.6.3] - 2026-08-19

本版本新增 human-writing Skill 并接入文档生成流程，同时修正 docs-site-bootstrap 的文档站页面骨架。本版本覆盖 v0.6.2 之后合并到 `main` 的 2 个 PR。

### Added

- **skills:** 新增 human-writing 并接入文档生成流程 ([#310](https://github.com/Neplich/dev-agent-skills/pull/310))。新增独立的 `human-writing` Skill，为面向真实读者的文档提供读者视角、信息顺序和自然表达规则；注册到 PM 插件和发现入口，并适配 6 个下游 Router 与 32 个文档类 Specialist，Router 路由和直接调用均可按需共同加载；主 Skill 保留对事实、结构、路径、门禁和验证的所有权，纯代码、配置、Schema、锁文件和数据输出不触发。

### Fixed

- **docs-site-bootstrap:** 对齐 Kimi 文档站页面骨架 ([#309](https://github.com/Neplich/dev-agent-skills/pull/309))。移除会让顶部栏覆盖侧栏滚动区域的自定义桌面栏位，恢复 VitePress 默认骨架关系；保留现有蓝色主题色和 Mermaid 样式，无右侧目录页面限制正文最大宽度为 688px 并保留 256px 空目录列；增补主题契约测试。

## 发布说明

- 发版清单：`.claude-plugin/marketplace.json` 的 `metadata.version` 更新为 `0.6.3`；7 个 `agents/*/.claude-plugin/plugin.json` 与 `.kimi-plugin/plugin.json` 的 `version` 同步为 `0.6.3`（由 `check_repository_contract.py` 强制校验）。
- 行为变更：docs-site-bootstrap 的 custom.css 骨架关系有变化，现有宿主不会被静默覆盖，需要重新执行 docs-site-bootstrap 并按冲突门禁明确合并 custom.css。
