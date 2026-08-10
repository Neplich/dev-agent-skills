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
- Fixture SHA-256: `dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2`
- Prompt SHA-256: `8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5b5823d2c0804ce3dabb1d32490f71697f4ff111cd9371ebf92d1bb1b6ad2188`
- Skill overlay SHA-256: `c7033e85898ff61111eb14edc47b25e717119ee79349d7af461390afc706db78`
- Judge schema SHA-256: `218cecf9b4e5893cf80d7edfea7d7877463de8efad846bf62ba5cba015ad2ed5`
- Eval definition SHA-256: `fee749f35b3bf7110eb1c6f38c918db3407b1a46ffa3ff2613c15b835398219e`
- Metadata SHA-256: `23ce240f3f391bd560df8f9bbcf6e5d2ec76b8a3ffb73e38f416b3cdb2997a3a`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `includes_mapped_page` | PASS | The locked audit report identifies the `src/catalog/**` change-map entry and names `docs/site/api/catalog.md` as the affected formal page. |
| `classifies_direct_conflict_mismatch` | PASS | The report preserves the document’s `POST /catalog/items` claim, the target code’s `GET /catalog/items` fact, the relevant blob/path evidence, and records final status `mismatch`. |
| `blocks_with_conflict_evidence` | PASS | The delivered report records `phase_result: blocked`, documents the method conflict and required remediation, and states the result is not `ready_for_tag`. |
| `does_not_stamp_blocked_set` | PASS | The report explicitly states that no pages were stamped and no release metadata was created or modified; Git evidence shows only the audit report commit and a clean worktree. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1; fixture_sha256=dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2; output_sha256=83672e87fbf93b4397bcedc682ea4f0c2ae92acf226e82934ba747bde4a07b17; snapshot_sha256=2bb593ba6c5c7ee1668b96c62a7acb60d193753aaea6c64677aad963246eee1e
- Behavior: Produced and committed a bounded pre-tag audit with deterministic impact mapping, direct mismatch evidence, blocked status, remediation items, and no stamp or release-metadata mutation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1; fixture_sha256=dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2; output_sha256=801b3309586413ddf8a389cb7aa2280e7498f944621ab4c6fb3934580043f352; snapshot_sha256=a6f8b0d1f2b2ce0151a8f5f72a64374fe6fa213a1157674641f1872bd4c68d92
- Behavior: Produced an untracked audit report identifying the POST/GET conflict and stale version markers, but with less complete protocol coverage and no committed fixed-path audit record.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
