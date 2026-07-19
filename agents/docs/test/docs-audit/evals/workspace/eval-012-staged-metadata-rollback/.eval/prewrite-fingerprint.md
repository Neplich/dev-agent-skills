# Host pre-write fingerprint

- branch SHA: `2222222`
- index/worktree: captured with `git status --porcelain=v2`
- authorized page modes/types: `100644 blob`
- candidate record preimage: absent
- discovery handoff preimage: absent
- unrelated user changes: preserve exactly; never restore or overwrite them

Successful restoration requires the same branch SHA, porcelain v2 inventory,
raw staged and unstaged diffs, per-path mode/type and byte hashes. If any value
cannot be reproduced, the phase remains blocked and must list residual paths,
index entries, and manual recovery commands.
