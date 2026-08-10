# PM Handoff Packet

产品与安全负责人已确认本次报表导出授权审查范围和可用材料。

```yaml
request_type: security
change_tier: standard
feature_path: report-export
feature: report-export
parent_feature: N/A
feature_level: 1
feature_path_evidence:
  - source: docs/site/api/report-export.md
    reason: 现有正式说明覆盖报表导出角色边界，可作为 report-export 审查的功能归属证据。
source_documents:
  - docs/site/api/report-export.md
  - src/access/report-export-policy.js
scope_decision:
  summary: 核对 admin 与 analyst 的报表导出权限，确认当前服务端策略是否符合已记录的角色边界。
  expectation_changed: false
  non_goals:
    - 修改报表查看权限
    - 实现授权修复
downstream_owner: Security
required_output: 在 docs/security/report-export/authz-review.md 形成报表导出授权审查，列出实际允许角色、证据、风险影响和整改建议。
risk_surface:
  - 服务端报表导出角色校验
assets:
  - 报表导出数据
permissions:
  - admin
  - analyst
data_categories:
  - 报表业务数据
blockers_risks:
  - 正式说明尚未核验，记录的角色边界可能与服务端策略不同
```
