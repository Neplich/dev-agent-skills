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
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
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
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `test_spec` | PASS | The with_skill test file covers all four required scenarios from docs/test-spec.md, including repository non-invocation for validation failures. |
| `test_execution_reported` | PASS | The with_skill output reports running npm test with 5 tests passing. |
| `project_test_conventions_followed` | PASS | The delivered file uses the expected test/services/notification-service.test.js naming, node:test, node:assert/strict, and structure matching the existing project test. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=46eea12ac62f02ceb89a8418aeab70d2e5bbf720f6ba0edc42f3a9c58a443a5e; fixture_sha256=1fc33cc2cafe76721e09e39f06834f83330e227e59b4aed334bc003945dfdf3c; output_sha256=4797083e645f94d443a6b9e69b5a319579058d4ef4719926c050eef402b63e1f; snapshot_sha256=0fe6ebcaccafb1ea3a0f0155f1dcf4054a89a6425191f594608b188ffa4327e1
- Behavior: Delivered a convention-compliant test file covering every specified scenario and reported all tests passing.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=46eea12ac62f02ceb89a8418aeab70d2e5bbf720f6ba0edc42f3a9c58a443a5e; fixture_sha256=1fc33cc2cafe76721e09e39f06834f83330e227e59b4aed334bc003945dfdf3c; output_sha256=e5e020166e62a7e46865b5f11e0a1ab4ae7ef3a37f797840dd21c0447287a561; snapshot_sha256=2496af56c37e269aab218e9ab32907be9adbee09152dccdf5cc22307fa51ffd3
- Behavior: Also covered the scenarios and reported passing tests; its output is comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `efd5ef5afb815bd08b4891a7e8121a2425c0d9fa58d54ab02bb52d9e0279793d`
- Metadata SHA-256: `f070f60ff223bb6ed508e78cdd69bdde29b46feeccf2713b0da03a7503f77d6f`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `test_spec` | PASS | The locked with_skill test file contains four tests matching all four required scenarios in docs/test-spec.md, including repository call/non-call behavior and unchanged error propagation. |
| `test_execution_reported` | FAIL | The with_skill prose reports `5 passed, 0 failed`, but the locked raw evidence contains no test-execution result proving that the tests were run; the pass claim is unsupported. |
| `project_test_conventions_followed` | PASS | The locked delivery uses test/services/notification-service.test.js and the existing node:test plus node:assert/strict structure. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=46eea12ac62f02ceb89a8418aeab70d2e5bbf720f6ba0edc42f3a9c58a443a5e; fixture_sha256=1fc33cc2cafe76721e09e39f06834f83330e227e59b4aed334bc003945dfdf3c; output_sha256=0026fc75294726eb6a74b5d4269e4ca8c66ff132e18024c83f99f6559e7a2741; snapshot_sha256=7ce7bbac0247eb7e859e023e1542842b699b6dbbab976107b12895b6c52b5861
- Behavior: Delivered tests covering all specified scenarios in the expected project structure and reported a pass result without execution evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=46eea12ac62f02ceb89a8418aeab70d2e5bbf720f6ba0edc42f3a9c58a443a5e; fixture_sha256=1fc33cc2cafe76721e09e39f06834f83330e227e59b4aed334bc003945dfdf3c; output_sha256=403b7142bc2b2329810c149e2670953e1c15abd41442fad2165feaf65efac079; snapshot_sha256=fec8b1cc5e3c0c3672a6abc89ac60bcd30ca1ed0dc2ac95c8efe604ff8faf461
- Behavior: Delivered equivalent four-scenario coverage and reported 5 passing tests, but its execution claim is likewise unsupported by raw execution evidence.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- test_execution_reported is unsupported because no locked raw evidence proves the reported test run occurred.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Skill overlay SHA-256: `951d3480264b2e92c6fe060b9ff2dd8bbbbc16570bec34932e5d89da435a6181`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `efd5ef5afb815bd08b4891a7e8121a2425c0d9fa58d54ab02bb52d9e0279793d`
- Metadata SHA-256: `f070f60ff223bb6ed508e78cdd69bdde29b46feeccf2713b0da03a7503f77d6f`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `test_spec` | PASS | The with_skill test snapshot covers all four required scenarios: valid creation/return, missing recipientId, blank message, and unchanged repository error propagation. |
| `test_execution_reported` | NOT_EXERCISED | The with_skill output reports that npm test passed, but the locked raw evidence contains no runtime execution result to verify that claim. |
| `project_test_conventions_followed` | PASS | The test uses the expected test/services naming and existing node:test plus node:assert/strict structure. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=46eea12ac62f02ceb89a8418aeab70d2e5bbf720f6ba0edc42f3a9c58a443a5e; fixture_sha256=1fc33cc2cafe76721e09e39f06834f83330e227e59b4aed334bc003945dfdf3c; output_sha256=18027d64e343516f957097c40b3e629a7bd2d530a88b187515fab0565ea54948; snapshot_sha256=3a2fed79b0ccbabd2b6a577a75a147c69cb0708b835d3101afa3f5599ed5a18a
- Behavior: Produced equivalent tests covering all four specified scenarios, followed project conventions, and reported five passing tests.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=46eea12ac62f02ceb89a8418aeab70d2e5bbf720f6ba0edc42f3a9c58a443a5e; fixture_sha256=1fc33cc2cafe76721e09e39f06834f83330e227e59b4aed334bc003945dfdf3c; output_sha256=a813e82a60517089c8c0f5bfdf3669735c7c2f4da6d50ecc5385325be7ee49ee; snapshot_sha256=d47d972365df399bbadfcd99a5306beaf786190a90a6d2e4166167002be4a6d9
- Behavior: Produced equivalent tests covering all four specified scenarios and reported five passing tests.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8676e9bdfb5dcb168ade64b20ca31fd5f471aaa2778319375ec606582ddd34da`
- Skill overlay SHA-256: `951d3480264b2e92c6fe060b9ff2dd8bbbbc16570bec34932e5d89da435a6181`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `efd5ef5afb815bd08b4891a7e8121a2425c0d9fa58d54ab02bb52d9e0279793d`
- Metadata SHA-256: `f070f60ff223bb6ed508e78cdd69bdde29b46feeccf2713b0da03a7503f77d6f`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `test_spec` | PASS | The with_skill test file contains tests for all four required scenarios, including repository call behavior and unchanged error propagation. |
| `test_execution_reported` | NOT_EXERCISED | The output reports that npm test passed, but locked raw evidence contains no execution log proving that the tests were actually run. |
| `project_test_conventions_followed` | PASS | The file is named test/services/notification-service.test.js and follows the existing flat node:test and node:assert/strict structure. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=46eea12ac62f02ceb89a8418aeab70d2e5bbf720f6ba0edc42f3a9c58a443a5e; fixture_sha256=1fc33cc2cafe76721e09e39f06834f83330e227e59b4aed334bc003945dfdf3c; output_sha256=ee4ceb8cf29b3e8134d11c6fddb6f744ca2e3ce293ed0ac1ae574fd644e44d0b; snapshot_sha256=804c4386ea5acb5ed06494972e9d3fa6c200c00ed0256beb601a5540a79791e9
- Behavior: Produced tests covering all specified scenarios and reported npm test success; no execution log is available.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=46eea12ac62f02ceb89a8418aeab70d2e5bbf720f6ba0edc42f3a9c58a443a5e; fixture_sha256=1fc33cc2cafe76721e09e39f06834f83330e227e59b4aed334bc003945dfdf3c; output_sha256=1fba3a9303feea8fb6649ab38323419e67055ba8b06fd0850308e05b888fb0e0; snapshot_sha256=6fe0ae869776201511302bf6229de66dec476413bec62d282e2a8b32e1d794e8
- Behavior: Produced equivalent tests and reported 5 passing tests; no execution log is available.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide locked npm test execution evidence to exercise the test_execution_reported assertion.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `aa1be9b48d34fae0ff9f72011ff46a9443fe17dcc0c3310cdf8f09cc429c5ad5`
- Skill overlay SHA-256: `ace601443802587183e16fb4f65142cf4208a38f026e9e5a4042033023fff242`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `efd5ef5afb815bd08b4891a7e8121a2425c0d9fa58d54ab02bb52d9e0279793d`
- Metadata SHA-256: `f070f60ff223bb6ed508e78cdd69bdde29b46feeccf2713b0da03a7503f77d6f`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `test_spec` | PASS | with_skill 提供了 4 个测试，分别覆盖有效输入、缺少 recipientId、空白 message 和仓储错误原样透传；与 Test Spec 的全部 Required Scenarios 一致。 |
| `test_execution_reported` | PASS | with_skill 输出明确报告 npm test 通过，5 个测试全部通过；fixture 中已有 1 个测试，加上新增 4 个测试与该数量一致。 |
| `project_test_conventions_followed` | PASS | 测试文件位于 test/services/notification-service.test.js，使用 node:test 与 node:assert/strict，结构和现有 health-service.test.js 一致。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=46eea12ac62f02ceb89a8418aeab70d2e5bbf720f6ba0edc42f3a9c58a443a5e; fixture_sha256=1fc33cc2cafe76721e09e39f06834f83330e227e59b4aed334bc003945dfdf3c; output_sha256=485b9b38c5196658e955d46c8399e4c019ce4ee2aff98f042fd25b1ce52f10eb; snapshot_sha256=159691bd58d008874e8881b2f3f07d895e0e21571c88bd8dacae041306e4e53a
- Behavior: 新增 4 个 NotificationService.create 测试，完整覆盖规范场景，遵循项目测试约定，并报告 5 个测试通过。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=46eea12ac62f02ceb89a8418aeab70d2e5bbf720f6ba0edc42f3a9c58a443a5e; fixture_sha256=1fc33cc2cafe76721e09e39f06834f83330e227e59b4aed334bc003945dfdf3c; output_sha256=0b74ebc0f10c9236bebbc6ec1f4b51218cc30b4d48b5f76a50167bf9c737a023; snapshot_sha256=a7e4bef59d76fddea43625a8d9a3a41b798722d06307c12b61eda88cb7740992
- Behavior: 同样新增了符合命名和结构的测试，覆盖 4 个规范场景，并报告 5 个测试通过。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `044621ea5e06de080877cb29e7795dc6b010bafa03f5ae20c49efdc9791d4cb1`
- Skill overlay SHA-256: `4783dfb3f1f07cb9b7807b31a1f84259200dc0c5fa863343b23c167911863dfb`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `efd5ef5afb815bd08b4891a7e8121a2425c0d9fa58d54ab02bb52d9e0279793d`
- Metadata SHA-256: `f070f60ff223bb6ed508e78cdd69bdde29b46feeccf2713b0da03a7503f77d6f`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `test_spec` | PASS | with_skill 的测试覆盖 Test Spec 要求的四个场景：有效输入、缺少 recipientId、空白 message、仓储错误原样透传；并验证了校验失败时不调用仓储。 |
| `test_execution_reported` | PASS | with_skill 输出明确报告运行 npm test，5 个测试全部通过；测试文件包含 4 个 NotificationService 场景，fixture 现有健康测试构成第 5 个测试。 |
| `project_test_conventions_followed` | PASS | 测试文件位于 test/services/notification-service.test.js，使用 node:test 与 node:assert/strict，结构符合现有 fixture 测试模式。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=46eea12ac62f02ceb89a8418aeab70d2e5bbf720f6ba0edc42f3a9c58a443a5e; fixture_sha256=1fc33cc2cafe76721e09e39f06834f83330e227e59b4aed334bc003945dfdf3c; output_sha256=7e7dc9e3af9aa849c8c691daeb84fbe12637b8971d4b432a386aef16e7f29f41; snapshot_sha256=877b5a3e0d88e5e06a55298027641bbed7548118696681a8cec11450610e5771
- Behavior: 覆盖全部四个规范场景；使用项目既有 node:test 结构，并报告 5 个测试通过。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=46eea12ac62f02ceb89a8418aeab70d2e5bbf720f6ba0edc42f3a9c58a443a5e; fixture_sha256=1fc33cc2cafe76721e09e39f06834f83330e227e59b4aed334bc003945dfdf3c; output_sha256=4a135e6459a53f3b477d3938b855c95fbe5a1e0b92b8d63892dec84863784f3f; snapshot_sha256=488a7a85635d80470c18cd14ba8074a65a722e35cfdb31dd2989ab036494998e
- Behavior: 覆盖全部四个规范场景，并额外验证校验失败时不调用仓储；报告 5 个测试通过。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

# Eval Result: eval-001-write-tests-from-spec

## Evaluation Target

- Agent: `engineer`
- Skill: `test-writer`
- Eval: `eval-001-write-tests-from-spec`
- Test case: write-tests-from-spec
- Workspace: `workspace/eval-001-write-tests-from-spec`
- Evaluation date: 2026-08-07
- Overall result: PASS
- Behavior result: PASS
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 根据 docs/test-spec.md 为 NotificationService 编写测试
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `test_spec`: 实际读取 Test Spec 与新增测试文件：4 个必需场景均有对应测试，且验证成功结果、错误消息、仓库未调用及错误对象原样透传。
- PASS `assertion_2`: with_skill transcript 记录执行新增测试及 npm test，结果为 5 tests、5 pass、0 fail；exit_code 为 0。
- PASS `assertion_3`: 新增文件为 test/services/notification-service.test.js，使用 node:test、node:assert/strict 和现有扁平 test() 结构，符合项目模式。

## With Skill Behavior

新增测试文件实际存在并覆盖全部 4 个规范场景；workspace 文件哈希与 output.sha256 一致；JSONL transcript 有效；测试报告 5/5 通过。

## Without Skill Baseline

作为对照，without_skill 也实际生成同名测试文件并记录 5/5 通过；其 workspace 哈希与 output.sha256 一致。

## Failures / Findings

- None.
- Root cause: None.

## Next Steps

- 后续修改该 skill、fixture 或 assertions 时，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-001-write-tests-from-spec

## Evaluation Target

- Agent: `engineer`
- Skill: `test-writer`
- Eval: `eval-001-write-tests-from-spec`
- Test case: write-tests-from-spec
- Workspace: `workspace/eval-001-write-tests-from-spec`
- Latest result: PASS - 2026-07-26 fresh paired validation completed; with_skill and fresh without_skill both satisfied 3/3 assertions.
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: approved test spec, implementation code, existing test pattern, and runnable package scripts
- Expected output: 测试文件 + 测试运行结果

## Assertions

- PASS `test_spec`: with_skill 覆盖 test spec 的 4/4 场景，包括不调用 repository 与保留错误 identity。
- PASS `assertion_2`: `npm test` 报告 5 passed、0 failed。
- PASS `assertion_3`: 使用现有 `test/services/*.test.js`、`node:test` 和 `node:assert/strict` 规范。

## With Skill

- 新增与现有模式一致的 notification service 测试，明确记录 spec 场景到测试的追踪关系。

## Without Skill / Baseline

- 2026-07-26 使用同一 prompt 和 fixture 重新生成 fresh baseline，未读取或应用 test-writer skill、Agent README、历史 comparison 或旧 baseline。
- baseline 同样满足 3/3 assertions并通过相同测试命令；批准的 test spec 足够明确，因此没有 assertion-level 增益。

## Failures

- 无 assertion failure。

## Next Steps

- 保留 spec 全覆盖、真实运行和项目规范三项门禁。

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics were generated only in an ignored scratch workspace and are not committed.
