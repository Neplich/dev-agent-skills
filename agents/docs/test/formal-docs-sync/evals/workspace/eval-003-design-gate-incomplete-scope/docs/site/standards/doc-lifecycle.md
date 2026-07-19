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

# 文档生命周期

正式文档围绕三个通用节点维护，始终写成最新状态，不追加变更流水账。

```mermaid
flowchart LR
  A[功能落地] --> B[部署验证]
  B --> C[发版审计]
  C --> A
```

## 功能落地

根据已确认范围和实际代码、测试更新受影响页面与 change map。新增或改动
页面使用 `last_verified_version: unverified`。

## 部署验证

根据真实部署配置、验证命令和环境差异维护运维事实；无法复现的步骤必须
明确标记为待核对，不能猜测。

## 发版审计

对受影响页面逐项核对声明与证据。只有全部通过审计，才可统一写入真实
版本锚；无版本体系时记录版本锚不可用。
