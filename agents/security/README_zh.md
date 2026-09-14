# 安全能力

本插件包含 5 个 Skill，提供应用安全、授权、依赖与隐私数据流。每个 Skill 均可直接使用；`security-agent` 帮助按任务选择相关方法。

助手根据用户目标组合这些能力，贯穿分析、实现、验证与交付。已有授权随任务延续，文档与专业参考按实际需要使用。

## 能力目录

| Skill | 用途 |
| --- | --- |
| [security-agent](./skills/security-agent/SKILL.md) | 安全能力导航 |
| [appsec-checklist](./skills/appsec-checklist/SKILL.md) | 应用安全审查 |
| [authz-reviewer](./skills/authz-reviewer/SKILL.md) | 身份与授权审查 |
| [dependency-risk-auditor](./skills/dependency-risk-auditor/SKILL.md) | 依赖风险审查 |
| [privacy-surface-mapper](./skills/privacy-surface-mapper/SKILL.md) | 隐私与数据流梳理 |

## 安装与使用

```text
/plugin install security-agent@dev-agent-skills
```

也可按 [Codex 安装指南](../../docs/README.codex.md) 安装全部能力。直接描述目标，或点名所需 Skill 即可。

[仓库架构](../../docs/architecture.md) · [文档说明](../../docs/AGENTS.md) · [English](./README.md)
