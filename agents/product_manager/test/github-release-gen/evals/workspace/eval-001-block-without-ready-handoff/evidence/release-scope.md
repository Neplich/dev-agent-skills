# 候选发布范围证据

- 功能候选：文件卡片与失败消息原位重试。
- 架构候选：`workflow_finished` 转换为统一附件模型。
- 状态：证据已收集，但完整站内正文尚未获得维护者确认。
- 约束：不得根据本候选证据绕过 `confirmation_status: confirmed` 门禁。
