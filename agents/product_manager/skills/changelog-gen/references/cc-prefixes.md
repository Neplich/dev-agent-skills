# Conventional Commits — Prefix Reference

## Standard Prefixes

| Prefix | Changelog Section | Include? |
|--------|------------------|---------|
| `feat` | Added | ✅ Yes |
| `fix` | Fixed | ✅ Yes |
| `perf` | Changed | ✅ Yes |
| `refactor` | Changed | ✅ Yes |
| `deprecate` / `deprecated` | Deprecated | ✅ Yes |
| `remove` / `revert` | Removed | ✅ Yes |
| `security` | Security | ✅ Yes |
| `docs` | Review body/context | Conditional |
| `chore` | — | ❌ Skip |
| `ci` | Review body/context | Conditional |
| `test` / `tests` | Review body/context | Conditional |
| `build` | Review body/context | Conditional |
| `style` | Review body/context | Conditional |
| `wip` | — | ❌ Skip |

## Conditional Low-Value Prefixes

`docs`, `test`, `ci`, `build`, and `style` are low-priority candidates, not automatic skips. Read the PR body, title, and any available file context before deciding.

Include these PRs when the content changes:

- skill behavior, routing, handoff, gates, or collaboration boundaries
- eval fixtures, assertions, durable `comparison.md`, fresh validation, or required checks
- marketplace registry, skill metadata, installation, packaging, or lockfile semantics
- release workflow, changelog preflight, tags, draft releases, or publishing flow
- public README, reference, or skill documentation that changes how users operate the project

Skip these PRs when they are only:

- spelling, copyediting, formatting, or link text cleanup
- README examples that do not change behavior or operational guidance
- test renames, fixture cleanup, mock cleanup, or coverage reshuffling without contract changes
- CI cache, runner, dependency install, or lint-only maintenance without release-gate impact

If the body is empty and changed files are unavailable, skip low-value prefixes unless the title itself clearly describes user-visible behavior.

## Scope Handling

`feat(auth): add OAuth2` → strip `feat(auth):` → `Add OAuth2`
`fix(api): resolve null pointer` → strip `fix(api):` → `Resolve null pointer`

## Breaking Changes

Indicated by `!` after type/scope:
- `feat!: redesign config API` → ⚠️ BREAKING, Added section
- `fix(core)!: change return type` → ⚠️ BREAKING, Fixed section

Or in PR body:
```
BREAKING CHANGE: the `config` field has been renamed to `configuration`
```

When a breaking change is detected, format the entry as:
```
- ⚠️ **BREAKING**: Redesign config API ([#42](url))
```
And place it at the top of its section.

## Ambiguous / No Prefix

When a PR title has no conventional prefix, classify by keywords:

**→ Added** (new capability introduced):
- starts with: `add`, `implement`, `introduce`, `create`, `support`, `enable`, `new`

**→ Fixed** (something broken now works):
- starts with: `fix`, `resolve`, `patch`, `correct`, `repair`, `handle`, `prevent`
- contains: `crash`, `bug`, `error`, `issue`, `broken`

**→ Changed** (existing behavior modified):
- starts with: `update`, `change`, `improve`, `enhance`, `refactor`, `migrate`, `upgrade`, `replace`

**→ Removed**:
- starts with: `remove`, `delete`, `drop`, `deprecate`

**→ Security**:
- contains: `security`, `vulnerability`, `CVE`, `XSS`, `injection`, `auth bypass`

**Default fallback**: if none of the above match, use **Changed**.

## Bot PR Detection

Skip PRs where `author.login` matches:
- `dependabot`, `dependabot[bot]`
- `renovate`, `renovate[bot]`
- `github-actions`, `github-actions[bot]`
- Any login ending in `[bot]`

Also skip PRs with these title patterns regardless of author:
- `chore(deps):` or `chore(deps-dev):`
- `chore(release):`
- `build(deps):` or `build(deps-dev):`
- `Bump X from Y to Z`
