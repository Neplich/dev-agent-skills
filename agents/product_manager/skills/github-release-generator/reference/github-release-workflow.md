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
gh release view {THIS_TAG} --json tagName,name,body,isDraft,publishedAt,targetCommitish,url
gh api repos/{OWNER}/{REPO}/compare/{PREV_TAG}...{TARGET_REF}
```

Before preview or draft, verify the trusted pre-tag handoff states
`phase_result: ready_for_tag` for the same release version. This workflow never
creates, moves, deletes, or recreates `THIS_TAG`. After the actual tag exists,
re-run the compare against `PREV_TAG...THIS_TAG` and require the tag to resolve
to the audited release content before publication.

## Preview

Build the complete title and body using `release-outline.md`. Show the preview
and identify:

- the confirmed site Release Notes path;
- the exact compare range;
- the PR, commit, and contributor links added for traceability; and
- any GitHub evidence conflict that must return to Docs.

Do not mutate GitHub while the requested action is preview-only or ambiguous.

## Create Or Update A Draft

Only after the user explicitly requests the draft mutation, read the current
release and remote tag state. If an existing draft is found, update it and
prove the tag state did not change:

```bash
git ls-remote --tags origin refs/tags/{THIS_TAG}
gh release view {THIS_TAG} --json tagName,name,body,isDraft,publishedAt,targetCommitish,url
gh release edit {THIS_TAG} --title "{TITLE}" --notes-file {NOTES_FILE}
```

If no draft exists, create one only after the remote tag already exists. Use
`--verify-tag` so this skill cannot create the missing tag:

```bash
gh release create {THIS_TAG} --draft --verify-tag --title "{TITLE}" --notes-file {NOTES_FILE}
```

If neither an existing draft nor the actual remote tag exists, keep the complete
draft content as the preview artifact and return tag creation to the host
release owner. Do not call `gh release create`: its documented missing-tag
behavior would create a tag and violate this skill's boundary. `ready_for_tag`
authorizes draft preparation, not tag mutation.

Read the draft back:

```bash
gh release view {THIS_TAG} --json tagName,name,body,isDraft,publishedAt,targetCommitish,url
git ls-remote --tags origin refs/tags/{THIS_TAG}
```

Require the expected tag, title, and body, `isDraft: true`, and no publication
time. Require the remote tag state to equal its pre-write value. A mismatch is
a failed draft mutation.

## Publish

Immediately before publishing, verify all of the following again:

- the actual tag exists and is the declared target tag;
- the issue #117 post-tag handoff states `phase: post-tag` and
  `phase_result: release_verified` for the same version;
- the draft readback matches the approved preview; and
- the maintainer has explicitly approved publication in a separate, current
  instruction.

Then publish the already-approved draft:

```bash
gh release edit {THIS_TAG} --title "{TITLE}" --notes-file {NOTES_FILE} --verify-tag
gh release edit {THIS_TAG} --draft=false --latest
```

Read the release back:

```bash
gh release view {THIS_TAG} --json tagName,name,body,isDraft,isPrerelease,publishedAt,url,targetCommitish
```

Require the expected tag, title, and body, `isDraft: false`, a non-null
`publishedAt`, and the expected URL before reporting success.

## Blocked Outcomes

- Missing or unconfirmed page, docs check gap, or page/GitHub fact conflict:
  return to `docs-agent:release-notes-generator`.
- Missing or invalid `ready_for_tag` / `release_verified`: return to
  `docs-agent:docs-audit`.
- Unclear version or compare range: return to `pm-agent`.
- Missing tag: host release owner creates the tag outside this skill.
- Missing publish approval: keep the draft unchanged.
