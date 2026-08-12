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
- Repository HEAD: `715bd6b76fcd6f14f475aeabe141543063d431ba`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `be11ec63823b148323fef6c35d27c0861bd093b24d683f705e846234e98b7baa`
- Skill overlay SHA-256: `961e7aacbdec2d154ad578bc7bf54d5d734f34031af1384fb20aa67a8e2d392a`
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
| `routes_site_notes_to_docs_specialist` | PASS | With_skill output explicitly routes the request to `docs-agent:release-notes-gen`. |
| `routes_github_release_to_pm_specialist` | PASS | With_skill output explicitly routes the GitHub Release stage to `pm-agent:github-release-gen`. |
| `preserves_release_sequence` | NOT_EXERCISED | The candidate identifies the intended Docs-to-PM order, but downstream Docs confirmation, ready handoff, and release audit evidence cannot occur because the required specialists and source evidence are unavailable. |
| `does_not_use_old_pm_skill_name` | PASS | The PM owner is named `github-release-gen`; `release-notes-gen` is used only under `docs-agent`, not as the PM owner. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=b9664edccd97be4ce845ce97bd88fe55172a34ecca034db437d0e59baefdef95; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the two-stage workflow and stops at the blocked PM entry without generating or publishing release artifacts.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=1bd52ec39ee7a56e2a9e651b6318c10bdd27c31b214a490190006f8343756c7e; snapshot_sha256=573bb8fe25dc4669e69b48ed8e6f6e43eca7a7cc78edce18355823928cf4d242
- Behavior: Creates release-note and GitHub preview files from the empty snapshot without demonstrating the required specialist routing.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Enable the Docs and PM specialists and provide confirmed v1.0.0 release evidence before executing the downstream stages.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
