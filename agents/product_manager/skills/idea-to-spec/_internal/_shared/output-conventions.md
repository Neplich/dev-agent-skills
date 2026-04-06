# Output Conventions

> Shared output format standards referenced by gen, iteration, and validator
> skills.

## 1. Document Metadata Header

Every generated formal document MUST begin with a YAML frontmatter block:

```yaml
---
title: "<Document Title>"
type: BRD | PRD | TRD | ADR | API | TEST_SPEC | DECISIONS
version: "1.0.0"
status: Draft | In Review | Approved | Superseded | Deprecated
author: "<author name>"
date: "YYYY-MM-DD"
generated_by: "<skill-name>"
related_docs:
  - "docs/pm/<feature-name>/DECISIONS.md"
changelog:
  - version: "1.0.0"
    date: "YYYY-MM-DD"
    changes: "Initial version"
---
```

### Required Fields

| Field | Required | Description |
| --- | --- | --- |
| title | Yes | Document title |
| type | Yes | Document type enum |
| version | Yes | SemVer string |
| status | Yes | Document lifecycle status |
| author | Yes | Creator name |
| date | Yes | Creation/update date |
| generated_by | Yes | Skill that generated this document |
| related_docs | No | List of related document paths |
| changelog | Yes | Version history entries |

## 2. Version Numbering

Follow Semantic Versioning in frontmatter and changelog. Do not encode the
version into the filename.

- **MAJOR** (`X.0.0`): Fundamental scope change or complete rewrite
- **MINOR** (`1.X.0`): New sections added or significant content changes
- **PATCH** (`1.0.X`): Typo fixes, formatting, minor clarifications

### Version Bump Rules for Iteration Skills

| Change Type | Version Bump | Example |
| --- | --- | --- |
| Fix typo / formatting | PATCH | `1.0.0 -> 1.0.1` |
| Add or update section content | MINOR | `1.0.1 -> 1.1.0` |
| Change scope / objectives | MAJOR | `1.1.0 -> 2.0.0` |
| Status change only | PATCH | `1.0.0 -> 1.0.1` |

## 3. Directory and File Naming Convention

Use feature-scoped folders with stable filenames:

```text
docs/<agent-short>/<feature-name>/<DOC>.md
```

### Short Agent Paths

- `docs/pm/`
- `docs/design/`
- `docs/engineer/`
- `docs/qa/`
- `docs/devops/`
- `docs/security/`

### Canonical PM Filenames

- `DECISIONS.md`
- `BRD.md`
- `PRD.md`
- `design.md` for interim PM drafts only

### Canonical Downstream Filenames

- Design: `UI_UX_SPEC.md`
- Engineer: `TRD.md`, `API.md`, `ADR-001-<title>.md`
- QA: `TEST_SPEC.md`
- DevOps: `RELEASE_PLAN.md`
- Security: `SECURITY_REVIEW.md`

### Rules

- Use stable filenames for primary docs
- Keep versioning in frontmatter and git history, not in filenames
- Use uppercase canonical filenames for the main artifact in each feature folder
- Keep related docs in the same feature folder for that agent unless there is a
  clear reason to split further

## 4. Changelog Format

Within the YAML frontmatter `changelog` array:

```yaml
changelog:
  - version: "1.1.0"
    date: "2026-04-06"
    changes: "Expanded rollout section and updated API touchpoints"
  - version: "1.0.0"
    date: "2026-04-03"
    changes: "Initial version"
```

For iteration skills, also include an inline changelog section at the end of
the document when the doc has already undergone material revision.

## 5. Output Delivery Format

- **Primary format**: Markdown (`.md`)
- **Encoding**: UTF-8
- **Line endings**: LF
- **Max line length**: no hard limit, but prefer readable wrapping
- **Tables**: GitHub-flavored Markdown
- **Diagrams**: Mermaid fenced blocks
- **Code examples**: Fenced code blocks with language identifier

## 6. Documentation Memory Rules

- `docs/pm/{feature-name}/DECISIONS.md` is the canonical PM decision ledger
- When a generated document locks a new product or technical decision, update
  `DECISIONS.md` or explicitly reference the pending decision that still needs
  confirmation
- Before continuing a long-running feature design, re-read the active feature
  docs and treat them as the durable memory source
- After a major design stage, consolidate working notes into stable declarative
  prose

## 7. Validation Report Format

See `quality-rules.md` for the standard validation report template.
