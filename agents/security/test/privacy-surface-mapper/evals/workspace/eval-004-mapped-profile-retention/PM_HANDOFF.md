# PM Handoff Packet

产品与安全负责人已确认本次个人资料处理面审查范围和可用材料。

```yaml
request_type: security
change_tier: standard
feature_path: profile-data
feature: profile-data
parent_feature: N/A
feature_level: 1
feature_path_evidence:
  - source: docs/site/api/profile-data.md
    reason: 现有正式说明覆盖个人资料字段、处理目的和删除后保留期限，可作为 profile-data 审查的功能归属证据。
source_documents:
  - docs/site/api/profile-data.md
  - src/privacy/profile-processing.yaml
scope_decision:
  summary: 核对个人资料字段、处理目的和删除后的实际保留期限，确认当前配置是否符合已记录的数据处理事实。
  expectation_changed: false
  non_goals:
    - 扩展到其他个人数据处理活动
    - 实现保留策略整改
downstream_owner: Security
required_output: 在 docs/security/profile-data/privacy-map.md 形成个人资料处理面审查，列出字段、目的、实际保留期限、合规影响和整改建议。
risk_surface:
  - 账户删除后的个人资料保留
assets:
  - 用户个人资料
data_categories:
  - email
  - display_name
blockers_risks:
  - 正式说明尚未核验，记录的保留期限可能与处理配置不同
```
