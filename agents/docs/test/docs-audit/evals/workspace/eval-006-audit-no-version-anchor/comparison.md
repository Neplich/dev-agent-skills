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
- target_skill_sha256: `dafd53371901dfd724f88c70262b157e59494d29da1c613d0ef130564b6ff4f9`
- eval_definition_sha256: `405d79374055fe033af3883c346829478f3f76cf09e82f4870928a5901ad3a47`
- metadata_sha256: `953ef09fb5962b093fa646d68b6f137fe0b19f6ba0157a6c58aae94c9c50c930`
- fixture_sha256: `82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `7c0884fab11b08d46eb01de89abfa2125334493a96c7805f68a7161e9d7bff70`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `dfb1de5ef05668c278fa0bfcea0c360fed3169b7b4bae6483c3fb5fedeccf198`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `7e61bd8eca6431729aee1f3be4656be0a4348119eb1218623bafd54cfaead2ab`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_without_target_release_version` | PASS | With_skill output explicitly returns `blocked` because `target_release_version` is missing. |
| `allows_read_only_diagnostic` | NOT_EXERCISED | The lane stops before repository inspection, so the read-only diagnostic behavior is not exercised. |
| `does_not_persist_report_without_target` | PASS | Output states report writing was not executed; locked git evidence shows no diffs, new commits, or untracked files. |
| `does_not_write_version_stamp` | PASS | Output states version metadata modification was not executed; locked git evidence shows no repository changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=dfb1de5ef05668c278fa0bfcea0c360fed3169b7b4bae6483c3fb5fedeccf198; fixture_sha256=82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb; output_sha256=1a313a4257b1260c77f9ea985c794073d0b9115b581a73bf2418fd605bf481cb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks before audit work when no maintainer-confirmed target release version exists, with no persisted changes.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=dfb1de5ef05668c278fa0bfcea0c360fed3169b7b4bae6483c3fb5fedeccf198; fixture_sha256=82b55bed70c9cef729375a3351448011b6841c9c9416854e0ef1fd304e6c48bb; output_sha256=4b5d5e798d309695e568cf0dd7d4312689335da0bc78d2a19891b40bc9a1bc57; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Performs a read-only diagnostic and reports no confirmed regression, but does not block on the missing target release version.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain maintainer confirmation of the exact target_release_version before continuing the audit.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
