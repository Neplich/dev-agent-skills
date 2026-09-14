---
title: Release Notes 编写规范
visibility: internal
doc_type: release
stage: dev
owners:
  - docs
related_code:
  - docs/site/release-notes
last_verified_version: unverified
---

# Release Notes 编写规范

发布说明面向使用者和维护者，解释本次变化、升级动作与实际影响。语言与产品术语一致，事实来自本次版本范围、代码、测试、迁移、配置和资产证据。

按实际内容选择重点更新、其他改进、升级说明和变更明细。相关提交可以合并为主题，保留追溯链接。说明关键实现、接口、数据库与部署变化，并在涉及兼容性时给出操作顺序、适用条件和恢复方式。

版本页采用 `vX.Y.Z.md`，使用文档站七字段 frontmatter，`doc_type: release`、`stage: release`。经过核对的版本可写入 `last_verified_version`，其余使用 `unverified`。

同步版本页面、索引和 `.meta/releases.json`，保留既有版本与有效扩展字段。发布资产的名称、路径、摘要和可用状态来自实际输出。执行宿主文档检查，交付当前事实与验证结果。
