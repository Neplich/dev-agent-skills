# 部署与配置证据

- `deploy/helm/ai-hub/values.yaml` 新增 `features.fileCards.enabled`，生产默认 false。
- `deploy/helm/ai-hub/templates/web.yaml` 把该值注入 `FILE_CARDS_ENABLED`。
- 发布顺序：先数据库迁移，再 Gateway，最后 Web；回滚按相反顺序。
