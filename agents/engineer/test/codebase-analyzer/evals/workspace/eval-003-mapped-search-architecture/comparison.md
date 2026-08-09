# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `codebase-analyzer`
- Eval: `eval-003-mapped-search-architecture`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a3ef5b9cc00c15c74b103c208a46d73ff5b53e17721ec0a79184a10c02b16859` from `agents/engineer/test/codebase-analyzer/evals/workspace/eval-003-mapped-search-architecture`.
- Fixture SHA-256: `a3ef5b9cc00c15c74b103c208a46d73ff5b53e17721ec0a79184a10c02b16859`
- Prompt SHA-256: `0f34452462bbb10e7f7328b054a3e1b0e6f741b40ba12100a356dcedfa512f9c`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `de6d27a82a6affa1d54b83f57c4eb1889c4977944cd8849112c1a97798fbfd77`
- Skill overlay SHA-256: `be427177bb8618969a8c9c2b0aea6596dceb0dbc6a57e3c3bb5e1896d11ef1ed`
- Judge schema SHA-256: `953cf0ea99b9840a17c7b6706052165ac0b5ad2da8cf5b30696958f911637de4`
- Eval definition SHA-256: `df0ea3b9e16f84cfa3123784feaff62e9978d327069fdb7ff40819c75c9ebde1`
- Metadata SHA-256: `c79f8b60b8eda49d60383374b0b105b8c506dcb4b757a67593ed9721a0d169df`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_change_map_to_bound_context` | PASS | With-skill output explicitly scopes the task to `src/search/**`, identifies the change map, and names `docs/site/api/search.md` as required documentation. |
| `verifies_claims_against_code` | PASS | With-skill output cites and quotes `src/search/query.txt`, using `entrypoint: search` and `match_mode: exact` to establish the code-backed behavior. |
| `reports_document_code_conflict` | PASS | With-skill output clearly contrasts the documentation's fuzzy-matching claim with the code's exact mode and explains that the conflict affects the current baseline and follow-up evaluation. |
| `does_not_overclaim_unverified_docs` | PASS | With-skill output identifies `last_verified_version` as `unverified`, lowers document confidence, and declines to treat fuzzy matching as implemented without code evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0f34452462bbb10e7f7328b054a3e1b0e6f741b40ba12100a356dcedfa512f9c; fixture_sha256=a3ef5b9cc00c15c74b103c208a46d73ff5b53e17721ec0a79184a10c02b16859; output_sha256=9e7e78d1a199fe2bed13261e157f3b88452f82f233a6376ca64e114dc3886c5d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Core search-module analysis is accurate and satisfies all four assertions, but the appended project profile includes a false PM-document inventory claim.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0f34452462bbb10e7f7328b054a3e1b0e6f741b40ba12100a356dcedfa512f9c; fixture_sha256=a3ef5b9cc00c15c74b103c208a46d73ff5b53e17721ec0a79184a10c02b16859; output_sha256=360840071da88fe2b2fbe3ddb7695e6bf26eade8b824ac0af30b8dcc46e3c35a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline independently provides the core exact-mode analysis and document conflict, but lacks the structured change-map/evidence handoff detail of the with-skill output.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill output contains an unsupported and contradictory project-profile claim: `has_pm_docs: false`, despite the fixture containing `PM_HANDOFF.md` and the analysis relying on it.
- Next: Remove or correct the contradictory `has_pm_docs` project-profile field before accepting the with-skill delivery.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
