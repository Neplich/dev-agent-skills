# Execution Log

## Task

Generate the changelog entry for the latest release of `anthropics/anthropic-sdk-python` in Keep a Changelog format, including all associated PR references.

## Steps Taken

### 1. Identify the Latest Release

**Command:** `gh release list --repo anthropics/anthropic-sdk-python --limit 5`

**Result:** The latest release is `v0.86.0`, published on `2026-03-18T18:42:27Z`.

```
v0.86.0   Latest   v0.86.0   2026-03-18T18:42:27Z
v0.85.0            v0.85.0   2026-03-16T17:00:08Z
v0.84.0            v0.84.0   2026-02-25T05:22:10Z
...
```

### 2. Fetch Release Notes

**Command:** `gh release view v0.86.0 --repo anthropics/anthropic-sdk-python`

**Result:** The official release body contains the following conventional-commit-style changelog produced by Stainless:

- Features:
  - `feat: add support for filesystem memory tools (#1247)`
  - `feat(api): manual updates` (two commits)
- Bug Fixes:
  - `fix: AsyncAnthropic._make_status_error missing 529 and 413 cases (#1244)`
  - `fix(deps): bump minimum typing-extensions version`
  - `fix(pydantic): do not pass by_alias unless set`
- Chores:
  - `chore(internal): tweak CI branches`

### 3. Enumerate All Commits Between v0.85.0 and v0.86.0

**Command:** `gh api "repos/anthropics/anthropic-sdk-python/compare/v0.85.0...v0.86.0" --jq '.commits[] | {sha: .sha[0:7], message: .commit.message | split("\n")[0]}'`

**Result:** 8 commits identified:

| SHA     | Message |
|---------|---------|
| 05220bc | fix: AsyncAnthropic._make_status_error missing 529 and 413 cases (#1244) |
| 8669b92 | fix(pydantic): do not pass `by_alias` unless set |
| c5e5f3e | fix(deps): bump minimum typing-extensions version |
| 206252f | chore(internal): tweak CI branches |
| 5ccd6b4 | feat: add support for filesystem memory tools (#1247) |
| 34045e4 | feat(api): manual updates |
| c46a3e4 | feat(api): manual updates (/v1/models capabilities expansion) |
| d7c0974 | release: 0.86.0 |

### 4. Identify Directly Linked PRs

**Command:** `gh pr view 1244 --repo anthropics/anthropic-sdk-python --json number,title,mergedAt,url,body`

- **PR #1244** (`fix(client): AsyncAnthropic._make_status_error missing 529 and 413 cases`)
  - Merged: 2026-03-16T21:05:31Z
  - URL: https://github.com/anthropics/anthropic-sdk-python/pull/1244
  - Adds missing 529 and 413 status code handling to `AsyncAnthropic._make_status_error` to match the sync client.

**Command:** `gh pr view 1247 --repo anthropics/anthropic-sdk-python --json number,title,mergedAt,url,state`

- **#1247** is an open pull request (not merged); in the commit message and release notes, `#1247` is a reference to that PR/issue number used for tracking the filesystem memory tools feature. The actual code was committed directly as part of the release PR (#1249).

### 5. Confirm Merged PRs in Release Window

**Command:** `gh api "repos/anthropics/anthropic-sdk-python/pulls?state=closed&per_page=100" --jq '...'` (filtered to 2026-03-15 to 2026-03-19)

**Result:** Only two non-release PRs merged in this window:
- #1244 — `fix(client): AsyncAnthropic._make_status_error missing 529 and 413 cases` (merged 2026-03-16)
- #1209 — `release: 0.85.0` (prior release)

### 6. Investigate API Manual Update Commits

**Command:** Fetched files changed for commits `34045e4` and `c46a3e4`

- Commit `c46a3e4` (`/v1/models capabilities expansion`): Added new type files for model capabilities — `ModelCapabilities`, `BetaModelCapabilities`, `CapabilitySupport`, `ContextManagementCapability`, `EffortCapability`, `BetaThinkingCapability`, etc.
- Commit `34045e4` (no body): Added `error_type.py` under `types/shared/`.

These were internal stainless-generated API changes with no associated PR numbers.

## Decisions Made

1. **Keep a Changelog format used:** `Added`, `Fixed`, `Changed` sections (omitting `Removed`, `Deprecated`, `Security` as none were present).
2. **Chore/internal changes** were mapped to `Changed` (they are observable CI configuration changes, not pure internal noise).
3. **PR #1247** was included as a reference (`issues/1247`) matching the official release notes, noting it tracks the filesystem memory tools feature even though the PR itself was not merged at time of release.
4. **API manual updates** (no PR numbers) were described based on the actual file changes observed in the commits.
5. **Pydantic and deps fixes** had no associated PRs — described from commit messages only.

## Output

- `changelog.md` — Keep a Changelog formatted entry for v0.86.0
- `execution_log.md` — This file

## Timestamp

Generated: 2026-03-20
