# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-004-audit-all-verified`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897` from `agents/docs/test/docs-audit/evals/workspace/eval-004-audit-all-verified`.
- Fixture SHA-256: `085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897`
- Prompt SHA-256: `f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8588a4fc6bb55ff6a1ce485f659334cabf6f9624098f4db4f1066bdacc1fc3ec`
- Skill overlay SHA-256: `09c184e9256c59e7718f2b61600ec30436b550d1692a7c65f8b8e6c64fc491f3`
- Judge schema SHA-256: `a043187f1d82deb6ceb1f6f2a8dbb12db6dd01c71ced16d224de3ae50ca31c3b`
- Eval definition SHA-256: `9d29cd503dc3f38e1235bc8d674c667f9fc3bef38d94569b7888bb0dfed80506`
- Metadata SHA-256: `4c1ab6c77122f43adf1cbc9d6f05aea7b2b047fe1e69ba225e32d03f006dc954`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `verifies_complete_affected_set` | PASS | With-skill candidate records all four affected pages as verified with no unresolved evidence gap; final stamped page snapshots are present. |
| `stamps_all_pages_together` | PASS | Final snapshots show all four required surfaces at v1.1.0, and the candidate records a unified stamp set with successful read-back. |
| `verifies_release_metadata_read_only` | PASS | Release metadata remains unchanged in the final manifest and is explicitly audited as read-only. |
| `normalizes_mixed_version_forms` | PASS | The candidate inventory records prefixed and unprefixed sources, their raw forms, normalized SemVer values, and matching comparison results. |
| `persists_candidate_producer_schema` | PASS | The reachable candidate record contains the required schema, evidence, inventories, digests, staged gates, read-back commands, and candidate_verified conclusion without ready_for_tag or post-commit fields. |
| `anchors_candidate_then_discovers_success` | PASS | Locked git evidence shows candidate, anchor, handoff, and fast-forward commits; the final handoff snapshot contains ready_for_tag discovery metadata and final confirmation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=9ea839124b6074d747cba3957e5de386641ed4bae73f3f6693c75d987cb7b704; snapshot_sha256=acf4e1a516b0333f8cd4cdae012b72808d7ac7311a7beef62c17d3621bcfd788
- Behavior: Completed the documentation audit, persisted the candidate and handoff records, stamped the required pages, and returned ready_for_tag without creating a tag.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f182723403634fcd32c050786ed55f612a9685f404b0e23235cff29b52f7174c; fixture_sha256=085a9df9c5171410b3af490aa0eb671dd955de6207e401089976f50095ed2897; output_sha256=55b450d620370fbd825c4c3c1e56fecd8215255d744b6e756266089d6ecdbb5a; snapshot_sha256=9247dc286f355dc7e7351dbe582724d218bb7d11dbfe5340c27e67ed6c0ea897
- Behavior: Produced a standalone audit report identifying the metadata inconsistency, but did not stamp pages or create the required audit/handoff records.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
