---
name: docs-audit
description: "Internal documentation specialist—not a direct entry point. Invoked by docs-agent to audit formal documentation against current code and test evidence before release."
visibility: internal
---

# Docs Audit

Audits a host project's formal documentation through a deterministic impact
pass followed by fact verification. This file owns the entry and release gates;
load `_internal/INSTRUCTIONS.md` only after the entry basis and version baseline
are resolved.

## Entry Credentials

Require one confirmed audit entry basis:

- a release scope and pending-release version context;
- an explicit base and target for a bounded audit; or
- a PM handoff packet or equivalent confirmed documentation-audit scope.

Every audit requires `target_release_version`, the exact version
whose documentation is being verified. A maintainer must confirm this value
explicitly. Never infer it from `target_ref`, a branch name, a filename, or any
other context, and never accept `unknown`. If it is missing, inferred, unknown,
or not maintainer-confirmed, return `blocked` before writing a report, stamping
pages, or changing version metadata.

The PM packet definition lives in
`agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md`.
Direct invocation does not waive this gate. If the audit scope is ambiguous,
stop before writing a report or version metadata and return the missing scope
to `docs-agent` or `pm-agent`.

## Audit Phase Selection

Select exactly one phase after the entry credentials are complete:

- **Pre-tag:** the release PR is pending and the target tag may not exist yet.
  Compare `base_ref..target_ref`, verify the complete affected set and all
  release-version surfaces, then return `ready_for_tag` only after one unified
  stamp to the confirmed `target_release_version`.
- **Post-tag:** the actual tag exists. Read the valid pre-tag record and verify
  that the tag and every release-version surface still match the same
  `target_release_version`; do not regenerate or restamp content.

`ready_for_tag` means the documentation and version facts are ready for tag
creation. It must never be described as published or released.
`release_verified` means the post-tag consistency check passed. Any missing,
invalid, inconsistent, or insufficient evidence returns `blocked`.

## Authoritative Execution Gates

Before auditing or writing:

1. Resolve `base_ref`, `target_ref`, and the maintainer-confirmed
   `target_release_version` independently. Default the refs to the most recent
   release tag and pending-release `HEAD`; never treat either ref as the target
   release version.
2. Run the deterministic layer before fact verification. It establishes the
   changed files, change-map matches, affected formal pages, frontmatter
   validity, and suspect pages; it does not turn a missing same-diff document
   update directly into `stale`.
3. Verify every affected page against current code or test evidence under the
   trust model in
   `agents/product_manager/skills/idea-to-spec/_internal/_shared/consumption-contract.md`.
   Code and tests are ground truth; preserve each conflicting document claim,
   code fact, and impact.
4. Treat `stale`, `mismatch`, a page that remains unverified after fact review,
   and insufficient evidence as release blockers. The literal frontmatter value
   `unverified` remains valid and is not by itself a factual conclusion. Only a
   complete affected set whose conclusions are all `verified` may receive one
   unified pre-tag stamp; never stamp a verified subset.
5. `last_verified_version` records the version against which page content was
   verified; it is not publication state. Record every page's value before the
   pre-tag stamp. Do not add a persistent `baseline_verified_version` field.
6. Outside a valid pre-tag release audit, a page without a stampable confirmed
   version keeps its current value, and a new page keeps `unverified`, as
   required by the shared frontmatter contract. Never invent a version merely
   to replace `unverified`.

The exact two-layer protocol, status semantics, report format, stamp update,
and release handoff live in `_internal/INSTRUCTIONS.md`. Load that file only
after this gate passes; do not replace it with an ad hoc audit workflow.

## Missing Documentation Site

If `docs/site/standards/change-map.yaml` or the formal site foundation is
absent, do not initialize it silently. Report the missing audit foundation and
offer an explicit handoff to `docs-site-bootstrap`; wait for confirmation.

## Output

Report:

- selected phase, resolved `base_ref`, `target_ref`, and confirmed
  `target_release_version`
- changed files, change-map matches, and affected formal pages
- each page's pre-stamp `last_verified_version`, document claims, and code or
  test evidence
- `verified`, `stale`, or `mismatch` conclusions
- blockers, review commands, and any unified stamp update
- phase result: `ready_for_tag`, `release_verified`, or `blocked` with a
  concrete to-do list

At closeout, return the audit conclusion to the release handoff and follow the
safety-net behavior in
`agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md`.
Wait for confirmation before another role acts unless the user has enabled the
applicable continuation.
