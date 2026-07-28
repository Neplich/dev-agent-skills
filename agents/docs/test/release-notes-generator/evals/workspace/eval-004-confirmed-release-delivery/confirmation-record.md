# Maintainer Confirmation Record

recorded_by: repo-maintainer
recorded_at: 2026-07-28T15:30:00+08:00

## Target Release Version Confirmation

- target_release_version: v1.0.0
- status: maintainer_confirmed
- confirmed_by: repo-maintainer
- confirmed_scope: 文件卡片、消息重试及其后端附件模型、迁移和交付资产

维护者明确确认 `v1.0.0` 是本次站内版本说明和后续发布前文档审计的唯一目标版本。

## Release Notes Body Confirmation

维护者已审阅完整 Release Notes 正文，并明确确认正文必须完整保留以下事实类别及其
证据含义：

- 文件卡片与失败消息原位重试；
- workflow_finished 到统一附件模型的架构链路与旧文本兼容；
- nullable JSONB 迁移、回填顺序和删列数据风险；
- 数据库、Gateway、Web 的部署顺序和 feature flag；
- web/gateway 双架构镜像、已核对的 manifest digest 与静态 manifest；
- 分步升级、回滚、旧浏览器限制。

confirmation_status: confirmed
confirmation_scope: complete_release_notes_body
reconfirmation_required_if_body_changes: true
