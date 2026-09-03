---
feature: release-changelog
version: 0.6.6
date: 2026-09-03
last_updated: 2026-09-03
---

# Changelog - v0.6.6

## [v0.6.6] - 2026-09-03

本版本统一正式文档 frontmatter 字段口径并加严契约校验：迭代类 skill 更新既有文档时当场补齐缺失必填字段，文档契约检查从静默放低升级为硬失败；另完成 eval 机制移除后的文档残留清理，覆盖 v0.6.5 之后合并到 `main` 的 4 个 PR。

### Added

- **contract:** 正式文档必填字段校验加严与豁免显式登记 ([#333](https://github.com/Neplich/dev-agent-skills/pull/333))。`check_doc_contract.py` 在既有四字段基础上扩展至 output-conventions 必填全集（`title`/`type`/`feature_path`/`parent_feature`/`feature_level`/`status`/`author`/`generated_by`），缺失即报错；新增 changelog frontmatter 结构逐条校验与 PRD `child_features` 非空要求；新增 `FORMAL_DOC_FIELD_EXEMPTIONS` 豁免注册表，`CI_PLAN.md` 为当前唯一登记条目，基础四字段校验对豁免文档仍然生效。

### Changed

- 统一正式文档字段口径，迭代触及既有文档时补齐缺失必填字段 ([#332](https://github.com/Neplich/dev-agent-skills/pull/332))。`idea-to-spec` 输出约定移除必填字段的"仅新建"限定并新增 Updating Existing Documents 规则：`prd-iteration`、`trd-iteration`、`tspecs-iteration` 与 `trd-gen` 更新既有文档时当场补建缺失必填字段与 changelog 结构、按规则 bump 版本，不再因文档早于约定而跳过；可选字段与有文档化 fallback 的字段属设计意图，维持不变。65 份历史文档同步补齐 `child_features`、`changelog` 与 `generated_by`，`CI_PLAN.md` 登记豁免并维持最小 frontmatter。

### Fixed

- 清理活跃规格中的 eval 残留并对齐 human-writing 验收契约 ([#327](https://github.com/Neplich/dev-agent-skills/pull/327))。72 份活跃 PRD/TRD/CI_PLAN/DECISIONS 中以现行语气引用已移除 eval 机制的内容删除或改挂现存确定性检查；DECISIONS 新增 D-023，明确真实项目案例与人工语义验收是能力迭代原则、不作为完成门禁，不恢复 Skill eval 体系的结论不变。
- 清理 skill PRD persona 行与守护句中的惰性 eval 提及 ([#329](https://github.com/Neplich/dev-agent-skills/pull/329))。30 份 skill 级 PRD 的维护者 persona 行统一为"维护 skill 文档和确定性检查的人"；`idea-to-spec` TRD 三处防误扫守护句的 eval fixture 举例泛化为测试/评测夹具表述，守护语义不变。

## 发布说明

- 发版清单：`.claude-plugin/marketplace.json` 的 `metadata.version` 更新为 `0.6.6`；7 个 `agents/*/.claude-plugin/plugin.json` 与 `.kimi-plugin/plugin.json` 的 `version` 同步为 `0.6.6`（由 `check_repository_contract.py` 强制校验）。
- 行为变更：迭代类 skill 更新既有正式文档时须当场补齐缺失必填字段，不再按"仅新建"限定跳过（#332）；仓库文档契约校验扩展至必填全集并硬失败（#333）。其余为文档残留清理，不改变 skill 运行行为。
