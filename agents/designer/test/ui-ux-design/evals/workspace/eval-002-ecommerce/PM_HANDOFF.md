# PM Handoff Packet

```yaml
request_type: design
change_tier: standard
feature_path: handmade-crafts-store
feature: handmade-crafts-store
parent_feature: N/A
feature_level: 1
feature_path_evidence:
  - source: docs/pm/handmade-crafts-store/PRD.md
    reason: 已确认手工艺品商店的移动端浏览与购物车设计范围。
source_documents:
  - docs/pm/handmade-crafts-store/PRD.md
scope_decision:
  summary: 设计从商品列表、筛选、详情到购物车的 mobile-first 体验。
  expectation_changed: false
  non_goals:
    - 结账与支付
    - 账号中心
    - 前端实现
downstream_owner: Designer
required_output: docs/design/handmade-crafts-store/ui-ux-spec.md
blockers_risks: []
```

目标用户是使用手机选购独立手工艺品的消费者。设计必须覆盖加载、空结果、缺货、购物车数量调整与移除状态，并在设计交接处停止。
