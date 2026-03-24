---
name: trd-iteration
description: Iteratively update a Technical Requirements Document (TRD) based on change requests, architecture review feedback, or validator reports. Use when users say "update TRD", "revise tech spec", "iterate technical design", "apply architecture feedback", or need to evolve an existing TRD while maintaining version history.
---

# TRD Iteration

Apply changes to an existing TRD while preserving technical rationale, version
history, and cross-document consistency.

## When to use

- `trd-validator` reported issues that need fixing
- Architecture review or implementation learning requires TRD updates
- Data model, API, NFR, deployment, or security design changed
- **Not for** creating a new TRD from scratch (use `trd-gen`)

## Inputs

- **Required**:
  - `trd_document`: The existing TRD to update (file path or inline)
  - `change_request`: One of:
    - Validator report from `trd-validator`
    - Architecture review comments
    - Free-text change description
    - Structured change list
- **Optional**:
  - `related_prd`: PRD to preserve requirement alignment
  - `related_api`: API doc to preserve contract alignment
  - `preserve_sections`: Sections that must remain unchanged

## Workflow

1. **Read current document**: Parse the TRD and extract version metadata,
   related docs, and section structure.
2. **Classify the requested change**:
   - Validation fix
   - Technical clarification
   - Architecture / API / data-model update
   - Scope or operating-model change
3. **Apply focused updates**:
   - Preserve unchanged sections exactly
   - Update only the affected architecture, data model, API, NFR, security,
     deployment, observability, testing, or risk sections
   - Keep diagrams, tables, and endpoint references consistent
4. **Check cross-document impact**:
   - If the change alters a technical decision materially, recommend `adr-gen`
     or `adr-iteration`
   - If API contracts change, keep `related_api` aligned or flag follow-up work
   - If PRD assumptions are contradicted, flag that `prd-iteration` may also be
     required
5. **Bump version**: Use
`skills/product-dev/idea-to-spec/_internal/_shared/output-conventions.md`.
6. **Update changelog**: Add a frontmatter entry and inline changelog entry.
7. **Run inline validation**: Apply `trd-validator` checks to the updated doc.
8. **Present**: Show a diff summary, validation result, and the updated TRD.

## Output Contract

- **Format**: Updated Markdown TRD with bumped version
- **Diff summary**: Section-by-section summary of technical changes
- **Validation result**: Inline `trd-validator` score and remaining issues
- **Cross-doc notes**: Follow-up recommendations for ADR / API / PRD alignment

## Failure Handling

- Missing version metadata -> initialize at `1.0.0`
- Requested change conflicts with locked decisions -> surface the conflict and
  ask the user to choose
- Change would remove a required section -> warn before proceeding
- Post-iteration validation still FAIL -> list unresolved issues and suggest
  another iteration

## Safety Boundaries

- Preserve unchanged sections exactly
- Never silently remove endpoints, NFR targets, or security controls
- Confirm with the user before MAJOR version bumps
- Do not modify files on disk unless explicitly instructed

## Examples

### Example 1

**User**: Update the TRD based on this review:
> CRITICAL: No rollback strategy documented
> WARNING: Throughput target is vague
> We also decided to move avatar storage to object storage

**Expected Output**:

Changes summary:
- [FIXED] Deployment Architecture: Added rollback strategy for object-storage migration
- [FIXED] NFR table: Added throughput target `500 writes/min`
- [UPDATED] Data Model / System Interactions: Avatar upload path now uses object storage
- Version: `1.1.0` -> `1.2.0`

Updated TRD with changelog and inline validation result.
