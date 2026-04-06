---
name: trd-validator
description: Validate a Technical Requirements Document (TRD) against quality standards. Use when users say "validate TRD", "review tech spec", "check TRD quality", "technical review", or need to verify architecture completeness, API coverage, and NFR quantification before implementation.
---

# TRD Validator

Validate a TRD document against the standardized schema and quality rules.

## When to use

- TRD draft ready for architecture review
- Before starting implementation
- **Read-only** — never modifies the document

## Inputs

- **Required**:
  - `trd_document`: The TRD to validate
- **Optional**:
  - `related_prd`: PRD to cross-check API and requirement coverage
  - `strict_mode`: Treat warnings as errors

## Conventions

Follow `agents/product_manager/skills/idea-to-spec/_internal/_shared/validator-conventions.md` for standard workflow, output format, failure handling, and safety boundaries.

- **Schema**: `agents/product_manager/skills/idea-to-spec/_internal/_shared/doc-schemas/trd-schema.md`
- **Cross-check**: If PRD provided, verify all PRD endpoints appear in TRD.

## TRD-Specific Checks

| Check | Severity | Rule |
|-------|----------|------|
| Architecture diagram | CRITICAL | At least 1 Mermaid diagram present |
| Tech stack rationale | CRITICAL | Every technology choice must have a rationale |
| NFR targets | CRITICAL | All NFRs must have numeric, measurable targets |
| API completeness | CRITICAL | If PRD provided, all PRD endpoints must appear |
| Security section | CRITICAL | Must address auth, encryption, at least 1 threat |
| Sequence diagram | WARNING | At least 1 for primary flow |
| Deployment/rollback | WARNING | Must describe rollback strategy |
| Testing strategy | WARNING | Must cover at least 2 test levels |


## Examples

### Example 1

**User**: Validate the TRD for our payment service.

**Expected Output**: Report with scores. Example critical: "NFR table row 'Throughput' missing numeric target", warning: "No rollback strategy documented".
