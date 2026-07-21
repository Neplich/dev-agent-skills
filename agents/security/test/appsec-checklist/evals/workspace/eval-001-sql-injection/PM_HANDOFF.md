# PM Handoff Packet

pm-agent 已完成入口分类，并将用户搜索 API 的应用安全审查路由至 appsec-checklist。

```yaml
request_type: security
change_tier: standard
feature_path: user-search
feature: user-search
parent_feature: N/A
feature_level: 1
feature_path_evidence:
  - source: docs/pm/user-search/PRD.md
    reason: 该 PRD 已确认用户搜索 API 的输入、数据查询和安全审查范围，是 user-search 的正式产品依据。
source_documents:
  - docs/pm/user-search/PRD.md
  - src/api/user-search.js
scope_decision:
  summary: 审查用户搜索条件进入数据库查询的路径，识别可利用的应用安全风险并给出分级和修复建议。
  expectation_changed: false
  non_goals:
    - 重构用户目录数据模型
    - 实现搜索结果排序
downstream_owner: Security
required_output: 按 feature_path 输出 docs/security/user-search/appsec-checklist.md，包含可定位证据、影响、严重度依据和可执行修复建议，不直接修改应用代码。
risk_surface:
  - GET /api/users/search 查询参数
  - 用户目录数据库查询
assets:
  - 用户目录数据
  - 数据库可用性与完整性
permissions:
  - authenticated-user
data_categories:
  - 用户账号资料
remediation_expectations:
  - 应用代码修复项交回 engineer-agent
  - 修复后对恶意搜索输入执行回归验证
blockers_risks:
  - 搜索参数直接进入原始 SQL 时可能造成数据泄露或破坏
```
