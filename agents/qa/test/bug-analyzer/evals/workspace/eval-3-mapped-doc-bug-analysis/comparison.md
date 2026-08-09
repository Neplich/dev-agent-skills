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
- Fixture SHA-256: `7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf`
- Prompt SHA-256: `42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0d6c4b717279e8edddeea8100d93e004d25b98b502e0ca114092a3f0c007a52f`
- Skill overlay SHA-256: `4d1289a2f580cb07efcd85d24fb079acfc635807339f9469fa7653101393ff87`
- Judge schema SHA-256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Eval definition SHA-256: `5055f21aa292e91a955bc3aa635c808239336415cf083aba532e9d19a7985220`
- Metadata SHA-256: `6e065f47b93dd01060b700c2c7836503fb5797f7c0c1bb375677811fe6fa6d5f`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | The locked report records the matched change-map entry and required document, but the locked evidence cannot prove the actual read order or absence of an unrelated full-site traversal. |
| `verifies_against_code` | PASS | The delivered report records code value 2, documentation value 3, their separate evidence roles, and the impact on defect classification; the fixture confirms max_retry_attempts = 2. |
| `treats_unverified_as_low_trust` | PASS | The delivered report identifies last_verified_version: unverified as low-trust and keeps runtime defect confidence low pending code, test, and execution evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d; fixture_sha256=7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf; output_sha256=8b5e84a2f379b9d9cc1f1e5e73c05e09d78cc6cfd0f7eadc0e2484e1b0e69ff3; snapshot_sha256=c73eff7510c1ef2210bd4a1e6f062ba5b2b87af96eb15aee849b6dcc96954f18
- Behavior: Produced a structured evidence report with correct code/document discrepancy analysis, low-trust handling, uncertainty boundaries, and requested follow-up evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d; fixture_sha256=7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf; output_sha256=256b0e2e3603ec817b5b5916e3d5f8d0583794410ee41f57aca20425536ce2ce; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provided accurate comparison analysis in prose but no delivered report file; it also treated the discrepancy as unconfirmed runtime behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Use an observable read trace or equivalent raw process evidence to evaluate the mapped-document read-order assertion.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
