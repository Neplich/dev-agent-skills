# Output Conventions

> Shared output standards for feature-implementor modules.

## Code Output

When writing code, always:

1. Use the project's language version and syntax (don't use features not available in the project's target)
2. Match the project's indentation (tabs vs spaces, width)
3. End files with a newline
4. Don't leave debug code (console.log, print, dbg!) in production code

## Build Verification

After writing each file:

1. Check that the project compiles/builds without errors
2. If using TypeScript, ensure no type errors
3. If the project has a lint command, ensure no new lint violations

## Implementation Plan Documents

When creating or updating `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`:

1. Include frontmatter with `feature`, `feature_path`, `parent_feature`,
   `feature_level`, `version`, `date`, `last_updated`, `related_prd`, and
   `related_trd`
2. Start new implementation plans at `version: "0.1.0"` unless the repository
   specifies a stricter convention
3. Update both `version` and `last_updated` when the plan body changes
   substantively, including scope, steps, file lists, delegation, verification,
   status, rollout checks, or diagrams
4. Keep `version` unchanged for typo, formatting, or non-semantic copy edits,
   but refresh `last_updated` when the document is touched
5. Ensure `feature_path`, `parent_feature`, and `feature_level` match both the
   PRD and TRD. Legacy single-level docs without these fields may be read as
   level-1 features, but new plans must write the explicit fields.
6. Ensure `related_prd` points to `docs/pm/{feature_path}/PRD.md` and
   `related_trd` points to `docs/engineer/{feature_path}/TRD.md`; mismatches
   block plan writing and must be handed back to PM or `trd-gen`.

## Implementation Plan Closeout

When implementation is complete, update or confirm
`docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md` before QA E2E handoff or
delivery:

1. Set or confirm the final status, such as `status: "Implemented"` when the
   plan has been fully implemented.
2. Add an implementation result section or status table that records completed
   files, completed checks, remaining risks, and next owner.
3. Record deterministic check commands exactly as run, with pass/fail/blocked
   results.
4. For commands not run, record skipped or blocked reasons instead of leaving
   them as pending.
5. A completed plan must not keep unresolved planning-state wording such as
   "waiting for confirmation", "not started", "pending execution", or "model
   eval not executed" unless the same section clearly marks it as historical and
   records the current resolved result.

## Implementation Plan Archive

The active plan entry is always
`docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`. Historical plans live only
under `docs/engineer/{feature_path}/archive/`.

Before creating or replacing an active plan on a `feature_path`:

1. Scan for an existing active plan and the archive directory.
2. If an active plan exists with `status: "Implemented"` and no handling
   decision was recorded, do not overwrite it; ask the user to choose between
   archiving it as completed before creating a new plan, or archiving it as
   `Superseded` with a reason before creating a new plan.
3. If the active plan status is not `Implemented` and no archive on the same
   feature path faithfully preserves its current body, continue updating that
   current plan and bump its version by default; do not force archival or ask
   for an archive decision merely because the active entry exists. If such a
   faithful archive already exists, treat the current round as settled and ask
   the user to choose exactly one of three options: archive it then create a new
   active plan, continue updating it while redeclaring `previous_plan_archive`
   to that faithful archive, or archive it as `Superseded` with a reason then
   create a new active plan. If the user or maintainer explicitly abandons the
   unfinished plan, it may instead be archived as `Superseded` with
   `superseded_reason` before a new active plan is created, using the same
   archive metadata requirements as the `Implemented` branch.
4. If no active plan exists, inspect the feature path's archive history. A new
   active plan must record `previous_plan_archive` pointing to the most recent
   archive when history exists; no backlink is required for a genuinely new
   feature path with no archive history.

When archiving after closeout and user/maintainer approval:

1. Write the archive plan to
   `docs/engineer/{feature_path}/archive/IMPLEMENTATION_PLAN-<scope>.md`,
   where `<scope>` is lower kebab-case and describes the implemented scope. The
   `<scope>` must match the archive filename suffix.
2. Completed archives use `status: "Archived"`. Replaced or abandoned archives
   use `status: "Superseded"` and must add `superseded_reason`. Do not use other
   status values such as `Historical` or `Legacy`.
3. Archive frontmatter must include `implementation_scope`, `status`,
   `archived_at` (YYYY-MM-DD), `archive_approved_by`, and `source_plan` pointing
   to `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`. Preserve the
   original `feature`, `feature_path`, `parent_feature`, `feature_level`,
   `related_prd`, `related_trd`, `version`, `date`, `last_updated`, and `author`.
4. When a new active plan is created after archival, add
   `previous_plan_archive` to its frontmatter pointing to the archive file. This
   also applies when the archive and new active plan are written in the same
   change. When continuing to update the current plan, omit
   `previous_plan_archive` only while the round remains unsettled: its status is
   not `Implemented` and no archive on the same feature path faithfully
   preserves its current body. If the round is already settled by either
   condition, continuing it requires redeclaring `previous_plan_archive` to the
   faithful archive.

## Commit Granularity

When used with `delivery` skill:
- One logical change per commit
- Use Conventional Commits format if the project uses it
- Commit message references the PM document section when applicable
