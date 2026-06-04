# GitHub Release Workflow

Use this workflow when creating, updating, or publishing GitHub releases.

## Modes

| Mode | User intent | Allowed mutations |
| --- | --- | --- |
| Notes only | Write release notes text | Do not change tags or releases |
| Draft release | Create or update a release draft | Create or update tag only if requested or required |
| Publish release | User confirms draft can be published | Run preflight, ensure changelog archives, update tag if needed, publish |

## Publishing Preflight

Before publishing an approved draft release:

1. Get local time.
2. Verify repo and branch state.
3. Verify target version and release draft state.
4. Verify local and remote tag.
5. Verify required changelog archives exist.
6. Verify root `CHANGELOG.md` links to the versioned changelog archives.
7. If changelog files are missing, create them first through the normal branch and PR flow.

Commands:

```bash
date '+%Y-%m-%d %H:%M:%S %Z'
git status --short --branch
git branch --show-current
gh release view v{VERSION} --json tagName,name,isDraft,publishedAt,targetCommitish
git show --no-patch --format='%H%n%D%n%s' v{VERSION}
git ls-remote --tags origin v{VERSION}
test -f docs/changelog/changelog-v{VERSION}.md
```

For this repository, the root index must include the version:

```bash
rg -n "changelog-v{VERSION}\\.md" CHANGELOG.md
```

## Changelog Archive Repair

If `docs/changelog/changelog-v{VERSION}.md` is missing:

1. Create a maintenance branch from `main`.
2. Add the versioned changelog file.
3. Update root `CHANGELOG.md` as an index only.
4. Run repository checks.
5. Commit and push.
6. Create a PR.
7. Wait for required CI.
8. Merge the PR.
9. Sync local `main`.

Commands:

```bash
git checkout -b neplich-codex/changelog-v{VERSION}
uv run scripts/check_repository_contract.py
git diff --check
git add CHANGELOG.md docs/changelog/changelog-v{VERSION}.md
git commit -m "docs: 补充 v{VERSION} changelog"
git push -u origin neplich-codex/changelog-v{VERSION}
gh pr create --base main --head neplich-codex/changelog-v{VERSION} \
  --title "docs: 补充 v{VERSION} changelog" \
  --body "..."
gh pr checks {PR_NUMBER} --watch
gh pr merge {PR_NUMBER} --squash --delete-branch
```

If earlier version changelog archives are missing and the release checklist depends on a complete archive index, add those missing version files in the same PR.

## Tag Handling

If changelog repair changes the release commit after a tag was already created, recreate the tag at the new `main` HEAD before publishing.

Pre-check:

```bash
git rev-parse HEAD
git rev-parse origin/main
git show --no-patch --format='%H%n%D%n%s' v{VERSION}
```

Recreate tag:

```bash
git tag -d v{VERSION}
git push origin :refs/tags/v{VERSION}
git tag -a v{VERSION} -m "v{VERSION}"
git push origin v{VERSION}
```

If the remote reports repository rule bypass messages for tag deletion or creation, verify success with:

```bash
git ls-remote --tags origin v{VERSION}
git show --no-patch --format='%H%n%D%n%s' v{VERSION}
```

## Draft Release Creation

Create a draft release when the user asks for a release but says not to publish:

```bash
gh release create v{VERSION} \
  --draft \
  --title "{TITLE}" \
  --notes-file {NOTES_FILE}
```

GitHub may return an `untagged-*` URL for draft releases. Verify by querying the tag:

```bash
gh release view v{VERSION} --json tagName,name,isDraft,publishedAt,targetCommitish
```

Expected draft state:

```text
tagName = v{VERSION}
isDraft = true
publishedAt = null
```

## Draft Release Updates

After editing release notes, update the draft body:

```bash
gh release edit v{VERSION} --notes-file {NOTES_FILE}
```

Re-check:

```bash
gh release view v{VERSION} --json tagName,name,isDraft,publishedAt,body
```

## Publishing

Only publish after:

- The user explicitly approves publishing.
- Required changelog archives exist.
- Root `CHANGELOG.md` contains version links.
- Tag points at the final release commit.
- Draft release body is final.

Publish:

```bash
gh release edit v{VERSION} --notes-file {NOTES_FILE} --target main --verify-tag
gh release edit v{VERSION} --draft=false --latest
```

Final verification:

```bash
gh release view v{VERSION} \
  --json tagName,name,isDraft,isPrerelease,publishedAt,url,targetCommitish
git show --no-patch --format='%H%n%D%n%s' v{VERSION}
git ls-remote --tags origin v{VERSION}
```

Expected final state:

```text
isDraft = false
isPrerelease = false
publishedAt is not null
tag points at the final release commit
```

## Final Response Checklist

Report:

- Published release URL or draft URL.
- Final tag target commit.
- Whether `isDraft` and `publishedAt` match the requested state.
- PR number if changelog repair was needed.
- Checks that ran and their result.
