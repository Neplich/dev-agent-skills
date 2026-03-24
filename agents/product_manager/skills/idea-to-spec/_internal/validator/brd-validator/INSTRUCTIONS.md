---
name: brd-validator
description: Validate a Business Requirements Document (BRD) against quality standards. Use when users say "validate BRD", "review BRD", "check BRD quality", "BRD review", or need to assess completeness, consistency, and quality of a BRD before approval.
---

# BRD Validator

Validate a BRD document against the standardized schema and quality rules.

## When to use

- BRD draft is ready for quality review
- Before submitting BRD for stakeholder approval
- After `brd-iteration` to verify improvements
- **Read-only** — produces a validation report, never modifies the document

## Inputs

- **Required**:
  - `brd_document`: The BRD to validate (file path or inline content)
- **Optional**:
  - `strict_mode`: If true, treat warnings as errors (default: false)

## Conventions

Follow `skills/product-dev/idea-to-spec/_internal/_shared/validator-conventions.md` for standard workflow, output format, failure handling, and safety boundaries.

- **Schema**: `skills/product-dev/idea-to-spec/_internal/_shared/doc-schemas/brd-schema.md`

## BRD-Specific Checks

In addition to generic quality rules:

| Check | Severity | Rule |
|-------|----------|------|
| SMART objectives | CRITICAL | Each objective must be Specific, Measurable, with target date |
| Stakeholder table | CRITICAL | Must have ≥ 3 stakeholders including product owner |
| ROI section | WARNING | Must include at least rough estimates |
| Risk mitigations | CRITICAL | Every risk must have a mitigation strategy |
| Out-of-scope items | WARNING | Must list ≥ 2 items |
| Success criteria | CRITICAL | Each criterion must be measurable |
| Milestone dates | WARNING | ≥ 3 milestones with dates |


## Examples

### Example 1

**User**: Validate this BRD for our checkout redesign project.

**Expected Output** (abbreviated):

```markdown
## Validation Report
- Document: brd-checkout-redesign-v1.0.0.md
- Type: BRD
- Overall Score: 3.6 / 5
- Status: NEEDS_WORK

### Dimension Scores
| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| Completeness | 4/5 | 30% | 1.2 |
| Consistency | 3/5 | 25% | 0.75 |
| Clarity | 4/5 | 25% | 1.0 |
| Testability | 3/5 | 20% | 0.6 |

### Critical Issues
1. [CRITICAL] Business Objectives: Objective 2 missing target date
2. [CRITICAL] Risk Assessment: Risk 3 has no mitigation strategy

### Warnings
1. [WARNING] ROI section uses vague language ("significant savings")
```
