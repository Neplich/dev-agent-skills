# Dev Agent Skills

An on-demand professional knowledge library: seven plugins and forty skills covering product, design, engineering, QA, DevOps, security and documentation. The assistant selects relevant methods and carries the user’s task through completion.

[English](./README.md) · [中文](./README_zh.md)

## Installation

### Claude Code

Install the plugins relevant to your work:

```text
/plugin marketplace add Neplich/dev-agent-skills
/plugin install pm-agent@dev-agent-skills
/plugin install engineer-agent@dev-agent-skills
/plugin install qa-agent@dev-agent-skills
/plugin install devops-agent@dev-agent-skills
/plugin install designer-agent@dev-agent-skills
/plugin install security-agent@dev-agent-skills
/plugin install docs-agent@dev-agent-skills
```

### Codex

```text
Fetch and follow instructions from https://raw.githubusercontent.com/Neplich/dev-agent-skills/refs/heads/main/.codex/INSTALL.md
```

[Codex installation guide](./docs/README.codex.md)

### Kimi Code

```text
/plugins install https://github.com/Neplich/dev-agent-skills/tree/main
```

This README describes the current source. A pinned installation uses its release tag and the behavior recorded for that version.

## Use

Use any skill directly, or use a role guide to select methods. User requests, issues, code, tests and existing documents provide the working context. Plans and formal documents are selected as needed. Authorization carries through the task; the assistant asks when a material decision or additional permission is required.

```text
/debugger "Find and fix the login failure; verify success and failure paths."
/feature-implementor "Add filtering by status to the task list."
/human-writing "Update the installation guide from the current code."
```

## Plugins

| Plugin | Skills |
| --- | ---: |
| [`pm-agent`](./agents/product_manager/README.md) | 9 |
| [`engineer-agent`](./agents/engineer/README.md) | 7 |
| [`qa-agent`](./agents/qa/README.md) | 5 |
| [`devops-agent`](./agents/devops/README.md) | 5 |
| [`designer-agent`](./agents/designer/README.md) | 3 |
| [`security-agent`](./agents/security/README.md) | 5 |
| [`docs-agent`](./agents/docs/README.md) | 6 |

## Documentation

- [Architecture](./docs/architecture.md)
- [Documentation guide](./docs/AGENTS.md)
- [Skill maintenance](./docs/cookbook/maintain-skills.md)
- [Manual release](./docs/cookbook/release.md)
- [Contributing](./CONTRIBUTING.md)
- [Changelog](./CHANGELOG.md)

[Apache License 2.0](./LICENSE)
