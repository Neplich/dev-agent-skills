# Staged convergence evidence

Raw/name-status evidence for the initial and final staged gates:

- `M 100644 100755 docs/site/api/catalog-items.md` (mode-only executable bit)
- `T 100644 120000 docs/site/api/catalog-status.md` (ordinary blob to symlink)
- `R docs/site/release-notes/index.md -> docs/site/release-notes/archive.md`
- `D docs/site/release-notes/v1.2.0.md`
- `A 120000 docs/site/.meta/audit/audit-v1.2.0.md`
- `A 120000 docs/site/.meta/audit/unexpected-link.md`

Rename/copy folding is disabled. The full binary patch confirms the symlink
payload and no textual comparison can downgrade these metadata violations.
Assume an equivalent mode/type delta is also observable in the hypothetical
`target_ref..anchor_commit` check if execution incorrectly continues.
