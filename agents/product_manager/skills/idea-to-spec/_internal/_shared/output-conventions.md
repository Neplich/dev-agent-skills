# Output Conventions

> Shared output format standards referenced by all gen, iteration, and validator skills.

## 1. Document Metadata Header

Every generated document MUST begin with a YAML frontmatter block:

```yaml
---
title: "<Document Title>"
type: BRD | PRD | TRD | ADR | API | TEST_SPEC | WEEKLY_REPORT
version: "1.0.0"
status: Draft | In Review | Approved | Superseded | Deprecated
author: "<author name>"
date: "YYYY-MM-DD"
generated_by: "<skill-name>"
related_docs:
  - "<filename>"
changelog:
  - version: "1.0.0"
    date: "YYYY-MM-DD"
    changes: "Initial version"
---
```

### Required Fields

| Field | Required | Description |
|-------|----------|-------------|
| title | Yes | Document title |
| type | Yes | Document type enum |
| version | Yes | SemVer string |
| status | Yes | Document lifecycle status |
| author | Yes | Creator name |
| date | Yes | Creation/update date |
| generated_by | Yes | Skill that generated this document |
| related_docs | No | List of related document filenames |
| changelog | Yes | Version history entries |

## 2. Version Numbering (SemVer)

Follow Semantic Versioning for documents:

- **MAJOR** (X.0.0): Fundamental scope change, complete rewrite
- **MINOR** (1.X.0): New sections added, significant content changes
- **PATCH** (1.0.X): Typo fixes, formatting, minor clarifications

### Version Bump Rules for Iteration Skills

| Change Type | Version Bump | Example |
|-------------|-------------|---------|
| Fix typo / formatting | PATCH | 1.0.0 → 1.0.1 |
| Add/update section content | MINOR | 1.0.1 → 1.1.0 |
| Change scope / objectives | MAJOR | 1.1.0 → 2.0.0 |
| Status change only | PATCH | 1.0.0 → 1.0.1 |

## 3. File Naming Convention

```
<type>-<project-name>-v<version>.md
```

Examples:
- `brd-user-auth-v1.0.0.md`
- `prd-checkout-flow-v2.1.0.md`
- `trd-payment-service-v1.0.0.md`
- `adr-001-database-choice-v1.0.0.md`
- `api-order-service-v1.2.0.md`
- `tspecs-user-auth-v1.0.0.md`

### Rules

- All lowercase
- Hyphens as separators (no spaces or underscores)
- ADRs include sequential number: `adr-NNN-<title>`
- Version suffix included for traceability

### Multi-Document Naming (for chunked output)

When a document is split into multiple files (see gen-conventions.md L2 strategy):

- **Sub-documents**: `<type>-<project>-<module>-v<ver>.md`
  - Example: `prd-checkout-payment-v1.0.0.md`, `prd-checkout-shipping-v1.0.0.md`
- **Main document** frontmatter MUST include a `parts:` field:
  ```yaml
  parts:
    - prd-checkout-payment-v1.0.0.md
    - prd-checkout-shipping-v1.0.0.md
  ```
- **Sub-document** frontmatter MUST include a `parent:` field:
  ```yaml
  parent: prd-checkout-v1.0.0.md
  ```

## 4. Changelog Format

Within the YAML frontmatter `changelog` array:

```yaml
changelog:
  - version: "1.1.0"
    date: "2025-01-15"
    changes: "Added security section; updated API endpoints"
  - version: "1.0.0"
    date: "2025-01-10"
    changes: "Initial version"
```

For iteration skills, also include an inline changelog section at the end of the document:

```markdown
## Changelog

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.1.0 | 2025-01-15 | Alice | Added security section; updated API endpoints |
| 1.0.0 | 2025-01-10 | Alice | Initial version |
```

## 5. Output Delivery Format

- **Primary format**: Markdown (`.md`)
- **Encoding**: UTF-8
- **Line endings**: LF (Unix-style)
- **Max line length**: No hard limit, but prefer wrapping prose at ~120 chars
- **Tables**: Use GitHub-flavored Markdown tables
- **Diagrams**: Mermaid code blocks (` ```mermaid `)
- **Code examples**: Fenced code blocks with language identifier

## 6. Validation Report Format

See `quality-rules.md` for the standard validation report template.
