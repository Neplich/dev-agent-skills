---
feature: release-changelog
version: 0.3.4
date: 2026-07-28
last_updated: 2026-07-28
---

# Changelog - v0.3.4

## [v0.3.4] - 2026-07-28

本版本集中完善 docs-agent 正式文档契约：API 与数据库、Product 与 Design、Ops 部署三分类的信息架构分层落地，文档站侧边栏升级为任意深度递归嵌套，并新增文档站部署完整性安全网（Docs → PM → DevOps 条件式 handoff）；同时修复实施计划归档门禁的 status 触发检测与双态审计 handoff 门禁对无文档站宿主失效的问题，将 docs-site 模板 VitePress 依赖精确固定到已验证版本；并补齐两批共 26 个薄 fixture / 证据债务 eval 的确认上下文与 fresh 成对复验。本版本覆盖 v0.3.3 之后合并到 `main` 的全部变更（#156、#157、#163、#164、#165、#166、#167、#168、#171、#174、#179、#180）。

### Added

- **文档站部署完整性安全网**：在既有 Safety-Net Closeout 中建立 Docs → PM → DevOps 条件式 handoff，统一 `integrated` / `partial` / `not_integrated` / `not_applicable` / `unknown` 五态判定与逐构建变体证据要求；Docs 只读识别和报告，commit、镜像发布与部署保持独立授权边界。([#163](https://github.com/Neplich/dev-agent-skills/pull/163))
- **API 与数据库文档信息架构**：完善 API 文档「功能域 → 子功能 → 接口叶子页」与 Database 文档「数据库 / schema → 数据域 → 关系总览 → 实体页」层级契约，关系页与实体页双向链接，并明确区分物理外键与逻辑引用。([#164](https://github.com/Neplich/dev-agent-skills/pull/164))
- **Product 与 Design 分层文档契约**：Product 建立「产品域 → 功能 / 子功能 → 用户任务 / 场景」层级，Design 建立「系统 → 领域 → 子系统 / 组件 → 流程与边界」层级，落实组件/流程双向链接、跨领域唯一权威页与 API / Database contract 引用边界。([#165](https://github.com/Neplich/dev-agent-skills/pull/165))
- **Ops 部署文档三分类契约**：Ops 部署正式文档拆分为 Development、Docker、Kubernetes/Helm 三类，统一入口 `docs/site/ops/deployment/`，新增共享 `environment-reference.md` 证据规则，要求交叉核对 `.env.example`、配置读取与 Compose/Helm 映射。([#166](https://github.com/Neplich/dev-agent-skills/pull/166))
- **文档站侧边栏任意深度递归嵌套**：侧边栏生成器从固定层级升级为基于树结构的递归构建，支撑 Product / Design 文档的多级子功能、子系统结构，非叶子节点可递归嵌套并生成独立 `index.md`。([#167](https://github.com/Neplich/dev-agent-skills/pull/167))

### Changed

- **跨角色薄 fixture eval 确认上下文**：为 11 个 specialist 的 17 个高风险薄 fixture eval 按各自当前 entry gate 补齐最小确认上下文（PM handoff、已确认文档链、真实部署样本、竞品资料等），全部经 fresh `with_skill` / `without_skill` 成对复验并更新 durable `comparison.md`。([#168](https://github.com/Neplich/dev-agent-skills/pull/168))
- **跨角色证据债务 eval 复现策略判定**：完成第二批 9 个证据债务 eval 的逐项分类与 fresh paired validation，不修改 specialist 行为与 assertions，仅更新 canonical `comparison.md`。([#171](https://github.com/Neplich/dev-agent-skills/pull/171))
- **发版流程说明**：明确每次 tag 发版后由 `pm-agent → github-release-generator` 自动创建 GitHub Release draft 交维护者审批，draft 发布仍需维护者显式批准；并明确双态审计 handoff 门禁不适用于本仓库自身发版。([764dc2f](https://github.com/Neplich/dev-agent-skills/commit/764dc2f)、[ca1535c](https://github.com/Neplich/dev-agent-skills/commit/ca1535c))

### Fixed

- **实施计划归档门禁 status 触发检测**：活跃 `IMPLEMENTATION_PLAN.md` 的 `status` 设为 repository contract 无条件必填字段，以 merge-base 上 active plan 的 `status: Implemented` 触发 `previous_plan_archive` 校验，保留 base ref 容错与同提交 closeout 归档例外。([#179](https://github.com/Neplich/dev-agent-skills/pull/179))
- **双态审计 handoff 门禁**：修复门禁对无文档站宿主不生效的问题。([#156](https://github.com/Neplich/dev-agent-skills/pull/156))
- **docs-site 模板 VitePress 依赖固定**：模板依赖从 caret 范围精确固定为已验证版本 `1.6.4`，避免上游 minor 漂移破坏脚手架；resolved URL、integrity 及其余依赖均无漂移。([#157](https://github.com/Neplich/dev-agent-skills/pull/157))
- **changelog-generator 版本标题 eval assertion**：修正 `eval-002-single-version-mode` 的版本标题期望，统一为既定的 `## [v{VERSION}] - YYYY-MM-DD` 格式约定，不修改 specialist 行为。([#174](https://github.com/Neplich/dev-agent-skills/pull/174))

## Skill Eval 汇总（v0.3.4 发版前）

本节按 marketplace 当前注册的 **40 个 skill** 逐一汇总最新结论。与 v0.3.3 不同，本次按各 skill `evals.json` 的 `workspace` 契约路径定位每份 durable `comparison.md`（同时覆盖 canonical `evals/workspace/` 与仍在使用的当前 workspace 路径），共核对 **185** 份当前结论：**176 PASS、9 PARTIAL**。份数较 v0.3.3（155 份）增长来自各 PR 新增的 eval 定义，以及 `idea-to-spec` 7 个既有 eval 本次补齐 fresh 结论后纳入汇总。

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
| Docs | `docs-agent` | 6 | 6 PASS |
| Docs | `docs-audit` | 14 | 14 PASS |
| Docs | `docs-site-bootstrap` | 4 | 4 PASS |
| Docs | `formal-docs-sync` | 14 | 14 PASS |
| Docs | `release-notes-generator` | 4 | 4 PASS |
| Engineer | `codebase-analyzer` | 3 | 3 PASS |
| Engineer | `debugger` | 5 | 5 PASS |
| Engineer | `delivery` | 1 | 1 PASS |
| Engineer | `engineer-agent` | 4 | 4 PASS |
| Engineer | `feature-implementor` | 17 | 15 PASS、2 PARTIAL |
| Engineer | `project-bootstrap` | 2 | 2 PASS |
| Engineer | `test-writer` | 2 | 2 PASS |
| Engineer | `trd-gen` | 5 | 5 PASS |
| Product Manager | `changelog-generator` | 3 | 1 PASS、2 PARTIAL |
| Product Manager | `competitive-brief` | 1 | 1 PASS |
| Product Manager | `competitive-intelligence` | 1 | 1 PASS |
| Product Manager | `feature-catalog` | 4 | 4 PASS |
| Product Manager | `github-reader` | 4 | 3 PASS、1 PARTIAL |
| Product Manager | `github-release-generator` | 6 | 6 PASS |
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
| **合计** | **40 个 marketplace skill 分组** | **185** | **176 PASS、9 PARTIAL** |

本版本直接涉及的复验结果为：`idea-to-spec` 全部 8 个 eval 经 fresh Codex subagent 成对复验（全新 `without_skill` baseline）**30/30 assertions PASS**，覆盖 PR #163 新增「Documentation Site Deployment Completeness」契约节后的行为确认；`docs-site-bootstrap`、`formal-docs-sync`、`docs-audit`、`feature-implementor`、`changelog-generator` 等 skill 的新增或受影响 eval 已在各自 PR（#157、#163–#168、#171、#174、#179）合并时完成 fresh 复验并更新 durable `comparison.md`。本次汇总由 `scripts/summarize_eval_results.py` 按 `evals.json` workspace 契约路径机械提取，不重跑其余 skill eval。表中 **9 个 PARTIAL** 沿用各 skill 既有 durable 结论，主要记录历史 comparison 的证据缺口，不是本版回归。
