# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-014-route-site-notes-and-github-release`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-14-route-site-notes-and-github-release`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2`
- Repository HEAD: `33a503192c752d6227de1bc0d8d8a2e78e31cdf5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8b87fb93cdb85ecb0436a61b1aedfcf9c8b41c4cd8f9eff41c412a3196c1d245`
- Skill overlay SHA-256: `56390e18f057b654978938889dac7daf0263eaaf39d741419b573d12bff2c198`
- Judge schema SHA-256: `0e6be21ab02e72aa076a9b774d5cc60139434feba550f781574340027908427d`
- Eval definition SHA-256: `ae4335c3ea7ab2052d5988d1cbe329b872d3570826da6174d95ecdee75a8f11e`
- Metadata SHA-256: `7b48bd11ada861ee54366c474d903263630fabf2c5e0d3a66c9f38056e80908e`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_site_notes_to_docs_specialist` | PASS | With-skill routing explicitly selects docs-agent:release-notes-gen for the site-facing release notes request. |
| `routes_github_release_to_pm_specialist` | NOT_EXERCISED | The workflow is blocked before the downstream GitHub Release step because release evidence and the required specialist are unavailable; no contrary PM route is exercised. |
| `preserves_release_sequence` | PASS | The candidate explicitly preserves the site Release Notes → Docs audit/gates → GitHub Release sequence. |
| `does_not_use_old_pm_skill_name` | PASS | The PM owner is not named release-notes-gen; that name is used only for docs-agent. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=63fb3119d7d2a49dd0eedeb7a4f754407375218ed8c724e6279398413fa87f88; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes site notes to docs-agent:release-notes-gen and preserves the Docs-gated release sequence, but stops before downstream GitHub Release routing.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=844685d34e14f53e1db03ed71d47e6204c5ccafd908acd88d1d1f0df50a4ed68; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline requests missing repository and release evidence and does not exercise the workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide confirmed v1.0.0 release evidence and make the downstream GitHub Release specialist available to exercise the remaining assertion.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
