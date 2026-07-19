# Release Notes Handoff

- request_type: existing_update
- change_tier: major
- feature_path: products/ai-hub/v1-file-delivery
- release_version: v1.0.0
- release_scope: 文件卡片、消息重试、附件模型、数据库迁移与交付资产
- host_repository: current fixture repository
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
- required_output: 生成、确认、索引并校验 docs/site/release-notes/v1.0.0.md，随后提供 issue #120 handoff
- blockers_risks: 无入口阻塞；正文确认与宿主 docs checks 仍由 specialist gate 执行

只要求 Docs Agent 完成入口检查和 specialist 分流，不执行正文生成、GitHub Release、
tag、部署或 #117 盖章。
