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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8588a4fc6bb55ff6a1ce485f659334cabf6f9624098f4db4f1066bdacc1fc3ec`
- Skill overlay SHA-256: `09c184e9256c59e7718f2b61600ec30436b550d1692a7c65f8b8e6c64fc491f3`
- Judge schema SHA-256: `7dbaa3390632c779b209a0992154e3a2f393b139ccab7a74c59a949526e90023`
- Eval definition SHA-256: `15afea3ad3f743cdcf46b8c92f93ce64a903895054dc1b1a156e01c34538eba5`
- Metadata SHA-256: `2fa243367a1e388253aea518818683b603664720294e82f2ffeeeebe3d5f82e8`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `requires_exact_target_tree_blobs` | PASS | With_skill states that evidence must come from the resolved target_ref tree and treats staged, unstaged, and untracked changes as diagnostic only. |
| `blocks_every_in_scope_worktree_delta` | PASS | With_skill inventories staged routes, unstaged documentation and package.json, and the untracked audit draft, and concludes the inventory is blocked. |
| `performs_zero_audit_writes` | FAIL | Locked git evidence shows no writes, but with_skill explicitly says catalog-status may be marked verified despite the blocked branch. |
| `requires_clean_commit_update_ref_and_rerun` | PASS | With_skill requires submitting or removing all scoped changes, confirming a clean workspace, resolving the updated target_ref, and rerunning the complete pre-tag audit. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852; fixture_sha256=0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0; output_sha256=1a9652fe6ea10240a1cbf1e06ba6ce6844c5a58463874b678ac8e1dd1c144f86; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks the audit, uses target-tree evidence, inventories all scoped deltas, and specifies a full rerun, but incorrectly permits a page to be marked verified while blocked.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852; fixture_sha256=0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0; output_sha256=9a98646abd19e8822eac2bb109fa9664630cc939863e3139f7862aaa99b14900; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also blocks the audit and recommends committing changes and rerunning, but is comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- A blocked branch must not mark any page verified; with_skill says catalog-status can be verified.
- Next: Do not mark any page verified while the audit is blocked; defer all page verdicts until the clean, updated target_ref is fully re-audited.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
