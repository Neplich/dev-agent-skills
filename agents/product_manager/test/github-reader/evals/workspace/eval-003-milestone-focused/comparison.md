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
- target_skill_sha256: `99ea82f9c285d0cd51090c481c0892adf1bdf20367a2866bf82eabffdc17f4c7`
- eval_definition_sha256: `42081b8248822116670301abef5c529a038e386c92ca99283441306b2d8ac307`
- metadata_sha256: `99e5bae99fd448ea8124895faf739aa4393a75e56feb8e7b78841ca027a5f393`
- fixture_sha256: `2ba90e4cae03b1fd07ce6567f8fe44587f4577228f679c498afbf0484b96f05c`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `e8bf769ac89a10c9a014e6b2e125d2d95f024ce8d37a4e4481c16c75936c71a8`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `6506b5ece3ae9322200484db667c39628a3ba1c5902c8e50dced665ef74216a2`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `a9770b603fd249fd7f80da3e56ab1a6acb6432c1ad6dff3ad5cfc0e089124eab`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 明确结论指出 Documentation refresh 进度最慢、React 20 RC 已逾期。 |
| `assertion_2` | PASS | with_skill 为三个 milestone 均提供了 open/closed 总数及完成百分比：5/10（50%）、28/40（70%）、16/20（80%）。 |
| `assertion_3` | PASS | with_skill 使用一致的 🟡、🔴、🟢 状态标识，并分别配有“进度最慢”“已逾期”“进行顺利”等可读标签。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6506b5ece3ae9322200484db667c39628a3ba1c5902c8e50dced665ef74216a2; fixture_sha256=2ba90e4cae03b1fd07ce6567f8fe44587f4577228f679c498afbf0484b96f05c; output_sha256=8438beee2649dc8b48b60d7d5699b0bdfddbd0c47c4bd2c05bf9a50eb8022cd8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 准确基于快照数据时点和三个 milestone 的完成率，明确识别最慢与逾期项，并提供一致状态标识。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6506b5ece3ae9322200484db667c39628a3ba1c5902c8e50dced665ef74216a2; fixture_sha256=2ba90e4cae03b1fd07ce6567f8fe44587f4577228f679c498afbf0484b96f05c; output_sha256=48fb46705d18c3a40e1e8e57f505b300543d7336832fd29d1bf0b1af1ad59dc6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样正确识别最慢和逾期项并提供完成率，但未使用一致的状态标签或图例。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
