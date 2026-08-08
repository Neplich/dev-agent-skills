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
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
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
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_to_formal_docs_sync` | PASS | With_skill explicitly identifies the request as delivery after implementation and contract tests, selects `formal-docs-sync`, and excludes bootstrap, release notes, and audit routes. |
| `preserves_handoff_context` | PASS | With_skill preserves the feature path, source documents, implementation/test evidence, scope, formal API page and change-map outputs, exclusions, and blocker/risk guidance from `pm-handoff.md`. |
| `points_to_authoritative_gate` | PASS | With_skill explicitly names `formal-docs-sync` as the specialist and states that this router completes routing only, leaving evidence binding, scope confirmation, and synchronization to the specialist without exposing local skill paths or duplicating its protocol. |
| `stops_at_router_boundary` | PASS | The locked delivery snapshot is empty and git evidence shows unchanged HEAD, branch, worktree, index, and refs; with_skill explicitly states that no write is executed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=f1f23a9f59a30e65a6bb30aad0a327c7f7f62a579f7d1b0350cb9d228f039e58; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the confirmed Search API delivery handoff to `formal-docs-sync`, preserves the relevant context, and stops before documentation writes.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=8ec6d28e069e79094f8e11927c203cf22e62cef490d3d97a78f2be8b183df5ab; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a broadly correct but less structured routing response, with less explicit specialist gating and context detail.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Skill overlay SHA-256: `44e860f93f5d468075d88a048afe986ad68fcbae84270ffdc4d5a090573d59b8`
- Judge schema SHA-256: `d9120b553be3673816559c0b102ba0210980dbae3daaf9eeba42b66ee4308ec2`
- Eval definition SHA-256: `4f62b001057b225d1029a6284046afacf46248ad92aa43b0c065e0a0456b7450`
- Metadata SHA-256: `320948f19ccb8c159c24fdc827ddc592aac02ee3f64236dd9e4896bae8e4979e`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_to_formal_docs_sync` | PASS | With_skill explicitly identifies the request as post-delivery formal documentation synchronization and selects `formal-docs-sync`, without routing to bootstrap, release notes, or audit. |
| `preserves_handoff_context` | PASS | With_skill carries the search API path, confirmed source documents and evidence, API page and change-map outputs, excluded database/ops/release scope, and preservation risk. |
| `points_to_authoritative_gate` | PASS | With_skill names `formal-docs-sync` as the next specialist and states the execution boundary is routing; it does not expose a local skill path or reproduce the synchronization protocol. |
| `stops_at_router_boundary` | PASS | Locked git evidence shows unchanged HEAD, branch, status, diffs, and no delivery snapshots or declared outputs; the candidate states routing only. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=1981fbaaadcae29101b28b7ef2ed7a20bb256cc8d13bd02dc4a0243ed368b349; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the PM handoff to formal-docs-sync, preserves the relevant context, and stops before documentation writes.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=60cc87348dd373c427ab65cf8636f34131823676f4412f27348580bad83e832e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a fresh baseline that routes generically to delivery and lacks the authoritative specialist routing.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Skill overlay SHA-256: `44e860f93f5d468075d88a048afe986ad68fcbae84270ffdc4d5a090573d59b8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4f62b001057b225d1029a6284046afacf46248ad92aa43b0c065e0a0456b7450`
- Metadata SHA-256: `320948f19ccb8c159c24fdc827ddc592aac02ee3f64236dd9e4896bae8e4979e`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_to_formal_docs_sync` | PASS | with_skill explicitly selects formal-docs-sync and cites the completed implementation diff and passing API contract tests. |
| `preserves_handoff_context` | FAIL | Most handoff context is preserved, but the explicit feature_path_evidence reason and downstream_owner field from pm-handoff.md are omitted. |
| `points_to_authoritative_gate` | PASS | It identifies formal-docs-sync as the specialist, states the execution boundary, and does not expose local skill paths or reproduce the specialist protocol. |
| `stops_at_router_boundary` | PASS | The with_skill git evidence shows no changes, and the output explicitly limits this turn to routing without documentation writes, publishing, or deployment. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=22e9e00512b2c943d353f17eb15c6b3497a8b6656d61a3eed73a7c37a2d4e3fa; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes to formal-docs-sync, preserves most handoff context, and stops without repository mutation, but omits two explicit handoff fields.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=af6ae87ecf62985041cd4505bacd4bdb16fa9783831d9c331bf1a8ef65a22c44; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline misroutes the request to the delivery capability and omits the formal-docs-sync specialist boundary.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- preserves_handoff_context fails because the with_skill output omits the explicit feature_path_evidence reason and downstream_owner field from pm-handoff.md.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Target skill tree SHA-256: `e64e4dc492a2ff92be09822529f9abb1fbd17f4d0148b3045e0162382c5d46d3`
- Skill overlay SHA-256: `e55ecf59b3cd8d90a2ed4cf555bed2ad2fc2131494e0914246a868317b68f4e8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4f62b001057b225d1029a6284046afacf46248ad92aa43b0c065e0a0456b7450`
- Metadata SHA-256: `320948f19ccb8c159c24fdc827ddc592aac02ee3f64236dd9e4896bae8e4979e`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_to_formal_docs_sync` | PASS | With_skill explicitly routes the handoff to `formal-docs-sync` and identifies Feature delivery context; no bootstrap, release-notes, or audit routing is used as the primary owner. |
| `preserves_handoff_context` | FAIL | It preserves the main feature, source-document status, evidence, outputs, exclusions, and risk, but omits confirmed handoff fields including `change_tier: standard`, `parent_feature: search`, and `feature_level: 2`. |
| `points_to_authoritative_gate` | PASS | It clearly names `formal-docs-sync` as the downstream specialist and does not reproduce the synchronization protocol or change-map write details. The extra local SKILL.md link is unnecessary but not prohibited by the assertion. |
| `stops_at_router_boundary` | PASS | Raw git evidence shows unchanged HEAD, branch, status, diffs, and no declared or delivery outputs; the candidate reports routing/context handoff rather than performing documentation writes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=afc598644e20396a9bbcb1f3d26b9ec39ae0c9269054a1335b4a755bf03f0c55; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Routes to `formal-docs-sync`, preserves the principal handoff details, but omits several confirmed metadata fields; no repository mutation is evidenced.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=3a41ddfbfaa16c02e944c87e7ce29817166d953db296e4b56f65e6b6dc4e559a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline routes to a generic `delivery` API-docs capability, while retaining much of the handoff context and making no repository changes.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output does not preserve all confirmed handoff fields required by the lossless-context assertion.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e64e4dc492a2ff92be09822529f9abb1fbd17f4d0148b3045e0162382c5d46d3`
- Skill overlay SHA-256: `f896903fa1a8ae6886eb0b6365065625a2e60f6809acd0af6c7c8dc8f8f2bd40`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4f62b001057b225d1029a6284046afacf46248ad92aa43b0c065e0a0456b7450`
- Metadata SHA-256: `320948f19ccb8c159c24fdc827ddc592aac02ee3f64236dd9e4896bae8e4979e`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_to_formal_docs_sync` | PASS | with_skill 明确将请求交给 `formal-docs-sync`，符合正式文档同步路由；未误派其他能力。 |
| `preserves_handoff_context` | PASS | 保留了 feature path、变更级别、PRD/TRD/实施计划及实现和合同测试证据、同步产出、排除范围和风险信息。 |
| `points_to_authoritative_gate` | PASS | 明确由 `formal-docs-sync` 接管并停在路由阶段，未复制同步协议或 change-map 写入细节。 |
| `stops_at_router_boundary` | PASS | 输出明确表示尚未执行文档写入；raw git evidence 显示工作区、分支和提交均未变化。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=79cf8a7d014da2971f775810796a53c85cef6003fd3199bc5b8a57afc18126ae; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确路由至 `formal-docs-sync`，保留关键交接上下文，并停在无文件写入的路由边界。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=70954cdab092931c59e6f7940ace8a15c9a4eb6d9df983d9fcb7cfa5475b78cd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 基本保留交接内容并未写入文件，但将正式文档同步误路由为 `delivery`。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9b5483c75770358083301bcb4f3e774af3a6e851f51536b52de7b7f0a1bd16fd`
- Skill overlay SHA-256: `0c6a49eed1db242a95632eb0d142c1760f60ffc995c96026908ec8c0e6bd8d63`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `b427d27a75859a314db7ebafb8d73a16d8b21552e3c670e89632076d71f7b750`
- Metadata SHA-256: `320948f19ccb8c159c24fdc827ddc592aac02ee3f64236dd9e4896bae8e4979e`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_to_formal_docs_sync` | PASS | With-skill output routes to `docs-agent:formal-docs-sync` for the confirmed delivery handoff and formal API/change-map synchronization. |
| `preserves_handoff_context` | FAIL | It preserves most handoff fields, but omits `feature_level: 2` and the `feature_path_evidence` source/reason detail, so the context is not lossless. |
| `points_to_authoritative_gate` | FAIL | It names the `formal-docs-sync` capability but does not identify `formal-docs-sync/SKILL.md` and its internal instructions as the authoritative contract. |
| `stops_at_router_boundary` | PASS | The output describes routing and handoff only; git evidence shows no changes, no delivery snapshot, and no writes to documentation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=0757d9d4a75c01e247a3da6ec20f26090c28821372ed5cc94defda1e3b72910f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Routes to `docs-agent:formal-docs-sync`, carries most confirmed context, and remains read-only, but omits some handoff fields and the explicit authoritative SKILL.md reference.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=ec013d013a94dd2d0ffd4c73ec57fb1cfc914b4fb7593703b8a0eb226cdc78ed; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline routes generically to `delivery` and omits the specialist contract reference; it otherwise preserves much of the handoff context and makes no changes.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill output does not preserve every supplied handoff field.
- The with-skill output does not explicitly point to `formal-docs-sync/SKILL.md` and its internal instructions.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9fbb92b16f91777ce613be24ad3cd630730cfccd4cce1cf1d33c3b6c917671d6`
- Skill overlay SHA-256: `52a3ba7ee2d9485acf003417b40e0d0ca2ab263cbadde98fac58250b6c2a9778`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `b427d27a75859a314db7ebafb8d73a16d8b21552e3c670e89632076d71f7b750`
- Metadata SHA-256: `320948f19ccb8c159c24fdc827ddc592aac02ee3f64236dd9e4896bae8e4979e`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_to_formal_docs_sync` | PASS | With-skill output selects `formal-docs-sync` for the confirmed delivery handoff and does not route to bootstrap, release notes, or audit. |
| `preserves_handoff_context` | FAIL | It preserves most core context, but omits fixture fields including `feature`, `parent_feature`, `feature_level`, and the explicit feature-path evidence reason. |
| `points_to_authoritative_gate` | FAIL | It names `formal-docs-sync` but does not explicitly point to `formal-docs-sync/SKILL.md` or its internal instructions as the authoritative contract. |
| `stops_at_router_boundary` | PASS | The output states the routing stage does not modify formal documents, and raw git evidence shows no changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=8070ecf97bc66a95e8b08bfdbda48dac77d552a91243b44c32195656a0ae9cb2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly selects `formal-docs-sync` and stops at the routing boundary, but incompletely preserves all handoff fields and does not cite the specialist SKILL.md contract.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=bbeac4491430ff2e607febe72ab7ce9154d4dc3a06e63d0d83b599de26cbcfab; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Routes generally toward delivery/API documentation and preserves much handoff context, but does not identify the required `formal-docs-sync` capability.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill output omits several confirmed handoff fields.
- The with-skill output does not explicitly identify `formal-docs-sync/SKILL.md` and its internal instructions as the authoritative execution contract.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9fbb92b16f91777ce613be24ad3cd630730cfccd4cce1cf1d33c3b6c917671d6`
- Skill overlay SHA-256: `52a3ba7ee2d9485acf003417b40e0d0ca2ab263cbadde98fac58250b6c2a9778`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `b427d27a75859a314db7ebafb8d73a16d8b21552e3c670e89632076d71f7b750`
- Metadata SHA-256: `320948f19ccb8c159c24fdc827ddc592aac02ee3f64236dd9e4896bae8e4979e`
- Executor SHA-256: `c5ece8c6632badb84ff79ee67e4bea96a1d1db7e8afd66de87486af43e8fdd16`
- Runtime SHA-256: `5c4532cfa9ada91c16b3ae2d69922296ddc7c2c1c61841e01bc9c804be1b85fe`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_to_formal_docs_sync` | PASS | with_skill 明确选择 `formal-docs-sync`，并标注为 Feature delivery；未误派 bootstrap、release notes 或 audit。 |
| `preserves_handoff_context` | FAIL | 虽保留了功能、主要依据、同步范围、排除范围和风险，但遗漏了交接中的具体来源路径与状态、parent feature/level、feature-path 证据理由、downstream owner 及实现 diff/测试证据可供核验等字段，未达到无损保留。 |
| `points_to_authoritative_gate` | FAIL | 输出只说由 `formal-docs-sync` 处理，没有明确指向 `formal-docs-sync/SKILL.md` 或其内部指令作为权威执行合同。 |
| `stops_at_router_boundary` | PASS | 明确说明仅完成能力交接与范围确认，尚未执行文档写入；候选输出也没有修改 `docs/site/` 的证据。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确完成 formal-docs-sync 路由并停在路由边界，但上下文保留不完整，且未指向 specialist 的权威 SKILL.md 合同。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 新鲜基线错误路由至 `delivery`，但大部分交接字段和未写入边界得到保留。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未无损保留 pm-handoff.md 的全部已提供交接字段。
- 未明确指向 formal-docs-sync/SKILL.md 及其内部指令作为权威执行合同。
- Next: 补充完整的 handoff 字段与具体来源证据。
- Next: 明确将 formal-docs-sync/SKILL.md 及其内部指令作为后续执行权威。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-001-route-formal-docs-sync`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- 评估基线：`a273a00` 加本轮 cross-doc sync R2 working tree
- Harness：完整 `agents/docs/` 与 PM 共享契约；without-skill 零 skill/README；独立 fresh judge

## Latest Result

- Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `routes_formal_docs_sync` | PASS | PASS | 两条 `result.txt` 均选择 `docs-agent:formal-docs-sync`，并明确排除 database、ops、Release；with_skill 第 3–8 行，without_skill 第 3–4 行。 |
| `accepts_complete_handoff` | FAIL | FAIL | with_skill 仅说明依据为 `pm-handoff.md` 及路径，未保留全部 packet 字段；without_skill 未说明接受完整 handoff，且只报告更新了阻塞项。完整字段虽存在于各自 `pm-handoff.md`，但未在路由产物中完整体现。 |
| `references_specialist_gate_only` | FAIL | FAIL | 两条产物均未指向 `formal-docs-sync/SKILL.md` 及其内部指令；仅称专家流程不可用。 |
| `recognizes_shared_consumption_contract` | FAIL | FAIL | 两条产物均未提及 `agents/product_manager/skills/idea-to-spec/_internal/_shared/consumption-contract.md`，也未给出该权威指针。 |

未满足断言（with/without 任一 FAIL）：``accepts_complete_handoff``、``references_specialist_gate_only``、``recognizes_shared_consumption_contract``



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `routes_formal_docs_sync`：PASS。识别实现后正式文档同步，排除 bootstrap 与 audit。
- `accepts_complete_handoff`：PASS。保留 request_type、change_tier、全部 feature scope、source/scope/output/risk 字段。
- `references_specialist_gate_only`：PASS。只指向 `formal-docs-sync/SKILL.md` 及内部指令，不复制执行协议。
- `recognizes_shared_consumption_contract`：PASS。仅保留 PM 共享 `consumption-contract.md` 的权威指针。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：同一 prompt 与 fixture 全新生成，不含 skill/README，未复用历史 baseline。
- baseline 路由方向正确，但未逐字段保留 packet，也缺少 consumption contract 权威指针。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 无 assertion failure；router pristine/with_skill 仅新增 candidate output，没有 specialist 执行产物。

## Next Steps

- 后续 router eval 继续使用完整 harness 与独立 judge。

## Runtime Artifact Policy

- 运行期产物仅保留在 `tmp/eval-runs/116/`，不提交到 git。
