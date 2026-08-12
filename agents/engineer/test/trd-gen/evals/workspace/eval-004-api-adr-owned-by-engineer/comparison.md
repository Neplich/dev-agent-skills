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
- Identity schema: `2`
- target_skill_sha256: `7350d982beaf3dbc1ec747d4598f05c9a1dfb9b1eb61dcb04ae43dfd72f6fcfd`
- eval_definition_sha256: `c2e125b845f0cfd23a8b77d0953e79c0dfdb8a47bc09cbe45bf84d70fdf9a2db`
- metadata_sha256: `d32be481f3b029c028aa82a9a8adf92bda8ff5084062b1a65511dd3d764980a1`
- fixture_sha256: `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `2fb0119eb77903cfe9db053e59a3c85f9fb841609febdeb77953e7bac06ea0fe`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b`
- Repository HEAD: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `41df440b7248e793c6d9703098fb03264d5ab1871ee7f72726859596ddf5327e`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `engineer_owns_api_and_adr` | PASS | With-skill output and all three locked Engineer document frontmatters identify `engineer_document_owner: engineer-agent:trd-gen`. |
| `writes_all_engineer_docs_under_feature_path` | PASS | Locked delivery snapshots contain TRD.md, API.md, and ADR-001-postgresql-full-text-search.md under `docs/engineer/chat-interface/history-search/`. |
| `preserves_related_prd_and_metadata` | PASS | All three locked Engineer documents contain the required feature metadata and `related_prd: docs/pm/chat-interface/history-search/PRD.md`. |
| `does_not_use_pm_generators` | PASS | The with-skill delivery routes artifacts to Engineer paths and locked trace/git evidence shows no PM `api-gen` or `adr-gen` routing. |
| `no_plan_or_code` | PASS | Locked git evidence shows only Engineer documentation files were added; no implementation plan, code, or test changes are present. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=9516bd1445d513c044b474094abcd8acbe9fcc1bb4d13a800093d36ef8b799de; snapshot_sha256=a6230bd6e5be52ee8d7f62c2b0e5888680d1601033b7feee021a54f567bdb1f4
- Behavior: Produced the requested Engineer-owned TRD, API, and ADR under the mirrored feature path, with required metadata and no implementation work.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=6959ad788bf4db0085b551ffdc7428be5ff6a9418067cad5379cb2fd5d3fbf33; snapshot_sha256=b6e7cacb16a2cc4adc26ee3b207fd5ed047e0a1ab50668e1027ef09af39af529
- Behavior: Produced technically detailed documents under the PM path, demonstrating the fresh baseline's ownership and path failures.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
