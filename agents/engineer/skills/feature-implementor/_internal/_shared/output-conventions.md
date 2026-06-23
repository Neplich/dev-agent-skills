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

## Commit Granularity

When used with `delivery` skill:
- One logical change per commit
- Use Conventional Commits format if the project uses it
- Commit message references the PM document section when applicable
