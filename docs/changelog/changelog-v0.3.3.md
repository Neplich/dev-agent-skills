---
feature: release-changelog
version: 0.3.3
date: 2026-07-22
last_updated: 2026-07-22
---

# Changelog - v0.3.3

## [v0.3.3] - 2026-07-22

本版本收紧 GitHub Release 正文边界，将固定 outline 确立为唯一结构来源，禁止继承相邻 Release 的格式或写入内部质量证据；补齐四个 Security specialist 的薄 fixture 确认上下文与可审查样本，使 12 个既有 eval 恢复为完整 PASS；同时修复 VitePress 1.6.4 下 Mermaid fence 与旧 DOM 扫描选择器不匹配的问题，改用 Markdown-it fence renderer 和独立 Vue 组件稳定渲染 Mermaid。本版本覆盖 v0.3.2 之后合并到 `main` 的全部变更（#147、#149、#151）。

### Changed

- **Security specialist eval fixture**：为 `appsec-checklist`、`authz-reviewer`、`dependency-risk-auditor`、`privacy-surface-mapper` 的 12 个薄 fixture eval 补齐 PM handoff、已确认 `feature_path`、正式 PRD 与最小可审查代码或配置样本，在不修改 specialist skill 行为与既有 assertions 的前提下恢复完整确认上下文，关闭 [issue #143](https://github.com/Neplich/dev-agent-skills/issues/143)。([#149](https://github.com/Neplich/dev-agent-skills/pull/149))

### Fixed

- **GitHub Release 正文契约**：`github-release-generator` 以 `release-outline.md` 为唯一结构来源，不再读取或继承相邻 GitHub Release 的格式习惯；固定保留“重点更新 / 其他改进 / 升级说明 / 变更明细”四节，并明确 skill eval、assertion 计数、review 轮次与 QA 汇总等内部质量证据只进入仓库 changelog 的 Skill Eval 汇总，不进入用户向 GitHub Release 正文，关闭 [issue #146](https://github.com/Neplich/dev-agent-skills/issues/146)。([#147](https://github.com/Neplich/dev-agent-skills/pull/147))
- **VitePress Mermaid 脚手架 DOM 适配**：修复 VitePress 1.6.4 将 Mermaid fence 渲染为 `<div class="language-mermaid"><pre><code>...` 后旧选择器无法命中、页面只显示源码的问题；新实现由 Markdown-it fence renderer 输出全局注册的独立 `Mermaid.vue` 组件，支持严格安全级别、深浅色重渲染、多实例唯一 ID，以及失败时显示错误和原始源码，关闭 [issue #150](https://github.com/Neplich/dev-agent-skills/issues/150)。([#151](https://github.com/Neplich/dev-agent-skills/pull/151))

## Skill Eval 汇总（v0.3.3 发版前）

本版本复用各 PR 合并时已经完成并写入 durable `comparison.md` 的 fresh `with_skill` / `without_skill` 成对复验结果，不在发版环节重复运行 eval。

| Agent | Skill（eval 范围） | 复验结论 |
| --- | --- | --- |
| Product Manager | `github-release-generator`（既有 eval-001–004） | 4/4 eval PASS，18/18 assertions PASS |
| Product Manager | `github-release-generator`（新增 eval-005） | 1/1 eval PASS，3/3 assertions PASS |
| Security | `appsec-checklist`、`authz-reviewer`、`dependency-risk-auditor`、`privacy-surface-mapper`（各 eval-001–003） | 12/12 eval PASS，48/48 assertions PASS |
| Docs | `docs-site-bootstrap`（3 个）、`formal-docs-sync`（5 个）、`release-notes-generator`（3 个）、`docs-agent`（1 个 integration） | 12/12 eval PASS |

以上结果均已在对应 PR 合并时完成 fresh 成对复验并更新各自 `comparison.md`；本版本仅汇总并复用这些已提交结论，不重跑 skill eval。
