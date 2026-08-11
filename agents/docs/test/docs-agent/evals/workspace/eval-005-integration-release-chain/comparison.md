# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-005-integration-release-chain`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3` from `agents/docs/test/docs-agent/evals/workspace/eval-005-integration-release-chain`.
- Fixture SHA-256: `69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3`
- Prompt SHA-256: `62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e`
- Repository HEAD: `fecf485e8e3dcaf191b2b221d9cccbddfdea0b72`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `cf92649952a97be677cf5e900a4d9c793a6c0724813cf1fa3154f57e7d2c08f3`
- Skill overlay SHA-256: `27cf83a083bb86b8e2bfb6ab9d0be5964ee293f7ae0a8410b53398d75bcabf0e`
- Judge schema SHA-256: `1f2ea17b811fce39b8e906ef0e0a70b6a6223a188a2f4a05f2f0a88c54c6aceb`
- Eval definition SHA-256: `05d8b9eb5ccf6bbc077dad850c79899562c5b4ed9bbb4187abffd82f21410ea3`
- Metadata SHA-256: `af301306a3e584e9c32987cd73e02ac298dcd98f38208af58ca0764e8b5a4154`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_audit_entry` | PASS | The with_skill output accepts release-chain-entry.md plus the handoff and signed Git snapshot as the audit basis, preserves v1.4.0, AI-search scope, listed evidence, and the read-only/no-write boundary. |
| `evaluates_site_release_notes_gate` | PASS | The handoff is marked ready but the locked handoff and release-note files retain unverified state and no explicit confirmed body status; with_skill blocks and routes back to the site Release Notes owner. |
| `validates_release_window_basis` | PASS | The signed snapshot shows refs/tags/v1.3.0 and refs/heads/release-base both at 041b91a..., and with_skill explicitly identifies this usable release-window anchor. |
| `rejects_missing_pre_tag_authority` | PASS | The snapshot shows the candidate/tag-entry tree 7c8b9b... differs from the v1.4.0 tag tree 490d0b..., and with_skill states this cannot prove the tag corresponds to audited content or release readiness. |
| `detects_post_tag_evidence_drift` | PASS | The signed snapshot records v1.4.0 at 9ae0a8f.../490d0b... while candidate, tag-entry, and evidence-expected refs resolve to 5dc0861b.../7c8b9b...; with_skill identifies the inconsistency and blocks continuation. |
| `blocks_github_release_handoff` | PASS | With_skill concludes GitHub Release preparation cannot proceed, provides no preview/draft/publish handoff, and assigns remediation to the site Release Notes owner before returning to docs-audit. |
| `preserves_no_mutation_boundaries` | PASS | The locked git evidence shows unchanged HEAD/branch, empty ref and diff deltas, and empty delivery_snapshot; the with_skill trace contains read-only inspection and tests, with no tag or GitHub Release write. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=faba5d44be4cb18bcbc89534b601025d9882d94178a7c905b6900ae6866ca997; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly accepts the audit entry, validates the release window, detects unverified Release Notes state and tag/tree drift, blocks GitHub Release progression, routes remediation to the correct owner, and preserves read-only boundaries.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=bba8c859db51169e180d99a9f6f063a02a83aa1187310258f83b9731edb9b18c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also reaches the core blocked-release conclusion and identifies tag/tree drift, but provides a less structured routing decision and less precise release-window validation.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Site Release Notes owner should add explicit confirmed status and reconcile unverified page state.
- Next: Release manager/tag owner should provide corrected signed tag-to-candidate evidence.
- Next: Docs-audit should rerun pre-tag/post-tag eligibility after remediation.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
