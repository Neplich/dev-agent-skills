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
- target_skill_sha256: `340d804f93e6fcb990681bc077bb9f53d3744da12f12a7cfbbe7aa88f980f67e`
- eval_definition_sha256: `c2e125b845f0cfd23a8b77d0953e79c0dfdb8a47bc09cbe45bf84d70fdf9a2db`
- metadata_sha256: `62246848ad899e2c45f78627f4917a469fe8651f1607857696af955323ef348c`
- fixture_sha256: `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `2fb0119eb77903cfe9db053e59a3c85f9fb841609febdeb77953e7bac06ea0fe`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `efd5278a6dcac3b779ffc2f7bc7fbcdcc73c391218f35b1bba7e6f95759a7887`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `engineer_owns_api_and_adr` | PASS | With-skill delivery snapshots identify `engineer_document_owner: engineer-agent:trd-gen` on TRD, API, and ADR; final output also states Engineer owns the set. |
| `writes_all_engineer_docs_under_feature_path` | PASS | All three locked delivery snapshots are under `docs/engineer/chat-interface/history-search/`: TRD.md, API.md, and ADR-001-database-full-text-search.md. |
| `preserves_related_prd_and_metadata` | PASS | Each locked Engineer document preserves `feature_path`, `parent_feature`, `feature_level`, and `related_prd: docs/pm/chat-interface/history-search/PRD.md` in frontmatter. |
| `does_not_use_pm_generators` | PASS | The locked runner trace shows use of `trd-gen` and contains no `api-gen` or `adr-gen` invocation; the delivered files identify Engineer ownership. |
| `no_plan_or_code` | PASS | The locked delivery contains only the three Engineer documents; git status is `?? docs/engineer/`, with no implementation plan, code, or test files in the delivery snapshot. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=9c8f6951f391aa2e982e1b361d48a908244ae316790450cb09bd7a94e36acbe6; snapshot_sha256=63e3a78278e976457571f1458af9e2fe37bec7e20854c1e34e698b64f2a44512
- Behavior: Produced the requested Engineer-owned TRD, API, and ADR under the resolved feature path, preserving PRD traceability and stopping before implementation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=a749396240dd5176d0c879140afac9a4dde7b8ef4a5ca446aa194c5da7e1fc33; snapshot_sha256=e406f01a32d20dbf6a014b4c15a6a97fe57b1acf2736e68717c48aaa0f5693aa
- Behavior: Produced PM-path technical documents instead of the required Engineer document set; used only as baseline comparison context.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
