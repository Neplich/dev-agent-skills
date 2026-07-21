# GitHub Release Workflow

Use this workflow only after the `SKILL.md` applicability gate selects and
validates the release path: the issue #116/#117 handoff path for a site-enabled
host, or the maintainer-confirmed fallback fact-source path for a site-less host.

## Modes

| Mode | Required intent and evidence | Allowed mutation |
| --- | --- | --- |
| Preview | Site-enabled: complete #116 handoff and `ready_for_tag`; site-less: confirmed fallback fact source and recorded downgrade basis | None |
| Draft | Preview shown and user explicitly requests create/update; site-less writes also require explicit, current maintainer approval | Update an existing draft without tag mutation, or create a draft only when the actual tag already exists |
| Publish | Actual tag and separate maintainer approval, plus site-enabled `release_verified` or revalidated site-less fallback evidence | Publish the approved draft |

## Release Variables

- `THIS_TAG`: exact repository tag spelling used for GitHub reads and writes.
- `VERSION`: version identity with one repository-standard prefix removed only
  for comparison or titles that intentionally normalize it.
- `PREV_TAG`: exact previous release tag.
- `TARGET_REF`: immutable pre-tag target commit from the trusted
  `ready_for_tag` handoff, or compatible release-window evidence for the
  confirmed site-less fallback.
- `LATEST_FLAG`: the preview-confirmed, publish-only literal `--latest` or
  `--latest=false`; draft writes omit both forms.
- `PRERELEASE_FLAG`: the preview-confirmed literal `--prerelease` for a SemVer
  prerelease, or `--prerelease=false` for a stable version.
- `TARGET_TAG_OID`: the exact remote object ID read for `THIS_TAG`; any change
  between writes is tag drift and blocks further mutation.

Verify the applicable fact-source version (`release_version`, #116's canonical
`target_release_version`, or the confirmed site-less fallback version),
`THIS_TAG`, `PREV_TAG`, `TARGET_REF`, and the compare endpoints as one release
window. Do not infer a missing previous tag or use mutable `HEAD` as a
substitute for `TARGET_REF`.

## Read-Only Preflight

Use the GitHub Connector first, or authenticated `gh` when connector coverage
is insufficient. Read before every write:

```bash
gh repo view --json nameWithOwner,url,defaultBranchRef
gh release list --json tagName,publishedAt,name,isDraft --order desc --limit 20
gh release view --json tagName,name,isDraft,isPrerelease,publishedAt,url
gh release view {THIS_TAG} --json tagName,name,body,isDraft,isPrerelease,publishedAt,targetCommitish,url
gh api repos/{OWNER}/{REPO}/compare/{PREV_TAG}...{TARGET_REF}
```

Before preview or draft, verify that a site-enabled host's trusted pre-tag
handoff states `phase_result: ready_for_tag` for the same release version, or
that a site-less host's confirmed fallback fact source and downgrade basis
remain valid. This workflow never
creates, moves, deletes, or recreates `THIS_TAG`. After the actual tag exists,
re-run the compare against `PREV_TAG...THIS_TAG` and require the tag to resolve
to the audited release content before publication.

## Latest And Prerelease Decision

Compute this decision before showing the preview and before any write:

1. Identify the repository-standard `v` prefix from its real tag convention.
   Remove no more than one such prefix from `THIS_TAG` and from the current
   latest tag, then parse the remaining values as SemVer. Do not broadly strip
   arbitrary leading characters or multiple `v` prefixes.
2. If the target has any SemVer prerelease component, including `-rc`, `-fix`,
   or equivalent suffixes, set `PRERELEASE_FLAG=--prerelease` and
   `LATEST_FLAG=--latest=false` unconditionally.
3. If the target is stable, read the current latest GitHub Release. Set
   `PRERELEASE_FLAG=--prerelease=false`; set `LATEST_FLAG=--latest` only when
   both versions parse safely and the target SemVer is strictly greater than
   the current latest SemVer. Equal, older, absent, or unsafe-to-compare latest
   evidence uses `LATEST_FLAG=--latest=false`.

| Target and evidence | `PRERELEASE_FLAG` | `LATEST_FLAG` |
| --- | --- | --- |
| Any valid SemVer prerelease | `--prerelease` | `--latest=false` |
| Stable and strictly greater than safely parsed current latest | `--prerelease=false` | `--latest` |
| Stable but equal, older, absent, or unsafe to compare | `--prerelease=false` | `--latest=false` |

Put the exact normalized versions, current latest Release tag/URL, comparison
result, `LATEST_FLAG`, and `PRERELEASE_FLAG` in the pre-write preview. The
maintainer confirms them together with the title and body. Draft creation and
update use the confirmed `PRERELEASE_FLAG` but omit both forms of the latest
flag because a draft cannot be latest. `LATEST_FLAG` is reserved for the final
publish write. Immediately before each draft write and the final publish write,
re-read the current latest Release and re-evaluate the same comparison only to
detect drift. If the latest tag or comparison result changed, stop, refresh the
preview, and obtain new maintainer confirmation; do not reuse stale flags or
silently recompute a more permissive decision.

## Preview

Build the complete title and body using `release-outline.md`. Show the preview
and identify:

- the applicable confirmed fact source and either its site path or site-less downgrade basis;
- the exact compare range;
- the PR, commit, and contributor links added for traceability; and
- the target classification, current latest evidence, SemVer comparison, and
  exact `LATEST_FLAG` / `PRERELEASE_FLAG`; and
- any GitHub evidence conflict that must return to Docs for a site-enabled host
  or to the maintainer for a site-less host.

Do not mutate GitHub while the requested action is preview-only or ambiguous.

## Create Or Update A Draft

Only after the user explicitly requests the draft mutation, read the current
release, current latest Release, and remote tag state. For a site-less host,
obtain explicit, current maintainer approval for this write and revalidate the
fallback fact source and downgrade basis immediately before writing. Record
`TARGET_TAG_OID` and require the latest tag and comparison result to equal the
most recently confirmed preview. Drift returns to Preview for renewed confirmation. If the
Release is already published, do not downgrade it; report its current state and
route any content correction through a new approved publish cycle. If an
existing draft already matches the title, body, and prerelease state, perform no
write and report a verified no-op. Otherwise update it and prove the tag state
did not change:

```bash
git ls-remote --tags origin refs/tags/{THIS_TAG}
gh release view {THIS_TAG} --json tagName,name,body,isDraft,isPrerelease,publishedAt,targetCommitish,url
gh release edit {THIS_TAG} --title "{TITLE}" --notes-file {NOTES_FILE} {PRERELEASE_FLAG}
```

If no draft exists, create one only after the remote tag already exists. Use
`--verify-tag` so this skill cannot create the missing tag:

```bash
gh release create {THIS_TAG} --draft --verify-tag --title "{TITLE}" --notes-file {NOTES_FILE} {PRERELEASE_FLAG}
```

Draft commands intentionally omit `--latest` and `--latest=false`. Re-running
the draft step must re-read before choosing create/update/no-op, so it never
creates a duplicate Release.

If neither an existing draft nor the actual remote tag exists, keep the complete
draft content as the preview artifact and return tag creation to the host
release owner. Do not call `gh release create`: its documented missing-tag
behavior would create a tag and violate this skill's boundary. `ready_for_tag`
authorizes draft preparation, not tag mutation.

Read the draft back:

```bash
gh release view {THIS_TAG} --json tagName,name,body,isDraft,isPrerelease,publishedAt,targetCommitish,url
gh release view --json tagName,name,isDraft,isPrerelease,publishedAt,url
git ls-remote --tags origin refs/tags/{THIS_TAG}
```

Require the expected tag, title, and body, `isDraft: true`, no publication time,
the preview-confirmed prerelease state, and the same `TARGET_TAG_OID`. The
published latest pointer must remain equal to its pre-write value while the
Release is a draft. A mismatch is a failed draft mutation; report the observed
draft, latest, and tag states and do not claim completion.

## Publish

Before any publish write, verify all of the following again:

- the actual tag exists, is the declared target tag, and still resolves to
  `TARGET_TAG_OID`;
- the freshly read current latest Release and SemVer comparison still equal
  the most recently confirmed preview; drift returns to Preview for renewed
  maintainer confirmation;
- for a site-enabled host, the issue #117 post-tag handoff states `phase: post-tag`
  and `phase_result: release_verified` for the same version; for a site-less
  host, the recorded downgrade basis, confirmed fact source, and compatible
  version evidence remain valid;
- the draft readback matches the approved preview; and
- the draft matches the preview-confirmed prerelease decision and has never
  been assigned latest while still draft; and
- the maintainer has explicitly approved publication in a separate, current
  instruction.

The fresh target read used for this decision must include all fields needed to
choose published, exact-draft, or mismatched-draft behavior:

```bash
gh release view {THIS_TAG} --json tagName,name,body,isDraft,isPrerelease,publishedAt,url,targetCommitish
gh release view --json tagName,name,isDraft,isPrerelease,publishedAt,url
git ls-remote --tags origin refs/tags/{THIS_TAG}
```

If the Release is already published, do not write again. Read it back; when all
approved fields and the latest pointer match, report an idempotent no-op. If it
does not match, report a failed precondition and require a new approved
correction cycle.

If the draft title, body, or prerelease state differs from the approved preview,
perform the content write without a latest flag and immediately read back the
draft and tag OID:

```bash
gh release edit {THIS_TAG} --title "{TITLE}" --notes-file {NOTES_FILE} --verify-tag {PRERELEASE_FLAG}
gh release view {THIS_TAG} --json tagName,name,body,isDraft,isPrerelease,publishedAt,url,targetCommitish
git ls-remote --tags origin refs/tags/{THIS_TAG}
```

Only after that readback succeeds, or immediately when the draft content was
already exact, re-read the latest pointer and `TARGET_TAG_OID` once more. This
is the required drift check between the two possible publish writes. Drift
leaves the verified draft unchanged and returns to Preview or the host tag
owner. When the evidence still matches, atomically apply the lifecycle and
latest decision in the final write:

```bash
gh release view --json tagName,name,isDraft,isPrerelease,publishedAt,url
git ls-remote --tags origin refs/tags/{THIS_TAG}
gh release edit {THIS_TAG} --draft=false {PRERELEASE_FLAG} {LATEST_FLAG}
```

Read the release back:

```bash
gh release view {THIS_TAG} --json tagName,name,body,isDraft,isPrerelease,publishedAt,url,targetCommitish
gh release view --json tagName,name,isDraft,isPrerelease,publishedAt,url
git ls-remote --tags origin refs/tags/{THIS_TAG}
```

Require the expected tag, title, and body, `isDraft: false`, a non-null
`publishedAt`, the preview-confirmed prerelease/latest decision, and the
expected URL before reporting success. Require the final remote tag OID to
still equal `TARGET_TAG_OID`; `targetCommitish` does not replace this check. The
no-tag read must resolve to
`THIS_TAG` only when `LATEST_FLAG=--latest`; when
`LATEST_FLAG=--latest=false`, require the previously recorded latest pointer
to remain unchanged. If this final readback disagrees, report the publication
as failed verification and show, but do not run, the corrective command:

- expected target latest: `gh release edit {THIS_TAG} --latest`;
- expected prior pointer preserved: `gh release edit {PRE_WRITE_LATEST_TAG} --latest`.

If no prior latest tag was safely recorded, report that automatic correction
cannot be proposed safely. Never issue an unapproved third write against the
target or another Release.

## Write Failure And Recovery

| Failure point | Known state | Recovery hint |
| --- | --- | --- |
| Draft preflight drift | No write occurred | Refresh Preview and obtain current draft approval |
| Draft write/readback mismatch | Draft state is uncertain; published latest must be unchanged | Re-read target, latest, and tag OID before deciding whether the draft step is a no-op or needs a new approved update |
| Publish content write/readback mismatch | Release should still be draft, but content state is uncertain | Keep publication blocked; re-read and obtain approval for corrected content |
| Latest or tag drift before final publish write | Last verified state remains draft | Latest drift returns to Preview; tag drift returns to the host tag owner and post-tag audit |
| Final publish write/readback mismatch | Release may be published; latest pointer or tag OID may differ | Report observed state; latest mismatch may include the safe corrective command above, while tag drift returns to the host tag owner and post-tag audit; do not auto-correct, repair the tag, or repeat the lifecycle flip |

Every recovery begins with read-only target/latest/tag reads. A repeated run
must choose create, update, publish, or no-op from current state; it must not
create a second Release or re-flip an already published one.

## Blocked Outcomes

- Site-enabled host with a missing or unconfirmed page, docs check gap, or
  page/GitHub fact conflict: return to `docs-agent:release-notes-generator`.
- Site-enabled host with missing or invalid `ready_for_tag` / `release_verified`:
  return to `docs-agent:docs-audit`.
- Site-less host with a missing, unconfirmed, or conflicting fallback fact
  source, invalid downgrade basis, or missing pre-write approval: return to
  `pm-agent` / the maintainer.
- Unclear version or compare range: return to `pm-agent`.
- Missing tag: host release owner creates the tag outside this skill.
- Missing publish approval: keep the draft unchanged.
