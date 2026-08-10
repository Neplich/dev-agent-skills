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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5b5823d2c0804ce3dabb1d32490f71697f4ff111cd9371ebf92d1bb1b6ad2188`
- Skill overlay SHA-256: `c7033e85898ff61111eb14edc47b25e717119ee79349d7af461390afc706db78`
- Judge schema SHA-256: `6c436d29e1c4d967534d387d71455397c2a958eb0e9fdd8f24d404e3a4bfc7c7`
- Eval definition SHA-256: `65171d2c00ad7205a3b92eb523639da0ae1b9b851f9b225fb39f151ac8a09d1b`
- Metadata SHA-256: `393d49433e1e9b818095a60378e27c82e27a5159f0878e57881a2872b5feee91`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `marks_missing_doc_update_suspect` | PASS | The locked report states the required document was not updated and was reviewed as `suspect`, then separately records stale conclusions from fact review. |
| `confirms_outdated_claim_stale` | PASS | The locked report cites `QUERY locale required nonblank` and concludes the documented contract is `stale`. |
| `blocks_stale_release` | PASS | The locked report result is `blocked`, lists concrete documentation/version remediation and rerun steps, and explicitly does not express `ready_for_tag`. |
| `does_not_stamp_stale_set` | PASS | The locked report records pre-stamp `last_verified_version: v1.0.0`, says no unified stamp was applied, and Git evidence shows no index or worktree diff; `.meta/releases.json` is identified as missing rather than modified. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=75e91a3261160c51c3a3be9839180ee4b871400ebe4a923d8334f48729d4f530; snapshot_sha256=f169773f43f4658861b728992de760178abe642848485151752e65ef9619ccdd
- Behavior: Produced and saved a bounded pre-tag audit that distinguishes suspect detection from stale fact confirmation, blocks release, provides remediation, and performs no stamp or metadata mutation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=b61cb3306d0bc9e56b8812d0833826544583af0bf2d5875ace051f69643b66d5; snapshot_sha256=b0ab7361696f38ed2a2402b8dd41a3d12f6cec50f67ff973493a08b8e7a0a88b
- Behavior: Fresh baseline reported the missing locale and stale version metadata and saved a report, but used a generic FAIL framing without the with-skill protocol's explicit suspect/stale distinction and transaction safeguards.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
