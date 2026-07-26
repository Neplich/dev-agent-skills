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
  - pyproject.toml
  - app/main.py
scope_decision:
  summary: 为 FastAPI API-only 服务生成部署配置，不引入任何持久化依赖。
  expectation_changed: false
  non_goals:
    - 数据库、Redis 或 migration
    - CI/CD
    - 实际发布
downstream_owner: DevOps
required_output: 简化的 local、Docker 和 Helm 配置
blockers_risks: []
```

服务入口为 `uvicorn app.main:app --host 0.0.0.0 --port 8000`。所有部署目标都不得增加数据库服务、`DATABASE_URL`、Redis 或初始化步骤。
