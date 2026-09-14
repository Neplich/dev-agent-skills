# 文档同步方法

先定位要更新的事实，再组织读者需要的页面。既有文档使用稳定路径，结构调整在授权范围内连同链接与导航一起完成。

1. 阅读目标页面、相关实现、测试与配置。文档站存在 standards 与 change-map 时用它们定位模板和影响面。
2. 按类型读取必要资料：[产品](types/product/INSTRUCTIONS.md)、[设计](types/design/INSTRUCTIONS.md)、[API](types/api/INSTRUCTIONS.md)、[数据库](types/database/INSTRUCTIONS.md)、[运维](types/ops/INSTRUCTIONS.md)。
3. 把当前事实组织成清晰正文。一个事实选择一个主要维护位置，其他页面通过链接引用。
4. 更新正文、必要索引、导航和受影响 change-map 条目。移动页面时同步引用，保持读者从入口逐级到达目标内容。
5. 回读修改，核对来源与字段，执行宿主文档检查。适用时构建并查看 public/internal 页面及图片。

## 站点约定

使用 [页面字段](../../docs-agent/_internal/_shared/frontmatter-contract.md)。新页面可以从宿主模板唯一的 `docs-scaffold` 块生成，宿主提供 `npm run new:doc` 时可直接使用。

`change-map.yaml` 的 `code_glob` 与 `required_docs` 对应真实变化。每条映射应覆盖受该代码影响的事实页面及必要索引和交叉引用，保留其他条目与有效扩展字段。映射是检索和检查数据，按实际依赖维护。

根据 `docs/site/package.json` 和 CI 执行检查。内置站点支持 `npm run test:docs`、`npm run build:public` 与 `npm run build:internal`；依赖按宿主 lockfile 安装。仅检查版本 metadata 时可以使用 `npm run check:version -- --version vX.Y.Z`。

完成后提供更新入口、验证结果和影响使用的证据缺口。
