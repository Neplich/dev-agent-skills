# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `delivery`
- Eval: `eval-001-create-pr-with-commits`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e` from `agents/engineer/test/delivery/evals/workspace/eval-001-create-pr-with-commits`.
- Fixture SHA-256: `415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e`
- Prompt SHA-256: `0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `3291b3bf29fbba656cfab581113b3724f453df2f593ee385dae5e746a6649c65`
- Skill overlay SHA-256: `67f626d08e11b0e8b9b347a8746142889487e1229a1dc34e7b49ca498c9a191d`
- Judge schema SHA-256: `eaac8d5ec4179daca7a6c1c98e4847ae0114d9d33168a84593f70ca6474abe10`
- Eval definition SHA-256: `7e02d3842aadb84c2bf63d29c927cc522ebed52b96eed1878122982c38563924`
- Metadata SHA-256: `ddad21037c097d13ee42c91b495c2c2326e53dc9044ae9a3b160a51decc6ffbb`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feature_branch_created` | PASS | git_evidence shows branch changed from main to fix/notification-status, with a new reachable branch ref. |
| `meaningful_commit_created` | PASS | The new commit subject is `fix: support archived notification status`, which follows Conventional Commits. |
| `pr` | FAIL | PR creation was correctly blocked and a preview was provided, but it incorrectly states `PM/PRD: 未提供` even though docs/pm/notifications/PRD.md exists; the required PM document reference is missing. |
| `ci` | PASS | No PR was created; the output reports CI unavailable, explains the remote/gh blockers, and provides a `gh pr checks <pr-number> --watch` recovery command without claiming CI results. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5; fixture_sha256=415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e; output_sha256=281d70f06ea6b27502fbdd0f8641181b4b0e71dc1a0c07c2c640febb1063a040; snapshot_sha256=f0a9567b9f3ce3a4b5807827e70497510104912c63c94dd2369e71d511624ac8
- Behavior: Created a compliant feature branch and meaningful commit, passed tests, and accurately blocked PR/CI operations, but produced an incomplete and inaccurate PR preview by omitting the existing PM/PRD.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5; fixture_sha256=415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e; output_sha256=b113a55c2c44a825438bb7abddb0c60611107f54b987a22a2d9d612804b82634; snapshot_sha256=81d39d912af6a09f9968c5f2d1bbfffbee4780dc5e0180b61b4fc1364d31578e
- Behavior: Created a compliant feature branch and meaningful commit and reported the remote/Issue blocker, but did not provide the required PR preview or explicit CI handling.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The PR preview omits the existing PM/PRD reference and falsely says it was not provided.
- Next: Update the PR preview to reference docs/pm/notifications/PRD.md, then create the PR once a remote and gh are available.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
