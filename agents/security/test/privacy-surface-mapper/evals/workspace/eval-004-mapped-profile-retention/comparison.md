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
- target_skill_sha256: `2d9aa34423715a24783169e774af3c68a95cbc320b5fc5af4b5753bd7785f2a0`
- eval_definition_sha256: `4636a9753113bcd43710d7f9510814811413ce11cdc5e68daebdc570220f08a9`
- metadata_sha256: `77d448d668cd55f753d5775b3a1d6295d66bd9b2b4219c2edf0b6a48f8bc6666`
- fixture_sha256: `770d05d85a5304099a8f9433d2be942409c59c2f8ece13f985350673cd6e1b76`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `fe1f59786edfa4e3b7ee12601522d693ef12a42cdfce9b4a390ad6d7b95d03d2`
- Source lock SHA-256: `c58f04d32c2ca3a22aec96f7ee027af648da5971453d2a5553d7ab2cd9272551`
- Prompt SHA-256: `90526a6f11b7d07cc96154485f1093a95a1e0a80c1ca3d9a35272a8e6b6e737f`
- Repository HEAD: `60a4b3602dc07f3f6683a8873529bbdba6f8d27d`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `2eea2d31331dfff7d98326573b856ca9f269bca068d5f182bf99e8b0d5d75219`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | The trace shows the candidate consulted the handoff/change-map context, identified docs/site/api/profile-data.md as the required mapped document, and read only the relevant handoff, map, mapped document, and configuration context; the delivered report records the mapping. |
| `verifies_against_code` | PASS | The locked report directly cites src/privacy/profile-processing.yaml, distinguishes its configured 90-day value from the formal document's 30-day claim, identifies the 60-day discrepancy, and assesses transparency, deletion-commitment, and audit risk. |
| `treats_unverified_as_low_trust` | PASS | The report explicitly marks last_verified_version: unverified materials as low trust and states that configuration/code evidence cannot establish runtime retention; the trace also records the absence of deletion implementation, tests, and runtime observations. |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | The candidate returned the fact-changing conclusion and evidence to pm-agent for classification, created the Security-owned report, and did not modify formal docs. PM issue creation is a later interactive step pending confirmation, so it is not exercised by the locked evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=90526a6f11b7d07cc96154485f1093a95a1e0a80c1ca3d9a35272a8e6b6e737f; fixture_sha256=770d05d85a5304099a8f9433d2be942409c59c2f8ece13f985350673cd6e1b76; output_sha256=1dad68cd035b4399f7e9aa49e2ee64228386aff3e20f002587d095f51df18cb4; snapshot_sha256=d57955de15dab834a4b048bf7d8edc3c9681153c04754baf6806f9cf643853fc
- Behavior: Produced a grounded privacy report, verified the configuration/documentation discrepancy, treated unverified evidence cautiously, and routed the conclusion to PM without editing formal documentation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=90526a6f11b7d07cc96154485f1093a95a1e0a80c1ca3d9a35272a8e6b6e737f; fixture_sha256=770d05d85a5304099a8f9433d2be942409c59c2f8ece13f985350673cd6e1b76; output_sha256=21b27e4064bdf294e41ce9b32fc76d4b8a6e6eb7e9aab39ba2fe1b2c81607936; snapshot_sha256=abf0769d0f50a5b5f9648aa0c768c08200f7b5b411700c4e2e785eefc43b02bd
- Behavior: Produced a broadly correct report and discrepancy assessment, but its trace searched repository content before following the mapped-document workflow and did not show the required PM escalation behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: PM classification and issue creation require the pending user confirmation/next interactive step.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
