# v1.2.0 post-release review request

- Review phase: post-release
- Released tag: `refs/tags/v1.2.0`
- Released commit locator: resolve `refs/tags/v1.2.0^{commit}`
- Released tree locator: resolve `refs/tags/v1.2.0^{tree}`
- Pre-release authority ref: `refs/heads/pre-tag-handoff`
- Pre-release commit locator: resolve `refs/heads/pre-tag-handoff^{commit}`
- Pre-release tree locator: resolve `refs/heads/pre-tag-handoff^{tree}`
- Committed audit read: `git show refs/heads/pre-tag-handoff:docs/site/.meta/audit/audit-v1.2.0.md`
- Committed handoff read: `git show refs/heads/pre-tag-handoff:docs/site/.meta/audit/handoffs/pre-tag-v1.2.0.md`
- Current worktree record: `docs/site/.meta/audit/audit-v1.2.0.md`
- Current worktree status: `M docs/site/.meta/audit/audit-v1.2.0.md`
- Raw base-to-tag name status: `release-evidence/tag-tree-diff.name-status`
- Raw base-to-tag patch: `release-evidence/tag-tree-diff.patch`
- Post-release record ref: `refs/heads/release-evidence/v1.2.0`
- Target release version: `v1.2.0` (maintainer confirmed)

Version surfaces in scope are `docs/site/release-notes/v1.2.0.md`,
`docs/site/release-notes/index.md`, `docs/site/.meta/releases.json`, and
`package.json`. The captured post-release result path was absent before the
failed result-write attempt.
