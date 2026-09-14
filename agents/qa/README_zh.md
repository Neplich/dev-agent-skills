# 测试能力

本插件包含 5 个 Skill，提供探索测试、规格验收、缺陷分析与回归。每个 Skill 均可直接使用；`qa-agent` 帮助按任务选择相关方法。

助手根据用户目标组合这些能力，贯穿分析、实现、验证与交付。已有授权随任务延续，文档与专业参考按实际需要使用。

## 能力目录

| Skill | 用途 |
| --- | --- |
| [qa-agent](./skills/qa-agent/SKILL.md) | 测试能力导航 |
| [exploratory-tester](./skills/exploratory-tester/SKILL.md) | 探索真实用户路径 |
| [spec-based-tester](./skills/spec-based-tester/SKILL.md) | 按已知预期验证行为 |
| [bug-analyzer](./skills/bug-analyzer/SKILL.md) | 复现与分析缺陷 |
| [regression-suite](./skills/regression-suite/SKILL.md) | 组织与执行回归测试 |

## 安装与使用

```text
/plugin install qa-agent@dev-agent-skills
```

也可按 [Codex 安装指南](../../docs/README.codex.md) 安装全部能力。直接描述目标，或点名所需 Skill 即可。

[仓库架构](../../docs/architecture.md) · [文档说明](../../docs/AGENTS.md) · [English](./README.md)
