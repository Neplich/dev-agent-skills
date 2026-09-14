# 工程能力

本插件包含 7 个 Skill，提供代码分析、技术设计、实现、测试、调试与交付。每个 Skill 均可直接使用；`engineer-agent` 帮助按任务选择相关方法。

助手根据用户目标组合这些能力，贯穿分析、实现、验证与交付。已有授权随任务延续，文档与专业参考按实际需要使用。

## 能力目录

| Skill | 用途 |
| --- | --- |
| [engineer-agent](./skills/engineer-agent/SKILL.md) | 工程能力导航 |
| [codebase-analyzer](./skills/codebase-analyzer/SKILL.md) | 代码结构与依赖分析 |
| [trd-gen](./skills/trd-gen/SKILL.md) | 技术设计、API 与架构决策 |
| [feature-implementor](./skills/feature-implementor/SKILL.md) | 实现功能与修复问题 |
| [test-writer](./skills/test-writer/SKILL.md) | 编写针对行为的测试 |
| [debugger](./skills/debugger/SKILL.md) | 根因定位与修复验证 |
| [delivery](./skills/delivery/SKILL.md) | 提交、PR 与交付检查 |

## 安装与使用

```text
/plugin install engineer-agent@dev-agent-skills
```

也可按 [Codex 安装指南](../../docs/README.codex.md) 安装全部能力。直接描述目标，或点名所需 Skill 即可。

[仓库架构](../../docs/architecture.md) · [文档说明](../../docs/AGENTS.md) · [English](./README.md)
