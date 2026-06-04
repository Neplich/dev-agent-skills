# Changelog - v0.1.2

## [v0.1.2] - 2026-06-04

### Added

- 增加 QA E2E 功能树持久化规范，统一 `docs/qa/e2e/{一级功能}/{二级功能}/{三级功能}/` 下的 `TEST_SUITE.md`、`FLOW_INDEX.md`、`cases/`、`scripts/`、`results/` 和 `_reports/` 目录结构。([#25](https://github.com/Neplich/dev-agent-skills/pull/25))
- 增加 QA E2E 本地账号引用与测试报告 reference，明确 `.qa/e2e/accounts.local.json` 的本地凭据存储方式，避免明文账号、密码、token 或 session 进入测试文档。([#25](https://github.com/Neplich/dev-agent-skills/pull/25))
- 增加 `docs/pm/qa-e2e-case-memory/PRD.md`、`docs/engineer/qa-e2e-case-memory/TRD.md` 和 `docs/engineer/qa-e2e-case-memory/IMPLEMENTATION_PLAN.md`，沉淀 QA E2E 用例记忆能力的产品、技术和实施计划。([#25](https://github.com/Neplich/dev-agent-skills/pull/25))
- 增加 `debugger` 最小 failing-test eval workspace，让 bug 复现证据可以由真实 fixture 和测试命令给出。([#22](https://github.com/Neplich/dev-agent-skills/pull/22))

### Changed

- 调整 `feature-implementor` 实施流程，要求所有实现任务先产出或更新 `docs/engineer/{feature}/IMPLEMENTATION_PLAN.md`，并在用户确认后再修改代码；小功能、单文件变更和轻量 bug fix 也不能跳过实施计划。([#22](https://github.com/Neplich/dev-agent-skills/pull/22))
- 调整 `engineer-agent`、`feature-implementor`、`debugger` 和 `trd-gen` 的现有功能变更路径，在进入实现或修复前先对齐 PRD/TRD 预期；需求变化回 PM，TRD 缺口回 `trd-gen`。([#22](https://github.com/Neplich/dev-agent-skills/pull/22))
- 调整 `debugger` 流程，在根因分析后先汇报 bug 分析并询问是否产出 repair plan，修复计划确认前不直接修改代码。([#22](https://github.com/Neplich/dev-agent-skills/pull/22))
- 调整 eval metadata 与 runner 边界，运行期 transcript、subagent verdict、diagnostics 和 scratch eval run 不再作为 durable eval output 提交。([#24](https://github.com/Neplich/dev-agent-skills/pull/24))
- 迁移和补齐各 Agent 的 durable `comparison.md`，所有 eval item 都有显式 workspace、`eval_metadata.json` 和长期保留的 comparison 结果摘要。([#24](https://github.com/Neplich/dev-agent-skills/pull/24))

### Fixed

- 修复 skill eval 或 fresh Codex subagent validation 通过后，durable `comparison.md` 仍停留在 pending 状态的问题。([#24](https://github.com/Neplich/dev-agent-skills/pull/24))
- 修复 QA eval 空跑、运行期输出路径检查和 E2E scaffold 残留路径校验问题，避免 runner-only 产物污染 durable fixture。([#25](https://github.com/Neplich/dev-agent-skills/pull/25))
- 修复 eval contract 对 `workspace: null`、空 output metadata、diagnostics 目录和 runtime artifact 路径拦截不完整的问题。([#24](https://github.com/Neplich/dev-agent-skills/pull/24))

### Test

- 补充 `agents/test_eval_contract.py` 回归覆盖，校验 eval workspace、metadata output、runtime artifact blocklist 和 diagnostics path 约束。([#24](https://github.com/Neplich/dev-agent-skills/pull/24))
- 更新 QA、Engineer、PM、Designer、DevOps、Security 的 eval fixture、comparison 和测试说明，使 skill 行为变更有对应 durable 评测证据。([#24](https://github.com/Neplich/dev-agent-skills/pull/24), [#25](https://github.com/Neplich/dev-agent-skills/pull/25))
- 完成 QA E2E 用例持久化相关 fresh subagent validation，记录 23/23 PASS。([#25](https://github.com/Neplich/dev-agent-skills/pull/25))

### CI

- 保持 `repository-contract`、`eval-contract` 和 `python-tests` 作为 PR 必跑校验，并在本版本关联 PR 中通过。([#22](https://github.com/Neplich/dev-agent-skills/pull/22), [#24](https://github.com/Neplich/dev-agent-skills/pull/24), [#25](https://github.com/Neplich/dev-agent-skills/pull/25))
