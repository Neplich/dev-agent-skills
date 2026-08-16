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
- target_skill_sha256: `9ac7059a9a39550256d4de1ed82086d7f6b3c81bd069d831f0bf87ce02417c58`
- eval_definition_sha256: `d863b13d3e997477097b1a2de108729923e21619e10b2847114ea312db1c1bc8`
- metadata_sha256: `cba4c9b4e188e5fae3cb488fc06e9766a5898277f19d0fa6882623eeaaede5e7`
- fixture_sha256: `fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `fe1f59786edfa4e3b7ee12601522d693ef12a42cdfce9b4a390ad6d7b95d03d2`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `d316d6849a82751d5c66c424af9993a42c304fe892fdb2411469b461bec624ee`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Trace shows the candidate located the change-map entry and its required `docs/site/api/user-search.md`, then read the mapped document without evidence of traversing unrelated formal documents. |
| `verifies_against_code` | NOT_EXERCISED | The candidate correctly stopped at the missing PM/Security handoff gate before performing code verification; the code-fact comparison was therefore not exercised. |
| `treats_unverified_as_low_trust` | NOT_EXERCISED | The candidate identified `last_verified_version: unverified` and did not rely on the document for a security conclusion, but the subsequent code-verification step was blocked and not exercised. |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | No confirmed fact-changing security conclusion was reached, so the conditional PM escalation and issue-creation requirement was not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de; fixture_sha256=fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d; output_sha256=838fa14c55da135ce9f41d54fff02e43bc54dba4f57ec4cbd3319112c5905214; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Read the mapped change documentation, recognized its unverified status, and correctly returned to PM classification at the required entry gate without making an unsupported security conclusion or mutating files.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e2ae5e4d2822699f2cb15956131366187d45773423915faa9c9726d6be1fc4de; fixture_sha256=fc2995d30d3ccba9dfaf0358946382fa2b5ecd4e3e1f4b423d1635f72c325d7d; output_sha256=4908cf319d528da6c6bda9833edfbd1588e7d1ff4e92c20054a705e2b55e8c38; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Performed a complete code-versus-document review, identified direct SQL interpolation and the documentation mismatch, and made no repository changes.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the required PM/Security handoff context and confirmed feature_path, then perform the code verification and conditional escalation review.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
