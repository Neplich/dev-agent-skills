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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8676e9bdfb5dcb168ade64b20ca31fd5f471aaa2778319375ec606582ddd34da`
- Skill overlay SHA-256: `366b4a2398e19f83568cd66e852162fc58fb6933917f93836fccd17c7c2cfc59`
- Judge schema SHA-256: `76acf51e56db3c0b81097f6bd3d6543ba266417fd8281a9ea540a61e66eb1dc7`
- Eval definition SHA-256: `efd5ef5afb815bd08b4891a7e8121a2425c0d9fa58d54ab02bb52d9e0279793d`
- Metadata SHA-256: `f070f60ff223bb6ed508e78cdd69bdde29b46feeccf2713b0da03a7503f77d6f`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `test_spec` | PASS | with_skill delivery_snapshot contains four tests covering all four required Test Spec scenarios, including repository non-invocation and unchanged error identity. |
| `test_execution_reported` | PASS | with_skill runner_captured_trace records npm test completing with 5 tests passed and 0 failed. |
| `project_test_conventions_followed` | PASS | The delivered file is test/services/notification-service.test.js and uses the existing node:test plus node:assert/strict flat test structure. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=46eea12ac62f02ceb89a8418aeab70d2e5bbf720f6ba0edc42f3a9c58a443a5e; fixture_sha256=1fc33cc2cafe76721e09e39f06834f83330e227e59b4aed334bc003945dfdf3c; output_sha256=1b1a78fc4dbb54482b18c95811688fa360ac8e28e821fabffcce3e19276a2de8; snapshot_sha256=3a5fb482c75df549ccab0f12a410ef66a6cfd8ac8ab5cf01c88078f75c5bc47c
- Behavior: Added complete NotificationService tests and reported a passing full test run.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=46eea12ac62f02ceb89a8418aeab70d2e5bbf720f6ba0edc42f3a9c58a443a5e; fixture_sha256=1fc33cc2cafe76721e09e39f06834f83330e227e59b4aed334bc003945dfdf3c; output_sha256=d410baf9a1ba64ba4b910cd28a210179aac46117e32d2a2b82a959c7935a0dea; snapshot_sha256=dabde16d4abba6a6fb4afd94b509bf547c6aed20c25cd8f33c564cbfd8715f1f
- Behavior: Also added equivalent complete tests and reported a passing full test run; comparison baseline only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
