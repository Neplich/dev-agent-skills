# PM Handoff Packet

pm-agent 已完成入口分类，并将个人数据访问、删除与导出实现审查路由至 privacy-surface-mapper。

```yaml
request_type: security
change_tier: standard
feature_path: user-rights
feature: user-rights
parent_feature: N/A
feature_level: 1
feature_path_evidence:
  - source: docs/pm/user-rights/PRD.md
    reason: 该 PRD 已确认用户数据访问、删除和导出的产品范围与验收期望。
source_documents:
  - docs/pm/user-rights/PRD.md
  - src/api/user-rights.js
scope_decision:
  summary: 核对用户权利端点是否完整覆盖个人数据，且具备身份校验、删除传播与安全导出。
  expectation_changed: false
  non_goals:
    - 直接实现缺失端点
    - 修改账号认证方案
downstream_owner: Security
required_output: 按 feature 归档到 docs/security/user-rights/ 的结构化隐私处理面报告，包含数据范围、访问、删除、导出缺口及整改建议，不直接实现修复。
risk_surface:
  - 数据访问接口
  - 数据导出接口
  - 账号删除与第三方传播
assets:
  - 用户资料
  - 订单记录
  - 分析事件
permissions:
  - member
  - support-admin
data_categories:
  - 账号资料
  - 订单与交易元数据
  - 产品行为事件
remediation_expectations:
  - 用户权利端点与身份校验修复交回 engineer-agent
  - 删除任务与保留策略交回 devops-agent
blockers_risks:
  - 当前导出接口信任请求参数中的 userId
  - 当前删除仅做账号软删除且未传播到分析系统
```
