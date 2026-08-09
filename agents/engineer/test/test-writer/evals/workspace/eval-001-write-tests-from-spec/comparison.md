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
- Fixture SHA-256: `1fc33cc2cafe76721e09e39f06834f83330e227e59b4aed334bc003945dfdf3c`
- Prompt SHA-256: `46eea12ac62f02ceb89a8418aeab70d2e5bbf720f6ba0edc42f3a9c58a443a5e`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8676e9bdfb5dcb168ade64b20ca31fd5f471aaa2778319375ec606582ddd34da`
- Skill overlay SHA-256: `3ddde57487997fd2ff39d31cb5f9f0b20bccf604d883b4e7f63c7540bbbf4537`
- Judge schema SHA-256: `76acf51e56db3c0b81097f6bd3d6543ba266417fd8281a9ea540a61e66eb1dc7`
- Eval definition SHA-256: `efd5ef5afb815bd08b4891a7e8121a2425c0d9fa58d54ab02bb52d9e0279793d`
- Metadata SHA-256: `f070f60ff223bb6ed508e78cdd69bdde29b46feeccf2713b0da03a7503f77d6f`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `test_spec` | PASS | The locked with_skill test file contains all four required scenarios: valid creation, missing recipientId, blank message, and unchanged repository-error propagation. |
| `test_execution_reported` | PASS | The with_skill candidate output reports `npm test` with 5 tests all passing; the fixture contains one existing test plus four delivered tests. |
| `project_test_conventions_followed` | PASS | The delivered file uses the expected `*.test.js` naming and existing `node:test`/`node:assert/strict` structure. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=46eea12ac62f02ceb89a8418aeab70d2e5bbf720f6ba0edc42f3a9c58a443a5e; fixture_sha256=1fc33cc2cafe76721e09e39f06834f83330e227e59b4aed334bc003945dfdf3c; output_sha256=5c54c112575c95a1fd57c2985737c9095bad18fc002cd182711452ee327fad9e; snapshot_sha256=f949ee992dae7b4bf529fa19968cfe3671fb7bf103f6a1f4a88f3008cd3f7f29
- Behavior: Delivered tests cover every specified scenario, follow project conventions, and report all tests passing.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=46eea12ac62f02ceb89a8418aeab70d2e5bbf720f6ba0edc42f3a9c58a443a5e; fixture_sha256=1fc33cc2cafe76721e09e39f06834f83330e227e59b4aed334bc003945dfdf3c; output_sha256=90e4623b5103c41c616fd6d4357a57c40e7d28633cc19fc218790e55aa788092; snapshot_sha256=abd3e81956cf6131f84f104cc27a97d2694995424e6421a3c76713020b10aacc
- Behavior: Also covered all required scenarios and reported passing tests, with one additional validation scenario.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
