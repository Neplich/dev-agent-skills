---
name: tspecs-validator
description: Validate test specifications and test cases against quality standards. Use when users say "validate test specs", "review QA plan", "check test cases", "test spec review", or need to verify requirement coverage, traceability, and test-case completeness before execution.
---

# TEST_SPEC Validator

Validate a TEST_SPEC document against the standardized schema and quality
rules.

## When to use

- Test specification draft is ready for QA or release review
- Before test execution handoff
- After updating test coverage to verify no regressions
- **Read-only** - never modifies the document

## Inputs

- **Required**:
  - `test_spec_document`: The TEST_SPEC to validate
- **Optional**:
  - `related_prd`: PRD to cross-check requirement coverage
  - `related_trd`: TRD to cross-check NFR and architecture-driven tests
  - `related_api`: API document to cross-check endpoint and error coverage
  - `strict_mode`: Treat warnings as errors

## Conventions

Follow `skills/product-dev/idea-to-spec/_internal/_shared/validator-conventions.md` for standard
workflow, output format, failure handling, and safety boundaries.

- **Schema**: `skills/product-dev/idea-to-spec/_internal/_shared/doc-schemas/test-spec-schema.md`
- **Cross-check**: If related docs are provided, verify that requirement IDs,
  endpoint coverage, and NFR tests stay aligned.

## TEST_SPEC-Specific Checks

| Check | Severity | Rule |
| --- | --- | --- |
| Coverage summary | CRITICAL | Every P0 requirement must map to at least one test case |
| Traceability matrix | CRITICAL | Must exist and reconcile uncovered items explicitly |
| Test case completeness | CRITICAL | Every test case must have ID, Preconditions, Steps, and Expected Result |
| Negative / boundary coverage | CRITICAL | Each P0 requirement needs positive coverage plus a negative or boundary test |
| Environment & data | WARNING | Must describe execution environment and required fixtures / roles |
| NFR coverage | WARNING | Quantified PRD / TRD NFRs should map to operational tests |
| Regression / smoke pack | WARNING | Must identify release smoke or regression scope |
| Ambiguous linkage | WARNING | Requirement or endpoint references should be stable and unambiguous |

## Examples

### Example 1

**User**: Validate the test spec for our password reset feature.

**Expected Output**: Validation report. Example: "CRITICAL: `REQ-03` has no
negative coverage", "WARNING: Test environment section does not specify seeded
user roles".
