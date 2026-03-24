---
name: adr-iteration
description: Update an ADR's status or content based on review outcomes. Use when users say "accept ADR", "deprecate ADR", "supersede ADR", "update ADR status", or need to transition an ADR through its lifecycle (Proposed → Accepted → Deprecated → Superseded).
---

# ADR Iteration

Update an existing ADR's status or content following the ADR lifecycle.

## When to use

- ADR has been reviewed and needs status change (Proposed → Accepted)
- ADR is being deprecated or superseded
- Minor content updates based on review feedback
- **Simplest** iteration skill — primarily status transitions

## Inputs

- **Required**:
  - `adr_document`: The existing ADR
  - `action`: One of:
    - `accept` — transition to Accepted
    - `deprecate` — transition to Deprecated (requires rationale)
    - `supersede` — transition to Superseded (requires superseding ADR number)
    - `update` — content changes without status change
- **Optional**:
  - `rationale`: Reason for status change
  - `superseded_by`: ADR number that supersedes this one
  - `content_changes`: Specific content updates

## Workflow

1. **Read current ADR**: Parse status and content.
2. **Validate transition**: Check against allowed transitions in `adr-schema.md`:
   - Proposed → Accepted / Deprecated
   - Accepted → Deprecated / Superseded
   - Deprecated / Superseded → (terminal, no further transitions)
3. **Apply changes**: Update status, add rationale, update metadata.
4. **Bump version**: PATCH for status change, MINOR for content changes.
5. **Update changelog**.
6. **Run inline validation**: Apply adr-validator checks.
7. **Present**: Updated ADR.

## Output Contract

- **Format**: Updated Markdown ADR
- **Status transition**: Clearly documented in changelog

## Failure Handling

- Invalid transition (e.g., Deprecated → Accepted) → explain valid transitions, ask user to clarify
- Missing superseded_by for supersede action → ask for the ADR number
- Terminal status → inform user this ADR cannot be further transitioned

## Safety Boundaries

- Validate transition rules before applying
- Never skip directly to terminal states without proper rationale

## Examples

### Example 1: Accept an ADR

**User**: Accept ADR-001, it was approved in today's architecture review.

**Expected Output**:
- Status: Proposed → Accepted
- Version: 1.0.0 → 1.0.1
- Changelog: "Status changed to Accepted following architecture review on 2025-01-15"
