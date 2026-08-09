# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-004-nested-feature-path-bug-alignment`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1e51e9c8d509d705021a998a8e3fa6c6c2d1f11f8d331f94d613c603fe3acfe0` from `agents/engineer/test/debugger/evals/workspace/eval-004-nested-feature-path-bug-alignment`.
- Fixture SHA-256: `1e51e9c8d509d705021a998a8e3fa6c6c2d1f11f8d331f94d613c603fe3acfe0`
- Prompt SHA-256: `c6a119a607cc22724566b0886d0898a2191f1291f5ef19216b2d283dcf9bdf94`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2c7be3366028d6afd52b5eb4079e33c2b766f47c01e7c7ee8c4cd7cee5ef4d64`
- Skill overlay SHA-256: `d9980d41bb48adbaa0ffa94159cff2b9b190fc5504bbdbee7f3503d87a42c7b9`
- Judge schema SHA-256: `8752855324ba03bc8e8e5d406c04e9f47ee4871f83be7779dbe93e460aa8eb03`
- Eval definition SHA-256: `4ed41777f0081de6b22c8d5c1da9d06cff7a26fda1bb09b0b22361f263f5eaee`
- Metadata SHA-256: `92b34bddeb11ae5b3c6841a7115ad004679cbe8ce0c62b863a34d672cce43c83`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_nested_expected_behavior_docs` | FAIL | The output gives the feature_path and names PRD/TRD, but does not cite the required full document paths. |
| `validates_trd_related_prd` | PASS | It states that TRD related_prd is correct and classifies the technical documentation gap as trd_gap. |
| `classifies_before_repair_plan` | PASS | The output classifies the issue before proposing any repair or handoff plan. |
| `blocks_wrong_path_or_requirement_change` | NOT_EXERCISED | The fixture has a clear feature_path, present PRD, unchanged requirements, and matching TRD path, so this conditional blocking behavior is not exercised. |
| `does_not_fix_directly` | PASS | The output explicitly says no code or tests were modified, and git evidence confirms no changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a119a607cc22724566b0886d0898a2191f1291f5ef19216b2d283dcf9bdf94; fixture_sha256=1e51e9c8d509d705021a998a8e3fa6c6c2d1f11f8d331f94d613c603fe3acfe0; output_sha256=9166e65ec461e6d05bbd766c8f50b257fcca90b6172ef0a47fd689f2f3161e92; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classifies a trd_gap, validates related_prd, routes to trd-gen, and makes no changes, but omits the exact document paths.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a119a607cc22724566b0886d0898a2191f1291f5ef19216b2d283dcf9bdf94; fixture_sha256=1e51e9c8d509d705021a998a8e3fa6c6c2d1f11f8d331f94d613c603fe3acfe0; output_sha256=81fa81faafaa2480219ededa097862ce9823a42ba64c7462bb2a319a2a615fe4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Describes expected sorting and cites document paths, but does not classify the issue or route it through the required handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output omits the exact required PRD.md and TRD.md paths.
- Next: Include both exact document paths in the investigation output.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
