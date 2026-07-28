---
feature: release-changelog
version: 0.3.5
date: 2026-07-29
last_updated: 2026-07-29
---

# Changelog - v0.3.5

## [v0.3.5] - 2026-07-29

本版本集中完善 skill eval 的结果解释、区分度与 fixture 身份治理：comparison 采用 Behavior result 与 Coverage result 两维模型，实时样本缺口不再误判为行为失败；docs-agent 集成链、docs-audit、formal-docs-sync 与 release-notes-generator 的重点 eval 完成区分度重做或磨平回滚；运行协议中的历史 issue 身份统一替换为当前 skill 与状态名。同时，github-reader 增加 count-first 查询、精确总数、计算集合上限与截断声明，避免将部分 GitHub 数据误报为完整状态。本版本覆盖 v0.3.4 之后合并到 `main` 的全部变更（#182、#183、#184、#185、#186、#187）。

### Changed

- **运行协议身份与状态名**：将 Release Notes、文档审计、GitHub Release 协作链和 PM 入口中的历史 issue 身份替换为当前 skill 与运行状态名，保留历史设计文档的 issue 溯源，减少已关闭 issue 对现行协议的误导。([#182](https://github.com/Neplich/dev-agent-skills/pull/182))
- **Skill Eval 两维结果模型**：durable `comparison.md` 拆分 Behavior result 与 Coverage result；实时外部数据缺少场景样本时记为 `NOT EXERCISED`，并由 summarizer 分别汇总 `PASS`、`PASS (partial coverage)`、`PARTIAL` 与 `BLOCKED`。([#184](https://github.com/Neplich/dev-agent-skills/pull/184))
- **docs-agent 集成发布链 eval 区分度**：重做 `docs-agent/eval-005` 的 prompt、assertions 与原始 Git 证据 fixture，移除预制成功模板和协议答案，fresh 成对验证恢复 3 条 assertion 级差距。([#185](https://github.com/Neplich/dev-agent-skills/pull/185))
- **docs-audit eval 区分度**：重做 eval-010 至 eval-013，使用 authority、tree、version、staged metadata 与 normalization 的阻塞型原始证据恢复区分度，并修复集成发布链 fixture 的可执行位。([#186](https://github.com/Neplich/dev-agent-skills/pull/186))
- **正式文档发布链 eval 与 fixture 身份治理**：重做 formal-docs-sync 与 release-notes-generator 的重点 eval，回滚被模型通用能力磨平的零区分度改写，并清理 Docs 发布链与 GitHub Release fixture 中作为运行协议身份的历史 issue 编号；受身份更新影响的 10 个 fresh re-baseline 待办统一转交 issue [#188](https://github.com/Neplich/dev-agent-skills/issues/188)。([#187](https://github.com/Neplich/dev-agent-skills/pull/187))

### Fixed

- **github-reader 查询协议数据完整性**：Full status 与 Feed mode 增加 count-first 查询和精确 `total_count`，四类计算集合上限统一为 1000；当 `fetched < total` 时必须在集合与健康摘要中声明截断，并区分展示限行与计算集合限行。([#183](https://github.com/Neplich/dev-agent-skills/pull/183))

## Skill Eval 汇总（v0.3.5 发版前）

本节按 marketplace 当前注册的 **40 个 skill** 逐一汇总最新结论。`uv run scripts/summarize_eval_results.py` 按各 skill `evals.json` 的 workspace 契约路径机械提取，共核对 **187** 份 durable `comparison.md`：**168 PASS、3 PASS (partial coverage)、6 PARTIAL、10 BLOCKED**。

| Agent | Skill（eval 范围） | 纳入汇总的 durable comparison 数 | 最新结论 |
| --- | --- | ---: | --- |
| Designer | `designer-agent` | 3 | 3 PASS |
| Designer | `ui-ux-design` | 5 | 3 PASS、2 PARTIAL |
| Designer | `visual-design` | 3 | 2 PASS、1 PARTIAL |
| DevOps | `cicd-bootstrap` | 3 | 3 PASS |
| DevOps | `deployment-planner` | 4 | 4 PASS |
| DevOps | `devops-agent` | 2 | 2 PASS |
| DevOps | `env-config-auditor` | 4 | 3 PASS、1 PARTIAL |
| DevOps | `incident-playbook-writer` | 2 | 2 PASS |
| Docs | `docs-agent` | 6 | 5 PASS、1 BLOCKED |
| Docs | `docs-audit` | 14 | 11 PASS、3 BLOCKED |
| Docs | `docs-site-bootstrap` | 4 | 4 PASS |
| Docs | `formal-docs-sync` | 14 | 14 PASS |
| Docs | `release-notes-generator` | 5 | 5 PASS |
| Engineer | `codebase-analyzer` | 3 | 3 PASS |
| Engineer | `debugger` | 5 | 5 PASS |
| Engineer | `delivery` | 1 | 1 PASS |
| Engineer | `engineer-agent` | 4 | 4 PASS |
| Engineer | `feature-implementor` | 17 | 15 PASS、2 PARTIAL |
| Engineer | `project-bootstrap` | 2 | 2 PASS |
| Engineer | `test-writer` | 2 | 2 PASS |
| Engineer | `trd-gen` | 5 | 5 PASS |
| Product Manager | `changelog-generator` | 3 | 1 PASS、2 PASS (partial coverage) |
| Product Manager | `competitive-brief` | 1 | 1 PASS |
| Product Manager | `competitive-intelligence` | 1 | 1 PASS |
| Product Manager | `feature-catalog` | 4 | 4 PASS |
| Product Manager | `github-reader` | 5 | 4 PASS、1 PASS (partial coverage) |
| Product Manager | `github-release-generator` | 6 | 6 BLOCKED |
| Product Manager | `idea-to-spec` | 8 | 8 PASS |
| Product Manager | `pm-agent` | 15 | 15 PASS |
| Product Manager | `roadmap-generator` | 3 | 3 PASS |
| QA | `bug-analyzer` | 3 | 3 PASS |
| QA | `exploratory-tester` | 3 | 3 PASS |
| QA | `qa-agent` | 3 | 3 PASS |
| QA | `regression-suite` | 3 | 3 PASS |
| QA | `spec-based-tester` | 3 | 3 PASS |
| Security | `appsec-checklist` | 5 | 5 PASS |
| Security | `authz-reviewer` | 4 | 4 PASS |
| Security | `dependency-risk-auditor` | 4 | 4 PASS |
| Security | `privacy-surface-mapper` | 4 | 4 PASS |
| Security | `security-agent` | 1 | 1 PASS |
| **合计** | **40 个 marketplace skill 分组** | **187** | **168 PASS、3 PASS (partial coverage)、6 PARTIAL、10 BLOCKED** |

其中 **10 个 BLOCKED** 是 fixture 身份更新后按维护者决定挂起的 fresh re-baseline 待办：`github-release-generator` 6 个、`docs-audit` 3 个、`docs-agent` 1 个，统一由 issue [#188](https://github.com/Neplich/dev-agent-skills/issues/188) 跟踪，不表示本版本已观察到 skill 行为回归。`release-notes-generator/eval-002` 与 `formal-docs-sync/eval-009` 在无明显规则泄漏的前提下仍为零区分度，维护者将其保留为模型通用能力磨平 skill 增量的审查标本，同样归入 #188。其余 **6 个 PARTIAL** 为既有历史 comparison 证据缺口；**3 个 PASS (partial coverage)** 表示实际触发路径行为通过，但部分依赖实时数据的 assertion 场景未被本轮样本覆盖。
