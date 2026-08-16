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
- target_skill_sha256: `a2cf1652b5fea887d41dd3a13903616fd86413d7444b667455c1a1628200c5bc`
- eval_definition_sha256: `efd5ef5afb815bd08b4891a7e8121a2425c0d9fa58d54ab02bb52d9e0279793d`
- metadata_sha256: `d7923bf8ad60a9b78d8f4a2d5a8014a4c03857221ca26433305123c9d484c670`
- fixture_sha256: `1fc33cc2cafe76721e09e39f06834f83330e227e59b4aed334bc003945dfdf3c`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `76acf51e56db3c0b81097f6bd3d6543ba266417fd8281a9ea540a61e66eb1dc7`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `46eea12ac62f02ceb89a8418aeab70d2e5bbf720f6ba0edc42f3a9c58a443a5e`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `429fc1ef5ebbac055bdbd3fd7863138cf63bfb8f5e1115002085b81b61a4dab5`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `test_spec` | PASS | With_skill delivery_snapshot contains four tests covering all four required scenarios, including stored-record return, exact validation errors with no repository call, and unchanged repository error identity. |
| `test_execution_reported` | PASS | With_skill runner_captured_trace records `npm test` completing with 5 tests passed and 0 failed; the candidate also reports this result. |
| `project_test_conventions_followed` | PASS | The delivered file is under `test/services/notification-service.test.js` and uses the existing flat `node:test` plus `node:assert/strict` structure. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=46eea12ac62f02ceb89a8418aeab70d2e5bbf720f6ba0edc42f3a9c58a443a5e; fixture_sha256=1fc33cc2cafe76721e09e39f06834f83330e227e59b4aed334bc003945dfdf3c; output_sha256=e9925dd0c6c87ecbe564028192cec1d8e59af565c0aafa4892da723f288f2b8e; snapshot_sha256=822df810d1e24bfe6599247aaaff3d705fcadddbeaabc0ea364e8545f6436bf8
- Behavior: Added four semantically correct NotificationService tests, matching the spec and project conventions; all five project tests passed.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=46eea12ac62f02ceb89a8418aeab70d2e5bbf720f6ba0edc42f3a9c58a443a5e; fixture_sha256=1fc33cc2cafe76721e09e39f06834f83330e227e59b4aed334bc003945dfdf3c; output_sha256=dc4400567a44b03968af56397d17e9e3d0f518c2293c7e9b0e0635ce668181ad; snapshot_sha256=770c0d017bf5edcb3001edab369d1d6944d47e4f84c9420d850fddc298e6cbdf
- Behavior: Fresh baseline also added four correct scenarios and reported all five tests passing; behavior is equivalent to with_skill for this task.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
