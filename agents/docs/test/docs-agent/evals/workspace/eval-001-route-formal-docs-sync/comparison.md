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
- target_skill_sha256: `af94ca4b38768885230f6271f3d4ae9e1b1be30fcd2f5bdf1098250b4ded0306`
- eval_definition_sha256: `feba21121d4c3b05845e70bb42290b3e48f9ac62ef8bf5b095426802bc992c41`
- metadata_sha256: `320948f19ccb8c159c24fdc827ddc592aac02ee3f64236dd9e4896bae8e4979e`
- fixture_sha256: `5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `d9120b553be3673816559c0b102ba0210980dbae3daaf9eeba42b66ee4308ec2`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `423ca5e3f4ef1219a92f03bc262d7f2ca4bc9b68b5e71c112a143161c77467e6`
- Repository HEAD: `2f950c46c67111058957774f796ccf97ae616d36`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `cc06f7d0ec314789bbccd4de68e0c4e6f74c0821dbe36228153c86490ecf37d8`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_to_formal_docs_sync` | PASS | With-skill output explicitly identifies the request as formal documentation synchronization after feature delivery and routes it to `formal-docs-sync`; no competing route is selected. |
| `preserves_handoff_context` | PASS | With-skill output carries forward the confirmed search API scope, implementation diff and contract-test evidence, affected formal API page, API change-map, and exclusions without requiring field-by-field handoff repetition. |
| `points_to_authoritative_gate` | PASS | With-skill output names `formal-docs-sync` as the downstream specialist and does not expose local skill paths or reproduce the internal synchronization protocol. |
| `stops_at_router_boundary` | PASS | Locked git evidence shows no workspace changes, and the output limits this turn to routing/context handoff while requesting confirmation before synchronization proceeds. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=423ca5e3f4ef1219a92f03bc262d7f2ca4bc9b68b5e71c112a143161c77467e6; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=39bcc8ea03085d56e1942012764e069d47926a90401a5a4f8d49d5fbda53c5e2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the confirmed feature-delivery documentation request to `formal-docs-sync`, preserves the handoff scope and evidence, and stops before any write pending confirmation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=423ca5e3f4ef1219a92f03bc262d7f2ca4bc9b68b5e71c112a143161c77467e6; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=fc7a54ecc8b317edbfc2fe1a4188b01d33a1522d84d0a7ec900ca0dc8f68ec78; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a reasonable baseline synchronization plan and preserves the clean workspace, but does not explicitly route to the formal-docs-sync specialist.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Confirm continuation so the specialist can verify host-repository evidence and perform the synchronization workflow.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
