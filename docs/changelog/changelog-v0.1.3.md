# Changelog - v0.1.3

## [v0.1.3] - 2026-06-09

### Added

- 增加 `release-notes-generator` 的 release 大纲 reference，沉淀正式 release notes 的标题、重点更新、其他改进、升级说明、变更明细和完整变更顺序。([#27](https://github.com/Neplich/dev-agent-skills/pull/27))
- 增加 GitHub draft release 工作流 reference，覆盖 changelog preflight、tag 重打、发布复核和 compare link 规则。([#27](https://github.com/Neplich/dev-agent-skills/pull/27))

### Changed

- 调整 `release-notes-generator` 的 `SKILL.md` 为轻量入口，将详细发布规范拆分到 reference 文档，降低主 skill 入口复杂度。([#27](https://github.com/Neplich/dev-agent-skills/pull/27))
- 更新 release notes source audit 断言与 eval metadata，让发布源范围、tag 模板和 durable comparison 结果保持一致。([#27](https://github.com/Neplich/dev-agent-skills/pull/27))

### Fixed

- 修正 release notes tag 范围模板，区分 `{THIS_TAG}` 与 `{VERSION}`，避免 tag、release 和 compare 场景出现 `v` 前缀重复。([#27](https://github.com/Neplich/dev-agent-skills/pull/27))

### Test

- 完成 `release-notes-generator` 三个 eval fixture 的 fresh Codex subagent validation，并更新 durable `comparison.md`。([#27](https://github.com/Neplich/dev-agent-skills/pull/27))
