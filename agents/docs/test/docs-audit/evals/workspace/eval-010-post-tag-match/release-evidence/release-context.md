# v1.2.0 post-release review request

- Review phase: post-release
- Released tag: `refs/tags/v1.2.0`
- Released commit locator: resolve `refs/tags/v1.2.0^{commit}`
- Released tree locator: resolve `refs/tags/v1.2.0^{tree}`
- Pre-release package ref: `refs/release-evidence/v1.2.0`
- Package commit locator: resolve `refs/release-evidence/v1.2.0^{commit}`
- Package tree locator: resolve `refs/release-evidence/v1.2.0^{tree}`
- Package handoff path: `docs/site/.meta/audit/handoffs/pre-tag-v1.2.0.md`
- Package audit path: `docs/site/.meta/audit/audit-v1.2.0.md`
- Target release version: `v1.2.0` (maintainer confirmed)
- Proposed post-release record ref: `refs/heads/release-evidence/v1.2.0`
- Maintainer decision for the proposed record ref: no decision is included in this request

The review must be performed once in the current repository and once in a new
local clone created with the default clone refspec. The clone must be inspected
from its own Git directory; refs or object IDs must not be copied into it from
the source repository.

Version surfaces in scope are `docs/site/release-notes/v1.2.0.md`,
`docs/site/release-notes/index.md`, `docs/site/.meta/releases.json`, and
`package.json`.
