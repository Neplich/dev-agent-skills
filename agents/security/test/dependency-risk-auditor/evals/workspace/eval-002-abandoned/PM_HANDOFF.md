# PM Handoff Packet

pm-agent 已完成入口分类，并将废弃依赖审计路由至 dependency-risk-auditor。

```yaml
request_type: security
change_tier: standard
feature_path: dependency-inventory
feature: dependency-inventory
parent_feature: N/A
feature_level: 1
feature_path_evidence:
  - source: docs/pm/dependency-inventory/PRD.md
    reason: 该 PRD 已确认 Node.js 依赖维护状态与替代方案审计范围。
source_documents:
  - docs/pm/dependency-inventory/PRD.md
  - package.json
scope_decision:
  summary: 识别已废弃或长期未维护的 Node.js 依赖，并制定替换或隔离建议。
  expectation_changed: false
  non_goals:
    - 自动替换依赖
    - 重构网络请求功能
downstream_owner: Security
required_output: 按 feature 归档到 docs/security/dependency-inventory/ 的结构化依赖风险审计，包含维护状态证据、影响和替换建议，不直接修改依赖。
risk_surface:
  - 废弃生产依赖
  - 无维护者安全响应
  - 旧 API 兼容风险
assets:
  - 外部网络请求链路
  - 应用标识符生成逻辑
permissions:
  - application-runtime
data_categories:
  - 应用依赖元数据
remediation_expectations:
  - 依赖替换实现交回 engineer-agent
  - 发布期隔离措施交回 devops-agent
blockers_risks:
  - 废弃依赖不会继续获得安全修复
```
