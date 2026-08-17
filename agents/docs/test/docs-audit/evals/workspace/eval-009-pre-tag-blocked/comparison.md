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
- Identity schema: `2`
- target_skill_sha256: `a5e0bb043d61dbbb218e7d7efc08374e0d16a4d7aaa3b31817f2038830c90941`
- eval_definition_sha256: `d573477cbe6d660b40a0fd1ef0416d1d407e28ca525b29d8ef8303b282fe7f56`
- metadata_sha256: `2fa243367a1e388253aea518818683b603664720294e82f2ffeeeebe3d5f82e8`
- fixture_sha256: `0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `7dbaa3390632c779b209a0992154e3a2f393b139ccab7a74c59a949526e90023`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `d7e2242fcdf83209e6c0cb5ec9544aa009e79488a72f81ebd4bf387289fbabec`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `requires_exact_target_tree_blobs` | PASS | With-skill output explicitly anchors the conclusion to `release-head` commit `4d7edbe...`, states the target tree still has the legacy implementation and version `1.1.0`, and treats workspace/index changes only as diagnostic evidence. |
| `blocks_every_in_scope_worktree_delta` | PASS | The output identifies staged `src/catalog/routes.txt`, unstaged `docs/site/api/catalog-items.md`, unstaged `package.json`, and untracked `docs/site/.meta/audit/audit-v1.2.0.md`, and concludes the pre-tag audit is `blocked`. Raw fixture status confirms those exact paths and states. |
| `performs_zero_audit_writes` | PASS | Locked git evidence shows unchanged HEAD, branch, refs, commits, and diffs; the output returns `blocked`, explicitly prohibits `ready_for_tag`, and recommends only read-only diagnosis and cleanup/re-audit steps. |
| `requires_clean_commit_update_ref_and_rerun` | PASS | The output requires submitting or moving all listed differences, updating `release-head`, confirming clean index/worktree state, and performing a complete pre-tag rerun with explicit refs and rebinding from the inputs. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852; fixture_sha256=0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0; output_sha256=20282c09caa30ca477b43f86392fa43cede6d7f1bee4cae8c09c494798fe4982; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly returns a blocked pre-tag audit, binds conclusions to the immutable target tree, inventories every in-scope delta, performs no writes, and specifies full cleanup, ref update, and rerun requirements.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=542a6dbc4e91378f219fb9c7b639cb7670be62733499a20407d8c4586f25b852; fixture_sha256=0c59dd74f98f557b12899cbca54adf5aa4fe8aa94d37037f8495e06f83e726c0; output_sha256=4adad2e66b572d2f605e4de8e07cd0131333531ad722572f5aed4885c715ff91; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Also reaches the correct blocked conclusion and gives target-tree evidence and rerun guidance, but provides a less complete per-path disposition and protocol-specific restart detail than the with_skill lane.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
