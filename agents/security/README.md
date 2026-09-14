# Security Skills

This plugin provides 5 skills for application security, authorization, dependencies and privacy data flows. Every skill can be used directly; `security-agent` helps select relevant methods for a task.

The assistant combines capabilities to complete the user's goal through analysis, implementation, validation and delivery. Authorization carries through the task, and documents and references are selected as needed.

## Skills

| Skill | Purpose |
| --- | --- |
| [security-agent](./skills/security-agent/SKILL.md) | Security capability guide |
| [appsec-checklist](./skills/appsec-checklist/SKILL.md) | Application security review |
| [authz-reviewer](./skills/authz-reviewer/SKILL.md) | Identity and authorization review |
| [dependency-risk-auditor](./skills/dependency-risk-auditor/SKILL.md) | Dependency risk review |
| [privacy-surface-mapper](./skills/privacy-surface-mapper/SKILL.md) | Privacy and data-flow mapping |

## Installation and Use

```text
/plugin install security-agent@dev-agent-skills
```

The [Codex guide](../../docs/README.codex.md) installs all skills. Describe the goal or name a skill directly.

[Architecture](../../docs/architecture.md) · [Documentation](../../docs/AGENTS.md) · [中文](./README_zh.md)
