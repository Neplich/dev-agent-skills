# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-005-mapped-search-security`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d` from `agents/security/test/appsec-checklist/evals/workspace/eval-005-mapped-search-security`.
- Fixture SHA-256: `fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d`
- Prompt SHA-256: `e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `812b371fc30792cb2b0cf8d96079b3244c95b93efab7638e085d4e955d6ea42c`
- Skill overlay SHA-256: `11d9f677e9ab3fadaeeab596575848debc7e1fb3f4f8054e9e5572a63ccf426b`
- Judge schema SHA-256: `fe1f59786edfa4e3b7ee12601522d693ef12a42cdfce9b4a390ad6d7b95d03d2`
- Eval definition SHA-256: `d863b13d3e997477097b1a2de108729923e21619e10b2847114ea312db1c1bc8`
- Metadata SHA-256: `44e3487a1b0a940b7bf23d73f980b7d71bd0be1a4d04a13c48606fd67383de8a`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | With-skill trace shows change-map and its required_docs were read, and the output identifies docs/site/api/user-search.md as the mapped document without traversing unrelated formal docs. |
| `verifies_against_code` | NOT_EXERCISED | The candidate explicitly states that it did not read or review src/api/search-handler.js because the PM/Security handoff gate was missing; code verification and the document/code mismatch were therefore not exercised. |
| `treats_unverified_as_low_trust` | PASS | The candidate identifies last_verified_version: unverified and treats the document as low-trust navigation rather than authoritative evidence or a reason to refuse reading it. |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | No confirmed Security conclusion was reached because the required handoff and feature_path were missing, so PM classification and issue creation were not yet exercisable. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de; fixture_sha256=fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d; output_sha256=735f60ee6b25a73145c42dd093e35e9078f4a925cdf180dba6a8db30960cb7ad; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly stopped at the mandatory AppSec entry gate, read the mapped documentation, identified its unverified status, and directed the request back to pm-agent.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de; fixture_sha256=fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d; output_sha256=e947ef717041488dc75f4882e3918e70e2b56be1de1f73d09c59d11ccac2579f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Completed the code review and identified the SQL injection risk and documentation/code mismatch, but did not perform the required PM escalation workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the confirmed PM/Security handoff packet and feature_path, then continue the code review and required Security-to-PM escalation if the formal-documentation fact change is confirmed.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
