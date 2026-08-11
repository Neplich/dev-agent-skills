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
- Repository HEAD: `f2aa9b2c49be68550ec45538c221425607f428ce`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `cf92649952a97be677cf5e900a4d9c793a6c0724813cf1fa3154f57e7d2c08f3`
- Skill overlay SHA-256: `169fa6feaee2a3439ef1697f8695db0c122dae0703b31186cfbc7b44c0685be7`
- Judge schema SHA-256: `1f2ea17b811fce39b8e906ef0e0a70b6a6223a188a2f4a05f2f0a88c54c6aceb`
- Eval definition SHA-256: `05d8b9eb5ccf6bbc077dad850c79899562c5b4ed9bbb4187abffd82f21410ea3`
- Metadata SHA-256: `af301306a3e584e9c32987cd73e02ac298dcd98f38208af58ca0764e8b5a4154`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_audit_entry` | PASS | Identifies release-chain-entry.md and the confirmed version, scope, evidence sources, and read-only boundary. |
| `evaluates_site_release_notes_gate` | PASS | Rejects handoff_status=ready as insufficient confirmation and returns the site Release Notes owner for remediation. |
| `validates_release_window_basis` | PASS | Correctly reports previous tag and base ref resolving to the same signed snapshot anchor. |
| `rejects_missing_pre_tag_authority` | PASS | Does not claim pre-tag success and states that ready_for_tag/release_verified are not satisfied. |
| `detects_post_tag_evidence_drift` | FAIL | The signed snapshot shows candidate/tag tree drift, but the with_skill output does not identify that post-tag object mismatch. |
| `blocks_github_release_handoff` | PASS | Blocks GitHub Release preparation and assigns remediation to the Release Notes owner followed by post-tag audit. |
| `preserves_no_mutation_boundaries` | PASS | States a read-only boundary and reports no tag or GitHub Release writes; captured git evidence shows no mutation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=7c0cf765020d2dfd59f4224de06b2112294fe54287775acfc092f9892bffb32c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes and blocks the release, validates the window, and preserves read-only boundaries, but misses the decisive post-tag tree drift.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=a96a0ed5c3dddd10ee2b2c01f2f7ed3184bb4681e51075cb8a4d76d5a2301ff5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline correctly blocks the release and explicitly detects the candidate-versus-tag tree mismatch.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane failed to detect and report the signed-snapshot mismatch between the release-candidate/tag-entry tree and the actual v1.4.0 tag/release-evidence tree.
- Next: Require the with_skill lane to compare and report the candidate, tag-entry, actual-tag, and release-evidence tree identities before concluding post-tag eligibility.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
