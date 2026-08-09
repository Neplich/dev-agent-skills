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
- Fixture SHA-256: `bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b`
- Prompt SHA-256: `b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8ceb46669357c2ad2e3984067ae0ce5c97b019da23d3a0f850d2bedd7e38ab17`
- Skill overlay SHA-256: `fda3e87e887ba889a897540771dbb1fdc6d424a530b084850bba0cba716a1567`
- Judge schema SHA-256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Eval definition SHA-256: `69ea284c249fd48ea67518dcbbbb4aff0b51c724f5aa24139bc9524759db6c7c`
- Metadata SHA-256: `dbcf12ca577304c6eedeb3847e29d69b72d051700655cd6bd5000bc1d6f7a9d9`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | Locked raw evidence contains the candidate's claimed read order but no tool trace or other proof of sequencing. |
| `verifies_against_code` | PASS | The with_skill output identifies the formal document, its 80-character declaration, the code rule `nickname_max_length = 64`, and the 65–80 character acceptance impact. |
| `treats_unverified_as_low_trust` | PASS | The with_skill output explicitly marks `last_verified_version: unverified` as low trust and bases the key conclusion on the code value 64. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96; fixture_sha256=bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b; output_sha256=8df1c764ccf0a61b7779acdb58f6e2e0a697a9ec40b31656040b26404fc2148d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies the code/document mismatch, treats the documentation as unverified, and records evidence and impact; read sequencing is not independently provable.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96; fixture_sha256=bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b; output_sha256=0651e1aa72e5dda7a97e9cf1d8e62cb5848e26d2cfebc41372ebe2953ebde645; snapshot_sha256=c079e778f877afd1c1077460bc725705ce7e4245cab3271d165e505a99e58cd6
- Behavior: Claims to correct the documentation and add a requirements matrix, with delivery snapshots showing those artifacts.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Capture read-order/tool-trace evidence to exercise the mapped-document-first assertion.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
