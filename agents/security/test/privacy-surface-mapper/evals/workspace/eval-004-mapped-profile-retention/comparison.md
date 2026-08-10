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
- Fixture SHA-256: `770d05d85a5304099a8f9433d2be942409c59c2f8ece13f985350673cd6e1b76`
- Prompt SHA-256: `90526a6f11b7d07cc96154485f1093a95a1e0a80c1ca3d9a35272a8e6b6e737f`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `25bd4dbed66f3625883b2a2072dcd568eef569278521e1eac012e86f61347836`
- Skill overlay SHA-256: `4894e45a78f6999eae63835919f4d9ac1eddcf0e15978742e5f90f2ebd544560`
- Judge schema SHA-256: `fe1f59786edfa4e3b7ee12601522d693ef12a42cdfce9b4a390ad6d7b95d03d2`
- Eval definition SHA-256: `4636a9753113bcd43710d7f9510814811413ce11cdc5e68daebdc570220f08a9`
- Metadata SHA-256: `9a8afbbbec758d7a8301647fd089cbe8695096269334ba062d91dd1eead9320a`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Raw trace shows change-map lookup followed by targeted reading of docs/site/api/profile-data.md and src/privacy/profile-processing.yaml; delivered report records the matched document and scoped evidence. |
| `verifies_against_code` | PASS | Locked delivery snapshot identifies the configured 90-day value, documented 30-day value, 60-day discrepancy, and corresponding compliance risk; raw trace confirms configuration inspection and repository verification. |
| `treats_unverified_as_low_trust` | PASS | Locked report explicitly marks the formal documentation as unverified/low-trust and distinguishes configured policy from unverified runtime behavior, with additional implementation/test verification. |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | The Security-owned report hands the conclusion and evidence back to pm-agent for classification and PM-owned issue filing. Actual issue creation is not exercised because no PM confirmation or issue-tracker runtime is present. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=90526a6f11b7d07cc96154485f1093a95a1e0a80c1ca3d9a35272a8e6b6e737f; fixture_sha256=770d05d85a5304099a8f9433d2be942409c59c2f8ece13f985350673cd6e1b76; output_sha256=dc99e6f4321d30eeed68c7caaeec11e238495525b7b72a97f22412cb8323f822; snapshot_sha256=c9a488b41a845607230a026b269dcea716612f2501f40e31fcb317950460a4de
- Behavior: Produced the required Security report, used mapped evidence, verified the 90-day configuration against the 30-day document claim, treated unverified material as low-trust, and prepared PM handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=90526a6f11b7d07cc96154485f1093a95a1e0a80c1ca3d9a35272a8e6b6e737f; fixture_sha256=770d05d85a5304099a8f9433d2be942409c59c2f8ece13f985350673cd6e1b76; output_sha256=cd4552c270121fd0e943f2bd7fc7d0cb3fde94ba8937583b427442029c6dc18f; snapshot_sha256=b9d708ea0de380629e643256d2d97da9ad864ccf8d99e8173ae6c16ebbb9eb19
- Behavior: Produced a similar report and correctly identified the 90-day versus 30-day discrepancy, but provided less evidence of mapped-document and low-trust verification workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: pm-agent should classify the handed-off conclusion and create the remediation issue.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
