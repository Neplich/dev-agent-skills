# Conventional Commit 前缀参考

展示变更说明时去掉 `type:`、`type(scope):`、`type!:` 或 `type(scope)!:` 前缀，scope 有定位价值时保留为上下文。按实际语义选择类别。

| 前缀 | 常见分类 |
| --- | --- |
| feat | Added |
| fix | Fixed |
| perf / refactor | Changed |
| deprecate | Deprecated |
| remove / revert | Removed |
| security | Security |
| docs / test / ci / build / style / chore | 阅读正文和影响，选择适当类别 |

破坏性变化由 `!` 或 `BREAKING CHANGE` 提示，结合实际影响判断；现有行为的破坏性重设计通常属于 Changed。保留升级动作和兼容性说明。

安装、公开能力、验证与发布方式变化值得记录。例行依赖、格式、缓存和内部维护可以合并概述。bot 身份通过真实作者及 `[bot]` 后缀识别，实际用户影响仍按内容判断。

标题缺少前缀时根据其行为与 PR 内容分类。示例：`feat(auth): add OAuth2 login` 可写为 `**auth:** Add OAuth2 login`，`fix: resolve empty-list crash` 可写为 `Resolve empty-list crash`。
