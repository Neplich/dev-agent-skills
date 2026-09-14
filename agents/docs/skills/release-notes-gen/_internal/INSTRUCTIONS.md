# 发布说明编写方法

读取宿主发布说明规范和相邻版本的格式，再核对本次目标版本与实际变更范围。证据可来自用户明确范围、标签可达提交、PR、代码、测试、迁移、部署配置和资产清单。

按读者任务组织用户可见变化、关键技术变化、数据与配置迁移、交付资产、升级步骤、兼容性和已知限制。每项重要声明有可追溯来源。正文表达已交付的当前结果。

站内版本页通常采用 `docs/site/release-notes/vX.Y.Z.md`。使用宿主既有结构；需要初始化站点时可结合 docs-site-bootstrap。页面使用 [字段契约](../../docs-agent/_internal/_shared/frontmatter-contract.md)，`doc_type: release`、`stage: release`，`related_code` 覆盖版本证据，核对过的版本可作为 `last_verified_version`。

同步版本页、索引、宿主 metadata 和必要导航。内置 `.meta/releases.json` 的 `released` 保持唯一版本列表，`latest` 对应最后一项，`verifiedDocs` 引用已列入列表的版本。保留其他版本和有效扩展字段。

依宿主 lockfile 安装依赖，执行既有 docs checks，回读页面和关联版本信息。发布操作使用用户已有授权；交付说明中区分已写文档、草稿状态与真实发布结果。
