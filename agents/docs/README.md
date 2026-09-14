# Docs Skills

This plugin provides 6 skills for documentation sites, fact synchronization, user manuals, release notes and audits. Every skill can be used directly; `docs-agent` helps select relevant methods for a task.

The assistant combines capabilities to complete the user's goal through analysis, implementation, validation and delivery. Authorization carries through the task, and documents and references are selected as needed.

## Skills

| Skill | Purpose |
| --- | --- |
| [docs-agent](./skills/docs-agent/SKILL.md) | Documentation capability guide |
| [docs-site-bootstrap](./skills/docs-site-bootstrap/SKILL.md) | Initialize documentation sites |
| [formal-docs-sync](./skills/formal-docs-sync/SKILL.md) | Synchronize current product and technical facts |
| [manual-gen](./skills/manual-gen/SKILL.md) | Write manuals from real interfaces |
| [release-notes-gen](./skills/release-notes-gen/SKILL.md) | User-facing release notes |
| [docs-audit](./skills/docs-audit/SKILL.md) | Documentation accuracy and release checks |

## Installation and Use

```text
/plugin install docs-agent@dev-agent-skills
```

The [Codex guide](../../docs/README.codex.md) installs all skills. Describe the goal or name a skill directly.

[Architecture](../../docs/architecture.md) · [Documentation](../../docs/AGENTS.md) · [中文](./README_zh.md)
