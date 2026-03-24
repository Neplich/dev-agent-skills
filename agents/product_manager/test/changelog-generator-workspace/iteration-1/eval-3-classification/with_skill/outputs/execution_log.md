# Execution Log — PR Classification

## Skill Used
`changelog-generator` (Step 4 — Classify each PR)

## Input
10 PR titles to be classified into Keep a Changelog sections.

---

## Classification Decisions

### #101 — `feat(auth): add OAuth2 login support`
- **Rule matched**: `feat(scope):` → **Added**
- **Title cleaning**: Strip `feat(auth):` prefix and scope, capitalize → `Add OAuth2 login support`
- **Result**: Included under `Added`

---

### #102 — `fix: resolve crash when token expires`
- **Rule matched**: `fix:` → **Fixed**
- **Title cleaning**: Strip `fix:` prefix, capitalize → `Resolve crash when token expires`
- **Result**: Included under `Fixed`

---

### #103 — `chore(deps): bump requests from 2.28 to 2.31`
- **Rule matched**: `chore(deps):` → **Skip** (matches "chore(deps)" dependency-bump pattern)
- **Skill rule**: Step 3 says to skip PRs whose title matches `chore(deps)` or similar dependency/CI-only patterns
- **Result**: Skipped — dependency update, no user-facing change

---

### #104 — `perf: reduce API response time by caching`
- **Rule matched**: `perf:` → **Changed**
- **Title cleaning**: Strip `perf:` prefix, capitalize → `Reduce API response time by caching`
- **Result**: Included under `Changed`

---

### #105 — `feat!: redesign plugin configuration API`
- **Rule matched**: `feat!:` → **Added** + **BREAKING CHANGE**
- **Title cleaning**: Strip `feat!:` prefix, capitalize → `Redesign plugin configuration API`
- **Breaking change handling**: Title contains `feat!:`, so entry gets `⚠️ BREAKING:` prefix and is placed at the **top** of its section
- **Result**: Included under `Added` as `⚠️ BREAKING: Redesign plugin configuration API`, placed first

---

### #106 — `docs: update README with new examples`
- **Rule matched**: `docs:` → **Skip** (internal documentation)
- **Skill rule**: `docs:` → `—` (skip)
- **Result**: Skipped — documentation-only change

---

### #107 — `fix(ui): correct button alignment on mobile`
- **Rule matched**: `fix(scope):` → **Fixed**
- **Title cleaning**: Strip `fix(ui):` prefix and scope, capitalize → `Correct button alignment on mobile`
- **Result**: Included under `Fixed`

---

### #108 — `ci: add GitHub Actions workflow`
- **Rule matched**: `ci:` → **Skip**
- **Skill rule**: `ci:` → `—` (skip)
- **Result**: Skipped — CI/infrastructure change, no user-facing impact

---

### #109 — `remove: drop Python 3.7 support`
- **Rule matched**: `remove:` → **Removed**
- **Title cleaning**: Strip `remove:` prefix, capitalize → `Drop Python 3.7 support`
- **Result**: Included under `Removed`

---

### #110 — `security: patch XSS vulnerability in template renderer`
- **Rule matched**: `security:` → **Security**
- **Title cleaning**: Strip `security:` prefix, capitalize → `Patch XSS vulnerability in template renderer`
- **Result**: Included under `Security`

---

## Summary Table

| PR | Original Title | Section | Action |
|----|---------------|---------|--------|
| #101 | feat(auth): add OAuth2 login support | Added | Included |
| #102 | fix: resolve crash when token expires | Fixed | Included |
| #103 | chore(deps): bump requests from 2.28 to 2.31 | — | **Skipped** (dependency bump) |
| #104 | perf: reduce API response time by caching | Changed | Included |
| #105 | feat!: redesign plugin configuration API | Added | Included (BREAKING) |
| #106 | docs: update README with new examples | — | **Skipped** (internal docs) |
| #107 | fix(ui): correct button alignment on mobile | Fixed | Included |
| #108 | ci: add GitHub Actions workflow | — | **Skipped** (CI only) |
| #109 | remove: drop Python 3.7 support | Removed | Included |
| #110 | security: patch XSS vulnerability in template renderer | Security | Included |

**Total included**: 7 entries across 5 sections
**Total skipped**: 3 entries (#103, #106, #108)

## Section Order Applied
Per the skill's Step 5 specification:
`Added → Changed → Deprecated → Removed → Fixed → Security`
(Empty sections — Deprecated — are omitted.)
