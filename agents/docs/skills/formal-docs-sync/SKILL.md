---
name: formal-docs-sync
description: "Internal documentation specialist—not a direct entry point. Invoked by docs-agent to synchronize confirmed feature, deployment, and release facts or backfill current-state formal API documentation."
visibility: internal
---

# Formal Docs Sync

Synchronizes a host project's formal documentation from confirmed process
context and current system evidence. This file owns the entry and execution
gates that apply immediately; load `_internal/INSTRUCTIONS.md` only after the
mode and entry basis are resolved.

## PM Handoff Entry Gate

Require a PM handoff packet or an equivalent confirmed entry basis for the
selected mode. The PM packet definition lives in
`agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md`.
Direct invocation does not bypass the mode-specific gate.

- **Feature delivery:** require an Approved PRD, a Confirmed TRD with impact
  evidence, a confirmed `IMPLEMENTATION_PLAN.md`, and the actual diff and test
  evidence.
- **Deployment verification:** require confirmed deployment scope, the TRD
  deployment surface, deployment configuration, verification commands and
  results, and known environment differences.
- **Release:** require confirmed release scope, a verified version or tag,
  changelog and release-process evidence, and the documentation audit
  conclusion. Release-note content remains owned by
  `pm-agent:release-notes-generator`; this skill only verifies its placement
  and version context.
- **Existing-system backfill:** accept an explicit maintainer backfill request,
  a confirmed repository target, and either a PM feature catalog or permission
  to perform the bounded discovery pass. An implementation plan is not required
  for this mode, but each proposed batch requires maintainer confirmation.

If the selected mode lacks its basis, stop before writing formal docs, report
the missing evidence and owner, and return unresolved product or technical
scope to `pm-agent` or `engineer-agent:trd-gen` as appropriate.

## Modes

| Mode | Purpose | Primary evidence |
| --- | --- | --- |
| Feature delivery | Synchronize formal docs after confirmed implementation | PRD, TRD impact scope, confirmed plan, diff, tests |
| Deployment verification | Synchronize operational facts after deployment validation | TRD deployment surface, configuration, commands, results, environment differences |
| Release | Reconcile formal product and release context | Release scope, verified version/tag, changelog, release evidence, audit conclusion |
| Existing-system backfill | Establish a reviewed current-state baseline in bounded batches | Feature catalog or bounded API discovery, code, schemas, handlers, contract tests |

## MVP Boundary

The MVP acceptance surface covers only the API path for feature delivery and
existing-system backfill: API pages and their API `code_glob` entries in
`docs/site/standards/change-map.yaml`.

Database, design, operations, release notes, and product manuals remain product
target scope with documented lifecycle nodes and templates. Do not claim their
automatic synchronization as an implemented MVP capability. Deployment and
release modes may assess evidence and report future-target outputs without
presenting those outputs as accepted MVP automation.

## Authoritative Execution Gates

Before any write:

1. Resolve one mode and verify its node evidence.
2. Derive a bounded candidate scope from the approved evidence chain. If the
   technical impact scope cannot be established, stop and return a gap packet
   to `engineer-agent:trd-gen`.
3. Present the candidate docs, code globs, evidence sources, exclusions, and
   unresolved items. Wait for maintainer confirmation of the scope.
4. For backfill, execute only one confirmed batch at a time and request
   confirmation again before the next batch.
5. Apply the latest-state discipline: write every changed page as the stable
   current state, validate its claims against code or test evidence, and leave
   new or changed pages unverified for later audit.

The full node protocol, evidence order, batch mechanics, map merge behavior,
trust model, and output format are authoritative in
`_internal/INSTRUCTIONS.md`. Load that file after this gate passes; do not
invent a parallel workflow.

## Missing Documentation Site

If `docs/site/` or its standards are absent, do not create them silently.
Report the missing formal-documentation foundation and offer an explicit
handoff to `docs-site-bootstrap` before synchronization.

## Output

For an executed scope or batch, report:

- mode and confirmed scope
- changed formal docs
- evidence used and verification performed
- change-map delta
- unresolved discrepancies or missing evidence
- coverage and remaining gaps
- the recommended next node or collaboration owner

At closeout, follow the safety-net behavior in
`agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md` and
wait for confirmation before another role or batch unless the user has already
enabled the applicable continuation.
