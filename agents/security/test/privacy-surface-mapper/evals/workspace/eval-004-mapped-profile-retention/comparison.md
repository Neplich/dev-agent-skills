# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-004-mapped-profile-retention`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `770d05d85a5304099a8f9433d2be942409c59c2f8ece13f985350673cd6e1b76` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-004-mapped-profile-retention`.
- Identity schema: `2`
- target_skill_sha256: `36470092bada7ef550e554a98c281f2fe94c427f5a20542e3fb5f13c69f3b496`
- eval_definition_sha256: `4636a9753113bcd43710d7f9510814811413ce11cdc5e68daebdc570220f08a9`
- metadata_sha256: `77d448d668cd55f753d5775b3a1d6295d66bd9b2b4219c2edf0b6a48f8bc6666`
- fixture_sha256: `770d05d85a5304099a8f9433d2be942409c59c2f8ece13f985350673cd6e1b76`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `fe1f59786edfa4e3b7ee12601522d693ef12a42cdfce9b4a390ad6d7b95d03d2`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `90526a6f11b7d07cc96154485f1093a95a1e0a80c1ca3d9a35272a8e6b6e737f`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `04d179782a25ad87f73775d407c14368f4301d86a871528ca2b66e82792a813b`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Raw trace shows the task landing was identified, the change-map entry was located, and the required document was read; no unrelated formal documents were present or traversed. |
| `verifies_against_code` | PASS | The locked report directly records the YAML configuration as 90 days, the formal document as 30 days, distinguishes configured policy from runtime behavior, and states the compliance impact. |
| `treats_unverified_as_low_trust` | PASS | The report explicitly marks both mapped documents as unverified/low-trust and bases the retention conclusion on configuration evidence, while noting runtime behavior is unverified. |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | The Security report correctly specifies return to pm-agent for classification and PM-owned issue filing, and forbids direct Docs handoff or Security issue creation. PM confirmation and subsequent issue creation are not exercised in the locked run. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=90526a6f11b7d07cc96154485f1093a95a1e0a80c1ca3d9a35272a8e6b6e737f; fixture_sha256=770d05d85a5304099a8f9433d2be942409c59c2f8ece13f985350673cd6e1b76; output_sha256=9c7e95407603399df3b76f759feef2ed3ca553441863830296c007a07ace7a32; snapshot_sha256=fa1579182bf2b73c49d39b4e6ec3201f88de1b2cd8295a9032228ed8344420ab
- Behavior: Produced the required Security-owned privacy report with correct field, purpose, retention discrepancy, low-trust handling, compliance impact, and escalation guidance.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=90526a6f11b7d07cc96154485f1093a95a1e0a80c1ca3d9a35272a8e6b6e737f; fixture_sha256=770d05d85a5304099a8f9433d2be942409c59c2f8ece13f985350673cd6e1b76; output_sha256=5def917fe5f2346a9c41166d364abe2fbb963482194cfb8dc118c7537983e89f; snapshot_sha256=4de68a4022355757154dd1cbbd3d67506c0211a88c0b020c37863aa0d1b2c20f
- Behavior: Produced a broadly correct privacy summary and report, but did not evidence the mapped-document workflow or PM escalation behavior; this is comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: After user confirmation, have pm-agent classify the escalation and create the tracking issue.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
