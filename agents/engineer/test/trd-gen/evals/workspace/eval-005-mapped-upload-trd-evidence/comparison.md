# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-005-mapped-upload-trd-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b9272be266caff6ac38d8060f5dbdbc6e981647729fe1530cfc53ca05b58b007` from `agents/engineer/test/trd-gen/evals/workspace/eval-005-mapped-upload-trd-evidence`.
- Identity schema: `2`
- target_skill_sha256: `47bb3c8e8bad899368b78c2d70a8b75f85c0900f5ef5546caa9c9be9e034ebd2`
- eval_definition_sha256: `ed02404d14ffd40d542c29f44a74caf2fc5696740b01f75b11e50dfad6379f60`
- metadata_sha256: `c635fd02477c894e8c2d799454c0ae575efcc805f8bc3e18a331d13c47cdc0b8`
- fixture_sha256: `b9272be266caff6ac38d8060f5dbdbc6e981647729fe1530cfc53ca05b58b007`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `415550072b82b1b3b236c15b45beda7e56782899611899aec658b78876563888`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `b2bd7a022294f7539263ea78da33349f841bc77d827c181e2b2867a85cb18e8f`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Raw trace shows the candidate inspected the upload-related documentation and change map without traversing unrelated repository documents. |
| `verifies_against_code` | FAIL | The candidate never read `src/upload/limits.txt`, produced no TRD, and did not preserve the required 20 MB versus 10 MB discrepancy and impact in delivered evidence. |
| `treats_unverified_as_low_trust` | PASS | The final response explicitly treats `last_verified_version: unverified` as low trust and says it was not used as an interface fact. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=415550072b82b1b3b236c15b45beda7e56782899611899aec658b78876563888; fixture_sha256=b9272be266caff6ac38d8060f5dbdbc6e981647729fe1530cfc53ca05b58b007; output_sha256=e81d10f8792cf5dba701247fe06b89996abeaf48e70895776664e53d3ce2c4c1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identified the mapped documentation and low-trust status, but stopped without reading `src/upload/limits.txt` or delivering the requested technical plan.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=415550072b82b1b3b236c15b45beda7e56782899611899aec658b78876563888; fixture_sha256=b9272be266caff6ac38d8060f5dbdbc6e981647729fe1530cfc53ca05b58b007; output_sha256=c970be6a891756bc875f6dab0d01ef71f01db09774e24374c03a55a3c98d771b; snapshot_sha256=c7789aa51665afd6c39d2904094d943a8d1de1d891feaa4fbd2afdc1c321f033
- Behavior: Delivered a proposal that read the code fixture, captured the 10 MB versus 20 MB conflict, treated the document as unverified, and described the impact.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane omitted the required code verification and delivered TRD evidence.
- Next: Provide confirmed PM scope or handoff materials, then read `src/upload/limits.txt` and deliver the TRD with the documented discrepancy and impact.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
