---
feature: release-changelog
version: 0.3.3
date: 2026-07-22
last_updated: 2026-07-22
---

# Changelog - v0.3.3

## [v0.3.3] - 2026-07-22

本版本收紧 GitHub Release 正文边界，将固定 outline 确立为唯一结构来源，禁止继承相邻 Release 的格式或写入内部质量证据；补齐四个 Security specialist 的薄 fixture 确认上下文与可审查样本，使 12 个既有 eval 恢复为完整 PASS；同时修复 VitePress 1.6.4 下 Mermaid fence 与旧 DOM 扫描选择器不匹配的问题，改用 Markdown-it fence renderer 和独立 Vue 组件稳定渲染 Mermaid。本版本覆盖 v0.3.2 之后合并到 `main` 的全部变更（#147、#149、#151、#152）。

### Changed

- **Security specialist eval fixture**：为 `appsec-checklist`、`authz-reviewer`、`dependency-risk-auditor`、`privacy-surface-mapper` 的 12 个薄 fixture eval 补齐 PM handoff、已确认 `feature_path`、正式 PRD 与最小可审查代码或配置样本，在不修改 specialist skill 行为与既有 assertions 的前提下恢复完整确认上下文，关闭 [issue #143](https://github.com/Neplich/dev-agent-skills/issues/143)。([#149](https://github.com/Neplich/dev-agent-skills/pull/149))
- **README Codex 快速安装入口**：英文 README 恢复单句 Codex 快速安装提示，中文 README 同步移除手动 clone 与 Python 脚本步骤，保留 Codex Guide 作为实现原理与排障入口；不涉及安装脚本或安装行为变更。([#152](https://github.com/Neplich/dev-agent-skills/pull/152))

### Fixed

- **GitHub Release 正文契约**：`github-release-generator` 以 `release-outline.md` 为唯一结构来源，不再读取或继承相邻 GitHub Release 的格式习惯；固定保留“重点更新 / 其他改进 / 升级说明 / 变更明细”四节，并明确 skill eval、assertion 计数、review 轮次与 QA 汇总等内部质量证据只进入仓库 changelog 的 Skill Eval 汇总，不进入用户向 GitHub Release 正文，关闭 [issue #146](https://github.com/Neplich/dev-agent-skills/issues/146)。([#147](https://github.com/Neplich/dev-agent-skills/pull/147))
- **VitePress Mermaid 脚手架 DOM 适配**：修复 VitePress 1.6.4 将 Mermaid fence 渲染为 `<div class="language-mermaid"><pre><code>...` 后旧选择器无法命中、页面只显示源码的问题；新实现由 Markdown-it fence renderer 输出全局注册的独立 `Mermaid.vue` 组件，支持严格安全级别、深浅色重渲染、多实例唯一 ID，以及失败时显示错误和原始源码，关闭 [issue #150](https://github.com/Neplich/dev-agent-skills/issues/150)。([#151](https://github.com/Neplich/dev-agent-skills/pull/151))

## Skill Eval 汇总（v0.3.3 发版前）

本节以当前 eval 定义契约的 canonical `agents/{agent}/test/{skill}/evals/workspace/{eval}/comparison.md` 为统计范围，按 skill 去重汇总最新结论。共核对 **152** 份 canonical durable comparison：**126 PASS、26 PARTIAL**；未按现行 `evals/workspace` 合同归档的 legacy workspace comparison 不纳入本表。

| Agent | Skill（eval 范围） | Canonical durable comparison 数 | 最新结论 |
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
| Product Manager | `github-release-generator`（eval-001–005） | 5 | 5/5 PASS（21/21 assertions） |
| Product Manager | `idea-to-spec` | 1 | 1 PASS |
| Product Manager | `pm-agent` router（eval-001–014） | 14 | 14/14 PASS（45/45 assertions） |
| QA | `bug-analyzer` | 3 | 3 PASS |
| QA | `exploratory-tester` | 3 | 3 PASS |
| QA | `qa-agent` | 3 | 3 PASS |
| QA | `regression-suite` | 3 | 3 PASS |
| QA | `spec-based-tester` | 3 | 3 PASS |
| Security | `security-agent` router（eval-001） | 1 | 1/1 PASS（6/6 assertions） |
| Security | `appsec-checklist`（eval-001–005） | 5 | 5/5 PASS（21/21 assertions） |
| Security | `authz-reviewer`（eval-001–004） | 4 | 4/4 PASS（16/16 assertions） |
| Security | `dependency-risk-auditor`（eval-001–004） | 4 | 4/4 PASS（16/16 assertions） |
| Security | `privacy-surface-mapper`（eval-001–004） | 4 | 4/4 PASS（16/16 assertions） |
| **合计** | **39 个 skill 分组** | **152** | **126 PASS、26 PARTIAL** |

本版本直接涉及的复验结果为：`github-release-generator` 的 4 个既有 eval 复验 **18/18 assertions PASS**，新增 eval-005 复验 **3/3 assertions PASS**；四个 Security specialist 的 12 个薄 fixture eval 复验 **48/48 assertions PASS**；`docs-site-bootstrap`、`formal-docs-sync`、`release-notes-generator` 与 `docs-agent` 的 12 个相关 eval 复验全部 PASS。以上均已在对应 PR 合并时完成 fresh `with_skill` / `without_skill` 成对复验并更新各自 `comparison.md`；本版本仅汇总并复用这些已提交结论，不重跑 skill eval。表中其余 **26 个 PARTIAL** 沿用各 skill 既有 durable 结论，主要记录历史 comparison 未生成 fresh `without_skill` baseline 等证据缺口，不是本版回归。
