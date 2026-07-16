---
name: docs-site-bootstrap
description: "Internal documentation specialist—not a default entry point. Invoked by docs-agent when a user explicitly requests initialization of a formal documentation site in a confirmed host repository."
visibility: internal
---

# Docs Site Bootstrap

Initializes a host repository's formal documentation foundation under the fixed
root `docs/site/`. This file owns the entry, opt-in, idempotency, and conflict
gates. Load `_internal/INSTRUCTIONS.md` only after every gate below passes.

## Entry Credentials

Require both of these credentials before inspecting or writing bootstrap
targets:

- the user explicitly requests initialization or creation of the formal
  documentation site; and
- the target host repository path is confirmed.

An explicit bootstrap request and a confirmed repository path are the
specialist entry basis. If either is missing, stop before writing and return to
`docs-agent` or `pm-agent` for clarification. The generated root is always
`docs/site/`; do not silently adapt the scaffold to another root.

## Authoritative Opt-In Gate

Bootstrap is opt-in. Do not trigger it because another workflow merely discovers
that `docs/site/` is absent. In particular, `formal-docs-sync` and `docs-audit`
may explain the missing foundation and suggest this specialist, but they must
not initialize it or create a partial scaffold on the user's behalf.

Before writing, restate the confirmed repository and `docs/site/` target, then
confirm that the request covers the generated manifest and the complete
scaffold described in `_internal/INSTRUCTIONS.md`.

## Idempotency and Conflict Gate

Build the complete target inventory and establish
`docs/site/.meta/bootstrap-manifest.json` before applying template files. For
every target path:

- create it when it does not exist and record `created`;
- skip it when its content is identical to the embedded template and record
  `skipped-identical`;
- if it differs, report it in the complete conflict list and stop before
  overwriting that file; never preserve a conflict silently.

For each conflict, require the user to choose overwrite, explicit merge, or
keep the existing file. A keep decision records `kept-as-is` in the manifest;
later runs must skip template-equality enforcement for that exact path. An
existing `kept-as-is` record is not permission to overwrite or normalize the
file.

Do not partially overwrite conflicting files before the user resolves them.
Non-conflicting new files may be generated within the already confirmed
bootstrap scope. Repeated execution must produce zero content changes when the
templates and manifest decisions are unchanged, and must never reset an
existing change map, release metadata, or formal documentation page.

## Execution Source

The authoritative path inventory, manifest state transitions, write order,
read-back checks, and complete embedded template text live in
`_internal/INSTRUCTIONS.md`. Load that single instruction entry only after the
entry and opt-in gates pass. Render its templates exactly except for explicit
user-approved conflict resolution; do not fetch scaffold files from another
repository.

## Output

Report:

- confirmed host repository and generated root
- created and identical-skipped paths
- `kept-as-is` paths and the user decision that authorized each one
- unresolved conflicts and available resolution choices
- manifest path and read-back result
- whether a repeat run would be zero-diff
- recommended handoff to `formal-docs-sync`, then wait for confirmation

At closeout, follow the safety-net behavior in
`agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md`.
