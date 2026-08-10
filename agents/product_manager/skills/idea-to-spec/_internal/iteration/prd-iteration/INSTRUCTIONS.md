---
name: prd-iteration
description: Iteratively update a PRD document based on change requests, feedback, or validator reports. Use when users say "update PRD", "revise PRD", "iterate PRD", "apply changes to PRD", "fix PRD issues", or need to evolve an existing PRD while maintaining version history.
---

# PRD Iteration

Apply changes to an existing PRD while maintaining version history and quality standards.

## When to use

- PRD validator reported issues that need fixing
- Stakeholder feedback requires PRD updates
- Scope changes or new requirements to incorporate
- **Not for** creating a new PRD from scratch (use `prd-gen`)

## Inputs

- **Required**:
  - `prd_document`: The existing PRD to update (file path or inline)
  - `change_request`: One of:
    - Validator report from `prd-validator`
    - Free-text change description
    - Structured change list
- **Optional**:
  - `preserve_sections`: Sections to not modify (default: none)

## Workflow

1. **Read current document**: Parse existing PRD, extract version metadata and
   `feature_path` metadata. If missing on an old single-level PRD, infer level
   1 from the containing folder. Reconcile `child_features` on every updated
   PRD: derive the current direct child feature paths from the subdirectories
   under `docs/pm/{feature_path}/` and their frontmatter first, refresh the
   field from that derivation, and use `"N/A"` only when no direct children
   exist.

2. **Analyze changes**: Classify the change request:
   - Fix validation issues (CRITICAL first, then WARNING)
   - Apply content changes (additions, modifications, removals)
   - Scope changes (may require MAJOR version bump)

3. **Stage changes**: Prepare the affected-section changes in memory while
   preserving unchanged content; do not write the PRD yet.
   The body must state only the current target state: delete or rewrite
   superseded designs instead of keeping them with "deprecated" / "not part of
   the target architecture" annotations. Record removals in the changelog (see
   the body-consolidation rule in `_internal/_shared/gen-conventions.md`).
   If the change would move the PRD to a child feature path or reveals an
   existing parallel directory is misplaced, stop and present a path conflict
   summary instead of silently editing the wrong PRD.

4. **Evaluate L2b split signals**: After staging the requested content change,
   evaluate the four L2b signals in `_internal/_shared/gen-conventions.md`:
   total lines `> 500`, at least 3 independent domains, at least 15 combined
   `US-*` / `FR-*` table rows, or sections with clear child-feature ownership.
   If any signal is met, present the required child `feature_path` tree,
   section migration map, and downstream mirror impact list, then wait for
   explicit user confirmation. Do not move or split files while waiting. If the
   user rejects the proposal, keep the current path and continue this workflow.

   Complete this assessment before version bump, validation, or presentation.
   Render the result explicitly as `l2b_assessment`, including the triggered
   signals. When triggered, the same response must contain the candidate child
   `feature_path` tree, complete section migration map, downstream mirror
   impacts for Engineer, Design, QA, DevOps, and Security, and the pending
   confirmation boundary. Do not silently continue as though the assessment
   were not triggered.

   When triggered, the existing PRD remains byte-for-byte unchanged until the
   split proposal is accepted or rejected. Only a non-triggered assessment or a
   resolved proposal may continue to the version bump and durable PRD write.

5. **Bump version**: Per `_internal/_shared/output-conventions.md`:
   - Typo/formatting → PATCH
   - New/updated content → MINOR
   - Scope change → MAJOR

6. **Update changelog**: Add entry to both frontmatter and inline changelog.

7. **Run inline validation**: Apply `prd-validator` checks to the updated document. Report any remaining issues.

8. **Present**: Show a diff summary of changes + the full updated document.

## Output Contract

- **Format**: Updated Markdown PRD with bumped version
- **Diff summary**: Section-by-section list of changes
- **Validation result**: Inline validation score of the updated document
- **Changelog**: Updated with new entry
- **L2b assessment**: Triggered signals and the complete confirmation-gated
  split proposal when any signal is met
- **Body consolidation check**: Confirm that superseded behavior appears only
  in changelog or decision history, not in the current-state PRD body

## Failure Handling

- Version metadata missing → add it (start at 1.0.0)
- `feature_path` frontmatter conflicts with the file path → blocked until the
  user confirms whether to correct metadata or migrate the document
- Requested change belongs under a different parent feature → return to
  `idea-to-spec` path clarification or create a PM handoff; do not update the
  current PRD as if it owned the child feature
- L2b proposal is pending confirmation → preserve the current document and
  path; a proposal or read-only assessment is not permission to restructure
- Conflicting changes → ask user to prioritize
- Changes would remove required sections → warn and ask for confirmation
- Post-iteration validation still FAIL → present issues and suggest next iteration

## Safety Boundaries

- Always preserve unchanged sections exactly as-is
- Body consolidation: the body states only the current target state; superseded
  designs are deleted or rewritten, not annotated as deprecated in the body
- "Never silently remove content" means removals must be recorded in the
  changelog and git history — not that content should be kept with status
  annotations; exceptions are ledger-style docs (`DECISIONS.md`, ADRs,
  changelogs, QA `results/`) where history is the design intent
- Confirm with user before MAJOR version bumps
- Do not modify files on disk unless explicitly instructed

## Examples

### Example 1: Fix validator issues

**User**: Update the PRD based on this validator report:
> CRITICAL: US-03 missing acceptance criteria
> WARNING: NFR table missing latency target

**Expected Output**:

Changes summary:
- [FIXED] US-03: Added acceptance criteria "Given... When... Then..."
- [FIXED] NFR table: Added latency target "p95 < 2s"
- Version: 1.0.0 → 1.1.0

Updated PRD with new version header and changelog entry.
