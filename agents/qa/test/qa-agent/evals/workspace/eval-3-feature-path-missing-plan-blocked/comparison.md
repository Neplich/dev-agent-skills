# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-003-feature-path-missing-plan-blocked`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc` from `agents/qa/test/qa-agent/evals/workspace/eval-3-feature-path-missing-plan-blocked`.
- Fixture SHA-256: `39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc`
- Prompt SHA-256: `094ec5b09f42125c7ea3b42f7f8365ddf4bd40bef6652060cfeb7ff368908608`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `23a4457fc9bf10be6976d98ea55607b47c6c623db1e20d5c73160d9f386c2a36`
- Skill overlay SHA-256: `5754523ab6dc67a27703c13629b577962774677f13b55627e2b1a056ffc0bc71`
- Judge schema SHA-256: `7c827cee8609863280607c031efdc95a92d32b851664d68126eccd9d66c1f27a`
- Eval definition SHA-256: `ffa490cd1f58367914b109adc50e94706c92cbf66e7c95942ae329d3f9a191c7`
- Metadata SHA-256: `aa798ca118679678c2fef882d4726badd357a387202dcb387aceaa4b86696bd0`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_same_feature_path` | PASS | Trace directly shows reads of docs/pm/account/profile/preferences/PRD.md, docs/engineer/account/profile/preferences/TRD.md, and the same-path QA TEST_SUITE.md/FLOW_INDEX.md; output sets feature_path to account/profile/preferences, and git evidence shows no QA-tree mutation. |
| `specialist_gate_pointer` | PASS | Output selects spec-based-tester as execution_owner, identifies the missing same-path IMPLEMENTATION_PLAN.md gate, states execution cannot proceed, and says the router will not create cases, reports, or execute E2E. |
| `keeps_single_route` | PASS | Output names exactly one narrow route, spec-based-tester; trace shows no specialist execution or implementation changes, and git status/diff are empty. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=094ec5b09f42125c7ea3b42f7f8365ddf4bd40bef6652060cfeb7ff368908608; fixture_sha256=39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc; output_sha256=06f9f4af97f02368c19f8973eb8d596e2b83732f604d6656ceb402b2e7460ef7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routed the request to spec-based-tester, preserved the same feature path, enforced the implementation-plan gate, and stopped before specialist execution or asset mutation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=094ec5b09f42125c7ea3b42f7f8365ddf4bd40bef6652060cfeb7ff368908608; fixture_sha256=39ecc1af9722a7aadd83ae04a9403edca1017d45bde6a98a57d2d87ccb7702dc; output_sha256=444ffd214d2a441168ca23f1a78935f48b823493fe0c6aa08eef863ab5fb0c4d; snapshot_sha256=fb6494026fd90bf01ffd204ca76948cecfc2d4d60758403e4a300ee582f68fa9
- Behavior: Fresh baseline edited QA assets and performed execution probing without the specialist gate or single-route handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
