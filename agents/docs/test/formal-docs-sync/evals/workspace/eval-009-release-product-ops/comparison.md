# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-009-release-product-ops`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `88db6a4117456e7d2f0e14115ea2a173ee0022fedba47576986e4b24262edb75` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-009-release-product-ops`.
- Fixture SHA-256: `88db6a4117456e7d2f0e14115ea2a173ee0022fedba47576986e4b24262edb75`
- Prompt SHA-256: `8feaf10d86a83aace4d8ae6456c2cfec394b2d1dd27b83a16d97b82d9a82c1f2`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f24bfeb12dba77a74fcf3f0161749ae4671b83762eac08484e7ae08621d9bacb`
- Skill overlay SHA-256: `5dbb8d8559bfab3926047aa028e19f362490751247c2142101cfd687fff5239e`
- Judge schema SHA-256: `56b98af2f6fc5a04535db999157836236eb69830528cbecc99ca00f23b4d8d9e`
- Eval definition SHA-256: `c9bcafbf3ecc8c0e0ac28908b463b075e9d1371a95444953a8afc3d41757e192`
- Metadata SHA-256: `d04b92e9a3754ad51ae5d707b3601a2084dc53a6e309122269ca881bc88a10ef`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `limits_release_to_affected_product_ops` | PASS | Locked delivery snapshot and git evidence show only the product and ops pages changed; matched change-map entries were retained and no unrelated surfaces changed. |
| `reconciles_confirmed_version_facts` | PASS | Delivered pages use limit 25 and image v1.5.0, consistent with implementation, configuration, and release evidence; no v1.5.1 claim was delivered. |
| `preserves_release_notes_surfaces` | PASS | Locked git status and delivery snapshot contain no Release Notes or navigation changes; the candidate explicitly excludes Release Notes surfaces. |
| `keeps_release_pages_unverified` | PASS | Both locked delivered pages contain last_verified_version: unverified. |
| `runs_release_host_checks_and_handoffs` | NOT_EXERCISED | Raw runner events prove npm run test:docs, npm run build:public, and npm run build:internal completed with exit code 0. The claimed docs-agent handoff has no independent non-message evidence, so that later handoff step is not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8feaf10d86a83aace4d8ae6456c2cfec394b2d1dd27b83a16d97b82d9a82c1f2; fixture_sha256=88db6a4117456e7d2f0e14115ea2a173ee0022fedba47576986e4b24262edb75; output_sha256=31705dcc3acf777d79139c922dda97fca152cb41ce0c4d3964a3432812635b9b; snapshot_sha256=ad81ceea56071110b83ee018d1f98126a9537df65193ae832823e1b547685f8d
- Behavior: Correctly limited the release, reconciled v1.5.0 facts, preserved Release Notes surfaces, kept both pages unverified, and passed the documented host checks; the handoff itself is not independently evidenced.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8feaf10d86a83aace4d8ae6456c2cfec394b2d1dd27b83a16d97b82d9a82c1f2; fixture_sha256=88db6a4117456e7d2f0e14115ea2a173ee0022fedba47576986e4b24262edb75; output_sha256=9be7bfd0a8a8bf2356f10842ef538d4a96f39087815971962c67baa6c52b47fd; snapshot_sha256=3abe89046ac74a47ae7626bbfb612a0d7d1d80febf3ec1e4dd8baaadb0176c3a
- Behavior: Fresh baseline updated the two pages and facts but stamped both pages v1.5.0 instead of leaving them unverified; it is comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Complete or independently record the docs-agent:docs-audit pre-tag handoff with the two-page affected set, confirmed v1.5.0 source, and supporting evidence.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
