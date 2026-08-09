# Release Notes Handoff

- request_type: existing_update
- change_tier: major
- feature_path: products/ai-hub/v1-file-delivery
- release_version: v1.0.0
- release_scope: 文件卡片、消息重试、附件模型、数据库迁移与交付资产
- host_repository: current product repository
- source_documents:
  - docs/pm/products/ai-hub/v1-file-delivery/PRD.md
  - docs/engineer/products/ai-hub/v1-file-delivery/TRD.md
  - docs/engineer/products/ai-hub/v1-file-delivery/IMPLEMENTATION_PLAN.md
- evidence_sources:
  - apps/web/src/features/chat/
  - services/gateway/src/workflow-events.ts
  - migrations/2026071901_add_message_files.sql
  - deploy/helm/ai-hub/
  - dist/manifest.json
  - test-results/release-v1.0.0.md
- required_output: 面向站内读者的 `docs/site/release-notes/v1.0.0.md` 版本说明
- blockers_risks: 版本说明正文尚未生成，宿主文档检查尚未执行

目标版本、变更范围、宿主仓库和证据位置均已确认。当前工作区还没有
`docs/site/release-notes/v1.0.0.md` 或该版本的文档审计结果。
