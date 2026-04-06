---
name: iteration-coordinator
description: Coordinate multi-document iteration when a change affects multiple project documents. Use when users say "update all docs", "cascade change", "multi-doc iteration", "propagate changes", "sync documents", or need to apply a change across BRD, PRD, TRD, and test specs while maintaining consistency.
---

# Iteration Coordinator

Orchestrate multi-document iteration by running change impact analysis, then
sequentially updating affected documents while maintaining cross-document
consistency.

This is an internal secondary skill. Expect `idea-to-spec` to load it after an
existing-project update has already been framed and the affected doc set is
likely broader than a single artifact.

## When to use

- A change affects multiple documents (for example scope change impacts BRD,
  PRD, TRD)
- After `change-impactor` identifies multiple documents needing updates
- After `idea-to-spec` or stakeholder review stabilizes a change request that
  now needs to be propagated across the doc set
- Need to ensure all project documents stay in sync after a change
- **Orchestrates** iteration and validator skills; does not modify documents
  directly

## Inputs

- **Required**:
  - `change_description`: What changed and why
- **Optional**:
  - `docs_directory`: Path to project documents (default: `docs/`)
  - `impact_report`: Pre-computed impact report from `change-impactor` (skips
    re-analysis)
  - `handoff_packet`: Stabilized context packet from `idea-to-spec` or another
    upstream skill
  - `auto_validate`: Run validators after each iteration (default: true)

## Shared Routing Contract

Before selecting per-document iteration or validator skills, read
`agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md`.

Use it to:

- select the direct lifecycle skill for BRD / PRD / TRD / API / ADR /
  TEST_SPEC
- keep update ordering aligned with `idea-to-spec` and `flow`
- decide when fallback regeneration is actually necessary

## Workflow

1. **Assess impact**: If no `impact_report` is provided, run
   `change-impactor` to identify affected documents and the recommended update
   order.
2. **Plan iteration sequence**: Order documents by dependency using the shared
   lifecycle map:
   - BRD -> PRD -> TRD -> API -> TEST_SPEC
   - ADRs update in parallel if affected
3. **Iterate sequentially**: For each affected document in order:
   - Show the user what will change in this document
   - Run the corresponding direct iteration skill from the shared lifecycle
     matrix
   - If the document type falls outside the shared lifecycle matrix, fall back
     to focused regeneration with the closest `*-gen` skill, then produce a
     diff summary before asking the user to confirm
   - If `auto_validate`, run the corresponding validator
   - Report results and ask the user to confirm before proceeding
4. **Cross-consistency check**: After all iterations:
   - Run `trace-check` on the updated documents
   - Flag any new inconsistencies introduced
5. **Final summary**: Report all changes, version bumps, and remaining issues.

## Output Contract

- **Format**: Coordination report plus all updated documents
- **Structure**:
  ```markdown
  ## Iteration Coordination Report

  ### Change
  <description>

  ### Documents Updated
  | Document | Version Change | Iteration Result | Validation Score |
  |----------|---------------|------------------|------------------|

  ### Cross-Consistency
  - Trace check result: PASS / NEEDS_WORK
  - New gaps: ...

  ### Remaining Issues
  - ...
  ```

## Failure Handling

- Iteration skill fails on a document -> report the error, ask to skip or retry
- Validator FAIL after iteration -> offer to re-iterate or accept as-is
- Document type outside the shared lifecycle matrix -> use focused regeneration
  + validator + `version-differ`, and flag that the lifecycle is only partially
  automated for that custom type
- Circular dependency detected -> break the cycle and warn the user
- Too many documents affected (> 10) -> ask the user to prioritize

## Safety Boundaries

- Always confirm with the user before each document modification
- Never auto-commit changes; present diffs for review
- Do not modify documents that were explicitly excluded
- Checkpoint after each document iteration

## Examples

### Example 1: Auth system migration

**User**: We're migrating from session auth to JWT. Update all project docs.

**Expected Output**:

```text
Impact Analysis: 5 documents affected
  1. ADR (new: ADR-005 JWT migration) - HIGH
  2. PRD (auth requirements section) - HIGH
  3. TRD (auth architecture, API security) - HIGH
  4. API docs (auth headers) - MEDIUM
  5. Test specs (auth test cases) - MEDIUM

Starting iteration sequence...

Step 1/5: Creating ADR-005...
  OK ADR created, validation: PASS (4.5/5)

Step 2/5: Updating PRD auth requirements...
  OK PRD updated 1.2.0 -> 1.3.0, validation: PASS (4.0/5)

[Continue?]
```

## References

- `agents/product_manager/skills/idea-to-spec/_internal/_shared/output-conventions.md` -> Version bump rules
- `agents/product_manager/skills/idea-to-spec/_internal/_shared/quality-rules.md` -> Validation scoring
- `agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md` -> Routing and lifecycle coverage
