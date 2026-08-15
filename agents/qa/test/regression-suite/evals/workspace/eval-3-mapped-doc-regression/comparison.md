# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-003-mapped-doc-regression`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94` from `agents/qa/test/regression-suite/evals/workspace/eval-3-mapped-doc-regression`.
- Identity schema: `2`
- target_skill_sha256: `5f00953469c57cd0a924598017d2502b6a836948c3bfa067998cf3e91f7335a1`
- eval_definition_sha256: `e133160262ed184852d28136da76d373bddc3830b084351e43f62baba3d14a43`
- metadata_sha256: `8f1420b83ef9d543d57a760ebba7fc169b9c3d2172e7b3b1e191d47cfe76b856`
- fixture_sha256: `b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `ffcf3a2d7addddf903f6f7ab8491b7d6388aab8f8d43086a53d98c797d44a47b`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `07500a40de121399595841537e6aef1df4c976254ab123954a243d97bad454fb`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Trace reads the change map, then the mapped API document, before verifying the code; no other site-document contents are read. |
| `verifies_against_code` | PASS | The delivered conclusion records code threshold 3, documentation threshold 2, the discrepancy, and the direct regression paths without treating 2 as confirmed. |
| `treats_unverified_as_low_trust` | PASS | The conclusion identifies both documents as unverified, verifies the code, reports missing test/runtime evidence, and marks verification blocked with low confidence rather than release-ready. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ffcf3a2d7addddf903f6f7ab8491b7d6388aab8f8d43086a53d98c797d44a47b; fixture_sha256=b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94; output_sha256=30af815715e3117f634657dd1908d768699949ad3c2a6b7ff20c2bb872cf073d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly follows the mapped-document lookup, verifies the threshold against code, preserves the documentation/code conflict, and keeps the regression conclusion blocked pending missing evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ffcf3a2d7addddf903f6f7ab8491b7d6388aab8f8d43086a53d98c797d44a47b; fixture_sha256=b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94; output_sha256=b64485c037930cb6e771a4c3c690420677c270ae3d85bb498be3bd788bc4c289; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Finds the relevant files and code discrepancy but incorrectly treats the documentation value 2 as the repair target and does not apply the low-trust handling consistently.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
