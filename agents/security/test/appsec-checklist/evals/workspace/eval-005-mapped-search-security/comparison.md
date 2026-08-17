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
- Identity schema: `2`
- target_skill_sha256: `412a68c0dfdb2d720e3447fdc4faf74b408d3de29706093a3a69fb0ca69d983c`
- eval_definition_sha256: `d863b13d3e997477097b1a2de108729923e21619e10b2847114ea312db1c1bc8`
- metadata_sha256: `cba4c9b4e188e5fae3cb488fc06e9766a5898277f19d0fa6882623eeaaede5e7`
- fixture_sha256: `fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `fe1f59786edfa4e3b7ee12601522d693ef12a42cdfce9b4a390ad6d7b95d03d2`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `035cdf3596c1888564523ed3d4e73116a3d2b231b30d91c462fb62cf6da52e05`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | Trace shows the change-map and required_docs were identified, but the required API document was not read because the PM/Security handoff gate blocked continuation. |
| `verifies_against_code` | NOT_EXERCISED | The with_skill trace does not read or verify src/api/search-handler.js, so no code-versus-document security conclusion was reached. |
| `treats_unverified_as_low_trust` | NOT_EXERCISED | The candidate explicitly identified last_verified_version: unverified as low-trust navigation, but no key security judgment was completed or code verification performed. |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | No confirmed Security conclusion, report, PM return, or issue filing occurred because the required handoff and feature_path were missing. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de; fixture_sha256=fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d; output_sha256=c12dcf10ceaadf17eacf335a8f0b925bcaf1ee3c7e41801f333f029a15c208ad; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly enforced the Security entry gate, identified the mapped document and its unverified status, and returned the request to pm-agent without making unsupported security claims or mutating files.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de; fixture_sha256=fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d; output_sha256=cffdcb4effd92b30c9f4ffcb8595fb36d033a2255b01b41b085b8db4e71268b0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Completed a read-only code/document comparison and reported the SQL injection risk, but did not perform the required PM escalation workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the required PM/Security handoff and confirmed feature_path, then continue the mapped document and code review.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
