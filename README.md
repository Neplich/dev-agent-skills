<div align="center">

# Dev Agent Skills

Multi-agent skills for the full software delivery lifecycle.

[![Agents](https://img.shields.io/badge/agents-6-blue)](#agents)
[![Skills](https://img.shields.io/badge/skills-33-green)](#agents)
[![License](https://img.shields.io/badge/license-Apache%202.0-orange)](LICENSE)

`pm-agent` • `designer-agent` • `engineer-agent` • `qa-agent` • `devops-agent` • `security-agent`

[Quick Start](#quick-start) • [Agents](#agents) • [Collaboration Model](#collaboration-model) • [Repository Structure](#repository-structure) • [Local Validation](#local-validation)

</div>

> [!NOTE]
> Other languages: [中文](./README_zh.md)

## Overview

This repository publishes six role-based agents from one marketplace/source, covering the full path from product planning to design, implementation, testing, deployment, and security review.

It includes:

- 6 dispatcher skills, one entrypoint per agent
- 27 specialist skills across product, engineering, QA, DevOps, design, and security work
- Claude Code marketplace configuration
- Codex native skill discovery installation instructions
- Agent-level eval fixtures and local validation scripts
- Reference-backed visual design system data and lookup scripts for Designer Agent

> [!NOTE]
> These agents collaborate through Markdown documents and project assets. They do not require a shared runtime or fixed state machine, and you can install only the agents you need.

## Agents

| Agent | Focus | Skills | Entry | Docs |
| --- | --- | :---: | --- | --- |
| `pm-agent` | Requirements, specs, competitor research, roadmap, release communication, GitHub project status | 8 (`1 + 7`) | `/pm-agent` | [product_manager](./agents/product_manager/README.md) |
| `designer-agent` | UX flows, information architecture, wireframes, visual systems, design handoff | 3 (`1 + 2`) | `/designer-agent` | [designer](./agents/designer/README.md) |
| `engineer-agent` | Codebase analysis, project bootstrap, feature implementation, tests, debugging, delivery | 7 (`1 + 6`) | `/engineer-agent` | [engineer](./agents/engineer/README.md) |
| `qa-agent` | Spec validation, exploratory testing, bug analysis, regression verification | 5 (`1 + 4`) | `/qa-agent` | [qa](./agents/qa/README.md) |
| `devops-agent` | Deployment planning, CI/CD, environment configuration audits, incident playbooks | 5 (`1 + 4`) | `/devops-agent` | [devops](./agents/devops/README.md) |
| `security-agent` | AppSec, authorization review, dependency risk, privacy data-flow mapping | 5 (`1 + 4`) | `/security-agent` | [security](./agents/security/README.md) |

> [!TIP]
> Prefer an agent entry command such as `/pm-agent` or `/engineer-agent`. The dispatcher skill will classify the request and choose the right specialist skill.

## Collaboration Model

```mermaid
flowchart LR
    PM["PM Agent"] --> Designer["Designer Agent"]
    PM --> Engineer["Engineer Agent"]
    Designer --> Engineer
    Engineer --> QA["QA Agent"]
    QA --> Engineer
    QA -. "Requirement gap / acceptance issue" .-> PM
    Engineer --> DevOps["DevOps Agent"]
    Engineer --> Security["Security Agent"]
    Security --> Engineer
```

Common chains:

1. `pm-agent -> engineer-agent -> qa-agent`
2. `pm-agent -> designer-agent -> engineer-agent -> qa-agent`
3. `engineer-agent <-> qa-agent` for bugfix and regression loops
4. `engineer-agent -> devops-agent` for deployment, CI/CD, and runtime readiness
5. `engineer-agent -> security-agent` for pre-release or focused security review

Not every project needs the full chain. Each agent can complete its own role-specific loop, and cross-agent handoff happens only when another role is needed.

## Quick Start

### Claude Code

```bash
# Add the marketplace
/plugin marketplace add Neplich/dev-agent-skills

# Install only the agents you need
/plugin install pm-agent@dev-agent-skills
/plugin install designer-agent@dev-agent-skills
/plugin install engineer-agent@dev-agent-skills
/plugin install qa-agent@dev-agent-skills
/plugin install devops-agent@dev-agent-skills
/plugin install security-agent@dev-agent-skills
```

Claude Code scans installed plugins by plugin root. This repository scopes each plugin to its own agent directory, but installing only the agents you need is still recommended.

### Codex

In Codex, say:

```text
Fetch and follow instructions from https://raw.githubusercontent.com/Neplich/dev-agent-skills/refs/heads/main/.codex/INSTALL.md
```

The install flow will ask:

- whether this should be a `personal` or `project` install
- whether to install `all` agents or a selected subset

See [docs/README.codex.md](./docs/README.codex.md) for the full Codex guide.

## Usage Examples

```text
/pm-agent "I want to build a task management app. Help me shape the requirements first."
/designer-agent "Design the login and registration flow from the PRD."
/engineer-agent "Implement the login feature from the design docs."
/qa-agent "Validate the login feature against the spec."
/devops-agent "Add Docker and GitHub Actions."
/security-agent "Review authorization and dependency risk before release."
```

If you already know the specialist skill you need, you can call it directly:

```text
/idea-to-spec
/github-reader
/ui-ux-design
/visual-design
/feature-implementor
/spec-based-tester
/deployment-planner
/appsec-checklist
```

## Repository Structure

```text
dev-agent-skills/
├── .claude-plugin/          # Claude Code marketplace configuration
├── .codex/                  # Codex installation entrypoint
├── agents/                  # 6 agents with skills and evals
├── docs/                    # Public docs and historical design notes
├── skills-lock.json         # Skill metadata lock file
├── CLAUDE.md                # Claude Code repository guidance
└── AGENTS.md                # Shared agent repository guidance
```

Each agent follows the same basic shape:

```text
agents/{agent}/
├── README.md
├── skills/
│   └── {skill}/
│       └── SKILL.md
└── test/
    └── {skill}/
        └── evals/
            └── evals.json
```

Some skills also include `_internal/`, `references/`, or script directories for protocol details, design data, or validation helpers.

## Design System Data

Designer Agent's `visual-design` skill includes reference-backed design system capability:

- Local path: `agents/designer/skills/visual-design/references/design-system-data/`
- Data coverage: product types, style patterns, colors, typography, UX guidelines, charts, landing patterns, icons, and stack guidelines
- Usage boundary: design reasoning and design-system documentation only; it must not generate application code, install commands, or engineering task lists

The data design follows ui ux pro max's organization model and is maintained under this repository's own paths and documentation.

## Local Validation

> [!NOTE]
> Use `uv run ...` for Python-based validation scripts and eval runners in this repository.

```bash
# Designer eval
uv run agents/designer/test/run_all_evals.py

# QA eval
uv run agents/qa/test/run_all_evals.py

# PM idea-to-spec tests
uv run --with pytest pytest agents/product_manager/test/idea-to-spec

# JSON format checks
uv run python -m json.tool .claude-plugin/marketplace.json >/tmp/marketplace.json.out
uv run python -m json.tool skills-lock.json >/tmp/skills-lock.json.out
```

## Maintenance Notes

- Follow the existing `agents/*` structure when adding a new agent or skill.
- Keep `CLAUDE.md` and `AGENTS.md` identical.
- Restrictive repository permissions default to the sole administrator; add maintainers or bots explicitly when needed.
- Skill evals should verify role boundaries, context reading, execution-path selection, and structured artifacts instead of generic answer quality alone.

<div align="center">

[中文](./README_zh.md) • [Claude Guide](./CLAUDE.md) • [Agents Guide](./AGENTS.md) • [Codex Guide](./docs/README.codex.md)

</div>
