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
- target_skill_sha256: `cf92649952a97be677cf5e900a4d9c793a6c0724813cf1fa3154f57e7d2c08f3`
- eval_definition_sha256: `4f62b001057b225d1029a6284046afacf46248ad92aa43b0c065e0a0456b7450`
- metadata_sha256: `320948f19ccb8c159c24fdc827ddc592aac02ee3f64236dd9e4896bae8e4979e`
- fixture_sha256: `5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `d9120b553be3673816559c0b102ba0210980dbae3daaf9eeba42b66ee4308ec2`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `f2aa9b2c49be68550ec45538c221425607f428ce`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_to_formal_docs_sync` | PASS | With-skill output selects `formal-docs-sync`; raw handoff prompt preserves the confirmed delivery context and excludes bootstrap, release notes, and audit. |
| `preserves_handoff_context` | PASS | The locked specialist handoff carries the feature path, source documents and statuses, scope, required API page/change-map outputs, exclusions, and risk constraints from `pm-handoff.md`. |
| `points_to_authoritative_gate` | PASS | Output names `formal-docs-sync` as the authoritative execution gate and does not expose a local path or duplicate its protocol. |
| `stops_at_router_boundary` | PASS | Output explicitly stops at handoff; locked git evidence shows no changes, no snapshots, and no writes to documentation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=0ddac8387ee29d37ff2727a18ce021a3a96d2c6de5108718effbd220cb21e3b3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the confirmed feature-delivery handoff to `formal-docs-sync`, preserves context, and stops before specialist execution.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=4d52548d54375dba3a1082e163eaf0ee50c3287e6cbf136728880b22687e1275; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a generic delivery/documentation dispatch and claims execution is underway without selecting the authoritative `formal-docs-sync` route or clearly stopping at the router boundary.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
