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
- Identity schema: `2`
- target_skill_sha256: `d3991eb6cbaa175b6a277fc4b5fcfd2722f7236109022f8336344db1c65d4b7e`
- eval_definition_sha256: `42081b8248822116670301abef5c529a038e386c92ca99283441306b2d8ac307`
- metadata_sha256: `99e5bae99fd448ea8124895faf739aa4393a75e56feb8e7b78841ca027a5f393`
- fixture_sha256: `2ba90e4cae03b1fd07ce6567f8fe44587f4577228f679c498afbf0484b96f05c`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `e8bf769ac89a10c9a014e6b2e125d2d95f024ce8d37a4e4481c16c75936c71a8`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `6506b5ece3ae9322200484db667c39628a3ba1c5902c8e50dced665ef74216a2`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `e4717fcaf9f805711dd56f954fc18d08364c40568c6f66db73a7888140ce8305`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | With_skill explicitly identifies Documentation refresh as the slowest at 50% and React 20 RC as overdue. |
| `assertion_2` | PASS | With_skill gives open/closed totals and percentages for all three milestones: 5/10 (50%), 28/40 (70%), and 16/20 (80%). |
| `assertion_3` | PASS | With_skill consistently uses readable status markers and labels: 🟡 slowest, 🔴 overdue, and 🟢 ongoing. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6506b5ece3ae9322200484db667c39628a3ba1c5902c8e50dced665ef74216a2; fixture_sha256=2ba90e4cae03b1fd07ce6567f8fe44587f4577228f679c498afbf0484b96f05c; output_sha256=c33b7a6af1838e2675acef9c5ed1895e6bc1a91a3f9943f8a87c058b954f470f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly reports the snapshot time, computes milestone completion, identifies the slowest and overdue milestones, and applies readable status labels.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6506b5ece3ae9322200484db667c39628a3ba1c5902c8e50dced665ef74216a2; fixture_sha256=2ba90e4cae03b1fd07ce6567f8fe44587f4577228f679c498afbf0484b96f05c; output_sha256=18029316aaa75383f62f0f79e29e9c096f66b013618e667ab12a116b367ba3c8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Also correctly identifies the slowest and overdue milestones and provides completion data, but does not use a consistent status legend or labels.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
