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
- Fixture SHA-256: `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583`
- Prompt SHA-256: `a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4`
- Repository HEAD: `fecf485e8e3dcaf191b2b221d9cccbddfdea0b72`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5b11b38c1c44c386fe19122dfb1ce5918b2bfbc4830ad32aa994d8a7e39f35e7`
- Skill overlay SHA-256: `85c4ae0a1d58505c4a23c34e6f9116aed81a09b4b6270e3ce148424084f6c7e0`
- Judge schema SHA-256: `6c436d29e1c4d967534d387d71455397c2a958eb0e9fdd8f24d404e3a4bfc7c7`
- Eval definition SHA-256: `65171d2c00ad7205a3b92eb523639da0ae1b9b851f9b225fb39f151ac8a09d1b`
- Metadata SHA-256: `393d49433e1e9b818095a60378e27c82e27a5159f0878e57881a2872b5feee91`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
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
