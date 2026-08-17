# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-001-verify-bug-fix`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308` from `agents/qa/test/regression-suite/evals/workspace/eval-1-verify-bug-fix`.
- Identity schema: `2`
- target_skill_sha256: `0d39fb3d56a0db02711ebbb062de0261e33393ff0e6f5f258b11c870a160c7e5`
- eval_definition_sha256: `8ca6ea4c46c7a5a2c854d9ff5def7ea0ec612ddbf9888a829e50de270f1b84c4`
- metadata_sha256: `732278c998a10f6e6333dc13e2fc4edfbaed96da1abb806d2dc29682a3a79f75`
- fixture_sha256: `de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `2c18050b9a27d5dccf92b0604097b9078533d47105266364099eafbf3833aad8`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `33d70406ae3e91e1a71751cc4087074b666d7c138769b3f1c7b475a5d350ce65`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | Trace shows BUG-001, PR-001, and same-path PRD/TRD/QA/implementation materials were read; the delivered report preserves the original reproduction and expected behavior. |
| `qa` | PASS | The delivered result records TEST_SUITE.md, FLOW_INDEX.md, the case, script, prior results/, and prior _reports/ as inspected before execution; no new case or script was needed. |
| `assertion_3` | NOT_EXERCISED | The locked result explicitly labels original failure recheck, expected fixed behavior, and overall verification as blocked/not executed, but no runtime verification occurred. |
| `assertion_4` | PASS | The feature-update scope is limited to valid login plus the directly shared invalid-credential and locked-account paths; it does not expand to release-wide E2E coverage. |
| `alignment_version_archive` | PASS | The locked result documents confirmed PRD/TRD alignment, cites IMPLEMENTATION_PLAN.md, records platform version v1.2.0-fix.1, and delivers append-only result.md and testcase.snapshot.md at the required path. |
| `assertion_5` | PASS | The delivered regression report separates blocked run status from low evidence confidence and includes a needs more verification release recommendation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0; fixture_sha256=de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308; output_sha256=167c791c0ff92d4279d2bc6bd2b7eb05d7cb61ce91fd009ffefd1f11f51cc628; snapshot_sha256=62d2379e3506f88d3627f9ae568fafef42331e5a565877dd61ed6cab4cc6bd3c
- Behavior: Produced the required scoped regression artifacts, explicit blocked statuses, alignment gate, evidence confidence, and release recommendation without claiming the fix was verified.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0; fixture_sha256=de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308; output_sha256=7e5869aa1af5f6cadf68f45ba7438b61cb0f7ed341905166ca1ebfaf1ab316a4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Read the documentation and attempted the harness, but produced no regression artifacts and omitted the required evidence-confidence and release-recommendation report structure.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the fixed runnable build or restore the repository test harness and set QA_BASE_URL.
- Next: Rerun the valid-login, invalid-credential, and locked-account paths, then append updated result.md and testcase.snapshot.md evidence.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
