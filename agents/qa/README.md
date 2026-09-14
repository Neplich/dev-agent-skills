# QA Skills

This plugin provides 5 skills for exploratory testing, acceptance, defect analysis and regression. Every skill can be used directly; `qa-agent` helps select relevant methods for a task.

The assistant combines capabilities to complete the user's goal through analysis, implementation, validation and delivery. Authorization carries through the task, and documents and references are selected as needed.

## Skills

| Skill | Purpose |
| --- | --- |
| [qa-agent](./skills/qa-agent/SKILL.md) | QA capability guide |
| [exploratory-tester](./skills/exploratory-tester/SKILL.md) | Explore real user journeys |
| [spec-based-tester](./skills/spec-based-tester/SKILL.md) | Verify behavior against known expectations |
| [bug-analyzer](./skills/bug-analyzer/SKILL.md) | Reproduce and analyze defects |
| [regression-suite](./skills/regression-suite/SKILL.md) | Organize and run regression tests |

## Installation and Use

```text
/plugin install qa-agent@dev-agent-skills
```

The [Codex guide](../../docs/README.codex.md) installs all skills. Describe the goal or name a skill directly.

[Architecture](../../docs/architecture.md) · [Documentation](../../docs/AGENTS.md) · [中文](./README_zh.md)
