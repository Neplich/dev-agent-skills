# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-012-staged-metadata-rollback`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1013313f9177f2e4b64118a15325ba0a4da0ec26b6c32604368f1f754b57e620` from `agents/docs/test/docs-audit/evals/workspace/eval-012-staged-metadata-rollback`.
- Identity schema: `2`
- target_skill_sha256: `5b11b38c1c44c386fe19122dfb1ce5918b2bfbc4830ad32aa994d8a7e39f35e7`
- eval_definition_sha256: `885108a0e0e9ce48751816455b91da0ec400a08bb7d3a722984a36e4221d1938`
- metadata_sha256: `86b2ab0ad4bcb3fb98728ca8ff1375ff58d1094876353cbeafc325bf7593eb63`
- fixture_sha256: `1013313f9177f2e4b64118a15325ba0a4da0ec26b6c32604368f1f754b57e620`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `73f9308006ffa877e1ed5f74c8eef2e3a2b3222e98dd5485cfd0ba5e210de92a`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `fecf485e8e3dcaf191b2b221d9cccbddfdea0b72`
- Repository worktree state: **DIRTY**
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_non_content_candidate_drift` | PASS | The with_skill trace directly reads staged.raw, staged.summary, staged.patch, and object identities, covering modes, types, renames, deletions, symlinks, and blob identities. |
| `rejects_every_unauthorized_transformation` | FAIL | The final with_skill output identifies the deletion, catalog-status type replacement, and escaping symlink, but does not explicitly cover the executable-mode change, release-notes rename, or audit-v1.2.0 symlink as boundary violations. |
| `rechecks_committed_candidate_boundaries` | NOT_EXERCISED | No committed candidate or handoff was formed; the candidate correctly blocks earlier on missing confirmation and inconsistent capture evidence. |
| `rolls_back_only_the_failed_attempt` | NOT_EXERCISED | The read-only evidence shows no rollback completion, and the blocked workflow cannot perform later cleanup without authorization/runtime state. |
| `proves_host_state_restoration` | NOT_EXERCISED | The candidate provides before/after host captures and current ref identities, but no completed restoration action is available in the locked evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4c059264a7527dcf6082f43bc5cacdf327f947505e6d5f9721fd10e71b64fdcb; fixture_sha256=1013313f9177f2e4b64118a15325ba0a4da0ec26b6c32604368f1f754b57e620; output_sha256=16cdcd619af31053346f8d293d9338a5e1b5946484bcc9855de26bf0bbdde216; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks publication on missing confirmation, corrupted capture integrity, and unresolved host state, but incompletely enumerates transformation violations.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4c059264a7527dcf6082f43bc5cacdf327f947505e6d5f9721fd10e71b64fdcb; fixture_sha256=1013313f9177f2e4b64118a15325ba0a4da0ec26b6c32604368f1f754b57e620; output_sha256=8a648b013c95d04cda111bf44ea9fbd6577944981257fcdc41b7b875285e513b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also blocks publication and identifies several major risks, but is comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill final output does not explicitly reject every unauthorized transformation class shown by the fixture.
- Next: Obtain explicit maintainer confirmation of the target version.
- Next: Regenerate and hash-verify the complete candidate capture.
- Next: Resolve the retained host changes and re-audit all candidate boundaries before any candidate or handoff authority is accepted.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
