# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-004-api-adr-owned-by-engineer`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116` from `agents/engineer/test/trd-gen/evals/workspace/eval-004-api-adr-owned-by-engineer`.
- Fixture SHA-256: `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116`
- Prompt SHA-256: `825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `73cec46ef0287c25bd7a41d37b6bcee4e1ea25b1101672fb45bd299ecec77b0d`
- Skill overlay SHA-256: `8f09b52303d9393824dd3e732e656dd74f7ac606a082939547181274986dfb2d`
- Judge schema SHA-256: `2fb0119eb77903cfe9db053e59a3c85f9fb841609febdeb77953e7bac06ea0fe`
- Eval definition SHA-256: `c2e125b845f0cfd23a8b77d0953e79c0dfdb8a47bc09cbe45bf84d70fdf9a2db`
- Metadata SHA-256: `d32be481f3b029c028aa82a9a8adf92bda8ff5084062b1a65511dd3d764980a1`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `engineer_owns_api_and_adr` | FAIL | The Engineer documents contain `generated_by: "trd-gen"`, but neither the locked output nor file content states that API and ADR are owned by `engineer-agent:trd-gen`; the output instead says the main flow completed them because the Engineer document subagent was unavailable. |
| `writes_all_engineer_docs_under_feature_path` | PASS | The delivery snapshot contains TRD.md, API.md, and ADR-001-search-index.md under `docs/engineer/chat-interface/history-search/`. |
| `preserves_related_prd_and_metadata` | PASS | All three Engineer documents contain the required feature_path, parent_feature, feature_level, and related_prd metadata pointing to the PM PRD. |
| `does_not_use_pm_generators` | PASS | The with_skill output and snapshots contain no routing to `api-gen` or `adr-gen`; generation is identified as `trd-gen`. |
| `no_plan_or_code` | PASS | Git evidence shows only untracked Engineer documentation files, with no implementation plan or code changes. The TRD explicitly states this stage does not implement code or create an implementation plan; its testing strategy is documentation, not added tests. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=3387cb020b5b9be1f2f66d7d9986ff3330b00b08e8f6e2fa8586afa284e35982; snapshot_sha256=059d708749478013d2ffddd270bf392ac6a626da8b42e1b596589a69a634be08
- Behavior: Created the requested Engineer TRD, API, and ADR under the correct feature path, preserved metadata and PRD linkage, and avoided implementation changes; however, it did not satisfy the required explicit Engineer-agent ownership statement.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=0084f26d0297f8d5c6904ac679e7c5dba0fc665e3252806fdeeb1a10332b50de; snapshot_sha256=5888f3412bbabee943d80b4f3e8c0f9493df2b994bc343120ed0781e4bfa43c7
- Behavior: Created technical, API, and ADR files under the PM path, providing a fresh baseline that misplaced Engineer artifacts and did not demonstrate the required Engineer ownership routing.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane does not establish the required `engineer-agent:trd-gen` ownership for the API and ADR, and explicitly says the main flow completed the work because the Engineer document subagent was unavailable.
- Next: Route or explicitly identify API and ADR generation as owned by `engineer-agent:trd-gen`.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
