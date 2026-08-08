# Isolated release-index capture

- Capture source: temporary index created during the failed release attempt
- Capture time: `2026-07-19T09:42:18+08:00`
- Work tree used by the capture: `/srv/releases/atlas-docs`

| Command | Captured output | SHA-256 |
| --- | --- | --- |
| `git diff --cached --raw --full-index -M` | `capture/staged.raw` | `c0bd043e30f88ecdac6bad84ee152c1fdf0f5e00647d8c6ce436dc7fb96993a8` |
| `git diff --cached --name-status -M` | `capture/staged.name-status` | `7142b87aed6a4278a76ae965ffeb441141ceb84a881bf66da0a25e16d1df8058` |
| `git diff --cached --summary -M` | `capture/staged.summary` | `178de020f2ca83706208909e04275d2cb8d2c6c3f6caefb1b506e04d87654294` |
| `git diff --cached --binary --full-index -M` | `capture/staged.patch` | `e9ef0cdec08429b791ff38bfb78f24cf21038588d27cee5a7d21dfa7012ce22e` |

Blob preimages referenced by the raw output and patch are stored under
`capture/objects/` for independent `git hash-object` checks.
