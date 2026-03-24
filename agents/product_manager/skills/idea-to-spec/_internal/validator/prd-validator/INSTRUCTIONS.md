---
name: prd-validator
description: Validate a Product Requirements Document (PRD) against quality standards. Use when users say "validate PRD", "review PRD", "check PRD quality", "PRD review", or need to assess completeness and testability of product requirements before development.
---

# PRD Validator

Validate a PRD document against the standardized schema and quality rules.

## When to use

- PRD draft ready for quality review
- Before handing off PRD to engineering
- After `prd-iteration` to verify improvements
- **Read-only** — never modifies the document

## Inputs

- **Required**:
  - `prd_document`: The PRD to validate (file path or inline content)
- **Optional**:
  - `strict_mode`: Treat warnings as errors (default: false)
  - `related_brd`: BRD to cross-check alignment

## Conventions

Follow `skills/product-dev/idea-to-spec/_internal/_shared/validator-conventions.md` for standard workflow, output format, failure handling, and safety boundaries.

- **Schema**: `skills/product-dev/idea-to-spec/_internal/_shared/doc-schemas/prd-schema.md`
- **Cross-check**: If BRD provided, verify all BRD objectives map to PRD features.

## PRD-Specific Checks

| Check | Severity | Rule |
|-------|----------|------|
| P0 acceptance criteria | CRITICAL | Every P0 user story/requirement must have testable AC |
| User persona | CRITICAL | At least 1 persona with needs and pain points |
| Primary user flow | CRITICAL | At least 1 documented user flow |
| Non-goals | WARNING | Must list at least 1 non-goal |
| NFR metrics | WARNING | NFRs must have numeric targets |
| Open questions | WARNING | Should have owners and deadlines |
| BRD alignment | WARNING | If BRD provided, all BRD objectives must map to PRD features |


## Examples

### Example 1

**User**: Review this PRD for quality.

**Expected Output**: Validation report with scores, critical issues (e.g., "US-03 missing acceptance criteria"), warnings, and suggestions.
