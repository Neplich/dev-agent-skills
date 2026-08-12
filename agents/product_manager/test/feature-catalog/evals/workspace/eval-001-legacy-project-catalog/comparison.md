# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-001-legacy-project-catalog`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554` from `agents/product_manager/test/feature-catalog/evals/workspace/eval-001-legacy-project-catalog`.
- Identity schema: `2`
- target_skill_sha256: `272c84e241c5d52534922fccf2bc6732492a0d70c9f6e2ab8dc1eff2533f7b0c`
- eval_definition_sha256: `6316196cbc0024d8a369162c20842d191078adb23f3f59cfbc5541923081da5e`
- metadata_sha256: `aa9b419ec00ff2ce5f9c2775fc1e620cf1eb45a8d316e5adf573b14f5b74c3e2`
- fixture_sha256: `fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6731c51ff9f69981e5ade0a40fa5fb4f93b6c439e428212a1b46155c6fa123f1`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `draft_before_formal_docs` | NOT_EXERCISED | The with_skill lane stopped at the required workspace-scope confirmation before producing a catalog; no formal PM files were delivered. |
| `evidence_and_confidence` | NOT_EXERCISED | No feature entries were produced because the candidate paused for scope confirmation. |
| `business_capability_naming` | NOT_EXERCISED | No candidate feature names were produced because the candidate paused for scope confirmation. |
| `open_questions_present` | NOT_EXERCISED | No feature entries or uncertainty questions beyond workspace scope were produced. |
| `confirmation_gate` | NOT_EXERCISED | The candidate correctly requested workspace scope first; feature_path confirmation could not yet occur without the maintainer’s response. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2; fixture_sha256=fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554; output_sha256=1166c9d4ee73d08a60244d70b30f3792f70cd9aad1ff65179e4b0d987ce1569e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly paused at the workspace-scope checkpoint and made no file changes.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2; fixture_sha256=fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554; output_sha256=cf4a98f95b5620135beeb59eb35319e0400e5074f028ddfd4865af47d8f5a918; snapshot_sha256=b5f4ae0803ccf6d328a4f6920b04106201b8479390439e2300b2a4a4da2a12a0
- Behavior: Produced a detailed catalog file without the required pending-confirmation and feature_path confirmation gate.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain maintainer confirmation of the workspace scope, then produce the pending feature catalog draft with evidence, confidence, open questions, and a feature_path confirmation gate.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
