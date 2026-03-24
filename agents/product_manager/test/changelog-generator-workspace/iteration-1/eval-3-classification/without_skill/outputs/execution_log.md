# Execution Log

## Task

Classify a batch of PR titles into Keep a Changelog sections and output a formatted changelog.

## Method

Used general knowledge of Keep a Changelog format (https://keepachangelog.com/en/1.0.0/) to classify each PR by its conventional commit prefix.

## Classification Decisions

| PR | Title | Decision | Section | Reasoning |
|----|-------|----------|---------|-----------|
| #101 | feat(auth): add OAuth2 login support | INCLUDE | Added | `feat` prefix = new feature |
| #102 | fix: resolve crash when token expires | INCLUDE | Fixed | `fix` prefix = bug fix |
| #103 | chore(deps): bump requests from 2.28 to 2.31 | SKIP | — | `chore(deps)` = dependency bump, internal maintenance, not user-facing |
| #104 | perf: reduce API response time by caching | INCLUDE | Changed | `perf` = performance improvement, changes existing behavior |
| #105 | feat!: redesign plugin configuration API | INCLUDE | Changed | Breaking change (`!`) to an existing API = Changed, not Added |
| #106 | docs: update README with new examples | SKIP | — | `docs` = documentation only, not a code/behavior change |
| #107 | fix(ui): correct button alignment on mobile | INCLUDE | Fixed | `fix` prefix = bug fix |
| #108 | ci: add GitHub Actions workflow | SKIP | — | `ci` = CI/CD internal tooling, not user-facing |
| #109 | remove: drop Python 3.7 support | INCLUDE | Removed | Explicitly removes support |
| #110 | security: patch XSS vulnerability in template renderer | INCLUDE | Security | Security fix |

## Skipped Entries

- **#103** (`chore(deps)`): Dependency version bumps are internal maintenance and do not appear in user-facing changelogs.
- **#106** (`docs`): Documentation-only changes do not represent code or behavior changes.
- **#108** (`ci`): CI/CD pipeline changes are internal and not relevant to end users.

## Notes on Edge Cases

- **#105 `feat!`**: The `!` denotes a breaking change. Although it is a "feature" in the conventional commits sense, a breaking API redesign is classified under **Changed** (not Added) because it modifies existing functionality in a breaking way. Some teams may also add a `### Breaking Changes` sub-section; this was omitted here as Keep a Changelog does not define that section by default.
- **#104 `perf`**: Performance improvements fall under **Changed** since they alter how existing functionality behaves (faster response), even though no API surface changes.

## Output

Written to: `changelog.md` in the same directory.
