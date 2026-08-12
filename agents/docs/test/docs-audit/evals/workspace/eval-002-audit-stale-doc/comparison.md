# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-002-audit-stale-doc`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583` from `agents/docs/test/docs-audit/evals/workspace/eval-002-audit-stale-doc`.
- Identity schema: `2`
- target_skill_sha256: `5b11b38c1c44c386fe19122dfb1ce5918b2bfbc4830ad32aa994d8a7e39f35e7`
- eval_definition_sha256: `65171d2c00ad7205a3b92eb523639da0ae1b9b851f9b225fb39f151ac8a09d1b`
- metadata_sha256: `393d49433e1e9b818095a60378e27c82e27a5159f0878e57881a2872b5feee91`
- fixture_sha256: `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6c436d29e1c4d967534d387d71455397c2a958eb0e9fdd8f24d404e3a4bfc7c7`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `fecf485e8e3dcaf191b2b221d9cccbddfdea0b72`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `marks_missing_doc_update_suspect` | NOT_EXERCISED | NOT_EXERCISED: locked report and trace prove the final stale finding, but do not prove the deterministic layer’s intermediate suspect classification or handoff. |
| `confirms_outdated_claim_stale` | PASS | PASS: the locked delivery snapshot cites the target code’s required nonblank locale and 400 invalid_locale behavior, and concludes the documentation is stale. |
| `blocks_stale_release` | PASS | PASS: the locked report lists stale evidence and concrete remediation, concludes blocked, and contains no ready_for_tag result. |
| `does_not_stamp_stale_set` | PASS | PASS: the locked report preserves last_verified_version as v1.0.0, states no stamp or metadata was written, and raw Git evidence shows no formal-document or metadata diff. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=af46c68dcff92f82be2569c90cc811516b5a8ffde4a3a332e577af6303a306b0; snapshot_sha256=75281e0e277c2886b50b76891d84e1878a8f62632856d87eb5bf3b31a1d0205f
- Behavior: Produced a saved audit report concluding stale and blocked, with concrete remediation and no release stamp.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=3220702fb870e54adfbb00bb31e0951993f95eed6f3ae56fa5d3ba3ef4205f55; snapshot_sha256=50d98dc069a9a03b3761fec60329e09a5ad4e70cee8d2895484de4f5e04d2858
- Behavior: Fresh baseline also identified the missing locale contract and recommended blocking release, but did not provide the with_skill report’s explicit stale/blocked audit structure.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
