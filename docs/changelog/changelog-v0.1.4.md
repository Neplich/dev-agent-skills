# Changelog - v0.1.4

## [v0.1.4] - 2026-06-25

### Added

- 补齐 6 个 Agent 和 28 个 specialist skill 的 PRD 基线，为 skill marketplace 后续治理、元数据规则和行为审查提供统一需求承接基础。([#39](https://github.com/Neplich/dev-agent-skills/pull/39))
- 固化多级 `feature_path` 文档契约，覆盖 PM、Engineer、QA、Designer、DevOps、Security 的跨角色文档主键和下游消费路径。([#42](https://github.com/Neplich/dev-agent-skills/pull/42))

### Changed

- 补齐 README / README_zh 协作门禁主链路，将 PRD/TRD 对齐、TRD 确认、实施计划确认和 QA E2E handoff 纳入主流程。([#34](https://github.com/Neplich/dev-agent-skills/pull/34))
- 规范实施计划元数据和 marketplace 版本同步规则，增加发布前 metadata、changelog 和 tag 检查约束。([#36](https://github.com/Neplich/dev-agent-skills/pull/36))
- 规范正式 Markdown 文档的 author 元数据，禁止使用 `AI Assistant` 或裸 `Codex` 作为正式文档作者。([#40](https://github.com/Neplich/dev-agent-skills/pull/40))

### Fixed

- 调整 `changelog-generator` 的 docs/test/ci/build/style 前缀处理策略，避免 skill marketplace 中的重要文档、eval 或发布流程变化被无条件跳过。([#41](https://github.com/Neplich/dev-agent-skills/pull/41))
- 固化前端 UI 更新路由，要求 Engineer 完成 PRD/TRD 对齐后检查设计交付物，设计缺失或过期时回接 Designer。([#43](https://github.com/Neplich/dev-agent-skills/pull/43))
- 补齐 `feature-implementor` 实施计划收尾门禁，防止 `status: Implemented` 与正文计划状态冲突进入 handoff / delivery。([#45](https://github.com/Neplich/dev-agent-skills/pull/45))
- 规范 eval baseline 证据契约，明确 baseline 是 `without_skill` 对照输入；deterministic checker 不再根据 baseline 自由文本判断 PASS、PARTIAL 或 BLOCKED，baseline output 与 baseline-only assertion 只作为报告证据。([#47](https://github.com/Neplich/dev-agent-skills/pull/47))
