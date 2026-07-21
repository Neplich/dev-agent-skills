# PM Handoff Packet

pm-agent 已完成入口分类，并将 Python 依赖漏洞审计路由至 dependency-risk-auditor。

```yaml
request_type: security
change_tier: standard
feature_path: dependency-inventory
feature: dependency-inventory
parent_feature: N/A
feature_level: 1
feature_path_evidence:
  - source: docs/pm/dependency-inventory/PRD.md
    reason: 该 PRD 已确认 Python 服务依赖清单与上线前漏洞审计范围。
source_documents:
  - docs/pm/dependency-inventory/PRD.md
  - requirements.txt
scope_decision:
  summary: 审查 Python 服务固定依赖版本中的公开漏洞与过期风险，输出升级或缓解建议。
  expectation_changed: false
  non_goals:
    - 自动修改 requirements.txt
    - 改变模板或 HTTP 功能
downstream_owner: Security
required_output: 按 feature 归档到 docs/security/dependency-inventory/ 的结构化依赖风险审计，包含包版本证据、严重度和升级或缓解建议，不直接修改依赖。
risk_surface:
  - Python HTTP 客户端
  - TLS 与连接处理
  - 服务端模板渲染
assets:
  - 应用运行时
  - 用户请求与响应内容
permissions:
  - application-runtime
data_categories:
  - 应用依赖元数据
remediation_expectations:
  - Python 依赖升级项交回 engineer-agent
  - 发布阻断与临时缓解项交回 devops-agent
blockers_risks:
  - 固定的老版本依赖可能包含公开漏洞
```
