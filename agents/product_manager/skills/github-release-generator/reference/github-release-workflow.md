# GitHub Release Workflow

Use this workflow only after the `SKILL.md` issue #116 entry gate and issue
#117 `ready_for_tag` gate pass for the same version.

## Modes

| Mode | Required intent and evidence | Allowed mutation |
| --- | --- | --- |
| Preview | Complete #116 handoff and `ready_for_tag` | None |
| Draft | Preview shown and user explicitly requests create/update | Update an existing draft without tag mutation, or create a draft only when the actual tag already exists |
| Publish | Actual tag, `release_verified`, and separate maintainer approval | Publish the approved draft |

## Release Variables

- `THIS_TAG`: exact repository tag spelling used for GitHub reads and writes.
- `VERSION`: version identity with one repository-standard prefix removed only
  for comparison or titles that intentionally normalize it.
- `PREV_TAG`: exact previous release tag.
- `TARGET_REF`: immutable pre-tag target commit from the trusted
  `ready_for_tag` handoff.
- `LATEST_FLAG`: the preview-confirmed literal `--latest` or `--latest=false`.
- `PRERELEASE_FLAG`: the preview-confirmed literal `--prerelease` for a SemVer
  prerelease, or `--prerelease=false` for a stable version.

Verify `release_version` (or #116's canonical `target_release_version`),
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
gh release view {THIS_TAG} --json tagName,name,body,isDraft,publishedAt,targetCommitish,url
gh api repos/{OWNER}/{REPO}/compare/{PREV_TAG}...{TARGET_REF}
```

Before preview or draft, verify the trusted pre-tag handoff states
`phase_result: ready_for_tag` for the same release version. This workflow never
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
maintainer confirms them together with the title and body. Draft creation,
draft update, and publication must use the exact flags from the most recently
confirmed preview. Immediately before each write, re-read the current latest
Release and re-evaluate the same comparison only to detect drift. If the latest
tag or comparison result changed, stop, refresh the preview, and obtain new
maintainer confirmation; do not reuse stale flags or silently recompute a more
permissive decision.

## Preview

Build the complete title and body using `release-outline.md`. Show the preview
and identify:

- the confirmed site Release Notes path;
- the exact compare range;
- the PR, commit, and contributor links added for traceability; and
- the target classification, current latest evidence, SemVer comparison, and
  exact `LATEST_FLAG` / `PRERELEASE_FLAG`; and
- any GitHub evidence conflict that must return to Docs.

Do not mutate GitHub while the requested action is preview-only or ambiguous.

## Create Or Update A Draft

Only after the user explicitly requests the draft mutation, read the current
release, current latest Release, and remote tag state. Require the latest tag
and comparison result to equal the most recently confirmed preview. Drift
returns to Preview for renewed confirmation. If an existing draft is found,
update it and prove the tag state did not change:

```bash
git ls-remote --tags origin refs/tags/{THIS_TAG}
gh release view {THIS_TAG} --json tagName,name,body,isDraft,publishedAt,targetCommitish,url
gh release edit {THIS_TAG} --title "{TITLE}" --notes-file {NOTES_FILE} {PRERELEASE_FLAG} {LATEST_FLAG}
```

If no draft exists, create one only after the remote tag already exists. Use
`--verify-tag` so this skill cannot create the missing tag:

```bash
gh release create {THIS_TAG} --draft --verify-tag --title "{TITLE}" --notes-file {NOTES_FILE} {PRERELEASE_FLAG} {LATEST_FLAG}
```

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

Require the expected tag, title, and body, `isDraft: true`, and no publication
time. Require the preview-confirmed prerelease/latest decision and the remote
tag state to equal their expected values. The published latest pointer must
remain equal to its pre-write value while the Release is a draft. A mismatch
is a failed draft mutation.

## Publish

Immediately before publishing, verify all of the following again:

- the actual tag exists and is the declared target tag;
- the freshly read current latest Release and SemVer comparison still equal
  the most recently confirmed preview; drift returns to Preview for renewed
  maintainer confirmation;
- the issue #117 post-tag handoff states `phase: post-tag` and
  `phase_result: release_verified` for the same version;
- the draft readback matches the approved preview; and
- the draft still matches the preview-confirmed latest/prerelease decision;
  and
- the maintainer has explicitly approved publication in a separate, current
  instruction.

Then publish the already-approved draft:

```bash
gh release edit {THIS_TAG} --title "{TITLE}" --notes-file {NOTES_FILE} --verify-tag {PRERELEASE_FLAG} {LATEST_FLAG}
gh release edit {THIS_TAG} --draft=false {PRERELEASE_FLAG} {LATEST_FLAG}
```

Read the release back:

```bash
gh release view {THIS_TAG} --json tagName,name,body,isDraft,isPrerelease,publishedAt,url,targetCommitish
gh release view --json tagName,name,isDraft,isPrerelease,publishedAt,url
```

Require the expected tag, title, and body, `isDraft: false`, a non-null
`publishedAt`, the preview-confirmed prerelease/latest decision, and the
expected URL before reporting success. The no-tag read must resolve to
`THIS_TAG` only when `LATEST_FLAG=--latest`; when
`LATEST_FLAG=--latest=false`, require the previously recorded latest pointer
to remain unchanged.

## Blocked Outcomes

- Missing or unconfirmed page, docs check gap, or page/GitHub fact conflict:
  return to `docs-agent:release-notes-generator`.
- Missing or invalid `ready_for_tag` / `release_verified`: return to
  `docs-agent:docs-audit`.
- Unclear version or compare range: return to `pm-agent`.
- Missing tag: host release owner creates the tag outside this skill.
- Missing publish approval: keep the draft unchanged.
