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
- target_skill_sha256: `5f3a5999aa1efa139e50399981290b3134eeec82bfa2eeeccd743979bbb2eb31`
- eval_definition_sha256: `dffdc1de9650924aeba7f48471eac1b4c1592e52cef441419d14a463af648ff5`
- metadata_sha256: `dd6a44fd990ce66c25d528434ffde60d69dfd0c22dc5694badf75d832012ae4f`
- fixture_sha256: `866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `74d5ef1ceb04052c742ef9500d8bca484457637293371f2cd945a5336fc8d8e9`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Trace shows change-map resolution followed by reading docs/site/api/pagination.md before unrelated repository exploration. |
| `verifies_against_code` | PASS | Locked test file reads src/pagination/defaults.txt and asserts default_page_size is 25; trace records the document value 50 and code value 25 mismatch. |
| `treats_unverified_as_low_trust` | PASS | Trace and final output identify last_verified_version: unverified as low trust, retain the document's 50, and use code-backed 25 in the test. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428; fixture_sha256=866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d; output_sha256=54dfe9dd919c8ada6a909f53dbb2cfe607eda68892cb6b885cd7466e24b559b0; snapshot_sha256=bbeb432d43b8981cb6110f5ef297148a97f2cd7de60937f9bb015505b961f858
- Behavior: Read the mapped documentation and code evidence, treated the unverified document as lower trust, and added tests asserting the code-backed default of 25.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428; fixture_sha256=866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d; output_sha256=ab8bde0ee4a46912302088257688e26578e713ec9a0874745fc237b695bfe392; snapshot_sha256=b996e6920e05508c60c21139ae5b9a466395dbb5b5d5ba25084de1d16ebf2740
- Behavior: Added broader boundary tests and rewrote the unverified documentation value from 50 to 25; comparison only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
