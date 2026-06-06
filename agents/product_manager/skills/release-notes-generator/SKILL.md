---
name: release-notes-generator
description: Generate user-facing release notes for a specific version from GitHub PRs and release tags. Unlike changelog-generator, release notes explain why changes matter to users. Use this skill when the user asks to write release notes, draft a release announcement, create a GitHub release body, prepare or publish a draft release, or summarize what changed in a version.
---

# Release Notes Generator

Generate user-facing release notes and, when requested, prepare or publish GitHub releases from version tags, changelog archives, merged PRs, and release metadata.

Use this skill for:

- Writing release notes or a release announcement.
- Drafting a GitHub Release body.
- Updating an existing draft release body.
- Publishing an approved GitHub draft release.
- Explaining what changed in a version for users or customers.

## Reference Files

Read the relevant reference before acting:

- `reference/release-outline.md` - release note structure, writing rules, and formatting expectations.
- `reference/github-release-workflow.md` - standard tag, changelog, draft release, and publish workflow.

## Step 1 - Identify Release Context

Determine:

- Target version, for example `v1.2.0`.
- Previous version or compare range.
- Whether the task is only writing notes, updating a draft, creating a tag, or publishing a release.
- Whether the release should remain a draft.

Ask only if the version or publish/draft intent is unclear.

Useful commands:

```bash
gh repo view --json nameWithOwner,url,defaultBranchRef
gh release list --json tagName,publishedAt,name,isDraft --order desc --limit 20
gh release view v{VERSION} --json tagName,name,body,isDraft,publishedAt,targetCommitish
git tag --list --sort=version:refname
```

## Step 2 - Gather Change Data

Prefer existing versioned changelog archives:

```bash
docs/changelog/changelog-v{VERSION}.md
```

Always audit the full compare range before writing release notes:

- Inspect all commits in `PREV_TAG..THIS_TAG`.
- Inspect all merged PRs in the same release window.
- Do not discard bot, documentation, chore, or internal-looking changes before the audit. Use the complete source set as the basis for release decisions.
- The final release notes may group, summarize, or omit low-signal items, but the decision should come after the full source audit.

If the changelog is missing or incomplete, fetch merged PRs and commits from GitHub:

```bash
gh pr list \
  --state merged \
  --json number,title,body,mergedAt,author,labels,url \
  --search "merged:PREV_DATE..RELEASE_DATE" \
  --limit 200
```

For squash-heavy repositories, also inspect the compare range:

```bash
git log PREV_TAG..HEAD --date=iso --pretty=format:'%h%x09%ad%x09%s'
gh api repos/{OWNER}/{REPO}/compare/PREV_TAG...THIS_TAG
```

## Step 3 - Write Or Update Release Notes

Use `reference/release-outline.md` for the release body. Match the repository's existing release style before introducing a new outline.

Default rules:

- Write in the repository's documentation language. For this repository, use Chinese release notes.
- Keep the release user-facing and concise.
- Include PR links for major highlights.
- Include contributor mentions in the final change details, using `by @user in [#N](...)`.
- Put the full compare link after the change details section.

## Step 4 - Draft Or Publish On GitHub

Use `reference/github-release-workflow.md` before mutating tags or releases.

High-level rule:

- If the user asks for a draft, create or update a draft release only.
- If the user approves publishing, run the publishing preflight first, including changelog archive checks.
- Never publish before required changelog archives and root `CHANGELOG.md` index entries are present.

Common commands:

```bash
gh release create v{VERSION} --draft --title "{TITLE}" --notes-file {NOTES_FILE}
gh release edit v{VERSION} --notes-file {NOTES_FILE}
gh release edit v{VERSION} --draft=false --latest
```

## Edge Cases

- If the release tag points at an older commit and release checklist files are added afterward, merge those files first, then delete and recreate the tag at the new release commit before publishing.
- If GitHub returns an `untagged-*` URL for a draft release, verify it by querying `gh release view v{VERSION}` and checking `tagName` and `isDraft`.
- If a target changelog archive is missing, create it with `changelog-generator` style content before publishing.
- If the user only wants release notes text, do not mutate GitHub releases or tags.
