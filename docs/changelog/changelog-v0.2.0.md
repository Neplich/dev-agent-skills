---
feature: release-changelog
version: 0.2.0
date: 2026-07-05
last_updated: 2026-07-05
---

# Changelog - v0.2.0

## [v0.2.0] - 2026-07-05

### Added

- **`feature-catalog` skill**：新增项目画像与功能清单 skill，允许 AI agent 对存量代码库进行轻量扫描，自动生成功能目录草案（`feature_inventory`）；无 profile 时支持降级扫描出草案后请求确认，不阻断流程。([#67](https://github.com/Neplich/dev-agent-skills/pull/67), [#70](https://github.com/Neplich/dev-agent-skills/pull/70))
- **实施计划归档门禁**：`feature-implementor` 完成态或废弃态实施计划经 closeout 和维护者审批后，可归档到 `docs/engineer/{feature_path}/implementation-plans/archive/IMPLEMENTATION_PLAN-<scope>.md`；增加归档前置检查（preflight eval 012）和归档后允许创建新计划的流程验证（eval 013）；`hotfix` 等级合并 closeout 与归档为一次确认。([#57](https://github.com/Neplich/dev-agent-skills/pull/57))
- **变更分级契约**：在 AGENTS.md 引入 `change_tier`（`hotfix` / `standard` / `major`）三级分类，按等级调整各角色门禁强度，避免所有请求默认走最严格流程；`hotfix` 允许轻量计划形态和合并 closeout 确认，`standard` / `major` 维持完整流程。([#68](https://github.com/Neplich/dev-agent-skills/pull/68))
- **PM 唯一入口协议（Batch 1-4）**：补齐 `pm-agent` 高召回入口设计，覆盖 13 种请求类型的路由分类（产品、工程、测试、UI、部署、安全、交付、状态查询等）；引入 `change_tier` fast lane，hotfix 与 delivery 类请求在分类后立即放行；新增 PM 唯一入口 PRD 与 TRD 设计文档。([#69](https://github.com/Neplich/dev-agent-skills/pull/69), [#72](https://github.com/Neplich/dev-agent-skills/pull/72))
- **Batch 4 eval 覆盖**：补齐 PM 入口 eval 场景 9-13（目标 agent 未安装、`change_tier` hotfix fast lane、standard full gate、hotfix 滥用阻断、hotfix QA 直接影响路径）；集中执行 Batch 4 fresh Codex subagent validation，56 个 durable `comparison.md` 更新，验证覆盖 PM 入口、feature-catalog、idea-to-spec、role routers、feature-implementor 和 QA specialists。([#74](https://github.com/Neplich/dev-agent-skills/pull/74), [#75](https://github.com/Neplich/dev-agent-skills/pull/75))

### Changed

- **PR 合并确认规则**：AGENTS.md 仓库治理规则增加「创建 PR 后不要直接合并；必须等待维护者明确确认"可以合并"后再执行 merge / squash / rebase 合并操作」。([#56](https://github.com/Neplich/dev-agent-skills/pull/56))
- **Skill 目录相对路径可移植性**：将 skill 内部引用从工作区绝对路径改为 skill 目录相对路径，确保 skill 文档在不同机器和安装位置下引用一致，不依赖具体工作区结构。([#64](https://github.com/Neplich/dev-agent-skills/pull/64))
- **`_internal` 结构规范**：明确 `_internal/` 为可选目录，仅在需要渐进加载时创建；清理内部 README 双文件约束，跨模块共享内容统一放 `_internal/_shared/`；AGENTS.md 与各 Agent README 保持一致描述。([#65](https://github.com/Neplich/dev-agent-skills/pull/65))
- **跨 Agent 协作依赖与 handoff 降级规则**：显式声明 PM handoff packet 字段定义的权威来源（`skill-map.md`），统一各 role router 在缺少 PM handoff packet 时回到 `pm-agent` 做入口分类的降级规则；`project-bootstrap` 保留唯一直接调用例外。([#66](https://github.com/Neplich/dev-agent-skills/pull/66))
- **Gate 唯一副本下沉 specialist**：将各角色门禁的权威副本从 AGENTS.md 和 role router SKILL.md 下沉到各 specialist SKILL.md；role router 只保留入口凭据检查和分流指针，不再维护重复的执行 gate 规则。([#73](https://github.com/Neplich/dev-agent-skills/pull/73))
- **Marketplace 与 skill 触发描述收口**：更新 `.claude-plugin/marketplace.json` 各插件描述与各 skill frontmatter trigger 描述，确保入口语义与实际路由一致；pm-agent 描述扩展覆盖 feature-catalog 等新 skill 类型。([#71](https://github.com/Neplich/dev-agent-skills/pull/71))
- **Changelog 与归档口径修正**：明确实施计划归档为「窄例外」不适用于 PRD/TRD 等文档类型；修正 release 归档口径；补充 feature_path 迁移后的文档路径规范。([#49](https://github.com/Neplich/dev-agent-skills/pull/49), [#50](https://github.com/Neplich/dev-agent-skills/pull/50), [#53](https://github.com/Neplich/dev-agent-skills/pull/53))

---

## Skill Eval 汇总（v0.2.0 发版前）

基于 2026-07-05 Batch 4 fresh Codex subagent validation 结果，按 skill 维度汇总各自 `comparison.md` 最新结论。

### PM Agent（9 skills）

| Skill | Latest result | 说明 |
| --- | --- | --- |
| `pm-agent` | **PASS** | 13 eval 全部通过，2026-07-05 fresh validation，覆盖 change_tier fast lane、bypass gate、missing handoff 等场景 |
| `idea-to-spec` | **PASS** | 7 eval（3 个 iteration），最新 2026-07-05 fresh validation，覆盖嵌套路径和 API ADR handoff |
| `feature-catalog` | **PASS** | 3 eval，2026-07-05 fresh validation，v0.2.0 新增 skill |
| `roadmap-generator` | **PASS** | 3 eval 通过 |
| `changelog-generator` | **PARTIAL** | 3 eval，without_skill baseline 未生成，历史 with-skill 产物存在 |
| `competitive-brief` | **PARTIAL** | without_skill baseline 未生成 |
| `competitive-intelligence` | **PARTIAL** | without_skill baseline 未生成 |
| `github-reader` | **PARTIAL** | 3 eval，without_skill baseline 未生成 |
| `release-notes-generator` | **PARTIAL** | 3 eval，without_skill baseline 未生成 |

### Engineer Agent（8 skills）

| Skill | Latest result | 说明 |
| --- | --- | --- |
| `engineer-agent` | **PASS** | 4 eval，2026-07-05 fresh validation，覆盖前端 UI 路由和嵌套路径对齐 |
| `feature-implementor` | **PASS** | 13 eval，2026-07-05 fresh validation，含归档门禁 eval 012-013 |
| `codebase-analyzer` | **PARTIAL** | without_skill baseline 未生成 |
| `debugger` | **PARTIAL** | 4 eval 中 eval-001 PASS（2026-06-23）、eval-004 PASS（2026-06-25），另 2 eval without_skill baseline 未生成 |
| `delivery` | **PARTIAL** | without_skill baseline 未生成 |
| `project-bootstrap` | **PARTIAL** | without_skill baseline 未生成 |
| `test-writer` | **PARTIAL** | without_skill baseline 未生成 |
| `trd-gen` | **PARTIAL** | 4 eval 中 eval-003 PASS（2026-06-25 四级路径），其余 without_skill baseline 未生成 |

### QA Agent（5 skills）

| Skill | Latest result | 说明 |
| --- | --- | --- |
| `qa-agent` | **PASS** | 3 eval，2026-07-05 fresh validation，覆盖 E2E gate 和缺少计划的阻断场景 |
| `bug-analyzer` | **PASS** | 2 eval，2026-07-05 fresh validation |
| `exploratory-tester` | **PASS** | 2 eval，2026-07-05 fresh validation |
| `regression-suite` | **PASS** | 2 eval，2026-07-05 fresh validation |
| `spec-based-tester` | **PASS** | 2 eval，2026-07-05 fresh validation |

### DevOps Agent（5 skills）

| Skill | Latest result | 说明 |
| --- | --- | --- |
| `devops-agent` | **PASS** | 2026-07-05 fresh validation，CI 就绪路由场景 |
| `env-config-auditor` | **PASS** | 2026-06-25 四级路径覆盖更新 |
| `cicd-bootstrap` | **PARTIAL** | without_skill baseline 未生成 |
| `deployment-planner` | **PARTIAL** | 2 eval，without_skill baseline 未生成 |
| `incident-playbook-writer` | **PARTIAL** | without_skill baseline 未生成 |

### Designer Agent（3 skills）

| Skill | Latest result | 说明 |
| --- | --- | --- |
| `designer-agent` | **PASS** | 3 eval，2026-07-05 fresh validation，覆盖前端 UI 维护 handoff |
| `ui-ux-design` | **PARTIAL** | without_skill baseline 未生成 |
| `visual-design` | **PARTIAL** | without_skill baseline 未生成 |

### Security Agent（5 skills）

| Skill | Latest result | 说明 |
| --- | --- | --- |
| `security-agent` | **PASS** | 2026-07-05 fresh validation，auth release risk 路由场景 |
| `appsec-checklist` | **PARTIAL** | 4 eval 中 eval-004 PASS（2026-06-25 四级路径），其余 without_skill baseline 未生成 |
| `authz-reviewer` | **PARTIAL** | 3 eval，without_skill baseline 未生成 |
| `dependency-risk-auditor` | **PARTIAL** | 3 eval，without_skill baseline 未生成 |
| `privacy-surface-mapper` | **PARTIAL** | 3 eval，without_skill baseline 未生成 |

### 汇总统计

| 结论 | 数量 | Skills |
| --- | --- | --- |
| **PASS** | 15 | pm-agent, idea-to-spec, feature-catalog, roadmap-generator, engineer-agent, feature-implementor, qa-agent, bug-analyzer, exploratory-tester, regression-suite, spec-based-tester, devops-agent, env-config-auditor, designer-agent, security-agent |
| **PARTIAL** | 20 | changelog-generator, competitive-brief, competitive-intelligence, github-reader, release-notes-generator, codebase-analyzer, debugger, delivery, project-bootstrap, test-writer, trd-gen, cicd-bootstrap, deployment-planner, incident-playbook-writer, ui-ux-design, visual-design, appsec-checklist, authz-reviewer, dependency-risk-auditor, privacy-surface-mapper |
| **BLOCKED** | 0 | — |

PARTIAL 原因集中在 without_skill baseline 未生成（历史 eval 在 Fresh Sub-Agent 门禁收紧前执行），with-skill 产物和行为证据已存在；下一版本应对 PARTIAL skill 补跑 fresh Codex subagent validation。
