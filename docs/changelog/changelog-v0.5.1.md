---
feature: release-changelog
version: 0.5.1
date: 2026-08-14
last_updated: 2026-08-14
---

# Changelog - v0.5.1

## [v0.5.1] - 2026-08-14

本版本完成 #281 与 #282 入口触发与路由输出收敛：`pm-agent` 入口规则改为显式点名能力优先，未显式点名时按研发意图进入 PM；7 个 role router 删除强制展示路由过程的要求，路由输出收敛，既有 gate 与 handoff 契约不变。本版本覆盖 v0.5.0 之后合并到 `main` 的 1 个直接提交（无关联 PR）。

### Changed

- **pm-agent 入口触发规则重构（#281）**：`pm-agent` description 与入口规则改为「显式点名能力优先」——用户显式点名 `pm-agent`、role agent 或 skill 时优先使用该能力并继续其既有入口 gate；未显式点名时，产品或工程研发意图默认进入 `pm-agent`，普通非研发请求由当前助手直接处理；显式点名其他能力而未点名 `pm-agent` 时不再激活 `pm-agent`。（直接提交，无关联 PR）
- **7 个 role router 路由输出收敛（#282）**：删除各 router 强制展示路由过程的要求，路由输出收敛为按需呈现；入口凭据检查、下游 gate 与 handoff packet 契约不变。（直接提交，无关联 PR）
- **同步面更新**：`AGENTS.md`、README、`.codex/INSTALL.md`、marketplace 发现描述、确定性测试、fresh paired eval 与 `skills-lock.json` 随本次变更同步刷新。

## Skill Eval 汇总（v0.5.1 发版前）

本节按 marketplace 当前注册的 **39 个 skill** 汇总。其中 `manual-gen` 为 manual-only 评测（不保留 evals.json），因此纳入常规汇总的为 **38 个 skill、201 份 durable `comparison.md`**（较 v0.5.0 新增 pm-agent 1 条）。`uv run scripts/summarize_eval_results.py` 机械提取，最新结论：**137 PASS、48 PASS (partial coverage)、16 FAIL**。

**结论说明**：本版为 v0.5.0 baseline 之上的增量重跑结论；入口触发与路由输出变更涉及的 dispatcher routing eval 已完成 fresh paired 重跑，`engineer-agent` 由 2 PASS、1 partial、2 FAIL 改善为 3 PASS、2 partial，`docs-agent` 由 3 PASS、4 FAIL 改善为 4 PASS、3 FAIL，`pm-agent` 21 条为 11 PASS、8 partial、2 FAIL。

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
| Docs | `docs-agent` | 7 | 4 PASS、3 FAIL |
| Docs | `docs-audit` | 15 | 8 PASS、5 PASS (partial coverage)、2 FAIL |
| Docs | `docs-site-bootstrap` | 4 | 3 PASS、1 PASS (partial coverage) |
| Docs | `formal-docs-sync` | 15 | 7 PASS、2 PASS (partial coverage)、6 FAIL |
| Docs | `release-notes-gen` | 5 | 4 PASS、1 PASS (partial coverage) |
| Engineer | `codebase-analyzer` | 3 | 3 PASS |
| Engineer | `debugger` | 7 | 3 PASS、3 PASS (partial coverage)、1 FAIL |
| Engineer | `delivery` | 1 | 1 PASS (partial coverage) |
| Engineer | `engineer-agent` | 5 | 3 PASS、2 PASS (partial coverage) |
| Engineer | `feature-implementor` | 17 | 14 PASS、3 PASS (partial coverage) |
| Engineer | `test-writer` | 2 | 2 PASS |
| Engineer | `trd-gen` | 6 | 3 PASS、3 PASS (partial coverage) |
| Product Manager | `changelog-gen` | 3 | 3 PASS |
| Product Manager | `competitive-brief` | 2 | 2 PASS |
| Product Manager | `feature-catalog` | 4 | 1 PASS、2 PASS (partial coverage)、1 FAIL |
| Product Manager | `github-reader` | 5 | 5 PASS |
| Product Manager | `github-release-gen` | 8 | 6 PASS、2 PASS (partial coverage) |
| Product Manager | `idea-to-spec` | 9 | 6 PASS、2 PASS (partial coverage)、1 FAIL |
| Product Manager | `pm-agent` | 21 | 11 PASS、8 PASS (partial coverage)、2 FAIL |
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

- 发版清单：`.claude-plugin/marketplace.json` 的 `metadata.version` 更新为 `0.5.1`；7 个 `agents/*/.claude-plugin/plugin.json` 与 `.kimi-plugin/plugin.json` 的 `version` 同步为 `0.5.1`（由 `check_repository_contract.py` 强制校验）。
- 本版无 breaking 变更；入口触发规则变化仅影响默认路由行为，显式点名调用方式不变。
