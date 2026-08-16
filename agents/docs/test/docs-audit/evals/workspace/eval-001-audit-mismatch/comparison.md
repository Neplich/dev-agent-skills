# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-001-audit-mismatch`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2` from `agents/docs/test/docs-audit/evals/workspace/eval-001-audit-mismatch`.
- Identity schema: `2`
- target_skill_sha256: `dafd53371901dfd724f88c70262b157e59494d29da1c613d0ef130564b6ff4f9`
- eval_definition_sha256: `fee749f35b3bf7110eb1c6f38c918db3407b1a46ffa3ff2613c15b835398219e`
- metadata_sha256: `23ce240f3f391bd560df8f9bbcf6e5d2ec76b8a3ffb73e38f416b3cdb2997a3a`
- fixture_sha256: `dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `218cecf9b4e5893cf80d7edfea7d7877463de8efad846bf62ba5cba015ad2ed5`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `7e61bd8eca6431729aee1f3be4656be0a4348119eb1218623bafd54cfaead2ab`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `includes_mapped_page` | PASS | With-skill output explicitly maps src/catalog/** to docs/site/api/catalog.md. |
| `classifies_direct_conflict_mismatch` | PASS | It preserves POST versus GET, cites the affected files, and classifies the page as mismatch. |
| `blocks_with_conflict_evidence` | FAIL | It returns blocked, lists the conflict, and rejects ready_for_tag, but does not present the required explicit choice to repair documentation or code. |
| `does_not_stamp_blocked_set` | PASS | Locked git evidence shows no page or metadata mutation; no delivery snapshot or diff records any stamp. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1; fixture_sha256=dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2; output_sha256=196ddce7f8bba1f32a1b568ae7ec773b89d96f58bc33ff65eefc0c493105aaab; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies the mapped page and direct POST/GET mismatch, blocks the audit, and leaves the worktree unchanged; its next steps prescribe documentation repair without requesting the required repair-choice confirmation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1; fixture_sha256=dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2; output_sha256=f9545f6ba56595c5d8ec4e99aec23d385624089c53eba2ce32f8816d4b802847; snapshot_sha256=d9d94c6e55b7b1893e234c126b95da4e8fd3435a972c636eb46b7ddd32ca0a05
- Behavior: Fresh baseline reports the stale POST documentation and metadata but omits the mapped impact classification, mismatch label, blocked phase, and no-stamp behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- blocks_with_conflict_evidence: the with_skill lane does not explicitly frame repair-documentation-versus-repair-code as a confirmation decision.
- Next: Require the audit result to explicitly ask the maintainer to confirm whether the documentation or code should be repaired before rerunning.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
