---
feature: release-changelog
version: 0.5.0
date: 2026-08-13
last_updated: 2026-08-13
---

# Changelog - v0.5.0

## [v0.5.0] - 2026-08-13

本版本完成 #246 真实场景 eval 重设计落地（38 个常规 skill、200 份 durable `comparison.md` 收敛为只保留最新结论），并把评测与 skill 生命周期维护收敛为两个项目级流程（`skill-eval-runner`、`maintain-skills`）；入口侧 `pm-agent` 新增 Scope Guard 隔离项目外场景的自动触发，路由决策输出精简为默认一行；engineer 侧 `debugger` 新增只读诊断模式，实施计划归档路径契约完成迁移。本版本覆盖 v0.4.1 之后合并到 `main` 的全部变更（#256、#257、#269、#270、#271、#272、#273、#276 与 5 个直接提交）。

### Added

- **debugger 只读诊断模式**：`debugger` 拆分为 `diagnosis_only`（只读取证与诊断报告，不做任何修改）与 `repair` 两种模式；用户显式要求只读调查时进入 `diagnosis_only`，诊断之后的修复请求必须重新走 `repair` 入口并完成修复计划确认，只读授权不外溢；`engineer-agent` 路由与 README 同步，并新增 2 个 eval。（直接提交，无关联 PR）
- **Scope Guard 项目外场景隔离（#266）**：`pm-agent` 新增入口前置门禁，未启用 dev-agent-skills 的目录中的一般对话、本机操作与通用文件处理直接给出提示并停止，不再自动触发重型 PM 工作流；显式点名或已启用目录放行；同 PR 将 Kimi Quick Start 主命令从可变 `main` 固定到 release tag（#261）。([#272](https://github.com/Neplich/dev-agent-skills/pull/272))
- **pm-agent 路由决策输出精简（#265）**：默认只输出一行路由说明（`已路由到 <skill>：<一句话原因>`），完整结构化 YAML 仅按需输出（入口 blocked、跨角色 handoff、调试与 eval 场景）；hotfix 判定场景仍显式呈现 `change_tier` 与 `hotfix_disposition` 字面值，入口分类与下游门禁不变。([#273](https://github.com/Neplich/dev-agent-skills/pull/273))
- **maintain-skills 项目级维护流程（#262）**：新增 `.agents/skills/maintain-skills/`，把角色 skill 新增、修改、重命名的同步面（注册、路由、发现、Agent 文档、顶层入口、lockfile `computedHash`、共享契约副本、eval 委派）收敛为仓库级标准流程，`AGENTS.md` 不再复制第二份同步面清单。([#271](https://github.com/Neplich/dev-agent-skills/pull/271))

### Changed

- **eval 重设计落地（#246）**：38 个常规 skill、193 条 eval 引入真实用户场景、paired lane 隔离、fresh judge 与统一 durable evidence；共享 runtime、executor、checker 与角色 runner 收敛，批量执行最多 10 worker；193 份 `comparison.md` 简化为只保留最新结果，旧结论交由 git 历史追溯。([#256](https://github.com/Neplich/dev-agent-skills/pull/256))
- **统一项目级评测工作流**：新增仓库级 `skill-eval-runner`，eval 的设计、编写、静态校验、fresh paired 执行、并发、judge、durable `comparison.md`、运行期清理与失败分诊统一入口；`AGENTS.md` 的 eval 专章收敛为项目 skill 指针。([#257](https://github.com/Neplich/dev-agent-skills/pull/257))
- **实施计划归档路径契约迁移（#264）**：归档路径从 `docs/engineer/{feature_path}/implementation-plans/archive/` 迁移为 `docs/engineer/{feature_path}/archive/IMPLEMENTATION_PLAN-<scope>.md`，移除 `implementation-plans/` 冗余中间层；活跃计划入口 `IMPLEMENTATION_PLAN.md` 与归档文件命名规则不变。([#276](https://github.com/Neplich/dev-agent-skills/pull/276))
- **PM 协作拓扑对齐与中文依赖安全网（#259、#260）**：PM Agent README 下游角色从 2 个补全为 6 个；六份中文 `README_zh.md` 补齐与英文版等价的 `Collaboration Dependencies` 契约（目标插件不可用 → blocked → 不代行职责）。([#270](https://github.com/Neplich/dev-agent-skills/pull/270))
- **贡献指南与角色 README 的 eval 入口对齐（#258）**：`CONTRIBUTING` 手动 eval 入口改为项目级 `skill-eval-runner` 与 `uv run scripts/run_skill_eval.py`，补齐本地 pytest 清单与 7 角色的 Manual Evals 范围。([#269](https://github.com/Neplich/dev-agent-skills/pull/269))
- **约定合并后清理本地分支**：统一 PR 合并后的本地分支清理流程，明确 squash merge 下的安全强制删除条件。（直接提交，无关联 PR）

### Fixed

- **批量修复角色 skill 与评测偏差**：按四类归因修复七个角色的 skill 与 eval 偏差，刷新 193 条常规评测 comparison 并通过全部仓库 CI。（直接提交，无关联 PR）
- **修复角色评测契约并加速收敛**：修复 `docs-audit`、`formal-docs-sync` 与 `pm-agent` 的评测契约，加入最小模型调用的评测收敛策略。（直接提交，无关联 PR）
- **eval 身份架构 v2 与缺陷修复（#277）**：跨运行 freshness 切换为七个精确哈希的身份架构（目标 skill、eval 定义、metadata、fixture、执行协议、运行时协议、judge schema），一次性迁移原子写入 v2 身份并留审计报告；同时修复 trd-gen eval-006 FAIL 与 scope guard inventory 未登记缺陷。（直接提交，无关联 PR）

## Skill Eval 汇总（v0.5.0 发版前）

本节按 marketplace 当前注册的 **39 个 skill** 汇总。其中 `manual-gen` 为 manual-only 评测（不保留 evals.json），因此纳入常规汇总的为 **38 个 skill、200 份 durable `comparison.md`**（较 v0.4.1 新增 debugger 2 条、pm-agent 4 条、engineer-agent 1 条）。`uv run scripts/summarize_eval_results.py` 机械提取，最新结论：**133 PASS、49 PASS (partial coverage)、18 FAIL**。

**结论说明**：本版数字是 #246 重设计后的新 baseline，取代 v0.4.1 旧 eval 定义下的重跑结论；18 个 FAIL 为真实场景断言未满足，将按角色拆分跟进。

| Agent | Skill（eval 范围） | 纳入汇总的 durable comparison 数 | 最新结论 |
| --- | --- | ---: | --- |
| Designer | `designer-agent` | 3 | 3 PASS |
| Designer | `ui-ux-design` | 5 | 5 PASS |
| Designer | `visual-design` | 3 | 3 PASS |
| DevOps | `cicd-bootstrap` | 3 | 2 PASS、1 PASS (partial coverage) |
| DevOps | `deployment-planner` | 4 | 3 PASS、1 PASS (partial coverage) |
| DevOps | `devops-agent` | 2 | 2 PASS |
| DevOps | `env-config-auditor` | 4 | 3 PASS、1 PASS (partial coverage) |
| DevOps | `incident-playbook-writer` | 2 | 2 PASS |
| Docs | `docs-agent` | 7 | 3 PASS、4 FAIL |
| Docs | `docs-audit` | 15 | 8 PASS、5 PASS (partial coverage)、2 FAIL |
| Docs | `docs-site-bootstrap` | 4 | 3 PASS、1 PASS (partial coverage) |
| Docs | `formal-docs-sync` | 15 | 7 PASS、2 PASS (partial coverage)、6 FAIL |
| Docs | `release-notes-gen` | 5 | 4 PASS、1 PASS (partial coverage) |
| Engineer | `codebase-analyzer` | 3 | 3 PASS |
| Engineer | `debugger` | 7 | 3 PASS、3 PASS (partial coverage)、1 FAIL |
| Engineer | `delivery` | 1 | 1 PASS (partial coverage) |
| Engineer | `engineer-agent` | 5 | 2 PASS、1 PASS (partial coverage)、2 FAIL |
| Engineer | `feature-implementor` | 17 | 14 PASS、3 PASS (partial coverage) |
| Engineer | `test-writer` | 2 | 2 PASS |
| Engineer | `trd-gen` | 6 | 3 PASS、3 PASS (partial coverage) |
| Product Manager | `changelog-gen` | 3 | 3 PASS |
| Product Manager | `competitive-brief` | 2 | 2 PASS |
| Product Manager | `feature-catalog` | 4 | 1 PASS、2 PASS (partial coverage)、1 FAIL |
| Product Manager | `github-reader` | 5 | 5 PASS |
| Product Manager | `github-release-gen` | 8 | 6 PASS、2 PASS (partial coverage) |
| Product Manager | `idea-to-spec` | 9 | 6 PASS、2 PASS (partial coverage)、1 FAIL |
| Product Manager | `pm-agent` | 20 | 9 PASS、10 PASS (partial coverage)、1 FAIL |
| Product Manager | `roadmap-gen` | 3 | 3 PASS |
| QA | `bug-analyzer` | 3 | 2 PASS、1 PASS (partial coverage) |
| QA | `exploratory-tester` | 3 | 2 PASS、1 PASS (partial coverage) |
| QA | `qa-agent` | 3 | 3 PASS |
| QA | `regression-suite` | 3 | 2 PASS、1 PASS (partial coverage) |
| QA | `spec-based-tester` | 3 | 2 PASS、1 PASS (partial coverage) |
| Security | `appsec-checklist` | 5 | 3 PASS、2 PASS (partial coverage) |
| Security | `authz-reviewer` | 4 | 3 PASS、1 PASS (partial coverage) |
| Security | `dependency-risk-auditor` | 4 | 3 PASS、1 PASS (partial coverage) |
| Security | `privacy-surface-mapper` | 4 | 3 PASS、1 PASS (partial coverage) |
| Security | `security-agent` | 1 | 1 PASS (partial coverage) |

## 发布说明

- 发版清单：`.claude-plugin/marketplace.json` 的 `metadata.version` 更新为 `0.5.0`；7 个 `agents/*/.claude-plugin/plugin.json` 与 `.kimi-plugin/plugin.json` 的 `version` 同步为 `0.5.0`（由 `check_repository_contract.py` 强制校验）。
- 本版无用户命令 breaking 变更；#276 的实施计划归档路径迁移影响 `feature-implementor` 归档契约，下游按新路径 `docs/engineer/{feature_path}/archive/` 消费。
- 本版 eval 汇总结论为 #246 重设计后的新 baseline（38 skill / 200 comparison），v0.4.1 旧定义下的重跑结论作废。
