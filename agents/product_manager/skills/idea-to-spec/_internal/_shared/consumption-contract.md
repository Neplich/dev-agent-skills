# Docs-Agent 消费契约

## 适用条件

- 仅当宿主存在 `docs/site/standards/change-map.yaml` 时启用本契约。
- 宿主不存在该文件时，静默沿用当前代码探索方式，不追问用户是否需要建站，也不引入额外前置步骤。

## Release Notes 归属

- `docs/site/release-notes/` 下的版本页、正文确认、metadata、索引和站点校验由
  `docs-agent:release-notes-generator` 负责。
- GitHub Release 正文、draft 与发布操作由
  `pm-agent:github-release-generator` 负责；面向用户的版本说明仍由上述 Docs
  specialist 交付。
- 消费 change map 只用于缩小证据读取范围，不改变上述站内与 GitHub Release
  边界。

## 读取协议

1. 从任务输入中识别功能、模块、文件或代码路径等任务落点。
2. 使用 `change-map.yaml` 中的 `code_glob` 和 `exclude` 反查命中项，并取得对应的 `required_docs`。
3. 只读取命中的 `required_docs` 及完成定位所必需的索引，不扩展为无关文档遍历。
4. 对影响范围、现有行为、接口约束或实现决策等关键判断，回到代码或测试证据进行验证。

## 信任模型

- 文档是项目探索地图，用于缩小检索范围和定位相关上下文；代码及测试证据是 ground truth。
- 文档声明与代码或测试事实冲突时，不以文档覆盖事实，也不静默忽略冲突。
- 分歧证据保留文档路径、文档声明、代码事实和影响，供 `docs-audit` 消费。

## 新鲜度

- 比较文档的 `last_verified_version` 与当前版本锚。
- 存在版本差距或两个版本锚不可比时，降低文档信任并扩大代码或测试验证范围，不直接拒绝读取文档。
- `last_verified_version` 为 `unverified` 时按最低信任处理，所有关键判断必须回到代码或测试验证。

## 输出约定

- 仅在发现文档与代码或测试事实存在分歧时结构化报告，报告包含文档路径、文档声明、代码事实和影响。
- 无文档站、无 `change-map.yaml` 命中或命中文档缺失时，不制造额外用户阻塞，继续使用现有代码探索方式完成任务。
