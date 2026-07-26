# PM Handoff Packet

```yaml
request_type: deployment
change_tier: standard
feature_path: N/A
feature: N/A
parent_feature: N/A
feature_level: N/A
feature_path_evidence: []
source_documents:
  - deploy/docker/docker-compose.yml
  - deploy/docker/.env.example
  - deploy/docker/README.md
scope_decision:
  summary: 为现有 production Docker Compose 服务编写回滚、故障响应、排查和值班手册。
  expectation_changed: false
  non_goals:
    - 实际执行回滚
    - 修改应用
    - 数据库 migration 回滚
downstream_owner: DevOps
required_output:
  - deploy/ROLLBACK.md
  - deploy/INCIDENT_RESPONSE.md
  - deploy/TROUBLESHOOTING.md
  - deploy/ON_CALL.md
blockers_risks:
  - 回滚必须使用已知健康的不可变 SemVer tag
```

P1 应用不可用要求 15 分钟内响应并升级至 on-call lead；P2 部分降级要求 30 分钟内响应。升级渠道使用 `#ops-incidents`，角色为 on-call engineer、incident commander 和 service owner。
