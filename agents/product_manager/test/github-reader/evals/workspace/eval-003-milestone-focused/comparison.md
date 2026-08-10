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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8b55857ad21cc937337dcf6bc1fa19fcc7f833c3e9c078d89a5db79725e98233`
- Skill overlay SHA-256: `b0004c5792dae6a7d4050cf6839b7073909210717e4fcd3dd4b28188da158276`
- Judge schema SHA-256: `e8bf769ac89a10c9a014e6b2e125d2d95f024ce8d37a4e4481c16c75936c71a8`
- Eval definition SHA-256: `42081b8248822116670301abef5c529a038e386c92ca99283441306b2d8ac307`
- Metadata SHA-256: `99e5bae99fd448ea8124895faf739aa4393a75e56feb8e7b78841ca027a5f393`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | With_skill explicitly concludes Documentation refresh is slowest at 50% and React 20 RC is overdue. |
| `assertion_2` | PASS | With_skill provides completion counts and percentages for every milestone: 28/40 (70%), 16/20 (80%), and 5/10 (50%). |
| `assertion_3` | PASS | With_skill consistently uses 🔴 for overdue, 🟡 for slow progress, and 🟢 for normal progress. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6506b5ece3ae9322200484db667c39628a3ba1c5902c8e50dced665ef74216a2; fixture_sha256=2ba90e4cae03b1fd07ce6567f8fe44587f4577228f679c498afbf0484b96f05c; output_sha256=49190dc7c8a0792579c6b1a196ffc6d71f53c3e7f12f6c70ee8ab7b107d14d68; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies the slowest and overdue milestones, includes the snapshot timestamp, supplies completion data for all milestones, and uses consistent status indicators.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6506b5ece3ae9322200484db667c39628a3ba1c5902c8e50dced665ef74216a2; fixture_sha256=2ba90e4cae03b1fd07ce6567f8fe44587f4577228f679c498afbf0484b96f05c; output_sha256=55f0be11c655c3d12587f6232dfdbd648ce4f0c256fd194b21f8272adf5cadb0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also correctly answers the milestone question with completion data and timestamp, but lacks the structured status indicators used by with_skill.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
