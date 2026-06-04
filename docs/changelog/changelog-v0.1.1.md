# Changelog - v0.1.1

## [v0.1.1] - 2026-05-20

### Added

- 将 `trd-gen` 从 PM 内部能力迁移为 Engineer Agent 的公开 skill，并注册到 marketplace；PRD 确认后由 Engineer 负责产出 `docs/engineer/{feature}/TRD.md`。([#19](https://github.com/Neplich/dev-agent-skills/pull/19))
- 增加 Engineer Agent 复杂编码任务分工规则，明确主进程、实现 sub-agent 和验收 sub-agent 的职责边界。([#16](https://github.com/Neplich/dev-agent-skills/pull/16))
- 增加 `feature-implementor` 文档驱动实现 eval fixture，并补充缺失 TRD 时不得直接实施的负向 eval。([#16](https://github.com/Neplich/dev-agent-skills/pull/16), [#19](https://github.com/Neplich/dev-agent-skills/pull/19))

### Changed

- 调整 Engineer 交付链路，明确 PRD 确认后移交 Engineer 编写 TRD，TRD 确认后再移交 `feature-implementor` 编写实现计划。([#19](https://github.com/Neplich/dev-agent-skills/pull/19))
- 调整 `feature-implementor` planner、implementor 和 reviewer 内部指令，使复杂 spec 驱动任务可以区分计划、实现、验收和最终交付。([#16](https://github.com/Neplich/dev-agent-skills/pull/16))
- 调整 `debugger` 复杂 bug 修复流程，保留复现优先路径，并支持最小修复与独立验收分工。([#16](https://github.com/Neplich/dev-agent-skills/pull/16))
- 调整 QA 浏览器 E2E 执行策略，在 Claude Code / Codex 环境下优先使用 Chrome 插件或 browser connector；平台外或 standalone skill 无插件时使用 Playwright 兜底。([#13](https://github.com/Neplich/dev-agent-skills/pull/13))
- 调整 Codex 安装入口和 README Quick Start，使用当前 `.agents` 路径模型暴露具体 skill 软链接。([#11](https://github.com/Neplich/dev-agent-skills/pull/11))

### Fixed

- 修复 Codex skill 旧聚合目录 `.agents/skills/dev-agent-skills` 的迁移兼容问题；子集重装或切换已选 Agent 时，会先清理本仓库 managed symlink，再创建本次选择的 skill 链接。([#17](https://github.com/Neplich/dev-agent-skills/pull/17))
- 修复工程输入缺失 TRD 时可能继续进入实现的问题，通过负向 eval 固定 handoff 行为。([#19](https://github.com/Neplich/dev-agent-skills/pull/19))

### Test

- 更新 PM、Engineer、QA、Designer、DevOps 文档和 eval fixture 中的 TRD 路径与角色边界。([#19](https://github.com/Neplich/dev-agent-skills/pull/19))
- 更新 QA E2E 策略相关 eval fixture，验证 Chrome 插件、browser connector 和 Playwright fallback 的执行路径选择。([#13](https://github.com/Neplich/dev-agent-skills/pull/13))
- 完成 `trd-gen`、PM handoff、`feature-implementor`、缺失 TRD handoff 以及复杂工程分工相关 fresh sub-agent validation。([#16](https://github.com/Neplich/dev-agent-skills/pull/16), [#19](https://github.com/Neplich/dev-agent-skills/pull/19))

### CI

- 在本版本关联 PR 中通过 repository contract、eval contract、eval artifacts 和确定性 pytest 校验。([#11](https://github.com/Neplich/dev-agent-skills/pull/11), [#13](https://github.com/Neplich/dev-agent-skills/pull/13), [#16](https://github.com/Neplich/dev-agent-skills/pull/16), [#17](https://github.com/Neplich/dev-agent-skills/pull/17), [#19](https://github.com/Neplich/dev-agent-skills/pull/19))
