# Engineer Agent

`engineer-agent` is the engineering-role dispatcher skill. It routes codebase analysis, project bootstrap, feature implementation, test coverage, debugging, and delivery requests to the right engineering specialist skill.

> [!NOTE]
> Other languages: [中文](./README_zh.md)

> [!IMPORTANT]
> Engineer Agent should only take over after the requirement or fix target is clear. If the user is still defining product goals, or an empty repository only contains an idea, route back to `pm-agent` first.

## Quick Facts

| Item | Details |
| --- | --- |
| Entry skill | `engineer-agent` |
| Specialist skills | 6 |
| Main inputs | PM documents, optional design documents, existing codebase, test results, failure logs |
| Main outputs | Code changes, tests, engineering docs, Git commits / PRs |
| Collaboration | Upstream `pm-agent` / `designer-agent`; downstream `qa-agent` / `devops-agent` / `security-agent` |

## Skills

| Skill | When to use | Main output |
| --- | --- | --- |
| `engineer-agent` | Engineering request routing | Specialist selection and execution path |
| `codebase-analyzer` | Taking over an existing repo, understanding structure and constraints | Project profile, stack and architecture summary |
| `project-bootstrap` | Initializing a project from approved PRD/TRD | Project skeleton, base config, startup notes |
| `feature-implementor` | Implementing a spec or design document | Code changes, necessary engineering docs |
| `test-writer` | Adding unit, integration, or validation coverage | Test files, test execution evidence |
| `debugger` | Reproducing, diagnosing, and fixing bugs or build failures | Minimal fix, regression evidence |
| `delivery` | Branches, commits, pushes, PRs, delivery wrap-up | Git commit, PR, delivery summary |

## Routing Rules

- Understand repository structure, stack, and architecture boundaries: use `codebase-analyzer`
- Bootstrap a new project or service: use `project-bootstrap`
- Implement features, behavior changes, or design handoff: use `feature-implementor`
- Add tests, coverage, or implementation validation: use `test-writer`
- Debug bugs, failed logs, failing tests, or broken builds: use `debugger`
- Commit, push, open PRs, or finish delivery: use `delivery`

Default rule: if the request changes production behavior, first confirm the requirement source and code context. If the request starts from a failure symptom, prefer `debugger`.

## Typical Flow

```mermaid
flowchart LR
    PM["PM docs"] --> Engineer["engineer-agent"]
    Design["Design docs"] --> Engineer
    Engineer --> Analyze["codebase-analyzer"]
    Analyze --> Implement["feature-implementor"]
    Implement --> Test["test-writer"]
    Test --> Delivery["delivery"]
    Implement -. failure .-> Debug["debugger"]
    Debug --> Test
```

## Inputs And Outputs

Engineer mainly consumes:

- `docs/pm/{feature}/PRD.md`
- `docs/pm/{feature}/TRD.md`
- `docs/pm/{feature}/DECISIONS.md`
- `docs/design/{feature}/ui-ux-spec.md`
- `docs/design/{feature}/visual-system.md`

Engineer's primary outputs are code and tests. It may also update:

- `docs/engineer/{feature}/TRD.md`
- `docs/engineer/{feature}/API.md`
- `docs/engineer/{feature}/ADR.md`

## Collaboration Boundary

- Engineer is the only role that turns PM/Designer documents into code, tests, and delivery artifacts.
- Engineer does not replace PM for requirement definition or Designer for UX/visual decisions.
- QA findings return to Engineer when they are implementation defects, and to PM when they are requirement gaps.
- DevOps and Security join only when deployment, runtime, or security review becomes the current goal.

## Local Maintenance

```bash
# Install one Engineer skill into the current project runtime
npx skills add ./agents/engineer/skills/feature-implementor

# Inspect engineering eval definitions
find agents/engineer/test -path '*/evals/evals.json' -print
```
