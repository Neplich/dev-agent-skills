---
feature: release-changelog
version: 0.3.0
date: 2026-07-16
last_updated: 2026-07-16
---

# Changelog - v0.3.0

## [v0.3.0] - 2026-07-16

本版本完整落地第 7 个角色 `docs-agent`，为宿主仓库提供正式文档站点初始化、功能同步、存量回填与发版审计能力；同时让 6 个既有 Agent 以统一契约消费正式文档，并将功能级设计文档同步收口到实现与测试完成后的交付链最后一步。该版本覆盖 v0.2.3 之后合并到 `main` 的全部变更（#108、#109、#110、#111、#113）。

### Added

- **第 7 个角色 `docs-agent`**：新增 router 与 3 个 specialist，形成 4-skill 终态。`docs-site-bootstrap` 以显式 opt-in、幂等和冲突门禁生成公开站点与内部站点骨架；`formal-docs-sync` 支持按变更影响域同步正式文档，并可按 feature catalog 或 API surface 分批回填存量项目；`docs-audit` 在发版前核对文档与代码事实，输出 verified / stale / mismatch 三态审计结论，存在 stale 或 mismatch 时阻止发布。([#108](https://github.com/Neplich/dev-agent-skills/pull/108)、[#110](https://github.com/Neplich/dev-agent-skills/pull/110)、[#111](https://github.com/Neplich/dev-agent-skills/pull/111))
- **正式文档消费契约**：新增共享 `consumption-contract.md`，覆盖 Product Manager、Engineer、QA、DevOps、Designer、Security 6 个既有 Agent 的 22 个 specialist；其中 21 个接入通用指针，`debugger` 增加 expected-behavior 安全规则，`release-notes-generator` 增加站点发布说明输出规则。契约要求以 change-map 定位文档、以代码和测试作为事实源，并结构化报告分歧。([#109](https://github.com/Neplich/dev-agent-skills/pull/109))
- **PM 入口 Docs 路由**：`pm-agent` 与共享 skill map 增加正式文档 bootstrap、sync/backfill、audit 的分类与 handoff，Docs Agent 纳入 PM-first 协作链。([#110](https://github.com/Neplich/dev-agent-skills/pull/110)、[#111](https://github.com/Neplich/dev-agent-skills/pull/111))

### Changed

- **设计文档交付链收口门禁**：功能交付模式下，`docs/site/design/**` 只在 PRD、TRD、已确认实施计划、实现范围和计划内测试证据全部对齐后进入候选范围确认；阻塞场景保持设计正文与 change-map 原子性零变化，避免正式文档提前描述尚未成立的未来状态。([#113](https://github.com/Neplich/dev-agent-skills/pull/113))
- **`trd-gen` 输出增强**：schema 新增可选 `related_code` 字段，可在有可靠代码证据时记录相关实现路径；该字段不改变既有 TRD 门禁。([#110](https://github.com/Neplich/dev-agent-skills/pull/110))

## Skill Eval 汇总（v0.3.0 发版前）

本节按本次变更涉及的 skill 汇总 durable `comparison.md` 的最新结论。全部结论均来自对应 PR 执行的 fresh Codex subagent validation；本次发版未修改 skill 执行协议或 eval fixture，因此复用已提交的最新结果，不重复运行模型 eval。

### WS1：既有 Agent 正式文档消费回归（22/22 PASS）

| Agent | Skill | 最新结论 |
| --- | --- | :---: |
| Product Manager | `feature-catalog`、`github-reader`、`idea-to-spec`、`release-notes-generator` | 4/4 PASS |
| Engineer | `codebase-analyzer`、`debugger`、`feature-implementor`、`test-writer`、`trd-gen` | 5/5 PASS |
| QA | `bug-analyzer`、`exploratory-tester`、`regression-suite`、`spec-based-tester` | 4/4 PASS |
| DevOps | `cicd-bootstrap`、`deployment-planner`、`env-config-auditor`、`incident-playbook-writer` | 4/4 PASS |
| Designer | `ui-ux-design` | 1/1 PASS |
| Security | `appsec-checklist`、`authz-reviewer`、`dependency-risk-auditor`、`privacy-surface-mapper` | 4/4 PASS |
| **合计** | **22 个 specialist eval** | **22/22 PASS** |

各 comparison 均验证了 change-map 定位、代码/测试事实核证、文档分歧处理与角色门禁；`debugger` 和 `release-notes-generator` 的专属规则也分别通过对应 eval。([#109](https://github.com/Neplich/dev-agent-skills/pull/109))

### WS2：Docs Agent 骨架、bootstrap 与 sync（8/8 PASS）

| Skill | Eval 范围 | 最新结论 |
| --- | --- | :---: |
| `docs-agent` | sync 分流、缺少入口凭据、WS2 审计请求门禁 | 3/3 PASS |
| `docs-site-bootstrap` | 空仓库生成、重复执行幂等、冲突阻塞 | 3/3 PASS |
| `formal-docs-sync` | 功能 API 同步、存量回填分批计划 | 2/2 PASS |
| **合计** | **8 个 eval** | **8/8 PASS** |

WS2 的 `docs-agent` 审计门禁用例在 WS3 启用 `docs-audit` 后更新为正式分流用例，并再次通过 fresh validation。([#110](https://github.com/Neplich/dev-agent-skills/pull/110)、[#111](https://github.com/Neplich/dev-agent-skills/pull/111))

### WS3：发版审计门禁与 4-skill 终态（7/7 PASS）

| Skill | Eval 范围 | 最新结论 |
| --- | --- | :---: |
| `docs-agent` | release audit 分流 | 1/1 PASS |
| `docs-audit` | mismatch、stale、纯重构 verified、全 verified 盖章、纯文档错误、无版本锚回退 | 6/6 PASS |
| **合计** | **7 个 eval** | **7/7 PASS** |

全部审计 comparison 均正确区分 verified / stale / mismatch；阻塞结论不盖章，全部 verified 后才允许统一盖章并建议继续发布。([#111](https://github.com/Neplich/dev-agent-skills/pull/111))

### 设计文档交付链收口门禁（4/4 PASS）

| Skill | Eval 范围 | 最新结论 |
| --- | --- | :---: |
| `formal-docs-sync` | 范围未完成、测试失败、证据路径不一致、全部证据通过 | 4/4 PASS |

三个反向用例均在设计正文与 design change-map 零变化的前提下原子阻塞；正向用例在六项完成态证据通过后停在维护者候选范围确认，未越权写入。([#113](https://github.com/Neplich/dev-agent-skills/pull/113))
