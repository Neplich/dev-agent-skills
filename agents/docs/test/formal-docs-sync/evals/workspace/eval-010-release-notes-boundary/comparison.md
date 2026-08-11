# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-010-release-notes-boundary`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-010-release-notes-boundary`.
- Fixture SHA-256: `f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c`
- Prompt SHA-256: `59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f`
- Repository HEAD: `f2aa9b2c49be68550ec45538c221425607f428ce`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `dd975083d3977d90b71b3396dff2498ef2b7e8d49c50fab50b5462a26f3248ee`
- Skill overlay SHA-256: `9667198915198da0404e03a7d4c962d38742b19c5de4de5f0cf1473f02db2bf1`
- Judge schema SHA-256: `b3a1a852c447e6e1ef51ed958da793390c6914ade2f68188c4962daac377d01b`
- Eval definition SHA-256: `73a1610671f9f97761837a796f3ae7908687bbe25fc17ad4582a0bb4ee5c7fae`
- Metadata SHA-256: `2352ae604513521c63a446b6d886e6c879f4a0cef5861b4ee1c9c3ee9f319eba`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `recognizes_release_communication_outcome` | PASS | With-skill output identifies the request as a release-notes workflow in release mode, explicitly excluding Product and Ops current-state synchronization. |
| `routes_complete_entry_to_site_owner` | PASS | The routing block preserves the confirmed repository, v1.5.0, scope, abc1500 evidence, zero-write boundary, and all three target site surfaces, routing them to release-notes-gen. |
| `keeps_entire_site_zero_diff` | PASS | With-skill delivery_snapshot is empty; git status and diff are empty, and the output states the workspace is unmodified. |
| `preserves_external_release_boundary` | PASS | With-skill git evidence shows no ref, commit, branch, or external-release changes, and the output contains no external release execution or authorization. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c; output_sha256=23cdc5d963375a085c4a8ed48959a2900bf1bfda48a157c6b51562a737320e5f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classifies and routes the confirmed release-notes request while preserving a zero-write boundary and excluding external release actions.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c; output_sha256=9a6d17804689dc6ecb467d444e4828cebafa987675c59066b92e8208c1003420; snapshot_sha256=27c15e218ea9207b3c693b4e115c21d2889e001d9f2fe2a7376606a415ee73d9
- Behavior: Fresh baseline directly modified the three site release-note surfaces and reported completion, providing contrast with the guarded routing behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
