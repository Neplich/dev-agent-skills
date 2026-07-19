---
title: Release Notes 编写规范
visibility: internal
doc_type: design
stage: release
owners:
  - docs-platform
related_code:
  - docs/site/release-notes
last_verified_version: unverified
---

# Release Notes 编写规范

- 页面命名为 `vX.Y.Z.md`，按版本从新到旧登记在 `index.md`。
- frontmatter 必须使用七字段默认契约；版本页固定使用 `doc_type: release`，
  `stage: release`，并在 #117 审计前保持 `last_verified_version: unverified`。
- 正文必须按证据分别说明用户功能、架构、数据库、部署配置、交付资产以及升级、
  兼容性和风险，不得用一段“其他改进”代替这些事实。
- 正文获维护者明确确认前，不得修改 `index.md`、`.meta/releases.json` 或导航。
- 确认后追加版本索引和 metadata；导航由站点脚本生成，不手工编辑 sidebar。
- 在 `docs/site` 执行 `npm run test:docs`，全部成功才可输出 ready handoff。
