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
3. **Evaluate L2b split signals**: Evaluate the proposed TRD content against
   the L2b signals in `_internal/_shared/gen-conventions.md`: total lines
   `> 500`, at least 3 independent domains, at least 15 related PRD `US-*` /
   `FR-*` rows, or sections with clear child-feature ownership. When any signal
   is met, include a child `feature_path` tree, section migration map, and
   downstream mirror impact list in the handoff, and require explicit user
   confirmation before Engineer changes paths. A TRD split must mirror the
   confirmed PRD child paths; it cannot define an independent technical tree.
4. **Prepare Engineer handoff**:
   - affected sections
   - requested change
   - source evidence
   - related PRD / DECISIONS impact
   - validator findings or review comments
   - an explicit requirement that the updated TRD body states only the current
     target state: superseded designs are deleted or rewritten, removals are
     recorded in the changelog and git history, and ledger-style docs
     (`DECISIONS.md`, ADRs) keep history per the body-consolidation rule in
     `_internal/_shared/gen-conventions.md`
5. **Check cross-document impact**:
   - If the change alters a technical decision materially, route ADR creation
     or revision to `engineer-agent:trd-gen`
   - If API contracts change, keep `related_api` aligned or flag follow-up work
   - If PRD assumptions are contradicted, flag that `prd-iteration` may also be
     required
6. **Hand off**: Route to `engineer-agent:trd-gen` for the actual TRD revision.
7. **Present**: Show the handoff packet and any PM-side docs that may also need
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
- L2b proposal is rejected -> keep the current PRD/TRD mirror and continue the
  existing revision handoff without structural changes

## Safety Boundaries

- Never silently remove endpoints, NFR targets, or security controls — "never
  silently" means removals must be recorded in the changelog and git history,
  not that superseded content stays in the body with status annotations
- Do not modify TRD files on disk from PM instructions
- Do not authorize a PM directory move until the downstream mirror impact list
  and mirror handling decision are confirmed

## Examples

### Example 1

**User**: Update the TRD based on this review:
> CRITICAL: No rollback strategy documented
> WARNING: Throughput target is vague
> We also decided to move avatar storage to object storage

**Expected Output**:

Handoff summary:
- [NEEDS ENGINEER] Deployment Architecture: add rollback strategy for object-storage migration
- [NEEDS ENGINEER] NFR table: clarify throughput target `500 writes/min`
- [NEEDS ENGINEER] Data Model / System Interactions: update avatar upload path for object storage
- Suggested version impact: `1.1.0` -> `1.2.0`

Route this packet to `engineer-agent:trd-gen` for the actual TRD update.
