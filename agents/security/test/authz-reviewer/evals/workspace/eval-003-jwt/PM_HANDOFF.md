# PM Handoff Packet

pm-agent 已完成入口分类，并将本次 JWT 认证安全审查路由至 authz-reviewer。

```yaml
request_type: security
change_tier: standard
feature_path: jwt-auth
feature: jwt-auth
parent_feature: N/A
feature_level: 1
feature_path_evidence:
  - source: docs/pm/jwt-auth/PRD.md
    reason: 该已确认 PRD 定义 JWT 身份与角色声明的信任边界和受保护 API 范围，是本次审查的正式产品依据。
source_documents:
  - docs/pm/jwt-auth/PRD.md
  - src/auth/jwt.js
scope_decision:
  summary: 审查 JWT 签发与校验路径，确认签名、算法、有效期和角色声明是否能安全保护用户及管理端 API。
  expectation_changed: false
  non_goals:
    - 更换认证产品形态
    - 实现 JWT 修复
downstream_owner: Security
required_output: 在 docs/security/jwt-auth/authz-review.md 形成结构化 JWT 安全审查，包含授权路径、代码证据、影响、严重度和修复及回归验证建议。
risk_surface:
  - JWT 签名校验
  - 算法约束
  - 有效期校验
  - 角色声明授权
assets:
  - 用户账户
  - 管理端 API
permissions:
  - user
  - admin
data_categories:
  - 身份认证数据
  - 角色声明
remediation_expectations:
  - JWT 实现修复项交回 engineer-agent
  - 正式产品预期变化回交 pm-agent 分类
blockers_risks:
  - 未验证的令牌声明可能导致身份伪造和 admin 越权
```
