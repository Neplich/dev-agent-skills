# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `test-writer`
- Eval: `eval-002-mapped-pagination-tests`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d` from `agents/engineer/test/test-writer/evals/workspace/eval-002-mapped-pagination-tests`.
- Identity schema: `2`
- target_skill_sha256: `a2cf1652b5fea887d41dd3a13903616fd86413d7444b667455c1a1628200c5bc`
- eval_definition_sha256: `dffdc1de9650924aeba7f48471eac1b4c1592e52cef441419d14a463af648ff5`
- metadata_sha256: `dd6a44fd990ce66c25d528434ffde60d69dfd0c22dc5694badf75d832012ae4f`
- fixture_sha256: `866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `429fc1ef5ebbac055bdbd3fd7863138cf63bfb8f5e1115002085b81b61a4dab5`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Trace shows change-map lookup before reading the mapped pagination document; no unrelated document contents were read first. |
| `verifies_against_code` | PASS | Locked test file asserts default_page_size equals 25; trace and output identify the document’s 50 as inconsistent with defaults.txt. |
| `treats_unverified_as_low_trust` | PASS | Trace records last_verified_version: unverified, and the locked test file never uses 50 as an expected value. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428; fixture_sha256=866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d; output_sha256=3ebbf0b050098c81b2c9415ffaaa039bb01ca9037c98d1376cfd1f1cd8bbd723; snapshot_sha256=36808fcf3c52d2f93e165f9b2e16aa7c3f18a74f9b43c0e1cb557bde4fc962fd
- Behavior: Added and ran four pagination default-boundary tests using 25 and 100 from defaults.txt, while treating the unverified 50-document value as non-authoritative.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428; fixture_sha256=866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d; output_sha256=b48141a20548c40cc4a784c6758e9e561623460b1204c48b8c022121723dd403; snapshot_sha256=ec5fa9ad3df493d20cdf2ee99ca9b9d0112f3435001c4a0c0ba0558226c85225
- Behavior: Fresh baseline also verified 25 versus the unverified document value 50 and delivered broader six-test boundary coverage.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
