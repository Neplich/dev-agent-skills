---
feature: release-changelog
version: 0.4.1
date: 2026-08-07
last_updated: 2026-08-07
---

# Changelog - v0.4.1

## [v0.4.1] - 2026-08-07

本版本完成 2026 年 8 月批次的 eval 治理与文档系能力收束：修复 187 个 eval 的 prompt/fixture 泄漏（issue #234）并完成全角色 fresh 重跑（docs 批次 46 个 + 剩余 145 个），重跑暴露旧 eval 定义代表性不足，issue #246 已立项以真实用户场景重设计全部 skill eval；新增 manual-gen skill 与 manual 文档类型（#226）、文档站侧栏 nav_order 排序机制（#231）、API 文档默认收紧为 internal、formal-docs-sync 扁平层级 drift 检测（#225），并将 4 个生成类 skill 后缀统一为 `-gen`（#230，breaking）。本版本覆盖 v0.4.0 之后合并到 `main` 的全部变更（#224、#227、#229、#232、#236、#237、#240、#241、#242、#243、#238 批次与全角色重跑）。

### Added

- **manual-gen skill 与 manual 文档类型**：docs-agent 新增第 5 个 specialist `manual-gen`，基于真实运行界面截图为维护者确认的有限范围生成或更新站内图文用户操作手册；`doc_type` 枚举新增 `manual`（权威定义与 docs-audit 副本、宿主 `pages.mjs`/`sidebar.mjs`/`scaffold-doc.mjs` 五处同步），并新增 manual 模板。([#232](https://github.com/Neplich/dev-agent-skills/pull/232))
- **文档站侧栏 nav_order 排序机制**：section 内排序优先按 frontmatter `nav_order`（非负整数升序），缺省或相等时回退路径 slug 字典序；`frontmatter-contract.md` 新增 Optional Fields 节定义 `nav_order`，`formal-docs-sync` 补充生成/迁移时写入 `nav_order` 的规则。([#242](https://github.com/Neplich/dev-agent-skills/pull/242))

### Changed

- **生成类 skill 后缀统一为 `-gen`（breaking）**：`changelog-generator` → `changelog-gen`、`github-release-generator` → `github-release-gen`、`roadmap-generator` → `roadmap-gen`（product_manager）、`release-notes-generator` → `release-notes-gen`（docs）。marketplace 注册名即用户 slash 命令名，旧命令失效；同步面覆盖目录与 frontmatter name、marketplace.json、skills-lock.json（10 个 computedHash 刷新）、router SKILL.md、AGENTS.md 与 README、PRD/TRD。([#241](https://github.com/Neplich/dev-agent-skills/pull/241))
- **manual-gen 调整为 manual-only 评测**：该 skill 依赖用户真实已登录运行环境、对应源码仓库、实际界面状态与用户对可用性的判断，常规合成 fixture 与 with/without lane 无法提供可信结论；不再保留 evals.json，改为在 `agents/docs/test/manual-gen/comparison.md` 维护真实使用结论。([#243](https://github.com/Neplich/dev-agent-skills/pull/243) 及全角色重跑提交)
- **迭代指令补正文收束规则**：`idea-to-spec/_internal/_shared/gen-conventions.md` 的 Consolidate 条款提升为生成与迭代共用——正文只描述当前目标状态，被替换/废弃方案直接删除或重写、不保留状态标注，删除必须经 changelog 与 git history 留痕，消除事实型文档迭代时的设计债务累积。([#240](https://github.com/Neplich/dev-agent-skills/pull/240))
- **精简 AGENTS.md 仓库指导**：压缩膨胀到 322 行的仓库指导，合并 8 处重复规则（版本规则、文档组织、PM 入口默认等），净减 48 行。([#236](https://github.com/Neplich/dev-agent-skills/pull/236))
- **全角色 eval 重跑结果与评测治理**：完成 #238 剩余 145 个 skill eval 的 fresh 重跑结果更新（docs 批次 46 个见 #238），补充真实用户场景与 lane 隔离治理。([#238](https://github.com/Neplich/dev-agent-skills/pull/238) 与全角色重跑提交)

### Fixed

- **修复 187 个 eval 的 prompt/fixture 泄漏（issue #234）**：187/197 个 eval 向 baseline 泄漏 skill 规则失去判别力；删除 179 个 `eval_metadata.json` 的 `skill_availability_goal` 字段，113 个 eval 的 prompt 改写为自然用户表述（协议名/门禁/产物清单/脚手架词 → 自然目标与授权），3 个 manual-gen 答案型脚本改写为任务规格；194 个受影响 comparison 标记 `Overall result: BLOCKED` 并保留历史结论待重跑。([#237](https://github.com/Neplich/dev-agent-skills/pull/237))
- **manual-gen 被测平台改为执行前维护者确认注入**：三个正向 eval 不再写死外部站点 `mermaid.live`，每轮执行前先向维护者确认平台名与平台在本地代码中的 pwd，以确认值作为环境事实注入，平台位于宿主仓库内时写入路径可走完；外部站点场景如实记录 PARTIAL。([#243](https://github.com/Neplich/dev-agent-skills/pull/243))
- **API 文档默认收紧为 internal**：`docs-site-bootstrap` 内置 `docs/site/api/index.md` 默认 `visibility` 从 `both` 收紧为 `internal`，公开首页移除 API 入口链接；`formal-docs-sync` API 类型模块补充显式规则（新建或同步的 API 页面默认 `internal`，仅确认范围明确授权外部访问时才用 `public`/`both`）。([#224](https://github.com/Neplich/dev-agent-skills/pull/224))
- **formal-docs-sync 为已有扁平文档补上分层迁移触发机制**：八步流程 Step 4 候选范围确认前，对每个已加载的嵌套层级 type module 执行扁平层级 drift 检测（类型根下 ≥2 个非 `index.md` 页面且其中 ≥2 个能被已确认证据支持时触发迁移），历史扁平结构不再永久保留。([#227](https://github.com/Neplich/dev-agent-skills/pull/227))
- **清理 change-map header 的废弃 doc_type 与空 related_code**：19 个 eval fixture 的 `doc_type: standard` → `design`（对齐 `frontmatter-contract.md` 合法枚举）、11 处 `related_code: []` → `[docs/site]`（对齐全类型 `related_code` 非空契约）。([#229](https://github.com/Neplich/dev-agent-skills/pull/229))

## Skill Eval 汇总（v0.4.1 发版前）

本节按 marketplace 当前注册的 **39 个 skill** 汇总。其中 `manual-gen` 为 manual-only 评测（不保留 evals.json），因此纳入常规汇总的为 **38 个 skill、193 份 durable `comparison.md`**。`uv run scripts/summarize_eval_results.py` 机械提取，最新结论：**71 PASS、24 PASS (partial coverage)、92 FAIL、6 BLOCKED**。

**结论说明（重要）**：本版数字是 #237 泄漏修复后、**旧 eval 定义**下的全角色 fresh 重跑执行事实（2026-08-07 凌晨执行）。重跑暴露旧 eval 定义本身代表性不足——issue #246 审计判定 **172/193（89.1%）的 eval 需重写或至少人工复核**，已立项「以真实用户场景重设计全部 skill eval 并统一 lane 隔离」，取代「先重跑旧 eval」的前提。因此当前 FAIL/BLOCKED 反映的是旧定义下断言未满足，**不代表 skill 真实可用性**；待 #246 重设计完成后重生成 baseline 与 comparison，本版结论届时作废。

| Agent | Skill（eval 范围） | 纳入汇总的 durable comparison 数 | 最新结论 |
| --- | --- | ---: | --- |
| Designer | `designer-agent` | 3 | 3 FAIL |
| Designer | `ui-ux-design` | 5 | 2 PASS、1 PASS (partial coverage)、2 FAIL |
| Designer | `visual-design` | 3 | 2 PASS、1 FAIL |
| DevOps | `cicd-bootstrap` | 3 | 1 PASS、1 PASS (partial coverage)、1 FAIL |
| DevOps | `deployment-planner` | 4 | 2 PASS、2 FAIL |
| DevOps | `devops-agent` | 2 | 1 PASS、1 FAIL |
| DevOps | `env-config-auditor` | 4 | 2 PASS、1 PASS (partial coverage)、1 FAIL |
| DevOps | `incident-playbook-writer` | 2 | 2 FAIL |
| Docs | `docs-agent` | 7 | 1 PASS、5 FAIL、1 BLOCKED |
| Docs | `docs-audit` | 15 | 7 PASS、6 FAIL、2 BLOCKED |
| Docs | `docs-site-bootstrap` | 4 | 1 PASS、2 FAIL、1 BLOCKED |
| Docs | `formal-docs-sync` | 15 | 5 PASS、8 FAIL、2 BLOCKED |
| Docs | `release-notes-gen` | 5 | 2 PASS、3 FAIL |
| Engineer | `codebase-analyzer` | 3 | 2 PASS、1 FAIL |
| Engineer | `debugger` | 5 | 1 PASS、1 PASS (partial coverage)、3 FAIL |
| Engineer | `delivery` | 1 | 1 FAIL |
| Engineer | `engineer-agent` | 4 | 4 FAIL |
| Engineer | `feature-implementor` | 17 | 6 PASS、11 FAIL |
| Engineer | `test-writer` | 2 | 2 PASS |
| Engineer | `trd-gen` | 6 | 2 PASS、1 PASS (partial coverage)、3 FAIL |
| Product Manager | `changelog-gen` | 3 | 1 PASS、2 PASS (partial coverage) |
| Product Manager | `competitive-brief` | 2 | 2 PASS |
| Product Manager | `feature-catalog` | 4 | 2 PASS、2 FAIL |
| Product Manager | `github-reader` | 5 | 1 PASS、3 PASS (partial coverage)、1 FAIL |
| Product Manager | `github-release-gen` | 8 | 3 PASS、2 PASS (partial coverage)、3 FAIL |
| Product Manager | `idea-to-spec` | 9 | 5 PASS、4 FAIL |
| Product Manager | `pm-agent` | 16 | 7 PASS、1 PASS (partial coverage)、8 FAIL |
| Product Manager | `roadmap-gen` | 3 | 3 PASS (partial coverage) |
| QA | `bug-analyzer` | 3 | 1 PASS、1 PASS (partial coverage)、1 FAIL |
| QA | `exploratory-tester` | 3 | 2 PASS、1 PASS (partial coverage) |
| QA | `qa-agent` | 3 | 3 FAIL |
| QA | `regression-suite` | 3 | 1 PASS、2 FAIL |
| QA | `spec-based-tester` | 3 | 1 PASS、2 FAIL |
| Security | `appsec-checklist` | 5 | 2 PASS、1 PASS (partial coverage)、2 FAIL |
| Security | `authz-reviewer` | 4 | 3 PASS (partial coverage)、1 FAIL |
| Security | `dependency-risk-auditor` | 4 | 2 PASS、1 PASS (partial coverage)、1 FAIL |
| Security | `privacy-surface-mapper` | 4 | 2 PASS、1 PASS (partial coverage)、1 FAIL |
| Security | `security-agent` | 1 | 1 FAIL |

## 发布说明

- 发版清单：`.claude-plugin/marketplace.json` 的 `metadata.version` 已更新为 `0.4.1`；7 个 `agents/*/.claude-plugin/plugin.json` 与 `.kimi-plugin/plugin.json` 的 `version` 同步为 `0.4.1`（由 `check_repository_contract.py` 强制校验）。
- 用户命令 breaking：#241 将 4 个生成类 skill 后缀统一为 `-gen`，旧命令 `/pm-agent:changelog-generator`、`/pm-agent:github-release-generator`、`/pm-agent:roadmap-generator`、`/docs-agent:release-notes-generator` 已失效，请改用新命令。
- 本版包含 #238 批次与全角色 fresh 重跑（旧 eval 定义下），未包含 #246 重设计后的新 baseline；受影响 skill 的 durable comparison 已在本版 PR 中更新为旧定义重跑结论。
