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
- Repository HEAD: `fecf485e8e3dcaf191b2b221d9cccbddfdea0b72`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5b11b38c1c44c386fe19122dfb1ce5918b2bfbc4830ad32aa994d8a7e39f35e7`
- Skill overlay SHA-256: `85c4ae0a1d58505c4a23c34e6f9116aed81a09b4b6270e3ce148424084f6c7e0`
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
| `requires_exact_target_tree_blobs` | PASS | With-skill output explicitly restricts passing evidence to the `release-head` tree and treats staged, unstaged, untracked, and evidence-file content as diagnostic only; raw evidence confirms the target tree retains the legacy dispatcher and version 1.1.0. |
| `blocks_every_in_scope_worktree_delta` | PASS | With-skill output identifies all four inventory entries—staged routes, unstaged API page, untracked audit draft, and modified package.json—and states they block the pre-tag audit. The locked porcelain inventory confirms each entry. |
| `performs_zero_audit_writes` | PASS | With-skill output states no audit records were written. Locked git evidence shows unchanged HEAD and branch, no ref delta, no new commits, no result diffs, and an empty delivery snapshot. |
| `requires_clean_commit_update_ref_and_rerun` | PASS | With-skill output requires committing or removing all scoped differences, updating `target_ref`, confirming a clean index/worktree, and rerunning the complete audit from immutable inputs; it explicitly disallows partial continuation and `ready_for_tag`. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852; fixture_sha256=0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0; output_sha256=e0e1e9f2e555b65bf7d7cf772d5bc37b58feeb7ad45d73381fe1e7f7a97a588a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks the audit, distinguishes exact target-tree evidence from workspace diagnostics, identifies every scoped delta, performs no audit writes, and specifies a complete clean-commit/ref-update rerun.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852; fixture_sha256=0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0; output_sha256=4fb1f831fb69f17e6202dee6d61f8c30e600236db9a496927121291a48d1934a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also reaches the correct blocked conclusion and rerun guidance, but provides less systematic scope classification and process detail.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
