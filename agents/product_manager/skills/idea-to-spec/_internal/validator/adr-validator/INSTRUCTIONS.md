---
name: adr-validator
description: Validate an Architecture Decision Record (ADR) against quality standards. Use when users say "validate ADR", "review ADR", "check ADR quality", or need to verify an ADR has proper context, clear decision, consequences, and alternatives before acceptance.
---

# ADR Validator

Validate an ADR against the standardized schema and quality rules.

## When to use

- ADR written and needs quality check before status change to Accepted
- Reviewing existing ADRs for completeness
- **Read-only** — never modifies the document

## Inputs

- **Required**:
  - `adr_document`: The ADR to validate

## Conventions

Follow `agents/product_manager/skills/idea-to-spec/_internal/_shared/validator-conventions.md` for standard workflow, output format, failure handling, and safety boundaries.

- **Schema**: `agents/product_manager/skills/idea-to-spec/_internal/_shared/doc-schemas/adr-schema.md`

## ADR-Specific Checks

| Check | Severity | Rule |
|-------|----------|------|
| Valid status | CRITICAL | Must be Proposed/Accepted/Deprecated/Superseded |
| Context forces | CRITICAL | Must describe at least 1 technical and 1 business force |
| Decision clarity | CRITICAL | Must be unambiguous "We will..." statement |
| Consequences balance | CRITICAL | At least 1 positive and 1 negative consequence |
| Alternatives | CRITICAL | ≥ 2 alternatives with pros, cons, rejection reason |
| Superseded reference | WARNING | If Superseded, must reference the superseding ADR |


## Examples

### Example 1

**User**: Check this ADR before we accept it.

**Expected Output**: Validation report. Example: Score 4.2/5, PASS. Warning: "Alternative 2 missing rejection reason."
