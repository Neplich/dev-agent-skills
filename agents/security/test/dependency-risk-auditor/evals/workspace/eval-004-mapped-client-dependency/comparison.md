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
- Fixture SHA-256: `9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5`
- Prompt SHA-256: `7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0f253c18407bc188d3558e673dc587116dcb519a01d7ef15849f9e98e350e1c1`
- Skill overlay SHA-256: `a20df761eb11be10e69d0c69c6cd83a1d8df72f5c18c6d851046ac906baa7ff4`
- Judge schema SHA-256: `fe1f59786edfa4e3b7ee12601522d693ef12a42cdfce9b4a390ad6d7b95d03d2`
- Eval definition SHA-256: `8b3afd523591d93b0ae2bfbea1c5709666ee81c09a14160679da5b53064efb14`
- Metadata SHA-256: `72846a754080f41b7de9981348b71040115d4704d0a16f2aad7aa4b526a44443`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Trace shows the mapped change-map and required network-client document were read, with no unrelated formal documents; the manifest-to-map reverse lookup itself is not independently proven. |
| `verifies_against_code` | NOT_EXERCISED | The with_skill lane explicitly states that manifest/lockfile or code verification was not performed because the required PM/Security handoff was missing. |
| `treats_unverified_as_low_trust` | PASS | The lane identifies both mapped documents as last_verified_version: unverified and treats them as low-trust navigation rather than accepting the documented 2.1.0 fact. |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | No confirmed code-versus-document conclusion was reached, so the conditional PM classification and issue-filing step was not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994; fixture_sha256=9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5; output_sha256=d477e738e023414a9c27fad11d9226037ba8127857f6e3dcf03d3d9af25f3aef; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly enforced the dependency-audit entry gate, read the mapped documentation, treated unverified metadata as low trust, and returned the work to pm-agent without unsupported audit conclusions or mutations.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7a3821e75530d0b15af01947cb71f52d6f838c90667f22241c35f06721254994; fixture_sha256=9287a8fa578b5447f010eec525225500d555d9e2f5c2758277bcae9488425fa5; output_sha256=81fc0cb9f1278d2ae462e5e4ca710a8c752b26b484c7f1440a6c0c14279c56da; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Completed a broader repository audit, verified the 1.4.0 manifest declaration against the 2.1.0 document claim, and gave risk and mitigation advice, but did not perform the required PM escalation workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain the required PM/Security handoff, then verify the manifest and repository evidence and escalate any confirmed documentation-fact change to pm-agent for classification and issue filing.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
