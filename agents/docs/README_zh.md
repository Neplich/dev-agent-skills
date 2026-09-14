# 文档能力

本插件包含 6 个 Skill，提供文档站、事实同步、操作手册、发布说明与审计。每个 Skill 均可直接使用；`docs-agent` 帮助按任务选择相关方法。

助手根据用户目标组合这些能力，贯穿分析、实现、验证与交付。已有授权随任务延续，文档与专业参考按实际需要使用。

## 能力目录

| Skill | 用途 |
| --- | --- |
| [docs-agent](./skills/docs-agent/SKILL.md) | 文档能力导航 |
| [docs-site-bootstrap](./skills/docs-site-bootstrap/SKILL.md) | 初始化文档站 |
| [formal-docs-sync](./skills/formal-docs-sync/SKILL.md) | 同步当前产品与技术事实 |
| [manual-gen](./skills/manual-gen/SKILL.md) | 编写真实界面操作手册 |
| [release-notes-gen](./skills/release-notes-gen/SKILL.md) | 面向用户的版本说明 |
| [docs-audit](./skills/docs-audit/SKILL.md) | 文档准确性与发布检查 |

## 安装与使用

```text
/plugin install docs-agent@dev-agent-skills
```

也可按 [Codex 安装指南](../../docs/README.codex.md) 安装全部能力。直接描述目标，或点名所需 Skill 即可。

[仓库架构](../../docs/architecture.md) · [文档说明](../../docs/AGENTS.md) · [English](./README.md)
