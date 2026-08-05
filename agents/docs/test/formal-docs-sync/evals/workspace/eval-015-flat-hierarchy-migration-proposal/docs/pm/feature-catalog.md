---
feature: inherited-feature-catalog
version: 1.0.0
date: 2026-08-05
last_updated: 2026-08-05
status: Confirmed
---

# Feature Catalog

| 一级功能域 | 功能 | Feature path | Owner | API surface |
| --- | --- | --- | --- | --- |
| 知识建设与维护 | 文档摄取 | `knowledge-building/document-ingestion` | `knowledge-platform` | `POST /api/knowledge-building/documents` |
| 知识建设与维护 | 知识维护 | `knowledge-building/knowledge-curation` | `knowledge-platform` | `PATCH /api/knowledge-building/documents/{document_id}` |
| 知识发现与应用 | 研究会话 | `knowledge-discovery/conversations` | `knowledge-discovery` | `POST /api/knowledge-discovery/conversations` |
| 知识发现与应用 | 图谱检索 | `knowledge-discovery/graph-search` | `knowledge-discovery` | `POST /api/knowledge-discovery/graph/search` |
| 知识发现与应用 | 会话消息 | `knowledge-discovery/conversations/messages` | `knowledge-discovery` | `POST /api/knowledge-discovery/conversations/{conversation_id}/messages` |
| 平台治理与运行 | 工作区治理 | `platform-governance/workspace-governance` | `platform-ops` | `GET /api/platform-governance/workspaces` |
| 平台治理与运行 | 后台任务 | `platform-governance/background-jobs` | `platform-ops` | `GET /api/platform-governance/jobs/{job_id}` |

这七个功能归属于表中三个一级功能域。目录层级以 `feature_path` 为准，
同一一级功能域的 owner 和 API route prefix 与该归属一致。
