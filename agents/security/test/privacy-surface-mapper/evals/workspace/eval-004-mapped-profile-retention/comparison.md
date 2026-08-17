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
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `90526a6f11b7d07cc96154485f1093a95a1e0a80c1ca3d9a35272a8e6b6e737f`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `2eea2d31331dfff7d98326573b856ca9f269bca068d5f182bf99e8b0d5d75219`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | Trace shows docs/site/api/profile-data.md was read at item_9 before docs/site/standards/change-map.yaml at item_11; the required document was not selected by first reverse-mapping from the target YAML. |
| `verifies_against_code` | PASS | The delivered report directly cites src/privacy/profile-processing.yaml, identifies configured retention as 90 days versus the documented 30 days, and explains the 60-day compliance discrepancy. |
| `treats_unverified_as_low_trust` | PASS | The delivered report records last_verified_version as unverified, treats the document as low trust, and distinguishes configured policy from unverified runtime behavior. |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | The report was delivered as a Security-owned docs/security process report and the final output states the conclusion and evidence should return to pm-agent. Actual issue creation is not exercised; the evidence contains no issue-creation event, and the next PM action would require confirmation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=90526a6f11b7d07cc96154485f1093a95a1e0a80c1ca3d9a35272a8e6b6e737f; fixture_sha256=770d05d85a5304099a8f9433d2be942409c59c2f8ece13f985350673cd6e1b76; output_sha256=67fe414e755418ecb155dd856b8d148bb0129b71bb8b3c50e881eff7982879cc; snapshot_sha256=160d76b8c9d74cdc4cf190414d343bea54974903851145897c1f961120660d25
- Behavior: Produced the required privacy report with accurate field, purpose, retention mismatch, low-trust documentation handling, runtime-evidence caveat, and PM escalation guidance.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=90526a6f11b7d07cc96154485f1093a95a1e0a80c1ca3d9a35272a8e6b6e737f; fixture_sha256=770d05d85a5304099a8f9433d2be942409c59c2f8ece13f985350673cd6e1b76; output_sha256=17cf1d791aa83ff0b61c2dbe35f66d82bac2d0c482c6bd2993cbaad0488f7889; snapshot_sha256=3960338f58730f6fcbe76685934331a934140964c45ad460c19b6e1e31e100d1
- Behavior: Produced a similar report identifying the 90-day versus 30-day mismatch and runtime evidence gap, but did not demonstrate low-trust handling or PM escalation.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill trace reads the mapped formal document before reading the change-map, contrary to the required reverse-mapping/read-order assertion.
- Next: After PM confirmation, classify the escalation and create the tracking issue.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
