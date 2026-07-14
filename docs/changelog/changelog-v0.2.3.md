---
feature: release-changelog
version: 0.2.3
date: 2026-07-14
last_updated: 2026-07-14
---

# Changelog - v0.2.3

## [v0.2.3] - 2026-07-14

聚焦 Codex 安装体验与入口路由的清晰化：新增 Codex 复制式安装脚本消除 plugin.json namespace 前缀（#97），修复安装器可能删除自身 checkout 的风险（#100），把 `pm-agent` 明确为唯一直接入口并收窄各 specialist 的触发面描述（#98），并重构 README / CONTRIBUTING 文档门面（#101 / #103 / #106）。无破坏性变更，已有安装可继续使用。

### Added

- **Codex 复制式安装脚本**：新增 `scripts/install_codex_skills.py`，以复制方式安装 skill，消除祖先 plugin manifest 造成的 namespace 前缀问题，并补充对应安装测试。([#97](https://github.com/Neplich/dev-agent-skills/pull/97))

### Changed

- **README 入口瘦身**：精简 README / README_zh 入口内容，将 Agents 明细、协作方式与维护流程分流到各自文档，突出 `pm-agent` 唯一直接入口与文档索引。([#103](https://github.com/Neplich/dev-agent-skills/pull/103))
- **中文贡献入口**：新增中文 `CONTRIBUTING_zh.md` 承接 README_zh 的贡献链接，并将 `CONTRIBUTING.md` 英文化，两文件互加语言切换链接；`AGENTS.md` 仍为仓库治理唯一事实源。([#106](https://github.com/Neplich/dev-agent-skills/pull/106))
- **README_zh Eval 维护说明补齐**：补齐 README_zh 中 Eval 维护流程缺失的说明段落，与英文 README 对齐。([#101](https://github.com/Neplich/dev-agent-skills/pull/101))

### Fixed

- **入口路由触发面收窄**：将 `pm-agent` 入口描述改为场景句式作为唯一直接入口，并把各 specialist 的 frontmatter `description` 收窄为「非直接入口、经 pm-agent 分类后调用」，消除下游 skill 抢占用户直达触发面的问题。([#98](https://github.com/Neplich/dev-agent-skills/pull/98))
- **安装器自我删除防护**：修复安装器在特定路径下可能删除自身 checkout 的风险，避免复制式安装误删来源目录。([#100](https://github.com/Neplich/dev-agent-skills/pull/100))

## Skill Eval 汇总（v0.2.3 发版前）

本版唯一涉及 skill 行为的变更是 #98，且仅修改各 skill 的 frontmatter `description`（触发面收窄），**未改动任何 skill 的正文执行协议**，因此影响面是入口路由，由 6 个 dispatcher 的 routing eval 覆盖。

#98 在合并（2026-07-08）时已对全部受影响的 dispatcher routing eval 完成 fresh Codex subagent validation 并同步更新 `comparison.md`，覆盖完整、无遗漏。按发版规则「skill 有更新且更新后遗漏测试才需重跑」，本版 skill 变更未漏测，发版直接复用最新 `comparison.md` 结论，不再重跑。

### Routing Eval 结论（#98，dispatcher 维度）

| Dispatcher | Routing eval | 结论 | 验证来源 |
| --- | :---: | :---: | --- |
| `pm-agent` | 13 | 全部 PASS | 2026-07-08 fresh Codex subagent validation |
| `engineer-agent` | 4 | 全部 PASS | 2026-07-08 fresh Codex subagent validation |
| `qa-agent` | 3 | 全部 PASS | 2026-07-08 fresh Codex subagent validation |
| `designer-agent` | 3 | 全部 PASS | 2026-07-08 fresh Codex subagent validation |
| `devops-agent` | 1 | 全部 PASS | 2026-07-08 fresh Codex subagent validation |
| `security-agent` | 1 | 全部 PASS | 2026-07-08 fresh Codex subagent validation |
| **合计** | **25** | **25 PASS / 0 FAIL** | — |

各 routing eval 的 `comparison.md` 均记录 `No routing regression found from the PR #98 trigger-description changes`。

### Specialist 执行 eval

各 specialist 的执行协议（SKILL.md 正文）本版未变更，其执行类 eval 不受 #98 影响，沿用上一版本（v0.2.1 / v0.2.2）最新 `comparison.md` 结论，未重新运行。发版未新增 skill 执行协议变更，因此不触发 specialist 执行 eval 重跑。
