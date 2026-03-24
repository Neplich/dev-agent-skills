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
| `docs` | — | ❌ Skip (internal) |
| `chore` | — | ❌ Skip |
| `ci` | — | ❌ Skip |
| `test` / `tests` | — | ❌ Skip |
| `build` | — | ❌ Skip |
| `style` | — | ❌ Skip |
| `wip` | — | ❌ Skip |

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
- `build(deps):`
- `Bump X from Y to Z`
