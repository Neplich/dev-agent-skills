# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `test-writer`
- Eval: `eval-001-write-tests-from-spec`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1fc33cc2cafe76721e09e39f06834f83330e227e59b4aed334bc003945dfdf3c` from `agents/engineer/test/test-writer/evals/workspace/eval-001-write-tests-from-spec`.
- Identity schema: `2`
- target_skill_sha256: `5f3a5999aa1efa139e50399981290b3134eeec82bfa2eeeccd743979bbb2eb31`
- eval_definition_sha256: `efd5ef5afb815bd08b4891a7e8121a2425c0d9fa58d54ab02bb52d9e0279793d`
- metadata_sha256: `d7923bf8ad60a9b78d8f4a2d5a8014a4c03857221ca26433305123c9d484c670`
- fixture_sha256: `1fc33cc2cafe76721e09e39f06834f83330e227e59b4aed334bc003945dfdf3c`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `76acf51e56db3c0b81097f6bd3d6543ba266417fd8281a9ea540a61e66eb1dc7`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `46eea12ac62f02ceb89a8418aeab70d2e5bbf720f6ba0edc42f3a9c58a443a5e`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `74d5ef1ceb04052c742ef9500d8bca484457637293371f2cd945a5336fc8d8e9`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `test_spec` | PASS | The locked with_skill test file covers all four required scenarios: valid creation/returned record, missing recipientId with exact error and no repository call, blank message with exact error and no repository call, and unchanged repository-error propagation. |
| `test_execution_reported` | PASS | The locked with_skill trace shows `npm test` completed with exit code 0 and 5 tests passed, 0 failed; the candidate also reports `5/5 通过`. |
| `project_test_conventions_followed` | PASS | The delivered file is `test/services/notification-service.test.js`, uses `node:test` and `node:assert/strict`, imports the service with the expected relative path, and follows the existing flat test structure. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=46eea12ac62f02ceb89a8418aeab70d2e5bbf720f6ba0edc42f3a9c58a443a5e; fixture_sha256=1fc33cc2cafe76721e09e39f06834f83330e227e59b4aed334bc003945dfdf3c; output_sha256=2725bbd435bfb47cbda14a88c96f59b4e298f21d248460a2fa1a0e80d57101bd; snapshot_sha256=c95b873be710950b10d92f2ae295d1fd8369f938c561e387b5ab444f994577c6
- Behavior: Added the expected NotificationService test file covering all four spec scenarios and reported a successful full test run.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=46eea12ac62f02ceb89a8418aeab70d2e5bbf720f6ba0edc42f3a9c58a443a5e; fixture_sha256=1fc33cc2cafe76721e09e39f06834f83330e227e59b4aed334bc003945dfdf3c; output_sha256=ef6e28ba9576d78baa0ae4c083d7cc1533ba23ee12a9d46e9c09da0b9c8bfd02; snapshot_sha256=cf52edc0df87572fc8431399fdbef2667f6dc9ff0544a6067e7fb4a0a2114b16
- Behavior: Also added equivalent coverage and reported passing tests; behavior is comparable, with an extra explicit repository-call scenario in its prose.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
