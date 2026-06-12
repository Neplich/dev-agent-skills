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

When creating or updating `docs/engineer/{feature}/IMPLEMENTATION_PLAN.md`:

1. Include frontmatter with `feature`, `version`, `date`, and `last_updated`
2. Start new implementation plans at `version: "0.1.0"` unless the repository
   specifies a stricter convention
3. Update both `version` and `last_updated` when the plan body changes
   substantively, including scope, steps, file lists, delegation, verification,
   status, rollout checks, or diagrams
4. Keep `version` unchanged for typo, formatting, or non-semantic copy edits,
   but refresh `last_updated` when the document is touched

## Commit Granularity

When used with `delivery` skill:
- One logical change per commit
- Use Conventional Commits format if the project uses it
- Commit message references the PM document section when applicable
