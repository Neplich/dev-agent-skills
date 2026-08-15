# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-004-mapped-client-dependency`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-004-mapped-client-dependency`.
- Identity schema: `2`
- target_skill_sha256: `4936716a99cef8bc1e927ef64eaa0d20fa85f573a00b76c6ef0e6212ccbb3af0`
- eval_definition_sha256: `8b3afd523591d93b0ae2bfbea1c5709666ee81c09a14160679da5b53064efb14`
- metadata_sha256: `b2c29426ebf4eb7772788a981043f00672d29ff296d5629f3103cb3b99a34acd`
- fixture_sha256: `9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `fe1f59786edfa4e3b7ee12601522d693ef12a42cdfce9b4a390ad6d7b95d03d2`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `41b45499ae9ca5616b92679964200469b31cddbc1797bbf9c8e3a1dc71be48a5`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Trace shows the candidate located the manifest/change-map relationship, read only the mapped network-client document, and did not traverse unrelated formal documentation. |
| `verifies_against_code` | PASS | The candidate explicitly reports manifest version 1.4.0 versus documented 2.1.0 and treats 1.4.0 as the actual repository dependency fact. |
| `treats_unverified_as_low_trust` | PASS | The candidate identifies both freshness markers as unverified, treats them as low-trust navigation, and bases the version conclusion on the manifest rather than rejecting the documents outright. |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | A confirmed Security conclusion and PM handoff context are absent; the candidate correctly stops at the PM/Security entry gate and requests PM classification. Issue creation and escalation evidence are therefore not yet exercisable. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994; fixture_sha256=9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5; output_sha256=e5bb02807d1a811d4d768d533326672daacf3d97879bc919069d706c620c8c53; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Followed the mapped-document and low-trust verification workflow, identified the 1.4.0/2.1.0 discrepancy, then correctly stopped at the missing PM/Security handoff gate.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994; fixture_sha256=9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5; output_sha256=dc6197ffe2931eba2ebc03bae1ae43a429a25af4e6b69f8cb2eb97ed938b0c09; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a substantive version-conflict risk assessment and remediation suggestions, but did not follow the PM/Security handoff and escalation contract.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide a confirmed PM/Security handoff packet, then complete the dependency audit and return any fact-changing conclusion and evidence to pm-agent for classification and issue filing.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
