---
version: 1.4.0
status: confirmed
confirmed_by: repository-maintainer
---

# v1.4.0

## 重点更新

- GitHub Release 生成流程现在先判断宿主是否初始化正式文档站。
- 无正式文档站的宿主可使用维护者确认的版本化 changelog 生成完整预览。

## 其他改进

- 预览和最终报告会记录门禁适用性及其证据。
- GitHub compare 只补充可追溯信息，不替代版本事实源。

## 升级说明

- 无需迁移数据或修改运行时配置。
- 发布仍由宿主的手动 release checklist 驱动。

## 变更明细

- 双态审计 handoff 降级只适用于无 `docs/site/` 且无 #116 站内 Release Notes 能力链的宿主。
- 有正式文档站的宿主继续执行原有 #116/#117 门禁。
- 每次 draft 或 publish 写入前仍需维护者显式、当前的批准。

## 兼容性与风险

- 降级不授权创建或移动 tag，也不授权任何 GitHub Release 写入。
- 若版本事实源未确认、与版本 bump 冲突或证据不完整，发布流程必须阻塞。
