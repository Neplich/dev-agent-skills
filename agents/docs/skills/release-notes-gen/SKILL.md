---
name: release-notes-gen
description: "Generate, preview, confirm, index, and validate a host documentation site's versioned Release Notes before GitHub Release work. Use after docs-agent routes confirmed version facts and release evidence."
visibility: internal
---

# Release Notes Generator

Generates a versioned Release Notes page inside an existing formal
documentation site, waits for user or maintainer confirmation, then updates
the host release metadata and indexes and runs the host documentation checks.
This file owns the entry, feature-scope, confirmation, and role-boundary gates.
Load `_internal/INSTRUCTIONS.md` only after the entry basis is complete.

## Mandatory Release-Notes Checkpoint

An ambiguous or unconfirmed version returns to `pm-agent`; a missing site or
Release Notes foundation returns to `docs-site-bootstrap`. Before explicit body
confirmation, keep release metadata, indexes, navigation, tags, GitHub Release,
and deployment surfaces unchanged. After confirmation, update only the
host-required derived surfaces, run the real host documentation checks, and
return a complete handoff to `docs-audit` containing confirmed version, scope,
evidence, page path, confirmation source, changed derived surfaces, and check
results. Tag creation, GitHub Release creation/publication, image publication,
and deployment remain zero-write external boundaries.

## PM Handoff And Feature-Scope Gate

Require a PM handoff packet or an equivalent confirmed release entry basis
that identifies all of the following:

- the target host repository;
- the confirmed target release version and release scope;
- the evidence sources available for the release; and
- the requested output as a site Release Notes page and downstream ready
  handoff.

The PM packet definition lives in
the active installed `idea-to-spec` skill's `_internal/_shared/skill-map.md`.
Direct invocation does not waive this gate. If the version, scope, host, or
evidence boundary is unresolved, stop before writing, name the missing entry
credential, and return product ambiguity to `pm-agent` or technical-impact gaps
to the owning engineering role.

After accepting the entry basis, verify that the host contains
`docs/site/release-notes/` and its writing rules or equivalent site contract.
If the formal documentation site or Release Notes foundation is absent, do not
create it. Return a bounded handoff to `docs-site-bootstrap` and wait for the
user to explicitly authorize site initialization.

## Confirmation Gate

The Release Notes body must be presented to the user or maintainer before any
release metadata, Release Notes index, or navigation is changed. Until the
body is explicitly confirmed:

- keep `confirmation_status` unconfirmed;
- do not update `docs/site/.meta/releases.json`;
- do not update the Release Notes index or navigation; and
- do not describe the downstream handoff as ready.

After confirmation, only the confirmed body and the host-required metadata,
index, and navigation changes may proceed. A revised body requires renewed
confirmation before those dependent writes.

## Role Boundary

This specialist owns only the documentation-site Release Notes delivery:

- reading host Release Notes rules and adjacent version pages;
- deriving a complete version page from verifiable release evidence;
- applying the shared frontmatter contract with `doc_type: release`;
- collecting body confirmation;
- updating host release metadata, indexes, and necessary navigation after
  confirmation;
- running host documentation checks; and
- producing the structured site-ready handoff consumed by
  `docs-agent:docs-audit` pre-tag audit, while preserving
  `pm-agent:github-release-gen` as the downstream GitHub Release owner.

The ready handoff proves only that the site Release Notes are confirmed and
validated. Send it directly to `docs-agent:docs-audit` pre-tag audit with the
explicitly maintainer-confirmed `target_release_version` and its confirmation
source. `pm-agent:github-release-gen` may not prepare a GitHub Release
draft until `docs-agent:docs-audit` returns `ready_for_tag`.

It does not create, edit, or publish a GitHub Release; create or move a tag;
publish images; update Helm; deploy software; initialize a documentation site;
or perform the version-stamping sequence owned by `docs-agent:docs-audit`.
`formal-docs-sync` remains responsible for other formal documentation types and
must not absorb this Release Notes workflow.

## Authoritative Execution

The seven-step evidence, generation, confirmation, metadata, validation, and
handoff protocol is authoritative in `_internal/INSTRUCTIONS.md`. Load it only
after the entry and site-foundation gates pass; do not replace it with an ad
hoc release or GitHub workflow.

## Output

Report:

- accepted entry basis, including the host, confirmed version and release scope,
  evidence boundary, and any missing entry credential;
- target release version and site Release Notes path;
- confirmation status;
- evidence sources used and unresolved evidence gaps;
- metadata, indexes, and navigation changed after confirmation;
- host documentation check commands and results; and
- a `ready` or `blocked` site-ready handoff for `docs-agent:docs-audit`,
  including the maintainer-confirmed `target_release_version` and confirmation
  source; `pm-agent:github-release-gen` remains the downstream owner
  after `ready_for_tag`.

Only an explicitly maintainer-confirmed `target_release_version`,
`confirmation_status: confirmed`, and successful host docs checks together can
produce a ready handoff. At closeout, follow the safety-net behavior
in the active installed `idea-to-spec` skill's `_internal/_shared/skill-map.md`
and wait for confirmation before another role acts unless the applicable
`auto-continue` authorization already exists.

If the confirmed Release Notes work materially changes a documentation build
target, navigation or assets, release scope, or runtime entry, invoke and
report the shared documentation-site deployment completeness state. Otherwise
preserve the prior state without rerunning or duplicating that protocol.
