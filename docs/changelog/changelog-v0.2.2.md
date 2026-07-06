---
feature: release-changelog
version: 0.2.2
date: 2026-07-06
last_updated: 2026-07-06
---

# Changelog - v0.2.2

## [v0.2.2] - 2026-07-06

修复 v0.2.1 的插件加载回归：v0.2.1 引入 per-plugin `plugin.json` 后，marketplace 条目仍为 `strict: false` 且显式列出 `skills`，导致 Claude Code `/reload-plugins` 报 `conflicting manifests`，6 个插件无法加载。v0.2.1 的其它内容随本版本继续可用。

### Fixed

- **插件 manifest 冲突（v0.2.1 回归）**：将 `.claude-plugin/marketplace.json` 6 个条目的 `strict: false` 改为 `strict: true`，让 `plugin.json` 成为 component 权威（官方推荐），消除 `plugin.json` 与 marketplace 条目双重声明 components 导致的 `conflicting manifests` 加载错误；保留 `skills` 数组以满足 `validate_marketplace` 与 `skills-lock` 校验。([#92](https://github.com/Neplich/dev-agent-skills/pull/92))

### Changed

- **`release-notes-generator` skill 补齐 release 标题惯例与市场感知升级说明**：`reference/release-outline.md` 新增 GitHub release `name` / `--title` 规则 `v{VERSION} - {概括性简述}`（约 3 项、与正文 highlights 对齐、不用裸 tag），并把无破坏性变更文案修正为 `无破坏性变更。已有安装可以继续使用；建议按使用环境执行下面的升级方式。`；`reference/github-release-workflow.md` 的创建、更新与发布（`gh release edit`）流程均补 `--title "{TITLE}"`，确保标题规则贯穿 edit/publish 而不仅创建。([#93](https://github.com/Neplich/dev-agent-skills/pull/93))

## Skill Eval 汇总（v0.2.2 发版前）

v0.2.2 的改动仅涉及 marketplace 条目配置（#92）与 `release-notes-generator` 的 reference 文档（#93），**不改变任何 dispatcher 的路由 / 安全网行为**，因此未新增 skill eval 运行；各 skill 最新 `comparison.md` 结论沿用 v0.2.1（6 个 dispatcher 于 2026-07-06 完成 #81 安全网 fresh Codex subagent validation，其余沿用 v0.2.0 Batch 4 2026-07-05 结果）。

### 汇总统计

| 结论 | 数量 | Skills |
| --- | --- | --- |
| **PASS** | 14 | pm-agent, idea-to-spec, feature-catalog, roadmap-generator, engineer-agent, feature-implementor, qa-agent, bug-analyzer, exploratory-tester, regression-suite, spec-based-tester, devops-agent, designer-agent, security-agent |
| **PARTIAL** | 21 | changelog-generator, competitive-brief, competitive-intelligence, github-reader, release-notes-generator, codebase-analyzer, debugger, delivery, project-bootstrap, test-writer, trd-gen, cicd-bootstrap, deployment-planner, env-config-auditor, incident-playbook-writer, ui-ux-design, visual-design, appsec-checklist, authz-reviewer, dependency-risk-auditor, privacy-surface-mapper |
| **BLOCKED** | 0 | — |

各 skill 逐项结论见 [changelog-v0.2.1.md](./changelog-v0.2.1.md) 的 `Skill Eval 汇总`。PARTIAL 原因仍集中在 without_skill baseline 未生成（历史 eval 在 Fresh Sub-Agent 门禁收紧前执行），下一版本应对 PARTIAL skill 补跑 fresh Codex subagent validation。
