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
- target_skill_sha256: `cd54295a0cbcb90462d5e5533bde1937cc7e871f8f4c9c53d7773ed40ace553e`
- eval_definition_sha256: `8b3afd523591d93b0ae2bfbea1c5709666ee81c09a14160679da5b53064efb14`
- metadata_sha256: `b2c29426ebf4eb7772788a981043f00672d29ff296d5629f3103cb3b99a34acd`
- fixture_sha256: `9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `fe1f59786edfa4e3b7ee12601522d693ef12a42cdfce9b4a390ad6d7b95d03d2`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `dede36cbf22736a6194a488a09a7dab4d5a1092bacb831a4913854fdff85a07a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Trace shows the mapped manifest, change-map, and required network-client document were read in sequence, with no unrelated formal documents inspected. |
| `verifies_against_code` | PASS | The candidate explicitly reports manifest version 1.4.0 versus formal-document claim 2.1.0 and treats the manifest as the code fact. |
| `treats_unverified_as_low_trust` | PASS | The candidate explicitly identifies both freshness markers as unverified, treats them as navigation only, and relies on the manifest for the version fact. |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | The candidate returns to pm-agent and requests the required handoff fields, but issue creation cannot yet occur without the missing PM confirmation/packet. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994; fixture_sha256=9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5; output_sha256=ff12912c76e45d680c8fa20f25be0ba8de9a4abaf75f3522b8b7c754596a081b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly applied the entry gate, read the mapped evidence, identified the 1.4.0 versus 2.1.0 conflict, downgraded unverified documentation, and returned the matter to pm-agent.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994; fixture_sha256=9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5; output_sha256=329c99611df6adb350d2c2eabb346e0770fd720310f6dced73bb11512c687455; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Completed a broader dependency-risk audit and provided version, provenance, mitigation, and upgrade recommendations without the role-entry gate.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain PM/Security handoff confirmation, then have pm-agent classify the conclusion and create the tracking issue if the documentation fact change is confirmed.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
