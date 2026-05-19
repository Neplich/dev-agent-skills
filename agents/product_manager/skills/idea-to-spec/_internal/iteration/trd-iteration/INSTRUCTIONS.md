---
name: trd-iteration
description: Handoff TRD revision requests to Engineer-owned trd-gen. Use when PM document iteration discovers that a Technical Requirements Document (TRD) must change; do not update TRD content directly from PM.
---

# TRD Iteration Handoff

TRD is owned by Engineer. This internal PM instruction only analyzes why a TRD
revision is needed and hands the work to `engineer-agent:trd-gen`.

## When to use

- `trd-validator` reported issues that need fixing
- Architecture review or implementation learning requires TRD updates
- Data model, API, NFR, deployment, or security design changed
- **Not for** creating or editing TRD content directly

## Inputs

- **Required**:
  - `trd_document`: The existing TRD path or summary
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
3. **Prepare Engineer handoff**:
   - affected sections
   - requested change
   - source evidence
   - related PRD / DECISIONS impact
   - validator findings or review comments
4. **Check cross-document impact**:
   - If the change alters a technical decision materially, recommend `adr-gen`
     or `adr-iteration`
   - If API contracts change, keep `related_api` aligned or flag follow-up work
   - If PRD assumptions are contradicted, flag that `prd-iteration` may also be
     required
5. **Hand off**: Route to `engineer-agent:trd-gen` for the actual TRD revision.
6. **Present**: Show the handoff packet and any PM-side docs that may also need
   updates.

## Output Contract

- **Format**: Engineer handoff packet for `engineer-agent:trd-gen`
- **Impact summary**: Section-by-section summary of technical changes needed
- **Cross-doc notes**: Follow-up recommendations for ADR / API / PRD alignment

## Failure Handling

- Missing version metadata -> note it in the Engineer handoff packet
- Requested change conflicts with locked decisions -> surface the conflict and
  ask the user to choose
- Change would remove a required section -> mark as a blocker for Engineer review

## Safety Boundaries

- Never silently remove endpoints, NFR targets, or security controls
- Do not modify TRD files on disk from PM instructions

## Examples

### Example 1

**User**: Update the TRD based on this review:
> CRITICAL: No rollback strategy documented
> WARNING: Throughput target is vague
> We also decided to move avatar storage to object storage

**Expected Output**:

Handoff summary:
- [FIXED] Deployment Architecture: Added rollback strategy for object-storage migration
- [FIXED] NFR table: Added throughput target `500 writes/min`
- [UPDATED] Data Model / System Interactions: Avatar upload path now uses object storage
- Version: `1.1.0` -> `1.2.0`

Route this packet to `engineer-agent:trd-gen` for the actual TRD update.
