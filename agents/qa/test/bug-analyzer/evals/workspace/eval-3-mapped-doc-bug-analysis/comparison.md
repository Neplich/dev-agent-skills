# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-003-mapped-doc-bug-analysis`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf` from `agents/qa/test/bug-analyzer/evals/workspace/eval-3-mapped-doc-bug-analysis`.
- Identity schema: `2`
- target_skill_sha256: `09e738dc9988190b7f79b8aac551bd1674e0642fae4817109cb4551b9f01f0cd`
- eval_definition_sha256: `5055f21aa292e91a955bc3aa635c808239336415cf083aba532e9d19a7985220`
- metadata_sha256: `98bdccb4e3241d7facbaf94d94c2edbbe1adcec302e237e84c10d586748147c6`
- fixture_sha256: `7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `147ea0edbf82c8ca9a07d9d6ff0b589da90d3fd96bbb89bae4f44faf26cc1243`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill trace reads the change-map and then the mapped `docs/site/api/notification-retry.md`; no unrelated site-document traversal is shown. |
| `verifies_against_code` | PASS | The locked report records the documentation claim of 3 retries, code value `max_retry_attempts = 2`, their discrepancy, and the unresolved runtime/counting-semantics impact. |
| `treats_unverified_as_low_trust` | PASS | The locked report explicitly identifies `last_verified_version: unverified`, treats the documents as low-trust, and classifies runtime impact as suspected/needs more evidence with low confidence pending code/runtime evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d; fixture_sha256=7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf; output_sha256=18f78302fd7b9479879638e1a84f534c82cd2bc69e4c8aab09ab7ae0737e9039; snapshot_sha256=0c9f3afb59f866bb1696c0d9960ff842de619db7364bbc45054d9578db3567f7
- Behavior: Created a durable evidence report, followed mapped-document context, verified the rule against code, and avoided overstating the runtime defect.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d; fixture_sha256=7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf; output_sha256=759bbc5ae015a63f06da731a9f2359fbb288fa68b33b7e69bff6d6d80cd80a75; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a strong prose-only comparison analysis identifying the same discrepancy and evidence gaps, without the durable report artifact.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
