# PM Handoff Packet

pm-agent 已完成入口分类，并将依赖漏洞审计路由至 dependency-risk-auditor。

```yaml
request_type: security
change_tier: standard
feature_path: dependency-inventory
feature: dependency-inventory
parent_feature: N/A
feature_level: 1
feature_path_evidence:
  - source: docs/pm/dependency-inventory/PRD.md
    reason: 该 PRD 已确认 Node.js 运行时依赖清单与上线前漏洞审计范围。
source_documents:
  - docs/pm/dependency-inventory/PRD.md
  - package.json
scope_decision:
  summary: 审查已固定版本的 Node.js 生产依赖，识别已知漏洞并给出升级或缓解建议。
  expectation_changed: false
  non_goals:
    - 修改应用功能
    - 自动升级依赖
downstream_owner: Security
required_output: 按 feature 归档到 docs/security/dependency-inventory/ 的结构化依赖风险审计，包含清单、证据、严重度和升级或缓解建议，不直接修改依赖。
risk_surface:
  - Node.js 生产依赖
  - 传递依赖
  - 已知漏洞暴露
assets:
  - 应用运行时
  - 用户输入处理链路
permissions:
  - application-runtime
data_categories:
  - 应用依赖元数据
remediation_expectations:
  - 依赖版本升级项交回 engineer-agent
  - 构建与发布缓解项交回 devops-agent
blockers_risks:
  - 老版本生产依赖可能包含公开漏洞
```
