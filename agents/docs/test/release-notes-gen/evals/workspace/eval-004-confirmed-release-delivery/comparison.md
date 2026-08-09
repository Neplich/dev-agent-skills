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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b7f7292c266a0e83e45fc11a264c0b52188a05a92b94c912c4a7b6c5c35058d2`
- Skill overlay SHA-256: `fcc8b19cc83a08b5f5e64f8b15695aa80b045962a63cbf1717889ea116dc31cc`
- Judge schema SHA-256: `5f19f02b941db43659fbfb03cc28f127d2b4bbc556ed59290b7811c966f30dc8`
- Eval definition SHA-256: `6ba71c78dee7f69b879178b4307965fc8b664b773fca948482dc1711c289b5ad`
- Metadata SHA-256: `2e15aaf06f83170c681a449f442bd9946bbef263dbea552644182da638b4addc`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `delivers_confirmed_release_page` | PASS | Locked delivery_snapshot contains docs/site/release-notes/v1.0.0.md with valid release frontmatter, last_verified_version: unverified, and six sections covering user features, architecture, database, deployment/configuration, delivery assets, and upgrade risks. |
| `updates_derived_surfaces_after_confirmation` | NOT_EXERCISED | The final snapshot shows the confirmed version added to the index and metadata while preserving v0.9.0, verifiedDocs, manualNote, and last_verified_version: unverified; however, the locked evidence does not prove the required pre-confirmation state or update ordering. |
| `passes_host_docs_checks` | PASS | The with_skill output reports npm run test:docs from docs/site passed with 75 tests, matching the host package script, and also reports git diff --check passed. |
| `returns_complete_ready_handoff` | FAIL | The handoff includes target version and confirmation source, page path, confirmation status, docs check command/result, updated surfaces, blockers, ready status, and release_execution_authorized: false, but it omits the required downstream_target field and an explicit evidence field. |
| `preserves_external_release_boundary` | PASS | git_evidence shows no commit, ref, branch, reflog, or reachable-commit changes; the snapshot retains unverified status; and the output explicitly states no tag, GitHub Release, image publication, or deployment occurred. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5d2eb8fee66e709ed28ba5aa53ac1e57295ed25d74500a43d924b8fbc434431e; fixture_sha256=c11c4570536758cb911b613643632dd7b15e8b492fb6a5c6cb788342176462bf; output_sha256=fe58b2deb331ba624fb2d96d9b2ad63da87d5a35bd818a5a566c3cd7da5b34ed; snapshot_sha256=67f2128475ba256217bf4774cd6875f0ff3764ce205391d2e8196224bcd15356
- Behavior: Delivered a complete confirmed v1.0.0 release page, updated the appropriate derived surfaces, reported host checks, and preserved the external-release boundary, but returned an incomplete ready handoff and lacks proof of pre-confirmation update ordering.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5d2eb8fee66e709ed28ba5aa53ac1e57295ed25d74500a43d924b8fbc434431e; fixture_sha256=c11c4570536758cb911b613643632dd7b15e8b492fb6a5c6cb788342176462bf; output_sha256=216a692cfae1e40797d2953b7ea8129b733706066e296c002c7a7c765e5bd36f; snapshot_sha256=8bc8a894d2eb6f23db1a0738c130e84da5a928ac437f1fb7c51594ec3e2bccdd
- Behavior: Produced a comparable page and surface updates and reported successful documentation work, but provided less structured handoff information and no explicit ready handoff boundary.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill handoff is incomplete because it does not provide the required downstream_target and explicit evidence fields.
- Next: Add explicit downstream_target and evidence fields to the pre-tag handoff.
- Next: Provide raw evidence of the pre-confirmation surfaces and confirmation-before-update ordering.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
