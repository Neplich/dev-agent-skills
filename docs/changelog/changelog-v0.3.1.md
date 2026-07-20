---
feature: release-changelog
version: 0.3.1
date: 2026-07-20
last_updated: 2026-07-20
---

# Changelog - v0.3.1

## [v0.3.1] - 2026-07-20

本版本将 `docs-agent` 从 v0.3.0 的 API-only MVP 演进为完整发布文档链：统一正式页面 frontmatter 契约，将站点写作内容资产化并提供确定性 `new:doc` 脚手架，把 `formal-docs-sync` 扩展到 API、database、design、ops、product 五类当前事实同步，新增站内 `release-notes-generator`，并以 `docs-audit` 双阶段版本审计和 `github-release-generator` 双时序门禁闭合从站内文档到 GitHub Release 的责任边界。同时修正 v0.3.0 对 `formal-docs-sync` 已验收范围的表述，保留其 API-only 历史事实。本版本覆盖 v0.3.0 发布提交 `6b5f555` 之后合并到 `main` 的全部变更（#123–#130）。

### Added

- **写作资产化与确定性脚手架**：`docs-site-bootstrap` 将 VitePress 静态输出迁入可复用资产，提供五类模板、`npm run new:doc`、dry-run、覆盖保护、页面与 change-map 原子写入及宿主测试契约。([#125](https://github.com/Neplich/dev-agent-skills/pull/125))
- **站内 Release Notes specialist**：新增 `docs-agent:release-notes-generator`，负责六类发布证据写作、统一 release frontmatter、正文确认、索引与 metadata 派生更新、宿主 docs checks，以及后续审计 handoff；tag 和 GitHub Release 仍不在其职责内。([#126](https://github.com/Neplich/dev-agent-skills/pull/126))
- **发布文档链集成 eval**：新增 AI Hub-shaped `eval-005-integration-release-chain`，覆盖共享 frontmatter、模板与脚手架、正式文档同步、站内 Release Notes、pre-tag / post-tag 审计及 GitHub Release handoff，并验证真实 tag 与 GitHub Release 零写入。([#130](https://github.com/Neplich/dev-agent-skills/pull/130))

### Changed

- **统一 frontmatter 契约**：`docs-agent` 建立七字段共享真源，bootstrap、sync 与 audit 使用同一生成和校验规则；页面缺少维护者确认版本时保持 `unverified`，不得提前盖章。([#124](https://github.com/Neplich/dev-agent-skills/pull/124))
- **五类正式文档同步**：`formal-docs-sync` 从 API-only 扩展为 API、database、design、ops、product 五类当前事实同步，并保持 Release Notes、审计、脚手架和 GitHub Release 的职责隔离。([#127](https://github.com/Neplich/dev-agent-skills/pull/127))
- **双阶段版本审计**：`docs-audit` 以独立的 `base_ref`、`target_ref` 和维护者确认版本执行 pre-tag / post-tag 审计，分别输出 `ready_for_tag` 与 `release_verified`，消除审计与 tag 的循环依赖。([#128](https://github.com/Neplich/dev-agent-skills/pull/128))
- **GitHub Release 双时序门禁**：PM Release 能力收敛为 `github-release-generator`，只消费已确认的站内 Release Notes、pre-tag 与 post-tag 审计证据；preview / draft 准备和最终 publish 分别执行独立当前批准及远端事实复查。([#129](https://github.com/Neplich/dev-agent-skills/pull/129))

### Fixed

- **v0.3.0 能力边界表述**：README、Docs Agent 说明和 v0.3.0 changelog 明确该版本实际验收的自动化范围仅为 API 文档，deployment / release 当时只执行证据检查、范围判断与 handoff，避免把后续五类同步能力写成既有事实。([#123](https://github.com/Neplich/dev-agent-skills/pull/123))

## Skill Eval 汇总（v0.3.1 发版前）

本节逐一核对当前仓库已提交的 durable `comparison.md`，按 skill 去重汇总最新结论。本发布 PR 只新增 changelog、更新根索引和版本字段，不修改 skill 协议或 eval fixture，因此不重复运行模型 eval。共 **39/39 cases PASS、190/190 with-skill assertions PASS**；集成 `eval-005` 单列，不重复计入 `docs-agent` router。

| Agent | Skill / eval | Durable comparison | 最新结论 |
| --- | --- | ---: | :---: |
| Docs | `docs-agent` router（eval-001–004） | 4 | 4/4 cases、14/14 assertions PASS |
| Docs | `docs-site-bootstrap` | 3 | 3/3 cases、12/12 assertions PASS |
| Docs | `formal-docs-sync` | 10 | 10/10 cases、42/42 assertions PASS |
| Docs | `docs-audit` | 13 | 13/13 cases、81/81 assertions PASS |
| Docs | `release-notes-generator` | 3 | 3/3 cases、11/11 assertions PASS |
| Product Manager | `github-release-generator` | 4 | 4/4 cases、18/18 assertions PASS |
| Product Manager | `pm-agent` router eval-14 | 1 | 1/1 case、4/4 assertions PASS |
| Integration | `docs-agent` eval-005 release chain | 1 | 1/1 case、8/8 assertions PASS |
| **合计** | **8 组 durable 结论** | **39** | **39/39 cases、190/190 with-skill assertions PASS** |

### Docs 四 skill 与站内 Release Notes

- `docs-agent` 的 4 个路由用例验证 formal sync、缺失入口依据、release audit 与站内 Release Notes 分流，全部保留入口上下文且不越权执行 specialist 协议。([#124](https://github.com/Neplich/dev-agent-skills/pull/124)、[#126](https://github.com/Neplich/dev-agent-skills/pull/126))
- `docs-site-bootstrap` 的 3 个用例验证 40 项 inventory 下的完整生成、重复执行 zero-diff 和冲突原子阻塞。([#125](https://github.com/Neplich/dev-agent-skills/pull/125))
- `formal-docs-sync` 的 10 个用例覆盖 API、回填规划、设计交付门禁、database / design、deployment ops、release product / ops 与 Release Notes 边界。([#127](https://github.com/Neplich/dev-agent-skills/pull/127))
- `docs-audit` 的 13 个用例覆盖事实三态、frontmatter、pre-tag / post-tag、目标树绑定、metadata 回滚与版本规范化边界。([#124](https://github.com/Neplich/dev-agent-skills/pull/124)、[#128](https://github.com/Neplich/dev-agent-skills/pull/128))
- `release-notes-generator` 的 3 个用例验证六类证据、确认前派生面零写入及 GitHub Release / tag 职责边界。([#126](https://github.com/Neplich/dev-agent-skills/pull/126))

### GitHub Release、PM 路由与全链集成

- `github-release-generator` 的 4 个用例验证缺少 ready handoff 时阻塞、发布顺序与双时序复查、已确认事实保真和站点 / tag 零写入；`pm-agent` router eval-14 验证站内 Release Notes 与 GitHub Release 的精确分流。([#129](https://github.com/Neplich/dev-agent-skills/pull/129))
- 集成 `eval-005` 以独立 judge 验证从 shared frontmatter、五类同步、站内 Release Notes 到 pre-tag / post-tag 审计和 `github-release-generator` handoff 的完整链路；with-skill 与 fresh without-skill baseline 均为 8/8 assertions PASS，本轮没有 assertion-level 增益，宿主和远端 tag、GitHub Release 均零写入。([#130](https://github.com/Neplich/dev-agent-skills/pull/130))
