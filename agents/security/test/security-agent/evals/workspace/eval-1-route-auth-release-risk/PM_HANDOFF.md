# PM Handoff Packet

pm-agent 已完成入口分类，并将本次上线前安全审查路由至 security-agent。

```yaml
request_type: security
change_tier: standard
feature_path: auth-model
feature: auth-model
parent_feature: N/A
feature_level: 1
feature_path_evidence:
  - source: docs/pm/auth-model/PRD.md
    reason: 该 PRD 覆盖登录、权限模型与上线前安全审查范围，可作为本次 auth-model 安全路由的正式产品依据。
source_documents:
  - docs/pm/auth-model/PRD.md
  - docs/security/auth-model.md
scope_decision:
  summary: 登录与权限模型重构准备上线，重点确认 admin 越权风险，并附带排查依赖漏洞。
  expectation_changed: false
  non_goals:
    - SSO 接入
    - 密码策略调整
downstream_owner: Security
required_output: 按 feature 归档到 docs/security/auth-model/ 的结构化安全 review 报告，包含风险矩阵、证据、影响和修复建议，不直接输出实现补丁。
risk_surface:
  - 登录会话
  - 角色权限矩阵
  - 敏感路由鉴权
  - 依赖供应链
assets:
  - 用户会话与身份信息
  - 角色及权限配置
  - 审计日志
  - 平台配置
permissions:
  - guest
  - member
  - admin
  - platform-ops
data_categories:
  - 身份认证数据
  - 会话数据
  - 权限与角色数据
  - 审计日志
  - 平台配置数据
remediation_expectations:
  - 应用代码与鉴权逻辑修复项交回 engineer-agent
  - 依赖、构建或部署配置修复项交回 devops-agent
blockers_risks:
  - admin 越权是本次上线前审查的主要风险
  - 依赖 CVE 状态待扫描确认
```
