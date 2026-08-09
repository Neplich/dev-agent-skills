# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-003-feature-path-missing-plan-blocked`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc` from `agents/qa/test/qa-agent/evals/workspace/eval-3-feature-path-missing-plan-blocked`.
- Fixture SHA-256: `39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc`
- Prompt SHA-256: `094ec5b09f42125c7ea3b42f7f8365ddf4bd40bef6652060cfeb7ff368908608`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `d70112827b0542d867a7689306d190b9c9a901f0d16faf502ff69330466e810c`
- Skill overlay SHA-256: `fda3e87e887ba889a897540771dbb1fdc6d424a530b084850bba0cba716a1567`
- Judge schema SHA-256: `7c827cee8609863280607c031efdc95a92d32b851664d68126eccd9d66c1f27a`
- Eval definition SHA-256: `ffa490cd1f58367914b109adc50e94706c92cbf66e7c95942ae329d3f9a191c7`
- Metadata SHA-256: `aa798ca118679678c2fef882d4726badd357a387202dcb387aceaa4b86696bd0`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_same_feature_path` | NOT_EXERCISED | The with_skill output names `account/profile/preferences` and lists the same-path PRD, TRD, and QA files, but the locked raw evidence cannot independently prove the read operation itself. |
| `specialist_gate_pointer` | PASS | The output selects `spec-based-tester` as the continuing execution owner, identifies the missing implementation plan and other execution prerequisites, and states that no E2E assets were created or run; clean git evidence supports no mutation. |
| `keeps_single_route` | PASS | The with_skill lane selects one narrow route, `spec-based-tester`, and explicitly does not create cases, reports, results, or execute E2E. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=094ec5b09f42125c7ea3b42f7f8365ddf4bd40bef6652060cfeb7ff368908608; fixture_sha256=39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc; output_sha256=63e204e6cf2ec296783a1711537e0494b8ebc5540cde45787cac4a5b0b0a347b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the work to one specialist and stops at the missing-material gate without mutating QA assets.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=094ec5b09f42125c7ea3b42f7f8365ddf4bd40bef6652060cfeb7ff368908608; fixture_sha256=39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc; output_sha256=504836b62d5129a2efc0e90cb341d07138e072e951ffc9d135dd6b7a8945a12d; snapshot_sha256=923d8947c5a061536adbc80a9ac422971e43d32e548fd9103f4dc882c279bb1a
- Behavior: Provides a fresh baseline that attempts execution, mutates QA assets, and reports blocked cases without the specialist routing behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the missing implementation plan and execution materials, then have the selected specialist perform the E2E acceptance.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
