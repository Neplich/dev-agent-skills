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
- target_skill_sha256: `5f00953469c57cd0a924598017d2502b6a836948c3bfa067998cf3e91f7335a1`
- eval_definition_sha256: `8ca6ea4c46c7a5a2c854d9ff5def7ea0ec612ddbf9888a829e50de270f1b84c4`
- metadata_sha256: `732278c998a10f6e6333dc13e2fc4edfbaed96da1abb806d2dc29682a3a79f75`
- fixture_sha256: `de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `2c18050b9a27d5dccf92b0604097b9078533d47105266364099eafbf3833aad8`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `07500a40de121399595841537e6aef1df4c976254ab123954a243d97bad454fb`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | With-skill trace shows BUG-001, PR-001, and related product, engineering, and QA evidence were read before scoping the regression. |
| `qa` | PASS | With-skill trace and delivery record show TEST_SUITE.md, FLOW_INDEX.md, the case, script, and absent prior results/_reports were checked; no new TC was needed. |
| `assertion_3` | NOT_EXERCISED | The report records the run as blocked and explains that original-failure and fixed-behavior checks were not executed because package.json/runtime evidence was unavailable. |
| `assertion_4` | PASS | The delivery snapshot identifies feature-update scope and covers the original flow plus invalid-credential and locked-account shared-response paths without expanding to release-wide E2E. |
| `alignment_version_archive` | PASS | The snapshot contains same-feature-path PRD/TRD alignment, a confirmed IMPLEMENTATION_PLAN.md, platform version v1.2.0-fix.1, and the required result.md and testcase.snapshot.md paths; no historical results were overwritten. |
| `assertion_5` | PASS | The report separates Status: blocked from evidence_confidence: low and gives release_recommendation: needs more verification. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0; fixture_sha256=de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308; output_sha256=1a6526143196f710b3b7b14394d28717a8cbbdf50ae597a7dcf2e0fa7ce12219; snapshot_sha256=8bc5f1739e2e6b66c92c67afeacd9ac6f7792f8276bc95cee942b7e8f7a48374
- Behavior: Correctly performs evidence preflight, alignment, scoped regression planning, and append-only blocked-result recording, but cannot execute runtime verification.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0; fixture_sha256=de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308; output_sha256=ccf69c6e6d4125bea57990badb696ec104aa0314987d95d14e9c07dba35c4c95; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline identifies the missing harness and avoids claiming the fix passed, but does not produce the required durable QA result artifacts or alignment/archive report.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the fixed build with package.json or an equivalent runnable harness, then rerun the original login flow and both adjacent credential-state paths.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
