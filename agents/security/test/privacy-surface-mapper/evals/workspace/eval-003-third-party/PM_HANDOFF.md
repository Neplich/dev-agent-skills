# PM Handoff Packet

pm-agent 已完成入口分类，并将第三方数据共享识别路由至 privacy-surface-mapper。

```yaml
request_type: security
change_tier: standard
feature_path: third-party-sharing
feature: third-party-sharing
parent_feature: N/A
feature_level: 1
feature_path_evidence:
  - source: docs/pm/third-party-sharing/PRD.md
    reason: 该 PRD 已确认分析、广告和支付供应商的数据共享审查范围。
source_documents:
  - docs/pm/third-party-sharing/PRD.md
  - src/integrations/user-events.js
  - config/vendors.json
scope_decision:
  summary: 识别所有接收用户数据的第三方服务，梳理字段、目的、同意、地域和保留缺口。
  expectation_changed: false
  non_goals:
    - 评价供应商商业条款
    - 直接移除集成
downstream_owner: Security
required_output: 按 feature 归档到 docs/security/third-party-sharing/ 的结构化隐私处理面报告，包含第三方、字段、目的、传输、保留、用户权利及整改建议，不直接实现修复。
risk_surface:
  - 产品分析事件
  - 广告受众同步
  - 支付客户资料
assets:
  - 用户标识与电子邮箱
  - IP 地址与页面行为
  - 订单金额与支付客户标识
permissions:
  - member
  - application-runtime
data_categories:
  - 账号标识
  - 联系信息
  - 在线标识与行为数据
  - 交易元数据
remediation_expectations:
  - 同意、字段最小化与用户选择实现交回 engineer-agent
  - 供应商配置与数据删除作业交回 devops-agent
blockers_risks:
  - 广告共享默认开启且包含电子邮箱
  - 供应商保留期限与删除支持未完整记录
```
