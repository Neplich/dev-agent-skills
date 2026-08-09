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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a0fd1ad6b8713d6036307d1b20788b4771cc4b6ba53645fe17625e0dd55bbb5b`
- Skill overlay SHA-256: `73e88fe8c07f988c3353f81f9b058d4f8350c48ee381f924fe8c8201b9f92bb4`
- Judge schema SHA-256: `56b98af2f6fc5a04535db999157836236eb69830528cbecc99ca00f23b4d8d9e`
- Eval definition SHA-256: `c9bcafbf3ecc8c0e0ac28908b463b075e9d1371a95444953a8afc3d41757e192`
- Metadata SHA-256: `d04b92e9a3754ad51ae5d707b3601a2084dc53a6e309122269ca881bc88a10ef`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `limits_release_to_affected_product_ops` | PASS | Locked delivery and git diff contain only the product and ops pages; the existing two change-map entries are unchanged, with API/database/design and unrelated pages excluded. |
| `reconciles_confirmed_version_facts` | PASS | Delivered pages contain limit 25 and image registry.example/ai-hub:v1.5.0, matching release evidence, code, configuration, and tests; no v1.5.1 facts are added. |
| `preserves_release_notes_surfaces` | PASS | Release Notes files, metadata, and navigation are unchanged in the locked manifest/diff, and the output excludes those surfaces. |
| `keeps_release_pages_unverified` | PASS | Both locked delivery_snapshot files explicitly retain last_verified_version: unverified and state that audit handoff remains required. |
| `runs_release_host_checks_and_handoffs` | NOT_EXERCISED | The candidate output reports the required command, cwd, exit status, and audit handoff, but locked raw evidence does not independently prove that the host checks actually ran or that the handoff entered pre-tag. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8feaf10d86a83aace4d8ae6456c2cfec394b2d1dd27b83a16d97b82d9a82c1f2; fixture_sha256=88db6a4117456e7d2f0e14115ea2a173ee0022fedba47576986e4b24262edb75; output_sha256=258f233ca5fea28f4143441b4fdd7f5b3674649810f1752d90618d8fa8fb9b34; snapshot_sha256=232b1471b892843d912fbf68c6e8ecb90673b6973a07a04af8d8e3221510b24a
- Behavior: Correctly limits the delivery, reconciles confirmed v1.5.0 facts, preserves Release Notes surfaces, and keeps pages unverified; reported host checks and audit handoff cannot be independently verified from raw evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8feaf10d86a83aace4d8ae6456c2cfec394b2d1dd27b83a16d97b82d9a82c1f2; fixture_sha256=88db6a4117456e7d2f0e14115ea2a173ee0022fedba47576986e4b24262edb75; output_sha256=9e0a178297f44568371063cfe7a340012dbc4586589535c7c5d024aed3d39860; snapshot_sha256=3abe89046ac74a47ae7626bbfb612a0d7d1d80febf3ec1e4dd8baaadb0176c3a
- Behavior: Updated the two affected pages and confirmed v1.5.0 facts, but incorrectly stamped both pages v1.5.0 and did not provide the structured audit handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Independently capture or verify the docs/site host-check execution and pre-tag audit handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
