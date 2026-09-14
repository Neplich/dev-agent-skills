---
title: 文档生命周期
visibility: internal
doc_type: design
stage: dev
owners:
  - docs
related_code:
  - docs/site
last_verified_version: unverified
---

# 文档维护

正式页面描述当前可验证状态。功能或部署变化时，根据实现、配置、界面和执行结果更新相关内容、链接与 change-map。

经过内容核对且有版本依据的页面记录 `last_verified_version`，其余使用 `unverified`。发布时核对页面、metadata 和实际版本一致性。历史内容由版本控制与发布说明承载。

`npm run test:docs` 验证页面字段、版本数据和脚本行为。需要分析代码变化对文档的影响时，运行 `npm run check:affected -- --base <base-ref>` 获取映射提示。
