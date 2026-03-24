---
name: api-validator
description: Validate API documentation against quality standards. Use when users say "validate API docs", "review API spec", "check API documentation", or need to verify endpoint completeness, schema consistency, and example coverage of API documentation.
---

# API Documentation Validator

Validate API documentation against the standardized schema and quality rules.

## When to use

- API docs written and need quality check
- Before publishing API reference
- After updating API docs to verify no regressions
- **Read-only** — never modifies the document

## Inputs

- **Required**:
  - `api_document`: The API documentation to validate
- **Optional**:
  - `code_source`: Source code to cross-check endpoint coverage

## Conventions

Follow `skills/product-dev/idea-to-spec/_internal/_shared/validator-conventions.md` for standard workflow, output format, failure handling, and safety boundaries.

- **Schema**: `skills/product-dev/idea-to-spec/_internal/_shared/doc-schemas/api-schema.md`
- **Cross-check**: If source code provided, verify all routes are documented.

## API-Specific Checks

| Check | Severity | Rule |
|-------|----------|------|
| Auth section | CRITICAL | Must include auth method and example header |
| Endpoint completeness | CRITICAL | Each endpoint must have method, path, ≥ 1 response |
| Error codes | CRITICAL | Each endpoint must document error responses |
| Request/response schemas | WARNING | Should have typed field definitions |
| Working example | WARNING | At least 1 complete curl example |
| Model definitions | WARNING | All referenced models must be defined |
| Code coverage | WARNING | If code provided, all routes must be documented |


## Examples

### Example 1

**User**: Validate our API documentation.

**Expected Output**: Validation report. Example: "CRITICAL: POST /users endpoint missing error response codes", "WARNING: No curl example provided".
