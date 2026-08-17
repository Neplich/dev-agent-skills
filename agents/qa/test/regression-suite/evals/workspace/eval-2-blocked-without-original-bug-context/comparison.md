# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-002-blocked-without-original-bug-context`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5` from `agents/qa/test/regression-suite/evals/workspace/eval-2-blocked-without-original-bug-context`.
- Identity schema: `2`
- target_skill_sha256: `0d39fb3d56a0db02711ebbb062de0261e33393ff0e6f5f258b11c870a160c7e5`
- eval_definition_sha256: `bde407cd9167fc95a8a68436fa7745a88790341ccffae265b6e1321da5b3938f`
- metadata_sha256: `e69dc8ec803ebfc43eb2e4147f1b861f4b02e94afa256d86c039101ea44fff1b`
- fixture_sha256: `811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `2f3ed1bac6bd41e43ecbd585f5beb95db8464a7cf767e9c9a3ef20fae4f56429`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `33d70406ae3e91e1a71751cc4087074b666d7c138769b3f1c7b475a5d350ce65`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | With-skill output explicitly identifies missing defect/failure/fix/environment evidence and refuses generic regression execution. |
| `blocked` | PASS | With-skill output marks original failure, fixed behavior, adjacent checks, platform version, and PRD/TRD alignment as blocked or not executed; none are passed. |
| `assertion_3` | PASS | Output includes all required fields: original failure recheck, fixed behavior, adjacent regression checks, release recommendation, and evidence confidence. |
| `assertion_4` | PASS | Release recommendation is explicitly `needs more verification`. |
| `no_unknown_or_unscoped_release` | PASS | Output lists required missing evidence and does not claim unknown-scope or release-wide E2E readiness. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=2847ed14fbf2267ebdbe0045fe023fddce4bda2f90b890148d162b6a108cc3f8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocked regression judgment and provided the required evidence gaps and release boundary.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=2c6abcaf7c2f8e8da9336a438e1984562a02f860124903e8814fb3a0520dc73d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Also blocked appropriately, but used as comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
