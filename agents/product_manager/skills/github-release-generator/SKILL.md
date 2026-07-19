---
name: github-release-generator
description: "Internal PM specialist—not a direct entry point. Invoked by pm-agent after site Release Notes and pre-tag audit are ready to preview, draft, or publish a traceable GitHub Release."
visibility: internal
---

# GitHub Release Generator

Generate a GitHub Release from confirmed site Release Notes without changing
the documentation site or release tags. The site Release Notes are the version
fact source; GitHub compare, PR, commit, and contributor data add traceability
and repository-native formatting only.

Read both references before acting:

- `reference/release-outline.md` for fact-preserving content conversion and
  GitHub Release formatting.
- `reference/github-release-workflow.md` for preview, draft, publish, and
  readback gates.

## Entry Gate: Issue #116 Ready Handoff

Require the complete site-ready handoff produced by
`docs-agent:release-notes-generator`, including:

- `release_version` (mapped to the #116 canonical
  `target_release_version` when that field name is used) and a readable
  `site_release_note_path`;
- `confirmation_status: confirmed`;
- every required host docs check command and a successful result;
- the updated version index, release metadata, and any required navigation;
  and
- the source evidence used for the confirmed Release Notes.

Read the referenced page and verify that the handoff fields and version agree.
Block before producing a publishable GitHub Release when the page is missing,
the body is unconfirmed, a required docs check failed or was not run, an
index/metadata update is missing or inconsistent, or the evidence is
incomplete. Name the missing field or failed evidence and return the work to
`docs-agent:release-notes-generator`.

## Version And Compare Gate

Resolve and record the intended target tag, previous release tag, immutable
pre-tag `target_ref`, and compare range.
Normalize versions only for identity comparison; use each repository's real
tag spelling in GitHub and Git commands. Verify that the handoff version,
intended target tag, previous tag, `target_ref`, and compare endpoints describe
one release window. Before the actual tag exists, audit
`previous_tag...target_ref`; after it exists, verify that the tag resolves to
the audited release content and use `previous_tag...target_tag` for the final
compare link.

If the target version and compare range cannot be aligned, stop. Return an
unclear release scope to `pm-agent`; return a conflict with the confirmed page
to the site Release Notes flow. Never guess a previous tag or silently replace
the confirmed release scope.

## Pre-Tag Gate: `ready_for_tag`

Before generating a submit-ready preview or creating or updating a draft,
require the trusted issue #117 pre-tag handoff for the same version with:

- `phase: pre-tag`;
- `phase_result: ready_for_tag`;
- immutable `base_ref` and `target_ref`; and
- the current docs-audit handoff evidence with no blocker.

Consume that handoff; do not generate, repair, restamp, or weaken it. Missing,
invalid, version-mismatched, or blocked audit evidence returns to
`docs-agent:docs-audit` and prohibits draft mutation.

## Generate The GitHub Release

1. Read the confirmed site Release Notes and preserve its functional,
   architecture, database, deployment, asset, upgrade, compatibility, and risk
   facts.
2. Audit the complete compare range, merged PRs, commits, and contributors.
3. Read adjacent GitHub Releases and the repository's release conventions.
4. Add compare, representative PR or commit, and contributor links without
   replacing the confirmed facts with a raw maintenance-data list.
5. Show the complete title and body preview before any GitHub write.

GitHub evidence may add traceability and formatting, not new or contradictory
version facts. If it exposes an omission or conflict, block and return the page
to `docs-agent:release-notes-generator` for renewed confirmation and checks.

## Draft Mutation Gate

Create or update a draft only when the user explicitly requests that mutation
after seeing the preview. The permission to prepare content is not permission
to write a draft. If no remote draft and no actual tag exists, keep the full
draft as a preview and block remote creation: GitHub release creation would
also create the missing tag, which this skill does not own. An existing remote
draft may be updated only after proving the remote tag state is unchanged; a
new remote draft may be created only for an already-existing tag. After any
draft write, read it back and verify the tag, title, body, `isDraft`, URL, and
unchanged remote tag state. Report any mismatch as a failed write; do not
describe it as complete.

## Publish Gate

Publish only when all three conditions are independently satisfied for the
same version:

1. the actual target tag exists;
2. issue #117 post-tag audit returns `release_verified`; and
3. the maintainer gives an explicit, current approval to publish.

Approval to confirm the site page, generate a preview, or create/update a
draft cannot be reused as publish approval. A missing or moved tag, invalidated
pre-tag authority, blocked post-tag audit, version mismatch, or absent approval
prohibits publication.

After publishing, read the GitHub Release back and verify its tag, title, body,
draft/published state, publication time, and URL before reporting success.

## Role Boundary

This skill must not:

- write or modify `docs/site/` or generate VitePress Release Notes;
- update site frontmatter, version indexes, release metadata, or navigation;
- execute or substitute for host docs checks such as `test:docs`;
- create, move, delete, or recreate a tag;
- generate or repair changelog archives as part of this workflow;
- publish images, Harbor artifacts, or other delivery assets;
- update Helm or perform a deployment;
- publish without the three publish-gate conditions; or
- dump raw PR or commit lists as the user-facing release explanation.

## Output

Report the accepted handoff and audit evidence, normalized version and compare
range, fact-source page, preview, requested mutation, readback results, and any
blocker with its next owner. A preview is not a draft, `ready_for_tag` is not a
publication state, and `release_verified` is not publish approval.
