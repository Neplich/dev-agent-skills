---
feature: release-changelog
version: 0.6.4
date: 2026-08-20
last_updated: 2026-08-20
---

# Changelog - v0.6.4

## [v0.6.4] - 2026-08-20

本版本为 feature-implementor 建立实施计划预期对账与门禁授权自动审查者，补齐 human-writing 的范围判断、结构权限与高风险事实回传，并修正其英文描述。本版本覆盖 v0.6.3 之后合并到 `main` 的 3 个 PR。

### Added

- **feature-implementor:** 实施计划预期对账与门禁授权自动审查者 ([#317](https://github.com/Neplich/dev-agent-skills/pull/317))。为 `feature-implementor` 增加六字段预期改动声明，在实施证据、closeout 与 reviewer 之间建立预期/实际对账；偏离记录补充统一字段、分类与处置规则（`scope_up` / `design_gap` 默认拆分 Issue，纯 `estimate_wrong` 仅留 closeout 记录）；PM handoff contract 增加 `plan_approval` / `trd_approval` 可选授权，并定义自动审查者的独立上下文、non-goals、发现定级、收敛和人工升级要求。

- **human-writing:** 补齐范围判断、结构权限与高风险事实回传 ([#314](https://github.com/Neplich/dev-agent-skills/pull/314))。工作方式扩展为创建/改写/审查三种，写前先判断模式与范围（passage/单文档/文档集/整站），局部任务不强制全站盘点，整站任务先查章节分组与读者路径；明确保留的是主 Skill 规定的必要结构与真实流程而非现有布局，授权后可重分章节；高风险事实变更需回传主 Skill。

### Fixed

- **human-writing:** 将发现描述改为英文 ([#312](https://github.com/Neplich/dev-agent-skills/pull/312))。将 human-writing 的显示名和短描述改为全英文，并同步刷新技能锁文件哈希。

## 发布说明

- 发版清单：`.claude-plugin/marketplace.json` 的 `metadata.version` 更新为 `0.6.4`；7 个 `agents/*/.claude-plugin/plugin.json` 与 `.kimi-plugin/plugin.json` 的 `version` 同步为 `0.6.4`（由 `check_repository_contract.py` 强制校验）。
- 行为变更：feature-implementor 的 closeout 与 review 流程引入预期/实际对账，偏离记录需按统一字段与分类处置；human-writing 的执行方式扩展为创建/改写/审查，写前需先判断模式与范围，结构保留以主 Skill 规定为准而非现有布局。
