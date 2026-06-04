# Release Outline

Use the repository's existing release outline before introducing a new structure.

For this repository, match the `v0.1.1` release outline:

```markdown
# Release Notes - v{VERSION} ({YYYY-MM-DD})

{One short paragraph describing the release theme and why it matters.}

## 重点更新

### {Highlight title}

{One concise user-facing paragraph. Include the key PR link inline, for example ([#25](https://github.com/owner/repo/pull/25)).}

### {Another highlight title}

{One concise user-facing paragraph.}

## 其他改进

- {Short improvement.}
- {Short improvement.}

## 升级说明

{State whether there are breaking changes. If there are no breaking changes, say so clearly.}

### Claude Code

{Only include when the repository/plugin uses Claude Code installation or update commands.}

```text
/plugin marketplace update {marketplace}
/plugin update {agent}@{marketplace}
/reload-plugins
```

### Codex

{Only include when the repository/plugin uses a Codex install or update entrypoint.}

```text
Fetch and follow instructions from {INSTALL_URL}
```

## 变更明细

- {conventional title} by @{author} in [#{number}]({PR_URL})

完整变更： {REPO_URL}/compare/{PREV_TAG}...{VERSION}
```

## Structure Rules

- Put `完整变更` after `变更明细`, not before it.
- Do not include an `已关闭 Issue` section unless the user explicitly asks for it.
- Keep `变更明细` as the final section.
- Mention contributors in `变更明细` with `by @user in [#N](PR_URL)`.
- Link major highlights inline, but avoid linking every sentence.
- Keep release notes in Chinese for this repository.

## Content Rules

- Write for users and maintainers, not as an internal implementation log.
- Start with the release outcome, then list details.
- Prefer 3 to 5 highlights. Group smaller changes under `其他改进`.
- Keep each highlight to one short paragraph unless an upgrade action needs more detail.
- Include upgrade commands only when they are stable and useful for the release audience.
- If a release has breaking changes, place them near the top and add concrete migration steps.
- If there are no breaking changes, say `无破坏性变更。已有安装可以继续使用。`

## Change Detail Rules

Fetch PR authors before writing `变更明细`:

```bash
gh pr view {NUMBER} --json number,title,author,url
```

Format each item as:

```markdown
- feat: 示例更新 by @Neplich in [#25](https://github.com/Neplich/dev-agent-skills/pull/25)
```

If a change came from a direct commit and no PR exists, use the commit author and short SHA:

```markdown
- fix: 示例修复 by @user in `abc1234`
```

## Optional Generic Outline

For repositories without an existing release style, use:

```markdown
# Release Notes - v{VERSION} ({YYYY-MM-DD})

{One short release theme paragraph.}

## What's New

### {Feature Name}

{User-facing description.}

## Bug Fixes

- {Fix summary.}

## Other Improvements

- {Improvement summary.}

## Upgrade Guide

{Upgrade guidance or no-breaking-change statement.}

## What's Changed

- {conventional title} by @{author} in [#{number}]({PR_URL})

Full changelog: {REPO_URL}/compare/{PREV_TAG}...{VERSION}
```
