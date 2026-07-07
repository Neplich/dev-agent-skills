---
name: changelog-generator
description: "Internal PM specialist—not a direct entry point. Invoked by pm-agent after entry classification to generate versioned changelogs from merged PRs, tags, and repository release history."
visibility: internal
---

# Changelog Generator

Generate and maintain per-version changelog files under `docs/changelog/`, such as `docs/changelog/changelog-v1.2.0.md`, following [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format. Source of truth: merged GitHub PRs and release tags, fetched via `gh` CLI — no external MCP required.

## Modes

Choose the mode based on what the user asks for:

| Mode | When to use | Scope |
|------|-------------|-------|
| **Unreleased** | "what's changed since last release" / "update unreleased" | PRs merged since latest tag |
| **New version** | "generate changelog for v1.2.0" / "add entry for latest release" | PRs between two specified tags |
| **Full** | "generate changelog from scratch" / "rebuild the whole changelog" | All releases in history |

If the user's intent is ambiguous, ask which mode they want before proceeding.

## Step 1 — Detect repo context

```bash
gh repo view --json nameWithOwner,url,defaultBranchRef
```

Confirm you're inside a GitHub-connected repo. Capture `REPO_URL` (e.g. `https://github.com/owner/repo`) for PR link formatting later.

Resolve the target changelog path before writing:

- Released versions use `docs/changelog/changelog-v{VERSION}.md`.
- Unreleased changes use `docs/changelog/changelog-unreleased.md`.

If the target file already exists, read it before making changes so you can do a surgical update instead of a full overwrite.

## Step 2 — Fetch releases

```bash
gh release list --json tagName,publishedAt,name --order desc --limit 100
```

Build a sorted list of `(tag, date)` pairs. This lets you determine the date window for each version's PRs.

For **Unreleased** mode: the window is `merged:>LATEST_RELEASE_DATE`.
For **New version** mode: the window is `merged:PREV_RELEASE_DATE..THIS_RELEASE_DATE`.
For **Full** mode: repeat for every adjacent tag pair, plus an Unreleased section.

## Step 3 — Fetch PRs per window

```bash
gh pr list \
  --state merged \
  --json number,title,body,mergedAt,author \
  --search "merged:START_DATE..END_DATE" \
  --limit 200
```

Paginate if needed (add `--limit 200` and re-query with narrower windows for dense histories).

**Skip these PRs/commits automatically:**
- Author is a bot: `dependabot`, `renovate`, `github-actions`, or any login ending in `[bot]`
- Title matches `chore(deps)`, `chore(deps-dev)`, `build(deps)`, `build(deps-dev)`, `chore(release)`, `Bump X from Y to Z`
- Scope is `internal`: e.g. `feat(internal):`, `fix(internal):`, `refactor(internal):` — these are implementation details not relevant to users

Do not automatically skip `docs:`, `test:`, `ci:`, general `build:`, or `style:` titles outside the dependency bump patterns above. Treat them as low-priority candidates and review the PR body, title, and any available file context before deciding.

## Step 4 — Classify each PR

Read the PR **title** to determine its changelog section. Use this mapping:

| Title prefix | Section | Notes |
|---|---|---|
| `feat:` / `feat(scope):` | Added | New feature |
| `fix:` / `fix(scope):` | Fixed | Bug fix |
| `perf:` | Changed | Performance improvement |
| `refactor:` | Changed | Internal restructuring |
| `deprecate:` | Deprecated | |
| `remove:` / `revert:` | Removed | |
| `security:` | Security | |
| `docs:` | Review body/context | Include if it changes user-facing docs, skill behavior, release workflow, installation, marketplace, or collaboration rules |
| `test:` / `ci:` / `build:` / `style:` | Review body/context | Include if it changes eval contracts, durable comparison, required gates, release workflow, installation, or user-visible behavior |
| `chore:` | — | Skip unless the title/body clearly describes user-visible behavior |

For docs-first or skill marketplace repositories, include `docs:`, `test:`, `ci:`, `build:`, or `style:` PRs when the PR body or title indicates changes to:

- skill behavior, routing, handoff, gates, or collaboration boundaries
- eval fixtures, assertions, durable `comparison.md`, fresh validation, or required checks
- marketplace registry, skill metadata, installation, packaging, or lockfile semantics
- release workflow, changelog preflight, tags, draft releases, or publishing flow
- public README, reference, or skill documentation that changes how users operate the project

Skip low-value maintenance PRs when title/body/context indicate only spelling, formatting, link text cleanup, test or fixture renames without contract changes, mock cleanup, CI cache/runner maintenance, or dependency installation details without release-gate impact. If the body is empty and changed files are unavailable, skip low-value prefixes unless the title itself clearly describes user-visible behavior.

**No prefix or ambiguous title**: use your judgment based on the PR title content — "add X", "implement X", "support X" → Added; "fix X", "resolve X", "patch X" → Fixed; anything that sounds like a change → Changed. Don't ask the user about every ambiguous case.

**Breaking changes**: if the title contains `feat!:` / `fix!:` or the body contains `BREAKING CHANGE:`, add a `⚠️ BREAKING:` prefix to the entry and place it at the top of its section.

**Clean the title for display**: strip the conventional prefix, capitalize the first letter, remove trailing period. Optionally keep the scope as a brief context prefix in bold if it adds meaningful location context for the reader (e.g. `**auth:**`, `**api:**`). Skip scope if it's generic (`core`, `internal`, `misc`).

Examples:
- `feat(auth): add OAuth2 login` → `**auth:** Add OAuth2 login` (or just `Add OAuth2 login`)
- `fix: resolve crash on empty list` → `Resolve crash on empty list`
- `fix(client): fix async error handling` → `**client:** Fix async error handling`
- `chore: bump deps` → skip
- `build(deps): bump vite` → skip
- `docs: update release workflow` with body mentioning changelog preflight → Changed
- `test: refresh eval fixtures` with body mentioning durable comparison contract → Changed
- `ci: tune cache restore key` with no release-gate impact → skip

## Step 5 — Format the output

Group entries by section in this order (omit empty sections):

```
### Added
### Changed
### Deprecated
### Removed
### Fixed
### Security
```

Each entry:
```
- CLEANED_TITLE ([#NUMBER](REPO_URL/pull/NUMBER))
```

Full version block:
```markdown
## [1.2.0] - 2024-03-15

### Added
- Support for OAuth2 login ([#87](https://github.com/owner/repo/pull/87))

### Fixed
- Resolve token expiry crash on mobile ([#91](https://github.com/owner/repo/pull/91))
```

If a version has no classifiable PRs after skipping bots and chores, note:
```markdown
## [1.0.1] - 2024-01-10

_No user-facing changes (dependency updates and internal maintenance only)._
```

## Step 6 — Write to docs/changelog/

**Version file header** (use this pattern if creating a released version file from scratch):
```markdown
# Changelog - v{VERSION}

## [v{VERSION}] - YYYY-MM-DD
```

**Unreleased file header** (use this exactly if creating `docs/changelog/changelog-unreleased.md` from scratch):
```markdown
# Changelog - Unreleased

## [Unreleased]

```

**Update strategy:**

- **Creating a released version file**: create or update only `docs/changelog/changelog-v{VERSION}.md`.
- **Updating Unreleased only**: create or update only `docs/changelog/changelog-unreleased.md`.
- **Full regeneration**: regenerate the per-version files under `docs/changelog/`. Warn the user before doing this if they have manually edited content in those files.
- **Root index**: if a root `CHANGELOG.md` exists, keep it as an index that links to versioned files. Do not duplicate changelog entries there.

Always create `docs/changelog/` if it doesn't exist.

## Edge Cases

- **Few or no PRs in a version window**: some repos (e.g. SDK generators) push changes as direct commits rather than PRs. Fall back to `gh api repos/{owner}/{repo}/compare/PREV_TAG...THIS_TAG` to get all commits, then classify commit messages by the same prefix rules.
- **PR number referenced but not merged**: when a commit message references `#NUMBER` but the PR was not actually merged (e.g. it's an issue reference), use `/issues/NUMBER` in the link instead of `/pull/NUMBER`. Verify with `gh pr view NUMBER --json state` if unsure.
- **More than 40 PRs in one release**: group closely related entries (e.g., multiple "add X field to Y" PRs) into a single summarized line, keeping all PR links. Note the grouping.
- **Squash merges with generic titles** like "Merge PR #42": fall back to reading the PR description for context.
- **Tags without a corresponding GitHub Release**: still work — use the tag date from `gh api repos/{owner}/{repo}/git/refs/tags` if `gh release list` doesn't have it.
- **First release (no previous tag)**: include all PRs merged up to the release date.

## Reference

See `references/cc-prefixes.md` for the full Conventional Commits prefix list and edge cases.
