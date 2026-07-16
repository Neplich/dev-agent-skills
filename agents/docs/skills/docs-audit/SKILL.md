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

The PM packet definition lives in
`agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md`.
Direct invocation does not waive this gate. If the audit scope is ambiguous,
stop before writing a report or version metadata and return the missing scope
to `docs-agent` or `pm-agent`.

## Authoritative Execution Gates

Before auditing or writing:

1. Resolve the base and target. Default to the most recent release tag and the
   pending-release `HEAD`; accept an explicit base and target when supplied.
   If no tag, Release, or explicit version anchor exists, the working scope may
   still be audited, but it has no stampable version anchor.
2. Run the deterministic layer before fact verification. It establishes the
   changed files, change-map matches, affected formal pages, frontmatter
   validity, and suspect pages; it does not turn a missing same-diff document
   update directly into `stale`.
3. Verify every affected page against current code or test evidence under the
   trust model in
   `agents/product_manager/skills/idea-to-spec/_internal/_shared/consumption-contract.md`.
   Code and tests are ground truth; preserve each conflicting document claim,
   code fact, and impact.
4. Treat `stale` and `mismatch` as release blockers. Only a complete affected
   set whose conclusions are all `verified` may receive one unified version
   stamp; never stamp a verified subset.
5. When the version anchor is unavailable, record
   `version_anchor: unavailable` and do not write `last_verified_version` or
   invent a version, even if every audited claim is verified.

The exact two-layer protocol, status semantics, report format, stamp update,
and release handoff live in `_internal/INSTRUCTIONS.md`. Load that file only
after this gate passes; do not replace it with an ad hoc audit workflow.

## Missing Documentation Site

If `docs/site/standards/change-map.yaml` or the formal site foundation is
absent, do not initialize it silently. Report the missing audit foundation and
offer an explicit handoff to `docs-site-bootstrap`; wait for confirmation.

## Output

Report:

- resolved base, target, and version anchor availability
- changed files, change-map matches, and affected formal pages
- per-page document claims and code or test evidence
- `verified`, `stale`, or `mismatch` conclusions
- blockers, review commands, and any unified stamp update
- release recommendation: proceed, or blocked with a concrete to-do list

At closeout, return the audit conclusion to the release handoff and follow the
safety-net behavior in
`agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md`.
Wait for confirmation before another role acts unless the user has enabled the
applicable continuation.
