# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `spec-based-tester`
- Eval: `eval-003-mapped-doc-acceptance`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b` from `agents/qa/test/spec-based-tester/evals/workspace/eval-3-mapped-doc-acceptance`.
- Identity schema: `2`
- target_skill_sha256: `8ceb46669357c2ad2e3984067ae0ce5c97b019da23d3a0f850d2bedd7e38ab17`
- eval_definition_sha256: `69ea284c249fd48ea67518dcbbbb4aff0b51c724f5aa24139bc9524759db6c7c`
- metadata_sha256: `dbcf12ca577304c6eedeb3847e29d69b72d051700655cd6bd5000bc1d6f7a9d9`
- fixture_sha256: `bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b`
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
| `reads_mapped_docs_first` | PASS | Trace shows the mapped change-map and required API document were read before the target rule file; no unrelated document contents were read. |
| `verifies_against_code` | PASS | Delivered validation report and trace directly compare the API statement of 80 characters with src/profile/validation.rules value 64, recording the mismatch and impact. |
| `treats_unverified_as_low_trust` | PASS | Delivered report explicitly identifies both documents as unverified and grounds conclusions in code/static validation evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96; fixture_sha256=bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b; output_sha256=4a6a529b1b1cbb87c8f0656834ca01dc4ef9049fb4a0634c6acbbea06c91620e; snapshot_sha256=b82c8fb9d8e08984383f8e32d6831f90ab877d830e147e4da0de9ed5d792e87f
- Behavior: Correctly mapped the change documentation, verified the 80-versus-64 mismatch against code, treated unverified documents as low trust, and delivered a validation report with impact and blocked runtime checks.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96; fixture_sha256=bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b; output_sha256=fc975bbc7755e37668353458914f2ae2463884bc8ccef373dd9643f9892f1568; snapshot_sha256=1547f9c64cafc1d8d17ace6f4cf5615989033a82deffcbede41857b9de7d3491
- Behavior: Also reported the core mismatch and created a requirements matrix, but provided less explicit validation framing and evidence handling.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
