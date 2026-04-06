---
name: adr-gen
description: Generate an Architecture Decision Record (ADR) for technical decisions. Use when users say "create ADR", "architecture decision", "record decision", "ADR", "document tech choice", or need to formalize why a specific technology, pattern, or approach was chosen.
---

# ADR Generator

Generate an Architecture Decision Record following the standardized ADR schema.

## When to use

- Making or documenting a significant technical decision
- Choosing between technologies, patterns, or architectural approaches
- Need a formal record of why a decision was made for future reference
- **Simplest** gen skill — ADR format is lightweight and well-defined

## Inputs

- **Required**:
  - `decision_context`: What decision needs to be made or was made
- **Optional**:
  - `alternatives`: Known alternatives to evaluate
  - `constraints`: Technical or organizational constraints
  - `adr_number`: Sequential ADR number (auto-incremented if not provided)
  - `existing_adrs_dir`: Directory to scan for existing ADRs to determine next number

## Conventions

Follow `agents/product_manager/skills/idea-to-spec/_internal/_shared/gen-conventions.md` for standard workflow, failure handling, and safety boundaries.

- **Schema**: `agents/product_manager/skills/idea-to-spec/_internal/_shared/doc-schemas/adr-schema.md`
- **Metadata**: `type: ADR`, version `1.0.0`, status `Proposed`
- **Naming**: `docs/engineer/<feature-name>/ADR-<NNN>-<decision-title>.md`

## Workflow Details

Clarifying questions (if input is brief, max 3): what forces drive this decision, what alternatives were considered, what constraints exist.

Generate ADR:
- Title: `ADR-<NNN>: <Descriptive Title>`
- Status: `Proposed`
- Context: Technical and business forces
- Decision: Clear "We will..." statement
- Consequences: Positive, Negative, and Neutral
- Alternatives Considered: ≥ 2 with pros/cons/rejection reason

**ADR-specific failure handling**:
- No alternatives known → research common approaches, present as `[RESEARCHED]`
- Decision already made → document retrospectively, note in Context section
- Cannot determine ADR number → start at `001`
- Present alternatives fairly — avoid bias toward a predetermined choice

## Examples

### Example 1: Database choice

**User**: Create an ADR for choosing PostgreSQL over MongoDB for our user management service.

**Expected Output** (abbreviated):

```
ADR-001: Use PostgreSQL for User Management Service

Status: Proposed

Context: The user management service requires ACID transactions for account operations, complex queries for reporting, and strong schema enforcement...

Decision: We will use PostgreSQL 16 as the primary database for the user management service.

Consequences:
- Positive: ACID compliance, mature ecosystem, strong SQL support
- Negative: Less flexible schema evolution compared to document stores
- Neutral: Team has moderate PostgreSQL experience

Alternatives Considered:
| MongoDB | Flexible schema, horizontal scaling | No ACID by default, weaker joins | User data is relational; ACID is critical |
| MySQL | ACID, wide adoption | Fewer advanced features (CTEs, JSON) | PostgreSQL offers better JSON + relational hybrid |
```
