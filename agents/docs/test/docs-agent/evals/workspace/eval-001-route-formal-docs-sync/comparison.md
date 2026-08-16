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
- Identity schema: `2`
- target_skill_sha256: `023cc6d8aa109db6ff7dcd662df567ae4f0c79dddb66dfe7bcf6f1eb91d20f39`
- eval_definition_sha256: `b7962cc5c7265d8b3c4f799e1e809f203d9b09d09c3950072c84712c7db0c562`
- metadata_sha256: `320948f19ccb8c159c24fdc827ddc592aac02ee3f64236dd9e4896bae8e4979e`
- fixture_sha256: `5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `d9120b553be3673816559c0b102ba0210980dbae3daaf9eeba42b66ee4308ec2`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `e48b238fe72b5801d36c88005426156c8c6d404e006c5bccb655f20f86d8f497`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84e19c3e634cfde176d2ff20ba8e9d25a4838db3ed1deb5def94a8d0f1d2ddd9`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_to_formal_docs_sync` | PASS | With-skill output explicitly routes the confirmed delivery handoff to `formal-docs-sync` and excludes bootstrap, database, ops, and Release documentation routes. |
| `preserves_handoff_context` | PASS | With-skill output preserves the `search/api-query` scope, required formal API page and change-map outputs, source evidence, exclusions, and blocker state without requiring field-by-field repetition. |
| `points_to_authoritative_gate` | PASS | With-skill output names `formal-docs-sync` as the next executor, keeps this turn read-only, exposes no local skill path, and does not reproduce the detailed sync protocol or map-writing procedure. |
| `stops_at_router_boundary` | PASS | With-skill delivery snapshot and git evidence show no workspace, index, branch, or commit changes; the output states that only routing was completed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e48b238fe72b5801d36c88005426156c8c6d404e006c5bccb655f20f86d8f497; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=55695fa552c436a65bfadcbe7844fa5dda52ad326af414c1e44aa754224fb147; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the confirmed handoff to formal-docs-sync, preserves the relevant context, and stops before documentation writes.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e48b238fe72b5801d36c88005426156c8c6d404e006c5bccb655f20f86d8f497; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=b54413de56d69f915de900a503cdbf12e3f204c781147be67caa5a0abfd8dd09; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline preserved much of the handoff scope but did not identify or route to formal-docs-sync, instead stopping on unavailable referenced artifacts.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
