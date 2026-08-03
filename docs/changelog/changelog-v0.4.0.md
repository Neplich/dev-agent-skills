---
feature: release-changelog
version: 0.4.0
date: 2026-08-04
last_updated: 2026-08-04
---

# Changelog - v0.4.0

## [v0.4.0] - 2026-08-04

本版本完成 skill 能力审查（issue #188）的实测收敛与 marketplace 正向分支 eval 覆盖（issue #220），并落地 2026 年 7-8 月批次的结构性重构：移除 project-bootstrap 与 BRD 生成链、删除三个 skill 中被模型通用能力磨平的冗余段落、新增 Kimi Code 原生安装支持与多级 feature_path 机制、收紧 GitHub Release 标题与升级说明门禁。全部 10 个 eval BLOCKED 挂账消解，189 份 durable comparison 中 178 PASS、8 PASS (partial coverage)、3 PARTIAL、0 BLOCKED。本版本覆盖 v0.3.5 之后合并到 `main` 的全部变更（#188、#190、#192、#196、#197、#198、#199-#213、#217、#219、#220、#221、#222）。

### Removed

- **project-bootstrap skill（D-1 决策）**：固定五目录模板不再适配 Go/Rust 等项目，AI 基于 PRD/TRD 与技术选型的内化能力已能搭建合适骨架，整体移除该 skill。([#205](https://github.com/Neplich/dev-agent-skills/pull/205))
- **BRD 生成链及下游 BRD 契约**：移除从未使用的 BRD 生成链与下游契约引用。([#214](https://github.com/Neplich/dev-agent-skills/pull/214))
- **competitive-intelligence skill**：L1 内容缺陷修正后整体移除（失效 skill 引用、缺失 handoff 目标等）。([#199](https://github.com/Neplich/dev-agent-skills/pull/199))
- **skill 能力审查 A 维冗余段落（issue #188）**：基于 fresh with/without 双侧实测确认磨平后，删除 codebase-analyzer 三张速查表、competitive-brief Analysis Frameworks 节（169 行）与 debugger 根因表；github-reader bot 枚举名单为部分磨平，保留待复测。删除后 paired 回归 14/14 PASS 无回归。([#222](https://github.com/Neplich/dev-agent-skills/pull/222))

### Added

- **Kimi Code CLI 插件原生安装**：新增 `.kimi-plugin/plugin.json` 与 Kimi Code 安装支持，GitHub Release 升级说明新增 Kimi 小节。([#216](https://github.com/Neplich/dev-agent-skills/pull/216))
- **PRD/TRD 多级 feature_path 自主拆分与结构梳理机制**：feature_path 支持多级 lower kebab-case 路径段，idea-to-spec 可自主拆分并梳理文档功能树。([#218](https://github.com/Neplich/dev-agent-skills/pull/218))
- **marketplace 正向分支 eval 覆盖（issue #220）**：github-release-generator 新增 eval-007（当前 tag 能力齐全）与 eval-008（历史 tag 能力不完整），覆盖标题强格式、三小节升级说明、plugin 列表推导与条件省略，fresh 双侧验证 Behavior PASS / Coverage FULL。([#221](https://github.com/Neplich/dev-agent-skills/pull/221))
- **Codex 与 Kimi Code 双宿主安装指引**：补充两宿主的安装文档与指引。([#217](https://github.com/Neplich/dev-agent-skills/pull/217))
- **competitive-brief Battlecard Mode**：pm-agent 以 `battlecard` 信号路由时直接产出单页 battlecard，并新增 eval-002 覆盖（fresh 验证 Behavior PASS / Coverage FULL）。([#222](https://github.com/Neplich/dev-agent-skills/pull/222))

### Changed

- **deployment-planner 目标矩阵驱动按需生成**：从无条件生成 local+docker+helm 改为按目标矩阵只生成明确需要的 target，三套结构降为示例。([#203](https://github.com/Neplich/dev-agent-skills/pull/203))
- **debugger 接入 change_tier 并合并修复确认**：根因分析与修复计划合并为一次呈现、一次确认，接入变更分级契约。([#202](https://github.com/Neplich/dev-agent-skills/pull/202))
- **QA 输出路径与 qa-agent router 收敛**：非 E2E fallback 不再写入日期子目录，输出路径与 router 行为对齐。([#200](https://github.com/Neplich/dev-agent-skills/pull/200))
- **L2-3 模板固化移除与 L2-4 router 单写收敛**：模板即产物模式统一改造，router 路由映射单写收敛。([#204](https://github.com/Neplich/dev-agent-skills/pull/204))
- **GitHub Release 标题与升级说明质量门禁（issue #190）**：标题强制 `vX.Y.Z - {主题概述}` 强格式，升级说明固定结构（简述句、Claude/Codex/Kimi 三小节、收尾句）；无固定版本安装路径时不承诺同步该 tag 能力。([#219](https://github.com/Neplich/dev-agent-skills/pull/219))
- **spec-based-tester 报告模板接入 preflight 基线与 blocked owner**。([#213](https://github.com/Neplich/dev-agent-skills/pull/213))
- **L1 事实缺陷修正**：env-config-auditor polyglot 漏扫、cicd-bootstrap 平台误判、失效 skill 引用、test-writer 冲突指令与路径漂移等 9 处修复。([#199](https://github.com/Neplich/dev-agent-skills/pull/199))

### Fixed

- **docs 系 4 个 eval BLOCKED 消解（issue #188）**：docs-audit eval-004/008/009 与 docs-agent eval-004 完成 fresh re-baseline（Behavior PASS / Coverage FULL），配合 #219 解封的 6 个 github-release-generator eval，10 个 BLOCKED 挂账全部消解。([#222](https://github.com/Neplich/dev-agent-skills/pull/222))
- **Release Notes 产物路径与角色归属旧契约残留清理**。([#212](https://github.com/Neplich/dev-agent-skills/pull/212))
- **DevOps PRD 与 README 同步按需产物行为**。([#211](https://github.com/Neplich/dev-agent-skills/pull/211))
- **CONTRIBUTING pytest 清单与 CI 对齐**。([#210](https://github.com/Neplich/dev-agent-skills/pull/210))

## Skill Eval 汇总（v0.4.0 发版前）

本节按 marketplace 当前注册的 **38 个 skill** 逐一汇总最新结论。`uv run scripts/summarize_eval_results.py` 按各 skill `evals.json` 的 workspace 契约路径机械提取，共核对 **189** 份 durable `comparison.md`：**178 PASS、8 PASS (partial coverage)、3 PARTIAL、0 BLOCKED**。

| Agent | Skill（eval 范围） | 纳入汇总的 durable comparison 数 | 最新结论 |
| --- | --- | ---: | --- |
| Designer | `designer-agent` | 3 | 3 PASS |
| Designer | `ui-ux-design` | 5 | 5 PASS |
| Designer | `visual-design` | 3 | 3 PASS |
| DevOps | `cicd-bootstrap` | 3 | 3 PASS |
| DevOps | `deployment-planner` | 4 | 4 PASS |
| DevOps | `devops-agent` | 2 | 2 PASS |
| DevOps | `env-config-auditor` | 4 | 3 PASS、1 PARTIAL |
| DevOps | `incident-playbook-writer` | 2 | 2 PASS |
| Docs | `docs-agent` | 6 | 6 PASS |
| Docs | `docs-audit` | 14 | 14 PASS |
| Docs | `docs-site-bootstrap` | 4 | 4 PASS |
| Docs | `formal-docs-sync` | 14 | 14 PASS |
| Docs | `release-notes-generator` | 5 | 5 PASS |
| Engineer | `codebase-analyzer` | 3 | 3 PASS |
| Engineer | `debugger` | 5 | 4 PASS、1 PASS (partial coverage) |
| Engineer | `delivery` | 1 | 1 PASS |
| Engineer | `engineer-agent` | 4 | 4 PASS |
| Engineer | `feature-implementor` | 17 | 15 PASS、2 PARTIAL |
| Engineer | `test-writer` | 2 | 2 PASS |
| Engineer | `trd-gen` | 5 | 5 PASS |
| Product Manager | `changelog-generator` | 3 | 1 PASS、2 PASS (partial coverage) |
| Product Manager | `competitive-brief` | 2 | 2 PASS |
| Product Manager | `feature-catalog` | 4 | 4 PASS |
| Product Manager | `github-reader` | 5 | 4 PASS、1 PASS (partial coverage) |
| Product Manager | `github-release-generator` | 8 | 7 PASS、1 PASS (partial coverage) |
| Product Manager | `idea-to-spec` | 9 | 9 PASS |
| Product Manager | `pm-agent` | 16 | 16 PASS |
| Product Manager | `roadmap-generator` | 3 | 2 PASS、1 PASS (partial coverage) |
| QA | `bug-analyzer` | 3 | 3 PASS |
| QA | `exploratory-tester` | 3 | 3 PASS |
| QA | `qa-agent` | 3 | 3 PASS |
| QA | `regression-suite` | 3 | 3 PASS |
| QA | `spec-based-tester` | 3 | 1 PASS、2 PASS (partial coverage) |
| Security | `appsec-checklist` | 5 | 5 PASS |
| Security | `authz-reviewer` | 4 | 4 PASS |
| Security | `dependency-risk-auditor` | 4 | 4 PASS |
| Security | `privacy-surface-mapper` | 4 | 4 PASS |
| Security | `security-agent` | 1 | 1 PASS |

## 发布说明

- 发版清单：`.claude-plugin/marketplace.json` 的 `metadata.version` 已更新为 `0.4.0`；7 个 `agents/*/.claude-plugin/plugin.json` 与 `.kimi-plugin/plugin.json` 的 `version` 同步为 `0.4.0`（由 `check_repository_contract.py` 强制校验）。
- 本版本不包含模型 eval transcript 重跑；受影响 skill 的 durable comparison 已在本版 PR 中更新。
