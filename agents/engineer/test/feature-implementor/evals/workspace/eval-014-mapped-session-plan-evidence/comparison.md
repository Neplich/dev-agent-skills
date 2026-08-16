# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-014-mapped-session-plan-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927` from `agents/engineer/test/feature-implementor/evals/workspace/eval-014-mapped-session-plan-evidence`.
- Identity schema: `2`
- target_skill_sha256: `248d30c2e10162217ecb1d6a0d7c66973ee945c6f2e9b7e4bf01a677aac7bc3c`
- eval_definition_sha256: `51a5d5a4f671b1df617b81a97fb84c601259cd9a8d3901d74d7d41b70d44d966`
- metadata_sha256: `8f8181a8b5f8f92c423cfb8a15a35438fa3fefe0e74f7a7daf711ceaa3d79ccb`
- fixture_sha256: `ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `8002de5f5ec8cbba9c876b3fa5b95d04da373914039535f254ff8fce02f9cbab`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Trace shows `change-map.yaml` was read first, then the mapped `docs/site/api/session.md`; no unrelated document contents were traversed. |
| `verifies_against_code` | PASS | The candidate verified `src/session/config.txt` as 30 minutes with renewal disabled, contrasted it with the document's 60 minutes, and included the discrepancy and impact in the planning gap packet. |
| `treats_unverified_as_low_trust` | PASS | The candidate explicitly treated `last_verified_version: unverified` as low trust and based the timeout and implementation-scope conclusions on source/config evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a; fixture_sha256=ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927; output_sha256=e34e01d9cb86cf8020dedce15ab12cf91951e1a8a6f6f6d95f3e032f0de79d2c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly verified the mapped documentation and source configuration, identified the 30/60-minute conflict, treated the document as unverified, and paused implementation pending required PM/TRD alignment.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a; fixture_sha256=ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927; output_sha256=b12bd76f3312f3a20a7e432de5f5cd01f5edb20240a7406560863e64ddfe6553; snapshot_sha256=c55217dec081c363b8be6868094f3dbf54bd0d1ce7d2182dbf54d3e4ec828a40
- Behavior: Implemented renewal configuration and rewrote the documentation without demonstrating the required mapped-document-first workflow or low-trust handling.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
