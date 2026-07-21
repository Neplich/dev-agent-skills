# PM Handoff Packet

pm-agent 已完成入口分类，并将个人数据收集与 GDPR 审查路由至 privacy-surface-mapper。

```yaml
request_type: security
change_tier: standard
feature_path: data-collection
feature: data-collection
parent_feature: N/A
feature_level: 1
feature_path_evidence:
  - source: docs/pm/data-collection/PRD.md
    reason: 该 PRD 已确认注册、日志和分析埋点中的个人数据收集范围。
source_documents:
  - docs/pm/data-collection/PRD.md
  - src/registration.js
  - config/analytics.json
scope_decision:
  summary: 梳理注册与分析链路中的个人数据、处理目的、同意、保留和用户权利缺口。
  expectation_changed: false
  non_goals:
    - 编写法律意见
    - 直接修改注册流程
downstream_owner: Security
required_output: 按 feature 归档到 docs/security/data-collection/ 的结构化隐私处理面报告，包含数据清单、目的、共享、保留、用户权利和改进建议，不直接实现修复。
risk_surface:
  - 注册数据收集
  - 应用日志
  - 分析埋点
assets:
  - 账号身份信息
  - IP 地址与设备信息
  - 行为事件
permissions:
  - guest
  - member
data_categories:
  - 姓名与电子邮箱
  - IP 地址
  - 设备标识
  - 产品行为事件
remediation_expectations:
  - 同意与数据最小化实现交回 engineer-agent
  - 保留与删除运维项交回 devops-agent
blockers_risks:
  - 当前样本未记录分析同意或保留期限
```
