---
name: github-release-gen
description: "Preview, draft, or publish a traceable GitHub Release after version facts and applicable Release Notes/audit gates are ready. Use after pm-agent routes release work."
visibility: internal
---

# GitHub Release Generator

Generate a GitHub Release from the applicable maintainer-confirmed version fact
source without changing the documentation site or release tags. For a host with
an initialized formal documentation site, the site Release Notes are the version
fact source. For a site-less host, use the explicitly confirmed fallback fact
source defined below. GitHub compare, PR, commit, and contributor data add
traceability and repository-native formatting only.

Read both references before acting:

- `reference/release-outline.md` for fact-preserving content conversion and
  GitHub Release formatting.
- `reference/github-release-workflow.md` for preview, draft, publish, and
  readback gates.

Apply reference requirements according to the host applicability decision in
this file. Their site Release Notes, `release-notes-gen` handoff,
`ready_for_tag`, and
`release_verified` premises apply only when the documentation-site gate is
applicable. For a site-less host, substitute the confirmed fallback fact source
and the alternate pre-tag/post-tag evidence defined here; this file's
applicability and degraded-gate rules take precedence over site-only wording in
the references. All reference mutation, tag-safety, latest, prerelease, and
readback protections remain in force on both paths.

## Mandatory Release Gate Summary

Before any mutation, report the ordered authority chain and current state:
`docs-agent:release-notes-gen` site Release Notes confirmation ->
`docs-agent:docs-audit` pre-tag `ready_for_tag` -> release-owner tag creation ->
`docs-agent:docs-audit` post-tag `release_verified` ->
`pm-agent:github-release-gen` preview, draft, or publication. `ready_for_tag`
permits only an inline preview or restricted draft;
it is not tag or publish authority. Missing tags return to the release owner;
missing post-tag evidence returns to `docs-agent:docs-audit`.
Name the owner at the preview stage explicitly as
`pm-agent:github-release-gen`: only after `docs-agent:release-notes-gen` confirms
the site page and `docs-agent:docs-audit` returns `ready_for_tag` may it produce
the submit-ready preview.

Every preview includes the complete body and normalized version/prerelease
decision. Draft commands explicitly set draft/prerelease flags, never infer or
move `latest`, and are followed by fresh readback, atomic final update, and
drift verification before publication. Never use `gh release create` when the
tag is absent because it can create the tag. Any conflict between GitHub facts
and the confirmed site/fallback source blocks and returns to the source owner.

Marketplace install sections are evidence-driven: omit a platform section when
the target tag lacks a verified pinned-install path, state that limitation
plainly outside that platform section, and derive the closing plugin count from
the target-tag manifest instead of memory or current HEAD. In particular, when
the target tag lacks `TARGET_TAG` support, do not render a `### Codex` heading.

Render the gate summary with explicit fields for `site_notes_handoff`,
`ready_for_tag`, `actual_tag`, `release_verified`, `allowed_action`,
`normalized_version`, `prerelease_flag`, `latest_policy`, `draft_command`,
`fresh_readback`, and `publish_recheck`. If the site handoff is absent, return
to `docs-agent:release-notes-gen`. If the tag is absent, preserve a complete
inline preview and state that `gh release create` is forbidden because it may
create the tag.

## Host Documentation-Site Applicability

Determine and record whether the host has an initialized formal documentation
site before applying either the `release-notes-gen` entry gate or the
`docs-audit` pre-tag and post-tag audit gates. Inspect repository evidence for
`docs/site/` and the host's `release-notes-gen` site Release Notes
capability chain. Record the evidence and
the applicability result in every preview and final report.

- If `docs/site/` exists and the `release-notes-gen` site Release Notes capability chain
  is initialized, treat the dual-state audit handoff gates as applicable. A
  missing or invalid handoff, version mismatch, or audit blocker is not a reason
  to downgrade: preserve the existing blocked behavior and return the work to
  the named Docs owner.
- If either `docs/site/` or the `release-notes-gen` site Release Notes capability chain
  is absent, the host does not have an initialized formal documentation site;
  treat the `release-notes-gen` / `docs-audit` handoff gates as not
  applicable and record the
  missing prerequisite or prerequisites as the downgrade basis. Do not infer a
  downgrade from an absent handoff alone or from ambiguous repository evidence.

For a site-less host, require a maintainer-confirmed version fact source, such
as a confirmed versioned changelog, together with compatible version-bump and
release-window evidence. Block when that source is missing, unconfirmed,
incomplete, or conflicts with the target version; never invent version facts.
When the fallback is valid, the absence of `release-notes-gen` /
`docs-audit` handoffs does not block a preview. Before every GitHub Release
write, including each draft create
or update and the final publish write, show the current preview and downgrade
basis and obtain explicit, current maintainer approval. Revalidate the fallback
fact source, version evidence, tag state, and downgrade basis immediately before
the write. Record the downgrade basis and readback result in the final report.

## Entry Gate: Site Release Notes Ready Handoff

For hosts where the documentation-site gate is applicable, require the complete
site-ready handoff produced by
`docs-agent:release-notes-gen`, including:

- `release_version` (mapped to the `release-notes-gen` canonical
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
`docs-agent:release-notes-gen`.

## Version And Compare Gate

Resolve and record the intended target tag, previous release tag, immutable
pre-tag `target_ref`, and compare range.
Normalize versions only for identity comparison; use each repository's real
tag spelling in GitHub and Git commands. Verify that the applicable fact-source
version (either the site handoff version or the confirmed site-less fallback),
intended target tag, previous tag, `target_ref`, and compare endpoints describe
one release window. Before the actual tag exists, audit
`previous_tag...target_ref`; after it exists, verify that the tag resolves to
the audited release content and use `previous_tag...target_tag` for the final
compare link.

If the target version and compare range cannot be aligned, stop. Return an
unclear release scope to `pm-agent`; for a site-enabled host, return a conflict
with the confirmed page to the site Release Notes flow; for a site-less host,
return the fallback fact source to the maintainer for renewed confirmation.
Never guess a previous tag or silently replace the confirmed release scope.

## Pre-Tag Gate: `ready_for_tag`

For hosts where the documentation-site gate is applicable, before generating a
submit-ready preview or creating or updating a draft, require the trusted
`docs-audit` pre-tag handoff for the same version with:

- `phase: pre-tag`;
- `phase_result: ready_for_tag`;
- immutable `base_ref` and `target_ref`; and
- the current docs-audit handoff evidence with no blocker.

Consume that handoff; do not generate, repair, restamp, or weaken it. Missing,
invalid, version-mismatched, or blocked audit evidence returns to
`docs-agent:docs-audit` and prohibits draft mutation.

## Generate The GitHub Release

1. Read the applicable confirmed version fact source and preserve its
   functional, architecture, database, deployment, asset, upgrade,
   compatibility, and risk facts. For a site-enabled host this is the confirmed
   site Release Notes; for a site-less host this is the confirmed fallback fact
   source and its compatible version evidence.
2. Audit the complete compare range, merged PRs, commits, and contributors.
3. Remove at most one repository-standard `v` prefix from the target and
   current latest tag, parse both as SemVer, and decide the explicit latest and
   prerelease flags. Every SemVer prerelease uses `--prerelease --latest=false`.
   For a stable version, read the current latest Release and use `--latest`
   only when the target SemVer is strictly greater; otherwise use
   `--latest=false`. An absent, non-SemVer, or otherwise unsafe comparison must
   use `--latest=false`.
4. Add compare, representative PR or commit, and contributor links without
   replacing the confirmed facts with a raw maintenance-data list.
5. Show the complete title and body preview, version-normalization evidence,
   current latest Release evidence, and the exact latest/prerelease decision
   before any GitHub write. The maintainer must confirm this decision with the
   preview. Before each draft write and immediately before the final publish
   write, re-read the current latest Release and require it to match the
   preview evidence. Drift invalidates the decision: stop, refresh the preview,
   and obtain new maintainer confirmation. Draft writes omit every latest flag;
   the confirmed latest flag is applied only by the final draft-to-published
   write, together with the final prerelease state.

Before presenting the preview, run this completeness check. A failed item makes
the preview not submit-ready:

- every date in the title or body comes from the confirmed fact source or
  release evidence; when no release date is confirmed, omit it instead of
  inserting the current date;
- every selected PR or direct commit includes its verified contributor link
  when the GitHub evidence provides one; verify the displayed contributor
  identity and profile URL as one evidence pair so a valid URL for a different
  contributor still fails this check;
- a request containing unauthorized site, check, tag, draft, or publish writes
  still receives the complete inline title and body preview when the content
  gates pass; the boundary report does not replace the preview; and
- for this marketplace, decide `render` or `omit` for Claude Code, Codex, and
  Kimi Code from the audited target ref before writing any platform heading or
  command. Historical-tag reconstruction omits Claude Code; missing
  `TARGET_TAG` support omits Codex; missing `.kimi-plugin/plugin.json` omits
  Kimi Code.

GitHub evidence may add traceability and formatting, not new or contradictory
version facts. If it exposes an omission or conflict, block. For a site-enabled
host, return the page to `docs-agent:release-notes-gen` for renewed
confirmation and checks; for a site-less host, return the fallback fact source
to the maintainer for renewed confirmation.

## Draft Mutation Gate

Before creating or updating a draft, verify that the preview satisfies the
`release-outline.md` title gate (for this marketplace `v{VERSION} - {主题概述}`;
for other hosts the confirmed naming convention, never a bare version string)
and the mandatory upgrade-note structure. A title or upgrade note failing
either gate is not submit-ready and blocks draft mutation.

Create or update a draft only when the user explicitly requests that mutation
after seeing the preview. The permission to prepare content is not permission
to write a draft. Re-read the current latest Release immediately before the
write; any change from the confirmed preview blocks mutation until a refreshed
preview is confirmed. If no remote draft and no actual tag exists, keep the full
draft as a preview and block remote creation: GitHub release creation would
also create the missing tag, which this skill does not own. An existing remote
draft may be updated only after proving the remote tag state is unchanged; a
new remote draft may be created only for an already-existing tag. After any
draft write, read it back and verify the tag, title, body, `isDraft`,
`isPrerelease`, URL, unchanged remote tag state, and unchanged published latest
pointer. Draft create/update commands must not pass `--latest` or
`--latest=false`; the previewed latest decision is reserved for publication.
Treat an already matching draft as a no-op, and never downgrade an already
published Release to draft. Report any mismatch as a failed write; do not
describe it as complete.

## Publish Gate

Publish only when all three conditions are independently satisfied for the
same version:

1. the actual target tag exists;
2. for a site-enabled host, `docs-audit` post-tag audit returns
   `release_verified`; for a site-less host, the recorded downgrade basis,
   maintainer-confirmed fact source, and compatible version evidence remain
   valid immediately before publication; and
3. the maintainer gives an explicit, current approval to publish.

Approval to confirm the site page or fallback fact source, generate a preview,
or create/update a draft cannot be reused as publish approval. A missing or
moved tag, invalidated applicable pre-tag authority, blocked applicable
post-tag audit, invalidated site-less downgrade evidence, version mismatch, or
absent approval prohibits publication.

If content must be updated before publication, write and read back that draft
content first without a latest flag. Immediately before the final
draft-to-published write, re-read the current latest Release and target tag
identity. If either differs from the confirmed preview/audited tag, stop with
the Release still in its last verified state and require the owning flow to
refresh its evidence. Apply `draft=false`, the final prerelease state, and the
confirmed latest flag in that one final write. An already published Release
that fully matches the approved state is a readback-only no-op; mismatches are
failures, not permission to flip it again.

After publishing, read the GitHub Release back and verify its tag, title, body,
draft/published state, prerelease/latest state, publication time, and URL
before reporting success. Re-read the remote tag OID as part of this final
verification; tag drift returns to the host tag owner and post-tag audit. If
the latest pointer differs, report the observed state and an exact corrective
`gh release edit <expected-tag> --latest` command, but do not execute that
third-party Release correction automatically or repair the tag.

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

Report the accepted handoff and audit evidence or the recorded site-less
downgrade basis, normalized version and compare range, applicable fact source,
current latest evidence, confirmed latest/prerelease decision, preview,
requested mutation, readback results, and any blocker with its next owner. A
preview is not a draft, `ready_for_tag` is not a publication state, and
`release_verified` is not publish approval.
