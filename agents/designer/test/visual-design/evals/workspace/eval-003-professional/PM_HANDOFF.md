# PM Handoff Packet

```yaml
request_type: design
change_tier: standard
feature_path: enterprise-analytics
feature: enterprise-analytics
parent_feature: N/A
feature_level: 1
feature_path_evidence:
  - source: docs/pm/enterprise-analytics/PRD.md
    reason: 已确认企业分析平台的受众、数据密度和可访问性要求。
source_documents:
  - docs/pm/enterprise-analytics/PRD.md
scope_decision:
  summary: 定义可信、权威、数据密集但易扫描的企业视觉系统。
  expectation_changed: false
  non_goals:
    - 重做信息架构
    - 生成组件代码或设计 token 配置
    - 强制提供暗色模式
downstream_owner: Designer
required_output: docs/design/enterprise-analytics/visual-system.md
blockers_risks: []
```

目标用户包括分析师、运营负责人和管理层。视觉规范必须覆盖表格、图表、筛选、状态和告警。
