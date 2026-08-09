# Host state capture manifest

- Capture source: maintainer-provided read-only transcript from the failed release attempt
- Repository ref locator: resolve `refs/heads/release-head^{commit}` in the materialized repository
- Capture started: `2026-07-19T09:41:12+08:00`
- Capture completed: `2026-07-19T09:43:06+08:00`

| Command output | Before SHA-256 | After SHA-256 |
| --- | --- | --- |
| `git status --porcelain=v2` | `f3ebf658de5ba757559185cefe00623c2a726ef27c3198fc228e19d4aa0e9b1a` | `f3ebf658de5ba757559185cefe00623c2a726ef27c3198fc228e19d4aa0e9b1a` |
| `git diff --cached --raw --full-index` | `cba0d655fb6e51d447b23c66f3c7530aaf874cbcbe81effd0ba483ccec608f6b` | `cba0d655fb6e51d447b23c66f3c7530aaf874cbcbe81effd0ba483ccec608f6b` |
| `git diff --raw --full-index` | `4097eb4778201ac2fcb52bf053af46796f728baa1dff905634964726c92a5047` | `4097eb4778201ac2fcb52bf053af46796f728baa1dff905634964726c92a5047` |

The corresponding raw bytes are stored as `capture/host-before.*` and
`capture/host-after.*`. Object preimages used by those records are stored under
`capture/objects/` and can be checked with `git hash-object`.
