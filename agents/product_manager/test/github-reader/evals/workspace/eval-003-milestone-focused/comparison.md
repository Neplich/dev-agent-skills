# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-reader`
- Eval: `eval-003-milestone-focused`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2ba90e4cae03b1fd07ce6567f8fe44587f4577228f679c498afbf0484b96f05c` from `agents/product_manager/test/github-reader/evals/workspace/eval-003-milestone-focused`.
- Fixture SHA-256: `2ba90e4cae03b1fd07ce6567f8fe44587f4577228f679c498afbf0484b96f05c`
- Prompt SHA-256: `6506b5ece3ae9322200484db667c39628a3ba1c5902c8e50dced665ef74216a2`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8b55857ad21cc937337dcf6bc1fa19fcc7f833c3e9c078d89a5db79725e98233`
- Skill overlay SHA-256: `68da0ba1f028f581794447a220a41c2a7932596fc89598d52df4a3ae7cae05a7`
- Judge schema SHA-256: `e8bf769ac89a10c9a014e6b2e125d2d95f024ce8d37a4e4481c16c75936c71a8`
- Eval definition SHA-256: `42081b8248822116670301abef5c529a038e386c92ca99283441306b2d8ac307`
- Metadata SHA-256: `99e5bae99fd448ea8124895faf739aa4393a75e56feb8e7b78841ca027a5f393`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | 明确指出 Documentation refresh 进度最慢（50%），并指出 React 20 RC 已逾期。 |
| `assertion_2` | PASS | 表格为每个 milestone 提供了具体的 open/closed 总量比例：5/10、28/40、16/20。 |
| `assertion_3` | PASS | 使用一致的 🟡 最慢、🔴 已逾期、🟢 顺利状态标签区分三种状态。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6506b5ece3ae9322200484db667c39628a3ba1c5902c8e50dced665ef74216a2; fixture_sha256=2ba90e4cae03b1fd07ce6567f8fe44587f4577228f679c498afbf0484b96f05c; output_sha256=7681efe142b08b0b16de7ffa316c3cdedd42aee314788de8ea3433ac2e523ae2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完整读取快照并给出数据时点、各 milestone 完成率及明确的最慢和逾期结论。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6506b5ece3ae9322200484db667c39628a3ba1c5902c8e50dced665ef74216a2; fixture_sha256=2ba90e4cae03b1fd07ce6567f8fe44587f4577228f679c498afbf0484b96f05c; output_sha256=74f56ca70b97e652c5ea7fd3a40b5f6c883d0a7890d702f87b9f13671f2ffc2a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样给出正确的最慢、逾期判断和完成率，但未使用状态表格图例。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
