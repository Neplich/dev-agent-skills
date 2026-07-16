# TRD (Technical Requirements Document) Schema

> Engineer-owned schema referenced by `engineer-agent:trd-gen`.

## Required Sections

### 1. Document Metadata

```yaml
title: <feature name> — Technical Requirements Document
type: TRD
version: <SemVer>
status: Draft | In Review | Approved | Superseded
feature: <last feature slug>
feature_path: <feature-path>
parent_feature: <parent feature path or N/A>
feature_level: <positive integer>
author: <generation requester display name + agent platform name>
date: <YYYY-MM-DD>
last_updated: <YYYY-MM-DD>
related_prd: docs/pm/<feature-path>/PRD.md
related_decisions: docs/pm/<feature-path>/DECISIONS.md
related_code: # optional machine-readable affected paths or globs
  - src/<feature>/**
```

The `author` value must identify both the generation requester and Agent
platform, for example `Neplich Codex`. The platform name may be custom; ask the
user when either part is unknown, and do not use empty values or placeholders
such as `AI Assistant`.

`feature_path` is the canonical cross-role key and supports one or more
directory segments separated by `/`, for example `chat-interface`,
`chat-interface/history-search`, `chat-interface/history-search/export`, or
`agents/engineer-agent/skills/trd-gen`. `feature` remains a compatibility
field; for new nested documents it should use the final slug while
`feature_path` stores the full path. `parent_feature` must be `N/A` for a
level-1 feature and the full parent path for deeper features. `feature_level`
must be a positive integer matching the number of path segments.

For legacy single-level TRDs or PRDs without these fields, read them as:

```yaml
feature_path: <directory-name>
parent_feature: N/A
feature_level: 1
```

New TRDs and substantive TRD updates must write the explicit fields above.
`related_prd` must point to `docs/pm/<feature-path>/PRD.md`; if the PRD is
missing or its path/frontmatter does not match, stop and return to PM alignment
or a TRD gap handoff instead of writing a mismatched TRD.

`related_code` is optional and, when present, must be an array of repository
paths or globs that machine-readably identifies the affected code domain for
`formal-docs-sync` and `docs-audit`. It is an enhancement rather than a TRD or
handoff gate. When it is absent, consumers must use their impact-domain
evidence-chain fallback instead of blocking solely on this field.

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
  `docs/engineer/<feature-path>/IMPLEMENTATION_PLAN.md`.
- Handoff conditions and blockers.
