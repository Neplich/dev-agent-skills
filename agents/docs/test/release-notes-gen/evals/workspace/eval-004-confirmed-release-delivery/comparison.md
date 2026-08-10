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
- Fixture SHA-256: `c11c4570536758cb911b613643632dd7b15e8b492fb6a5c6cb788342176462bf`
- Prompt SHA-256: `5d2eb8fee66e709ed28ba5aa53ac1e57295ed25d74500a43d924b8fbc434431e`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c8459f189e8d92d91e1c7ede8875090bfc1c2e1e04b8f18983b4339e6b65ba34`
- Skill overlay SHA-256: `c7d3b6793c943fb4d4971cf0d6f11988326a2dff978353bf3c4327d4e24c17b7`
- Judge schema SHA-256: `5f19f02b941db43659fbfb03cc28f127d2b4bbc556ed59290b7811c966f30dc8`
- Eval definition SHA-256: `6ba71c78dee7f69b879178b4307965fc8b664b773fca948482dc1711c289b5ad`
- Metadata SHA-256: `2e15aaf06f83170c681a449f442bd9946bbef263dbea552644182da638b4addc`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `delivers_confirmed_release_page` | PASS | Locked with_skill delivery_snapshot contains docs/site/release-notes/v1.0.0.md with valid release frontmatter, last_verified_version: unverified, and sections covering all six evidence categories plus both manifests. |
| `updates_derived_surfaces_after_confirmation` | PASS | Locked file_change and snapshots show only the confirmed page, index, and metadata changed; metadata preserves the host-owned field and existing version. Trace reads confirmation-record.md before the write event. |
| `passes_host_docs_checks` | PASS | Locked trace shows npm run test:docs executed in docs/site with exit_code 0; output reports frontmatter, affected-document, version, and 75 tests passing. |
| `returns_complete_ready_handoff` | PASS | With_skill output provides confirmed version and source, page path, confirmation status, docs check and cwd, updated surfaces, evidence mappings, blockers, downstream_target, and release_execution_authorized: false. |
| `preserves_external_release_boundary` | PASS | Git evidence shows no commit, branch, ref, or reflog changes; output states no tag, GitHub Release, image publication, or deployment; delivered page and index retain last_verified_version: unverified. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5d2eb8fee66e709ed28ba5aa53ac1e57295ed25d74500a43d924b8fbc434431e; fixture_sha256=c11c4570536758cb911b613643632dd7b15e8b492fb6a5c6cb788342176462bf; output_sha256=1e7db0ad20df673a407e6f07b7067c98cf46319076f523e159cd3cc2d40b6a64; snapshot_sha256=7a79722e025c4360b9708983f05c318933456ed97b50319fd31d1f3db1db0a46
- Behavior: Completed a confirmed, evidence-complete Release Notes delivery with passing host checks and an explicit pre-tag handoff boundary.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5d2eb8fee66e709ed28ba5aa53ac1e57295ed25d74500a43d924b8fbc434431e; fixture_sha256=c11c4570536758cb911b613643632dd7b15e8b492fb6a5c6cb788342176462bf; output_sha256=6a75688d01732cf0e4f4840f77011b2d7e30d6fa5cdc2a1f839eed28009a8f2b; snapshot_sha256=555810091bdffcf6eba64abadbb7afc0d603f93e1714eea6f7699f5c071976e6
- Behavior: Completed the page and index but incorrectly added the new version to verifiedDocs and provided a less complete boundary-aware handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
