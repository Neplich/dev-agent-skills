# Engineer Skills

This plugin provides 7 skills for code analysis, technical design, implementation, tests, debugging and delivery. Every skill can be used directly; `engineer-agent` helps select relevant methods for a task.

The assistant combines capabilities to complete the user's goal through analysis, implementation, validation and delivery. Authorization carries through the task, and documents and references are selected as needed.

## Skills

| Skill | Purpose |
| --- | --- |
| [engineer-agent](./skills/engineer-agent/SKILL.md) | Engineering capability guide |
| [codebase-analyzer](./skills/codebase-analyzer/SKILL.md) | Code structure and dependency analysis |
| [trd-gen](./skills/trd-gen/SKILL.md) | Technical design, APIs and architecture decisions |
| [feature-implementor](./skills/feature-implementor/SKILL.md) | Feature implementation and fixes |
| [test-writer](./skills/test-writer/SKILL.md) | Behavior-focused tests |
| [debugger](./skills/debugger/SKILL.md) | Root-cause analysis and fix verification |
| [delivery](./skills/delivery/SKILL.md) | Commits, pull requests and delivery checks |

## Installation and Use

```text
/plugin install engineer-agent@dev-agent-skills
```

The [Codex guide](../../docs/README.codex.md) installs all skills. Describe the goal or name a skill directly.

[Architecture](../../docs/architecture.md) · [Documentation](../../docs/AGENTS.md) · [中文](./README_zh.md)
