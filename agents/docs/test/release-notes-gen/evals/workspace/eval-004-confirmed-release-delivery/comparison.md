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
- target_skill_sha256: `3da1a9a1466d6ecd43ed5c082adf803d01b5c2ca25dfee7a882fcc8113f7ce5c`
- eval_definition_sha256: `6ba71c78dee7f69b879178b4307965fc8b664b773fca948482dc1711c289b5ad`
- metadata_sha256: `2e15aaf06f83170c681a449f442bd9946bbef263dbea552644182da638b4addc`
- fixture_sha256: `c11c4570536758cb911b613643632dd7b15e8b492fb6a5c6cb788342176462bf`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `5f19f02b941db43659fbfb03cc28f127d2b4bbc556ed59290b7811c966f30dc8`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `5d2eb8fee66e709ed28ba5aa53ac1e57295ed25d74500a43d924b8fbc434431e`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `9d7abf20333b60efc8aeaad2d302ecd422e44bb547e52f5a4d9623347a2b048b`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `delivers_confirmed_release_page` | PASS | delivery_snapshot contains the v1.0.0 page with valid release frontmatter, last_verified_version: unverified, and all six required evidence categories. |
| `updates_derived_surfaces_after_confirmation` | PASS | The snapshot preserves v0.9.0, appends v1.0.0 to the index and metadata, preserves manualNote, and leaves last_verified_version unchanged. |
| `passes_host_docs_checks` | PASS | runner_captured_trace shows npm run test:docs executed in docs/site with 75 tests passing; explicit v1.0.0 version validation also passed. |
| `returns_complete_ready_handoff` | FAIL | The with_skill output explicitly reports handoff_status: blocked instead of returning a complete ready handoff, despite confirmed version, confirmed body, passing checks, delivered page, and available locked evidence. |
| `preserves_external_release_boundary` | PASS | git_evidence shows no commit, ref, tag, or external-release mutation; delivery_snapshot keeps last_verified_version: unverified and the output states no tag, GitHub Release, image publication, or deployment. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5d2eb8fee66e709ed28ba5aa53ac1e57295ed25d74500a43d924b8fbc434431e; fixture_sha256=c11c4570536758cb911b613643632dd7b15e8b492fb6a5c6cb788342176462bf; output_sha256=3cb39ce18b9e76bf7d91c903dd758eb72dfaf7c1d10a223bca35520e09e1e050; snapshot_sha256=e848e49f4c76fa870d2b1867dc636f745d24a85de1020d39b3d147e7f6eeade3
- Behavior: Delivered a complete confirmed release page, correctly updated derived surfaces, passed host checks, and preserved external boundaries, but incorrectly blocked the final ready handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5d2eb8fee66e709ed28ba5aa53ac1e57295ed25d74500a43d924b8fbc434431e; fixture_sha256=c11c4570536758cb911b613643632dd7b15e8b492fb6a5c6cb788342176462bf; output_sha256=3a4a84710bae0fc7de0b234e15e78d331b8175a738a6e826aded781daf78bc26; snapshot_sha256=c46d65132e287a47c66d18aeae5e4d2e8a8541c990bd624aed48bb314fe80b24
- Behavior: Delivered a similar page and derived-surface updates, with additional generated build artifacts and less complete metadata preservation; comparison only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The required complete pre-tag ready handoff was not returned; the candidate returned blocked instead.
- Next: Return the complete docs-agent:docs-audit pre-tag ready handoff with the confirmed version, source, page, checks, updated surfaces, evidence, blockers, downstream_target, and release_execution_authorized: false.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
