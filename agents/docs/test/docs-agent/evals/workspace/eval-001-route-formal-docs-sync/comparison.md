# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-001-route-formal-docs-sync`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991` from `agents/docs/test/docs-agent/evals/workspace/eval-001-route-formal-docs-sync`.
- Fixture SHA-256: `5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991`
- Prompt SHA-256: `898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b04f0f833fdfe60f19dba4258110d7f6b0a3d6a6f2afb7034b0d3d883c30f83b`
- Skill overlay SHA-256: `73e88fe8c07f988c3353f81f9b058d4f8350c48ee381f924fe8c8201b9f92bb4`
- Judge schema SHA-256: `d9120b553be3673816559c0b102ba0210980dbae3daaf9eeba42b66ee4308ec2`
- Eval definition SHA-256: `4f62b001057b225d1029a6284046afacf46248ad92aa43b0c065e0a0456b7450`
- Metadata SHA-256: `320948f19ccb8c159c24fdc827ddc592aac02ee3f64236dd9e4896bae8e4979e`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_to_formal_docs_sync` | PASS | The with_skill output selects `formal-docs-sync` for the delivery request and explicitly distinguishes the formal API page and API change-map from out-of-scope database, ops, and release documentation. |
| `preserves_handoff_context` | PASS | The with_skill output carries the feature path, source documents and statuses, implemented-current-state scope, required outputs, evidence sources, exclusions, and map-entry preservation requirement from `pm-handoff.md`. |
| `points_to_authoritative_gate` | PASS | It identifies `formal-docs-sync` as the next capability and cites its authoritative entry gate/checkpoint, while stopping before synchronization execution and without exposing local skill paths or reproducing the protocol. |
| `stops_at_router_boundary` | PASS | The locked with_skill git evidence shows unchanged HEAD, branch, status, index, worktree, and no delivery snapshot; the output explicitly says no documents or change-map are written. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=317ca46f2946cafcdf0ad4fa2f28e131c67db1e21c9e3aaa8e03e05791a9eb6a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the handoff to `formal-docs-sync`, preserves the confirmed delivery context, identifies the authoritative continuation gate, and stops before any write.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=3edec35f229710ecd780307474bbc3dd7f7962a9ecc0c887332b4949329cb425; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a broadly relevant delivery-docs route and preserves much of the scope, but does not name the authoritative `formal-docs-sync` specialist or clearly establish the router boundary.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
