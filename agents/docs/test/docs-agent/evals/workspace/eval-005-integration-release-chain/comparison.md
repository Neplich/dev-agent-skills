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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `cf92649952a97be677cf5e900a4d9c793a6c0724813cf1fa3154f57e7d2c08f3`
- Skill overlay SHA-256: `5be76fc7f05f987d0dcf0e3f1254ab96a94a681a13a4c41d33898ae26441d21a`
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
| `accepts_release_audit_entry` | PASS | With-skill output accepts the maintainer-confirmed v1.4.0 entry, preserves scope and evidence sources, and states a read-only boundary. |
| `evaluates_site_release_notes_gate` | PASS | It rejects the handoff's ready label because confirmation and supporting gate credentials are incomplete, and returns ownership to site Release Notes owner. |
| `validates_release_window_basis` | PASS | It verifies v1.3.0 and release-base resolve to the same 041b91a... anchor and does not guess missing inputs. |
| `rejects_missing_pre_tag_authority` | PASS | It does not claim pre-tag success; it blocks before docs-audit pending confirmed Release Notes evidence. |
| `detects_post_tag_evidence_drift` | PASS | It identifies the signed-snapshot drift between the candidate/tag-entry tree 7c8b9b... and actual v1.4.0 tag tree 490d0b..., and blocks. |
| `blocks_github_release_handoff` | PASS | It concludes GitHub Release preparation cannot continue, provides no preview/draft/publish handoff, and routes remediation to the correct owner. |
| `preserves_no_mutation_boundaries` | PASS | The output and captured trace show only read/check activity and explicitly preserve the no-tag/no-GitHub-Release-write boundary. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=501eff9198be7fed10b00b447675cf94a7f825df9d56fd9ff4afb2e056b4d9ea; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly validates the entry, checks the release window, detects handoff incompleteness and ref/tree drift, blocks downstream release work, and preserves read-only boundaries.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=07203ea4f6f402443f19d9cda114347fc30effa1e9ef4c51c828d61e716dcbc7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Reaches the correct overall block and detects tree drift, but routes remediation to the release manager rather than the site Release Notes owner and provides less complete gate validation.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
