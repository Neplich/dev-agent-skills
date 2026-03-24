---
name: release-notes-generator
description: Generate user-facing release notes for a specific version from GitHub PRs and release tags. Unlike changelog-generator (developer-facing, exhaustive), release notes are benefit-oriented, concise, and written for end users or customers. Use this skill when the user asks to write release notes, draft a release announcement, create user-friendly version summary, publish what's new for a release, or describe changes in plain language. Trigger on phrases like "写发版说明", "生成 release notes", "发版公告", "用户友好的版本说明", "这个版本有什么新功能", "draft release announcement", "what's new in v1.x", or any request to describe a release to users or customers rather than developers.
---

# Release Notes Generator

Generate user-facing release notes for a GitHub release. This is distinct from `changelog-generator` — while changelogs document *what* changed for developers, release notes explain *why it matters* to end users in plain language.

All data comes from `gh` CLI — no external MCP needed. Can read from an existing `docs/changelog.md` as a shortcut, or fetch directly from GitHub PRs.

## Step 1 — Identify the target version

Ask if not specified: "Which version would you like release notes for?" Accept tag names (e.g. `v1.2.0`), "latest", or "last release".

```bash
# Get the target release
gh release view v1.2.0 --json tagName,publishedAt,name,body

# Or get latest
gh release list --json tagName,publishedAt,name --order desc --limit 5
```

Capture `VERSION`, `RELEASE_DATE`, `REPO_URL`, `OWNER/REPO`.

## Step 2 — Gather change data

**Preferred path — read existing changelog first:**

If `docs/changelog.md` exists, read it and extract the section for this version. This saves re-fetching and avoids redundant work. Skip to Step 3 if the changelog section is complete.

**Fallback — fetch from GitHub directly:**

```bash
# Get the previous release tag to define the PR window
gh release list --json tagName,publishedAt --order desc --limit 20

# Fetch merged PRs between prev and current release
gh pr list \
  --state merged \
  --json number,title,body,mergedAt,author,labels \
  --search "merged:PREV_DATE..RELEASE_DATE" \
  --limit 200
```

**Skip automatically:**
- Bot authors (`dependabot[bot]`, `renovate[bot]`, any `[bot]` suffix)
- Prefix `chore:` / `ci:` / `test:` / `build:` / `docs:` / `style:`
- Scope `internal` (e.g. `feat(internal):`)
- Generic infra bumps ("Bump X from Y to Z", "update lockfile")

## Step 3 — Identify highlights

Release notes are not an exhaustive list. The most important step is *curation*:

- **Select 2–4 headline features** — `feat:` PRs that deliver clear user value. Prefer things that change what the user can *do*, not how the internals work.
- **Group minor fixes** — don't list every `fix:` individually; summarize as "X bug fixes" unless a fix is significant enough that users should know about it.
- **Surface breaking changes prominently** — anything marked `feat!:` / `fix!:` or with `BREAKING CHANGE:` in the body must be in a dedicated section at the top.
- **Performance wins worth calling out** — only if measurably meaningful (e.g. "2× faster startup", "50% reduction in memory usage").

The goal: someone who reads this in 60 seconds knows whether to upgrade and what to expect.

## Step 4 — Write the release notes

Use this structure. Omit sections with no content.

```markdown
# Release Notes — v{VERSION} ({RELEASE_DATE})

> {One-sentence headline describing the release theme, e.g. "This release focuses on performance and easier onboarding."}

## ✨ What's New

### {Feature Name}
{1–2 sentences describing the feature from the user's perspective. What can they do now that they couldn't before?}

{Optional: when is this useful? 1–2 bullet points for library/framework releases, e.g. "Ideal for: live dashboards, AI streaming, real-time notifications."}

{Optional: 3–5 line code example. Include when it dramatically clarifies usage — especially for CLI commands, SDK methods, or API patterns where seeing the syntax is worth more than a paragraph of prose. Skip for conceptual features.}

### {Another Feature}
{...}

## 🐛 Bug Fixes

{If ≤ 3 significant fixes: list them individually with one sentence each.}
{If many minor fixes: "Fixed X issues including [short description of the most notable ones]."}

## 💥 Breaking Changes

> ⚠️ This section is required reading before upgrading.

### {Breaking Change Title}
**What changed:** {Describe the change in plain terms.}
**How to update:** {Step-by-step migration, or link to migration guide.}

## 🔧 Other Improvements

{Optional: a brief bullet list for changes that don't fit above — performance tweaks, minor enhancements, dependency updates worth noting.}

## ⚠️ Upgrade Actions

{Include this section ONLY when the release requires users to take specific action beyond running the install command — e.g. import path changes, config key renames, minimum dependency bumps, error handler updates. Use a numbered list of concrete steps. Omit entirely if no action required beyond installing the new version.}

1. {Specific action: "Update your import from `pkg.lib.X` to `pkg.X`"}
2. {Specific action: "If you catch `OldError`, update to `NewError`"}

## ⬆️ Upgrading

```
{install command, e.g. pip install pkg==VERSION or brew upgrade gh}
```

{State clearly if there are no breaking changes: "No breaking changes. Existing code works without modification."}

{If this is a CLI tool, provide platform-specific commands:}
- macOS: `brew upgrade {tool}`
- Windows: `winget upgrade {tool-id}`
- Linux: see [install docs]({URL})

---

{Full changelog: REPO_URL/compare/PREV_TAG...THIS_TAG}

{Optional — for open source projects with community contributors: "Thanks to our {N} first-time contributors: @user1, @user2, ..."}
```

**Writing tone:**
- Write for the user, not the developer: "You can now do X" not "Implemented X via Y"
- Use active voice and present tense
- Avoid jargon unless the audience is clearly technical (e.g. a developer SDK release can use technical terms)
- Keep feature prose to 2 sentences max — code examples can add clarity beyond that
- Don't say "We are pleased to announce" — get to the point

**When to include code examples:**
Code examples are worth including when: the feature is a new command/flag, a new method call, or a new pattern where seeing the syntax saves users time. Keep them to 3–8 lines. Skip for conceptual changes, config defaults, or internal improvements.

If a feature has a "before/after" migration (import path changed, API shape changed), a before/after code comparison is more useful than a description alone.

**PR link format** — include links to key PRs for traceability, but don't clutter every line:
- Highlight PRs: `([#N](REPO_URL/pull/N))` inline
- Grouped fixes: list PR numbers at the end `(#N, #N, #N)`

## Step 5 — Determine output location

| Scenario | Output path |
|----------|-------------|
| First time, single file | `docs/release-notes.md` (append newest at top) |
| Per-version files preferred | `docs/release-notes/v{VERSION}.md` |
| GitHub Release body | Output to console, ready to paste into `gh release edit` |

Ask the user if not clear from context. Default to `docs/release-notes/v{VERSION}.md` for new projects (easier to link to specific versions).

If the file already exists, read it first, then insert the new version at the top without overwriting older entries.

## Step 6 — Optionally update GitHub Release body

If the user wants to publish directly to GitHub:

```bash
gh release edit v{VERSION} --notes-file docs/release-notes/v{VERSION}.md
```

Confirm before running this — it overwrites the existing GitHub Release description.

## Edge cases

- **No user-facing changes in a release**: write a short note — "This release contains internal improvements and dependency updates only. No user-facing changes." Don't produce an empty file.
- **Major version (breaking-heavy)**: if more than 2 breaking changes, consider a "Migration Guide" section linking to a separate doc rather than inlining everything.
- **Pre-release or RC tags** (e.g. `v2.0.0-rc.1`): note the pre-release status prominently at the top — "This is a release candidate. Not recommended for production."
- **Very large releases (20+ features)**: group features into themes (e.g. "Developer Experience", "Performance", "New Integrations") instead of a flat list.
- **No GitHub Releases, only tags**: use `gh api repos/{OWNER}/{REPO}/git/refs/tags` to get tag dates, then fetch PRs using the date window.
