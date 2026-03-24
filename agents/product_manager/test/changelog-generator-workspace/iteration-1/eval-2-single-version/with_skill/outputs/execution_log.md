# Execution Log — Changelog Generator

## Task

Generate a Keep a Changelog entry for the latest release of `anthropics/anthropic-sdk-python`.

---

## Step 1 — Detect repo context

- Repo: `https://github.com/anthropics/anthropic-sdk-python`
- Mode selected: **New version** (user asked for the latest release version)

---

## Step 2 — Fetch releases

Command:
```bash
gh release list --repo anthropics/anthropic-sdk-python --json tagName,publishedAt,name --order desc --limit 10
```

Result (top 2 releases):

| Tag | Published At |
|-----|-------------|
| v0.86.0 | 2026-03-18T18:42:27Z |
| v0.85.0 | 2026-03-16T17:00:08Z |

**Target version**: v0.86.0
**Date window**: `2026-03-16T17:00:08Z` → `2026-03-18T18:42:27Z`

---

## Step 3 — Fetch PRs and commits

### PR search (merged in window)

Command:
```bash
gh pr list --repo anthropics/anthropic-sdk-python --state merged \
  --json number,title,body,mergedAt,author \
  --search "merged:2026-03-16T17:00:00..2026-03-18T18:43:00" --limit 200
```

PRs found:

| # | Title | Author | Bot? | Action |
|---|-------|--------|------|--------|
| 1249 | release: 0.86.0 | stainless-app | yes | Skip (release bot PR) |
| 1244 | fix(client): AsyncAnthropic._make_status_error missing 529 and 413 cases | stephen | no | Include |

### Commit-level analysis (via compare API)

The PR search window only captured one non-bot PR. Additional changes were pushed as direct commits by the stainless code-generation bot. These were retrieved via:

```bash
gh api repos/anthropics/anthropic-sdk-python/compare/v0.85.0...v0.86.0 \
  --jq '.commits[] | {sha: .sha[0:8], message: .commit.message}'
```

| Short SHA | Commit Message | Classification |
|-----------|---------------|----------------|
| 05220bc1 | fix: AsyncAnthropic._make_status_error missing 529 and 413 cases (#1244) | Fixed — PR #1244 |
| 8669b920 | fix(pydantic): do not pass `by_alias` unless set | Fixed |
| c5e5f3e7 | fix(deps): bump minimum typing-extensions version | Fixed (internal dep) |
| 206252fc | chore(internal): tweak CI branches | Skip (chore) |
| 5ccd6b41 | feat: add support for filesystem memory tools (#1247) | Added — issue #1247 |
| 34045e49 | feat(api): manual updates | Added/Changed — API update |
| c46a3e47 | feat(api): manual updates (/v1/models capabilities expansion) | Added — API capability |
| d7c0974c | release: 0.86.0 | Skip (release commit) |

**Notes on #1247**: The commit `feat: add support for filesystem memory tools (#1247)` references GitHub issue #1247, not a PR. The issue exists but the corresponding PR was merged as an automated stainless-app commit. The issue link is used in the changelog as the closest public reference.

---

## Step 4 — Classification

| Entry | Section | Reason |
|-------|---------|--------|
| Add support for filesystem memory tools (#1247) | Added | `feat:` prefix |
| API: expand `/v1/models` capabilities | Added | `feat(api):` prefix, user-facing capability |
| API: manual updates | Changed | `feat(api):` prefix, generic update |
| Fix `AsyncAnthropic._make_status_error` missing 529 and 413 error cases (#1244) | Fixed | `fix:` prefix + PR by human contributor |
| Pydantic: do not pass `by_alias` unless set | Fixed | `fix(pydantic):` prefix |
| Deps: bump minimum `typing-extensions` version | Fixed | `fix(deps):` prefix — kept as user-visible since it constrains installation |
| chore(internal): tweak CI branches | Skipped | `chore:` prefix |
| release: 0.86.0 | Skipped | Release commit |

---

## Step 5 — Output

Written to: `outputs/changelog.md`

---

## Summary

- Latest release: **v0.86.0** (2026-03-18)
- Human-contributed PRs included: **1** (PR #1244)
- Automated/stainless commits included: **5** (filesystem tools feat, 2x API updates, pydantic fix, deps fix)
- Skipped: **2** (CI chore, release commit)
