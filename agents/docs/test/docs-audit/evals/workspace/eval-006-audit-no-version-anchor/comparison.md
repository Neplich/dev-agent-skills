# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-006-audit-no-version-anchor`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb` from `agents/docs/test/docs-audit/evals/workspace/eval-006-audit-no-version-anchor`.
- Identity schema: `2`
- target_skill_sha256: `a5e0bb043d61dbbb218e7d7efc08374e0d16a4d7aaa3b31817f2038830c90941`
- eval_definition_sha256: `405d79374055fe033af3883c346829478f3f76cf09e82f4870928a5901ad3a47`
- metadata_sha256: `953ef09fb5962b093fa646d68b6f137fe0b19f6ba0157a6c58aae94c9c50c930`
- fixture_sha256: `82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `7c0884fab11b08d46eb01de89abfa2125334493a96c7805f68a7161e9d7bff70`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `dfb1de5ef05668c278fa0bfcea0c360fed3169b7b4bae6483c3fb5fedeccf198`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `d7e2242fcdf83209e6c0cb5ec9544aa009e79488a72f81ebd4bf387289fbabec`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_without_target_release_version` | PASS | with_skill explicitly returns `blocked` because `target_release_version` is missing and does not return `ready_for_tag` or `release_verified`. |
| `allows_read_only_diagnostic` | NOT_EXERCISED | The candidate correctly stops at the missing-version gate; the later affected-page diagnostic cannot occur before user confirmation, so this assertion is not exercised. |
| `does_not_persist_report_without_target` | PASS | Locked evidence shows no delivery snapshot, declared outputs, Git changes, new commits, or ref changes; the candidate also explicitly states it will not write a report. |
| `does_not_write_version_stamp` | PASS | The fixture retains `last_verified_version: unverified`; locked Git evidence shows clean status, unchanged HEAD/branch, no ref delta, and no delivered metadata changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=dfb1de5ef05668c278fa0bfcea0c360fed3169b7b4bae6483c3fb5fedeccf198; fixture_sha256=82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb; output_sha256=352f1fae994828f2ba15924f4ba8e890477010b04313caa45b679a41db09d403; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks at the missing maintainer-confirmed target release version and performs no persistence or stamping.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=dfb1de5ef05668c278fa0bfcea0c360fed3169b7b4bae6483c3fb5fedeccf198; fixture_sha256=82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb; output_sha256=1015a3e2726a141f87e2eac913aa99d45a5b169b4918be0fb94add658b9e22e3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a read-only comparison diagnosis and warns against treating the target ref as a confirmed release version, but does not explicitly return the required blocked phase result.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain explicit maintainer confirmation of the complete target_release_version, then perform the deferred affected-page diagnostic.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
