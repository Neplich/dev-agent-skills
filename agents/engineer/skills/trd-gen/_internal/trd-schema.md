# TRD (Technical Requirements Document) Schema

> Engineer-owned schema referenced by `engineer-agent:trd-gen`.

## Required Sections

### 1. Document Metadata

```yaml
title: <feature name> — Technical Requirements Document
type: TRD
version: <SemVer>
status: Draft | In Review | Approved | Superseded
feature: <feature-name>
date: <YYYY-MM-DD>
last_updated: <YYYY-MM-DD>
related_prd: docs/pm/<feature-name>/PRD.md
related_decisions: docs/pm/<feature-name>/DECISIONS.md
```

### 2. Source Context

- PRD, BRD, DECISIONS, design docs, issue links, and repo paths used as input.
- Explicit note that PM scope is an input, not something TRD changes.

### 3. Technical Overview

- Technical summary of the solution.
- Link to the PRD for business context.
- Mermaid architecture or flow diagram.

### 4. Impacted Components

| Component / Path | Responsibility | Planned Change | Source Requirement |
| --- | --- | --- | --- |

### 5. Interfaces and Data

- API changes, events, data models, migrations, and compatibility constraints.
- If no interface or data changes are needed, state that explicitly.

### 6. Implementation Constraints

- Existing patterns to follow.
- Non-goals and forbidden areas.
- Dependency and compatibility constraints.

### 7. Validation Strategy

| Level | Scope | Command / Evidence | Required Before Handoff |
| --- | --- | --- | --- |

### 8. Rollout and Operations

- Deployment, rollback, monitoring, logging, and alerting considerations.
- Mark non-applicable items as `N/A` with a short reason.

### 9. Security and Privacy

- Auth, authorization, input validation, sensitive data, and threat notes.
- Mark non-applicable items as `N/A` with a short reason.

### 10. Risks and Open Questions

| Type | Item | Owner | Blocking |
| --- | --- | --- | --- |

### 11. Feature-Implementor Handoff

- Confirmed TRD path.
- Implementation plan document path:
  `docs/engineer/<feature-name>/IMPLEMENTATION_PLAN.md`.
- Handoff conditions and blockers.
