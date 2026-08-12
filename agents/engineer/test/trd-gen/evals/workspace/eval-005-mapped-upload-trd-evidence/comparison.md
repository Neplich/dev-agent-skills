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
- target_skill_sha256: `7350d982beaf3dbc1ec747d4598f05c9a1dfb9b1eb61dcb04ae43dfd72f6fcfd`
- eval_definition_sha256: `ed02404d14ffd40d542c29f44a74caf2fc5696740b01f75b11e50dfad6379f60`
- metadata_sha256: `cfc84017a2f6130d5f5d58c0d09338a6a3beaaf2ead3e34eb6d3229566da0300`
- fixture_sha256: `b9272be266caff6ac38d8060f5dbdbc6e981647729fe1530cfc53ca05b58b007`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `415550072b82b1b3b236c15b45beda7e56782899611899aec658b78876563888`
- Repository HEAD: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `41df440b7248e793c6d9703098fb03264d5ab1871ee7f72726859596ddf5327e`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill trace item_4 reads change-map.yaml, then the mapped upload.md and limits.txt; the broad file listing only inventories paths and does not read unrelated documents. |
| `verifies_against_code` | NOT_EXERCISED | with_skill directly verified limits.txt as 10 MB and preserved the 20 MB documentation conflict and impact in its evidence summary, but no TRD artifact was created because the required PM handoff and feature_path were missing; the TRD-specific portion was not exercised. |
| `treats_unverified_as_low_trust` | PASS | with_skill explicitly treats last_verified_version: unverified as lowest-trust navigation evidence and does not use the page alone to determine interface behavior or the technical plan. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=415550072b82b1b3b236c15b45beda7e56782899611899aec658b78876563888; fixture_sha256=b9272be266caff6ac38d8060f5dbdbc6e981647729fe1530cfc53ca05b58b007; output_sha256=27c8d388f92b8daa71f7ecebdcf9a114aa828eb4466c22c73474c058e5dfd473; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Followed the mapped-document and low-trust workflow, verified the code-side limit and documented the conflict, then correctly stopped at the Engineer entry gate.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=415550072b82b1b3b236c15b45beda7e56782899611899aec658b78876563888; fixture_sha256=b9272be266caff6ac38d8060f5dbdbc6e981647729fe1530cfc53ca05b58b007; output_sha256=0f89339583e9b10f5a7b7e9ee25dceb3fbbecc5a39adf9813863920c20a5318b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a broad technical proposal and correctly identified the 10 MB versus 20 MB conflict, but did not demonstrate mapped-document-first process evidence.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain the confirmed PM handoff, product decisions, and feature_path, then exercise the TRD evidence requirement.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
