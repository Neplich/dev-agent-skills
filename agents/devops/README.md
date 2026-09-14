# DevOps Skills

This plugin provides 5 skills for deployment, ci/cd, configuration audits and incident response. Every skill can be used directly; `devops-agent` helps select relevant methods for a task.

The assistant combines capabilities to complete the user's goal through analysis, implementation, validation and delivery. Authorization carries through the task, and documents and references are selected as needed.

## Skills

| Skill | Purpose |
| --- | --- |
| [devops-agent](./skills/devops-agent/SKILL.md) | DevOps capability guide |
| [deployment-planner](./skills/deployment-planner/SKILL.md) | Deployment and recovery plans |
| [cicd-bootstrap](./skills/cicd-bootstrap/SKILL.md) | CI/CD configuration |
| [env-config-auditor](./skills/env-config-auditor/SKILL.md) | Environment and configuration audits |
| [incident-playbook-writer](./skills/incident-playbook-writer/SKILL.md) | Incident runbooks |

## Installation and Use

```text
/plugin install devops-agent@dev-agent-skills
```

The [Codex guide](../../docs/README.codex.md) installs all skills. Describe the goal or name a skill directly.

[Architecture](../../docs/architecture.md) · [Documentation](../../docs/AGENTS.md) · [中文](./README_zh.md)
