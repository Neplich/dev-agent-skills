# Candidate transaction event log

## Staged snapshot A

- `M 100644 100755 a111 b111 docs/site/api/catalog-items.md`
- `T 100644 120000 a222 b222 docs/site/api/catalog-status.md`
- `R docs/site/release-notes/index.md -> docs/site/release-notes/archive.md`
- `D docs/site/release-notes/v1.2.0.md`

## Staged snapshot B after final record replacement

- `A 120000 docs/site/.meta/audit/audit-v1.2.0.md`
- `A 120000 docs/site/.meta/audit/unexpected-link.md`

## Hypothetical committed snapshot

- `target_ref..anchor_commit`: `T 100644 120000 a222 b222 docs/site/api/catalog-status.md`
- `anchor_commit..handoff_commit`: `A 160000 000000 c333 docs/site/.meta/audit/linked-evidence`
