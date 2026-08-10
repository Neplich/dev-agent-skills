# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-009-pre-tag-blocked`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0` from `agents/docs/test/docs-audit/evals/workspace/eval-009-pre-tag-blocked`.
- Fixture SHA-256: `0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0`
- Prompt SHA-256: `542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5b5823d2c0804ce3dabb1d32490f71697f4ff111cd9371ebf92d1bb1b6ad2188`
- Skill overlay SHA-256: `c7033e85898ff61111eb14edc47b25e717119ee79349d7af461390afc706db78`
- Judge schema SHA-256: `7dbaa3390632c779b209a0992154e3a2f393b139ccab7a74c59a949526e90023`
- Eval definition SHA-256: `d573477cbe6d660b40a0fd1ef0416d1d407e28ca525b29d8ef8303b282fe7f56`
- Metadata SHA-256: `2fa243367a1e388253aea518818683b603664720294e82f2ffeeeebe3d5f82e8`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `requires_exact_target_tree_blobs` | PASS | With-skill output explicitly binds evidence to release-head's immutable commit/tree and rejects worktree, index, untracked, and patch-only evidence. |
| `blocks_every_in_scope_worktree_delta` | PASS | With-skill output identifies all four scoped deltas—staged routes, unstaged API page, untracked audit draft, and modified package.json—and concludes blocked. |
| `performs_zero_audit_writes` | PASS | Locked git evidence shows unchanged HEAD/branch, no ref delta, no new commits, and no result diffs; output does not return ready_for_tag. |
| `requires_clean_commit_update_ref_and_rerun` | PASS | With-skill output requires committing or moving all scoped changes, updating target_ref, proving a clean index/worktree, and rerunning the complete audit from input parsing. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852; fixture_sha256=0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0; output_sha256=ab98526ed6ecf4e5ea105a43ee1a093a91e3d5c5abbe6187dc2c29305cd47485; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks the audit, uses exact target-tree evidence, preserves state, and specifies a full clean-commit/ref-update rerun.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852; fixture_sha256=0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0; output_sha256=ed6ce5f0d7b223f8fce6921c47ac96df77c945778a77f5b39910d909fa313d6a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also reaches the correct blocked conclusion and broadly identifies the same deltas, but provides less complete audit-protocol detail.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
