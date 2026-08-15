# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-004-confirmed-release-delivery`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c11c4570536758cb911b613643632dd7b15e8b492fb6a5c6cb788342176462bf` from `agents/docs/test/release-notes-gen/evals/workspace/eval-004-confirmed-release-delivery`.
- Identity schema: `2`
- target_skill_sha256: `9d15471128b5c653c03406ba512b69c7510ab64bfd6b1cba8b6458bff7449a16`
- eval_definition_sha256: `6ba71c78dee7f69b879178b4307965fc8b664b773fca948482dc1711c289b5ad`
- metadata_sha256: `2e15aaf06f83170c681a449f442bd9946bbef263dbea552644182da638b4addc`
- fixture_sha256: `c11c4570536758cb911b613643632dd7b15e8b492fb6a5c6cb788342176462bf`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `5f19f02b941db43659fbfb03cc28f127d2b4bbc556ed59290b7811c966f30dc8`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `5d2eb8fee66e709ed28ba5aa53ac1e57295ed25d74500a43d924b8fbc434431e`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `875d94bbeede7fb3f25ae54a8099f5bb996a939530b57c2c2295a2fa54bd46e9`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `delivers_confirmed_release_page` | PASS | with_skill delivery_snapshot contains docs/site/release-notes/v1.0.0.md with valid release frontmatter, last_verified_version: unverified, and all six required evidence categories. |
| `updates_derived_surfaces_after_confirmation` | PASS | with_skill trace completes confirmation review before the file-change event; snapshots show one new v1.0.0 index entry, preserved v0.9.0, preserved manualNote/verifiedDocs, and generated navigation. No source navigation was modified. |
| `passes_host_docs_checks` | PASS | with_skill runner trace shows cd docs/site && npm run test:docs exiting 0, with 75 tests passed and all checks passed. |
| `returns_complete_ready_handoff` | PASS | with_skill output provides the confirmed version and sources, page path, confirmation status, docs checks and results, updated surfaces, six evidence sources, blockers, downstream_target, and release_execution_authorized: false. |
| `preserves_external_release_boundary` | PASS | with_skill git_evidence shows unchanged HEAD, branch, refs, commits, and reflog; delivery content keeps last_verified_version: unverified and explicitly preserves the external release boundary. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5d2eb8fee66e709ed28ba5aa53ac1e57295ed25d74500a43d924b8fbc434431e; fixture_sha256=c11c4570536758cb911b613643632dd7b15e8b492fb6a5c6cb788342176462bf; output_sha256=4a7a6da99141cce4d415282b2478d616101e8ba7a4e2d2a69a747c16f1b10a05; snapshot_sha256=f6ba9c0dfa973add46ba44ba728c568df03668ad2cc54e7e5b55a8fe4114293e
- Behavior: Completed the confirmed v1.0.0 site Release Notes delivery, passed host checks, and returned a complete pre-tag handoff while preserving the release boundary.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5d2eb8fee66e709ed28ba5aa53ac1e57295ed25d74500a43d924b8fbc434431e; fixture_sha256=c11c4570536758cb911b613643632dd7b15e8b492fb6a5c6cb788342176462bf; output_sha256=3f7681bf19a89c7cbb8dcd286fce7eba53a31e4f4b43c7647d45ac3c89ce5bac; snapshot_sha256=73277accd98616b361575bcb0c25576ecf715f9bf2c56e12415f404a44b0d16f
- Behavior: Created the page and some derived surfaces but duplicated the existing v0.9.0 index entry, lacked the structured ready handoff, and its initial docs-check invocation used the wrong working directory.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
