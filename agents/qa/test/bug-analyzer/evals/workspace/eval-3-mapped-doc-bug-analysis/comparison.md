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
- target_skill_sha256: `0d6c4b717279e8edddeea8100d93e004d25b98b502e0ca114092a3f0c007a52f`
- eval_definition_sha256: `5055f21aa292e91a955bc3aa635c808239336415cf083aba532e9d19a7985220`
- metadata_sha256: `6e065f47b93dd01060b700c2c7836503fb5797f7c0c1bb375677811fe6fa6d5f`
- fixture_sha256: `7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill trace shows the change-map contract was read, then the matched change map, required notification document, and code; no unrelated site-document traversal is evidenced. |
| `verifies_against_code` | PASS | The locked delivery snapshot separately records the document claim of 3 retries, code fact max_retry_attempts = 2, the literal mismatch, and the unresolved runtime/defect classification. |
| `treats_unverified_as_low_trust` | PASS | The locked report identifies last_verified_version: unverified, treats the document as low-trust evidence, and limits confidence in the user-visible defect pending code consumer/tests/runtime evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d; fixture_sha256=7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf; output_sha256=be554417a073c5eec2925ceb8085f4c8be23070622c80e42bd4d59ed6b75c33a; snapshot_sha256=9faf266d55b1d95a50c24239c97f38b76e61e79bc7a436697d4329d0d348a668
- Behavior: Produced the required durable evidence-based defect analysis, preserving the document/code conflict and uncertainty.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d; fixture_sha256=7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf; output_sha256=f6eb48408c7d806d57bc0b100c06d2db1d0627edbb0f99fc4322f303fad9b90f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provided a correct prose comparison of the code/document mismatch and uncertainty, but did not deliver a durable report file.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
