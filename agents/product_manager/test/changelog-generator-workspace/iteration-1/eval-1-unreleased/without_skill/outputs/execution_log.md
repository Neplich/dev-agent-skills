# Execution Log

## Task

Generate the `[Unreleased]` section of a changelog (Keep a Changelog format) for
`anthropics/anthropic-sdk-python`, covering all merged PRs after the latest release tag.

## Steps Performed

### 1. Identify the latest release tag

Command: `gh release list --repo anthropics/anthropic-sdk-python --limit 5`

Result:
- Latest release: **v0.86.0** — released 2026-03-18T18:42:27Z
- Previous: v0.85.0 (2026-03-16), v0.84.0 (2026-02-25), …

### 2. Find PRs merged after v0.86.0

Command: `gh api "repos/anthropics/anthropic-sdk-python/pulls?state=closed&sort=updated&direction=desc&per_page=50"`

Filtered to PRs where `merged_at > "2026-03-18T18:42:06Z"` (the merge timestamp of the release PR).

Result: **0 PRs** were merged after v0.86.0.

### 3. Verify via commit comparison

Command: `gh api "repos/anthropics/anthropic-sdk-python/compare/v0.86.0...main"`

Result:
- `ahead_by: 0`
- `behind_by: 0`
- `commits: []`

The `main` branch HEAD is exactly the v0.86.0 release commit. There are no unreleased changes.

### 4. Enumerate open (pending) PRs for informational purposes

Command: `gh pr list --repo anthropics/anthropic-sdk-python --state open --limit 10`

Found 10 open PRs (not merged), including:
- #1263 — fix: map SSE error types to correct HTTP status codes in streaming
- #1259 — feat(lib/tools): add observability hooks to tool_runner
- #1255 — fix: remove spurious pass statement in signature_delta handler
- #1251 — Fix: IndexError when streaming with multiple content blocks
- #1247 — perf: skip no-op recursive transform for types without PropertyInfo
- #1246 — fix(bedrock): add missing stream() method to beta.messages

These are listed as HTML comments in `changelog.md` for reference but are NOT included in
the `[Unreleased]` section because they have not been merged into `main`.

## Conclusion

As of 2026-03-20, there are **no unreleased changes** in `anthropics/anthropic-sdk-python`.
The `main` branch is at exactly v0.86.0. The `[Unreleased]` section in `changelog.md` is
intentionally empty, with a note explaining this state.

## Output

- `changelog.md` — Keep a Changelog formatted file with an empty `[Unreleased]` section
  and the most recent release (v0.86.0) included for reference.
