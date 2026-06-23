---
name: adr-gen
description: Deprecated PM-owned ADR generator. Do not use for new generation; route ADR requests to engineer-agent:trd-gen.
---

# ADR Generator

Deprecated PM-owned generator retained for historical reference. New ADRs are
Engineer-owned and must be routed to `engineer-agent:trd-gen` with confirmed PM
scope, decision context, alternatives, constraints, and feature path evidence.

## When to use

- Making or documenting a significant technical decision
- Choosing between technologies, patterns, or architectural approaches
- Need a formal record of why a decision was made for future reference
- **Deprecated**: do not trigger this PM generator for new ADRs. Use
  `engineer-agent:trd-gen` so ADRs are written with the TRD and feature path
  contract.

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
- **Naming**: `docs/engineer/{feature_path}/ADR-<NNN>-<decision-title>.md`

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
