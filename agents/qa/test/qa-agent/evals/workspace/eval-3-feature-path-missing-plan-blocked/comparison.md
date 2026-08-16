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
- Identity schema: `2`
- target_skill_sha256: `944bb130633ab2aa16595ed1d51c447f77cd06660f1aafc548f03bd9b22af162`
- eval_definition_sha256: `ec357d7e216245f12726027da14d7981d249bcac4a9eff1a2ed19f5ffc8af4f2`
- metadata_sha256: `aa798ca118679678c2fef882d4726badd357a387202dcb387aceaa4b86696bd0`
- fixture_sha256: `39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `7c827cee8609863280607c031efdc95a92d32b851664d68126eccd9d66c1f27a`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `094ec5b09f42125c7ea3b42f7f8365ddf4bd40bef6652060cfeb7ff368908608`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `2ae6df1e5892f15e69faa5eb27f67247be532cf172f30b6323b139a66d25acc0`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_same_feature_path` | PASS | With-skill output identifies feature_path `account/profile/preferences`, cites the same-path PRD/TRD, and lists the retained QA E2E directory and files. |
| `specialist_gate_pointer` | PASS | With-skill output routes follow-up to `spec-based-tester`, identifies the missing same-path `IMPLEMENTATION_PLAN.md` gate, and states E2E cannot execute; git status is clean with no delivered asset mutations. |
| `keeps_single_route` | PASS | With-skill output selects only the narrow `spec-based-tester` QA route and does not invoke implementation repair or create/update/run E2E assets. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=094ec5b09f42125c7ea3b42f7f8365ddf4bd40bef6652060cfeb7ff368908608; fixture_sha256=39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc; output_sha256=140a77d959c7cd08f3fcdd78ff4366bf2f526e8d3c9429e28abd2c22168c6b6d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly selected the narrow specialist route, preserved same-path context, and stopped at the missing implementation-plan gate without mutating QA assets.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=094ec5b09f42125c7ea3b42f7f8365ddf4bd40bef6652060cfeb7ff368908608; fixture_sha256=39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc; output_sha256=a7c75ccaf06e2853fc74d81338b4e996474de323058dbaf0e0972e55c401f360; snapshot_sha256=3669a60e652513a62e4b3a683bcaee8f1594bffd6c3406a33a04d6ae489d757f
- Behavior: Established the feature context but updated QA assets and did not provide the specialist gate pointer or single-route handoff behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
