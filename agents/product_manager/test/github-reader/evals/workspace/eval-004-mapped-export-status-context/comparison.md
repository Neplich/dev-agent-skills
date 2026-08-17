# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-004-mapped-export-status-context`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b91f8ca3f3681cf4c1a336f7748050f27d679c67ce39092970202362aab7af63` from `agents/product_manager/test/github-reader/evals/workspace/eval-004-mapped-export-status-context`.
- Identity schema: `2`
- target_skill_sha256: `d3991eb6cbaa175b6a277fc4b5fcfd2722f7236109022f8336344db1c65d4b7e`
- eval_definition_sha256: `c9320af546c098adb51ac45faa524e2216c221f13ecd2b33fb2f8f822f024522`
- metadata_sha256: `d12a4df00a2f5f04d2bf0e553078ba3dc62e403dd0f77a037fb5796abdce7123`
- fixture_sha256: `b91f8ca3f3681cf4c1a336f7748050f27d679c67ce39092970202362aab7af63`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `c3d78f9b9bc67f2a85f690ebb4f7d73fa301b8da080d83b39bba1b815957de1c`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `e4717fcaf9f805711dd56f954fc18d08364c40568c6f66db73a7888140ce8305`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill trace shows change-map inspection and required-doc resolution before the targeted read of docs/site/api/export.md; no full docs traversal is shown. |
| `verifies_against_code` | PASS | The locked trace reads src/export/handler.txt, records supported_format: csv, contrasts it with the document’s CSV/JSON claim, and the final report structures the discrepancy and delivery risks. |
| `treats_unverified_as_low_trust` | PASS | The trace and final report explicitly treat last_verified_version: unverified as low-trust, rejecting the document’s JSON claim as delivered without code/test evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c3d78f9b9bc67f2a85f690ebb4f7d73fa301b8da080d83b39bba1b815957de1c; fixture_sha256=b91f8ca3f3681cf4c1a336f7748050f27d679c67ce39092970202362aab7af63; output_sha256=ec0fcd34f163f1834be34c98d594a9a68c798651348d4dbd3ba38762c5db10ef; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Followed the mapped-document workflow, verified the documented format claim against handler.txt, and downgraded unverified documentation while reporting the resulting delivery risk.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c3d78f9b9bc67f2a85f690ebb4f7d73fa301b8da080d83b39bba1b815957de1c; fixture_sha256=b91f8ca3f3681cf4c1a336f7748050f27d679c67ce39092970202362aab7af63; output_sha256=7825a646e187e25dfb487fde9c9cbbfaeee18b37ae9fc2642d3f15e08d1c38bd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also reached the correct substantive conclusion, but is comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
