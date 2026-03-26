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

## Commit Granularity

When used with `delivery` skill:
- One logical change per commit
- Use Conventional Commits format if the project uses it
- Commit message references the PM document section when applicable
