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
- Fixture SHA-256: `ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927`
- Prompt SHA-256: `2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `1b3ba014c732559fe2d85e84b85c8db967bb14f4b1fc850a2267e7d4ee1cf03b`
- Skill overlay SHA-256: `7f72b0d2378eefdc164735f00c26c14522753a42e538abe02ba7accda3b0a9f5`
- Judge schema SHA-256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Eval definition SHA-256: `51a5d5a4f671b1df617b81a97fb84c601259cd9a8d3901d74d7d41b70d44d966`
- Metadata SHA-256: `85958a0c5140b007348a2041b6f7a9c97d73f65f93f4fafa12ba3e42d03d7a13`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Raw trace item_5 reads change-map.yaml and then session.md before bounded path checks; no full-repository document traversal is shown. |
| `verifies_against_code` | PASS | Raw trace item_8 reads src/session/config.txt; the checkpoint records 30 minutes versus the documented 60-minute conflict and blocks implementation pending alignment. |
| `treats_unverified_as_low_trust` | PASS | The with_skill checkpoint explicitly records last_verified_version: unverified, identifies the conflict, and requires code/config evidence before implementation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a; fixture_sha256=ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927; output_sha256=1349af384570da92ace4f62f2d71e1f0aea1986157526df979dc7c8956b0b013; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Mapped documentation was consulted, code evidence verified the timeout discrepancy, and implementation was correctly blocked pending product and technical alignment.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a; fixture_sha256=ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927; output_sha256=e096a69b2d9eea3c476a33d2578608a406c1cf4fcd04e900c11a6aefcd5b9a15; snapshot_sha256=0aa641297d6ff89143a5989d86c7280f6ef5ce59e09086e6a5533403a4eef718
- Behavior: Implemented the change and tests, but did not demonstrate the required mapped-document-first and low-trust verification workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
