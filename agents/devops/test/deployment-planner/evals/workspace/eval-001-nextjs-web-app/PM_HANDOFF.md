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
  - package.json
  - app/api/health/route.ts
scope_decision:
  summary: 为现有 Next.js 服务生成 local、Docker 和 Helm 三种部署配置。
  expectation_changed: false
  non_goals:
    - CI/CD
    - 实际部署
    - 保存生产凭据
downstream_owner: DevOps
required_output: deploy/local、deploy/docker 和 deploy/helm 下的可执行配置与说明
blockers_risks:
  - 示例配置只能使用占位值
```

运行约束：Node.js 22、应用端口 3000、启动命令 `npm run start`。PostgreSQL 与 Redis 是必须依赖，环境变量分别为 `DATABASE_URL` 和 `REDIS_URL`。Docker Compose 必须包含 `app`、`postgres`、`redis`；Helm 只部署应用，并通过 values 注入外部数据库与 Redis 地址。
