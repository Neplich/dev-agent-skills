---
feature: release-changelog
version: 0.3.2
date: 2026-07-21
last_updated: 2026-07-21
---

# Changelog - v0.3.2

## [v0.3.2] - 2026-07-21

本版本建立 Security 确认结论回到 `pm-agent` 的统一升级安全网：当审查发现或整改复审确认改变正式文档事实、对外行为、运维事实或发版就绪状态时，由 PM 通过 issue 生命周期分类、分派、跟踪整改，并在 Security 复审确认后关闭；Security 保留自有过程报告，但不再直交 `docs-agent`、自行创建 issue 或修改正式文档。同时补齐 security-agent 的 PM handoff eval 场景，扩展 router 与四个 security specialist 的升级路径断言，并维护贡献指南、Docs Agent 文档和 durable comparison 的一致性。本版本覆盖 v0.3.1（PR #135）之后合并到 `main` 的全部变更（#136、#137、#138、#139、#142、#144）；其中 Security 升级规则以 #144 的最终状态为准。

### Added

- **Security→PM 结论升级安全网**：Security 确认结论改变正式文档事实、对外行为、运维事实或发版就绪状态时，回到 `pm-agent` 入口分类，由 PM 使用 `gh issue create` 建立 issue、通过正常 handoff packet 分派整改，并在 Security 复审确认后关闭；Security 不直交 `docs-agent`、不自行创建 issue、不修改正式文档，其自有 `docs/security/` 过程报告仍为必产证据。该安全网挂载到 `security-agent` router 与四个 specialist 共五个出口，Docs 的 `docs-agent` 与 `formal-docs-sync` 两道入口 gate 明确 Security 证据必须持有 PM packet；该最终规则取代并细化 #139 确立的 Security→Docs 直接交接，并关闭 [issue #141](https://github.com/Neplich/dev-agent-skills/issues/141)。([#139](https://github.com/Neplich/dev-agent-skills/pull/139)、[#144](https://github.com/Neplich/dev-agent-skills/pull/144))

### Changed

- **Security 升级路径 eval 覆盖**：`security-agent` eval-001 与五个 mapped specialist eval 增加 Security 结论升级路径断言，验证确认结论回交 `pm-agent`、不直交 Docs、不自行创建 issue 且不修改正式文档。([#144](https://github.com/Neplich/dev-agent-skills/pull/144))
- **贡献指南与 Docs Agent 文档一致性**：中英文贡献指南同步 Docs 确定性测试、手动 eval 入口和 workflow target；Docs Agent 补齐中文 README 与语言互链，并同步 dispatcher 计数、`docs-audit` 双阶段 description 及相关 metadata。([#136](https://github.com/Neplich/dev-agent-skills/pull/136)、[#137](https://github.com/Neplich/dev-agent-skills/pull/137))
- **docs-agent eval-003 durable 结论**：更新 release audit 路由用例的 fresh paired validation 结论，确认 `docs-audit` 扩展为 pre-tag audit 与 post-tag verification 后，router 仍保持正确分流和 specialist gate 边界。([#138](https://github.com/Neplich/dev-agent-skills/pull/138))

### Fixed

- **security-agent eval-001 PM handoff 场景**：补齐 PM handoff packet 与 `auth-model` PRD fixture，使 `collects_security_context` 从 PARTIAL 恢复为原有 5/5 assertions PASS，并关闭 [issue #140](https://github.com/Neplich/dev-agent-skills/issues/140)；叠加 #144 的升级路径断言后，当前 durable 结论为 6/6 assertions PASS。([#142](https://github.com/Neplich/dev-agent-skills/pull/142)、[#144](https://github.com/Neplich/dev-agent-skills/pull/144))

## Skill Eval 汇总（v0.3.2 发版前）

本节逐一核对当前仓库已提交的 durable `comparison.md`，按 skill 去重汇总最新结论；未在本版本修改的 skill 沿用其当前 durable 结论。共核对 **151** 份 durable comparison：**113 PASS、38 PARTIAL**。

| Agent | Skill（eval 范围） | Durable comparison 数 | 最新结论 |
| --- | --- | ---: | --- |
| Designer | `designer-agent` | 3 | 3 PASS |
| Designer | `ui-ux-design` | 3 | 1 PASS、2 PARTIAL |
| Designer | `visual-design` | 1 | 1 PARTIAL |
| DevOps | `cicd-bootstrap` | 2 | 1 PASS、1 PARTIAL |
| DevOps | `deployment-planner` | 3 | 1 PASS、2 PARTIAL |
| DevOps | `devops-agent` | 1 | 1 PASS |
| DevOps | `env-config-auditor` | 1 | 1 PASS |
| DevOps | `incident-playbook-writer` | 2 | 1 PASS、1 PARTIAL |
| Docs | `docs-agent`（router eval-001–004；integration eval-005） | 5 | router：4/4 PASS（14/14 assertions）；integration：1/1 PASS（8/8 with-skill assertions） |
| Docs | `docs-audit`（eval-001–013） | 13 | 13/13 PASS（81/81 assertions） |
| Docs | `docs-site-bootstrap`（eval-001–003） | 3 | 3/3 PASS（12/12 assertions） |
| Docs | `formal-docs-sync`（eval-001–010） | 10 | 10/10 PASS（42/42 assertions） |
| Docs | `release-notes-generator`（eval-001–003） | 3 | 3/3 PASS（11/11 assertions） |
| Engineer | `codebase-analyzer` | 3 | 1 PASS、2 PARTIAL |
| Engineer | `debugger` | 5 | 3 PASS、2 PARTIAL |
| Engineer | `delivery` | 1 | 1 PARTIAL |
| Engineer | `engineer-agent` | 4 | 4 PASS |
| Engineer | `feature-implementor` | 14 | 14 PASS |
| Engineer | `project-bootstrap` | 2 | 2 PARTIAL |
| Engineer | `test-writer` | 2 | 1 PASS、1 PARTIAL |
| Engineer | `trd-gen` | 5 | 2 PASS、3 PARTIAL |
| Product Manager | `changelog-generator` | 3 | 3 PARTIAL |
| Product Manager | `competitive-brief` | 1 | 1 PARTIAL |
| Product Manager | `competitive-intelligence` | 1 | 1 PARTIAL |
| Product Manager | `feature-catalog` | 4 | 4 PASS |
| Product Manager | `github-reader` | 4 | 1 PASS、3 PARTIAL |
| Product Manager | `github-release-generator`（eval-001–004） | 4 | 4/4 PASS（18/18 assertions） |
| Product Manager | `idea-to-spec` | 1 | 1 PASS |
| Product Manager | `pm-agent` router（eval-001–014） | 14 | 14/14 PASS（45/45 assertions） |
| QA | `bug-analyzer` | 3 | 3 PASS |
| QA | `exploratory-tester` | 3 | 3 PASS |
| QA | `qa-agent` | 3 | 3 PASS |
| QA | `regression-suite` | 3 | 3 PASS |
| QA | `spec-based-tester` | 3 | 3 PASS |
| Security | `security-agent` router（eval-001） | 1 | 1/1 PASS（6/6 assertions） |
| Security | `appsec-checklist`（eval-001–005） | 5 | eval-004/005：2 PASS（9/9 assertions）；eval-001–003：3 PARTIAL |
| Security | `authz-reviewer`（eval-001–004） | 4 | eval-004：1 PASS（4/4 assertions）；eval-001–003：3 PARTIAL |
| Security | `dependency-risk-auditor`（eval-001–004） | 4 | eval-004：1 PASS（4/4 assertions）；eval-001–003：3 PARTIAL |
| Security | `privacy-surface-mapper`（eval-001–004） | 4 | eval-004：1 PASS（4/4 assertions）；eval-001–003：3 PARTIAL |
| **合计** | **39 个 skill 分组** | **151** | **113 PASS、38 PARTIAL** |

本轮 `security` 与 `pm-agent` 共 **32 个 eval** 于 2026-07-21 完成全量 fresh 复验，`with_skill` 与 `without_skill` 均重新生成：20 个 eval 为 PASS；其余 12 个 PARTIAL 均来自四个 security specialist 的 eval-001–003 薄 fixture，workspace 缺少 PM handoff packet、已确认上下文或可审查代码，属于预存 fixture 缺口而非 skill 回归，后续由 [issue #143](https://github.com/Neplich/dev-agent-skills/issues/143) 跟进。表中另外 26 个 PARTIAL 沿用各 skill 既有 durable 结论，主要记录历史 comparison 未生成 fresh `without_skill` baseline 等证据缺口，并非本轮 Security→PM 契约复验结果。
